import argparse
import json
import math
import os
from pathlib import Path

import dotenv
from langchain.prompts import PromptTemplate

from llm_mat_evaluation.materials.process_openai_ner_materials import PROMPT_TEMPLATE_CHAT_SYSTEM, \
    PROMPT_TEMPLATE_CHAT_USER_MATERIALS_COMPLEX

dotenv.load_dotenv(override=True)

from commons.reader import load_texts_and_classes_generic, group_by


def prepare_data(input, input_annotations):
    text_data, _ = load_texts_and_classes_generic(input)
    annotations_data, _ = load_texts_and_classes_generic(input_annotations)
    output_data = []

    # Preparing data
    annotations_by_file = group_by(annotations_data, 1)
    for record in text_data:
        id = record[0]
        filename = record[1]
        paragraph_idx = record[2]
        text = record[3]

        local_annotations = annotations_by_file[filename] if filename in annotations_by_file else []
        local_annotations_by_paragraphId = group_by(local_annotations, 1)

        entities = []

        if paragraph_idx not in local_annotations_by_paragraphId:
            continue

        for annotation in local_annotations_by_paragraphId[paragraph_idx]:
            entities.append(annotation[1])

        # output_data.append([text, materials, properties, values])

        materials_filtered = list(filter(None, set(entities)))
        # random.shuffle(materials_filtered)

        prefix = "- " if len(materials_filtered) > 0 else ""
        output_data.append({
            "messages": [
                {
                    "role": "system",
                    "content": PromptTemplate(
                        template=PROMPT_TEMPLATE_CHAT_SYSTEM,
                        input_variables=['text']
                    ).format_prompt(text=text)
                    .to_string()
                },
                {"role": "user",
                 "content": PROMPT_TEMPLATE_CHAT_USER_MATERIALS_COMPLEX
                 },
                {"role": "assistant", "content": prefix + ",\n- ".join(materials_filtered)}
            ]
        })


    return output_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process paragraphs from the original format with GPT-3/ChatGPT")

    parser.add_argument("--input-text", help="Input CSV/TSV file containing text", required=True)
    parser.add_argument("--input-annotations", help="Input CSV/TSV file containing annotations", required=True)
    parser.add_argument("--output", help="Output CSV/TSV file", required=True)

    args = parser.parse_args()

    input = args.input_text
    input_annotations = args.input_annotations
    output = args.output

    data = prepare_data(input, input_annotations)

    count_all = len(data)
    count_train = math.floor(count_all * 0.70)
    count_test = count_all - count_train

    print("All:", count_all, "training:", math.floor(count_train), "test:", count_test)

    output_path = Path(output)

    train_output_file = os.path.join(output_path, "train.jsonl")
    with open(train_output_file, encoding="utf-8", mode='w') as fo:
        for record in data[:count_train]:
            fo.write(json.dumps(record) + "\n")

    test_output_file = os.path.join(output_path, "test.jsonl")
    with open(test_output_file, encoding="utf-8", mode='w') as fo:
        for record in data[count_train:]:
            fo.write(json.dumps(record) + "\n")
