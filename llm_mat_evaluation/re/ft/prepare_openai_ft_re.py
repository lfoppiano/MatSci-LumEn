import argparse
import json
import math
import os
from pathlib import Path

from langchain.prompts import PromptTemplate

from llm_mat_evaluation.re.process_openai_re_supermat import PROMPT_TEMPLATE_CHAT_SYSTEM, prepare_data, \
    PROMPT_TEMPLATE_CHAT_HUMAN_STRATEGY_AGGREGATED, FORBIDDEN_VALUES


def format_as_text(answer):
    formatted_text = "relations:\n"
    relations = answer['relations']

    for relation in relations:
        formatted_text += "  - "
        formatted_text += ", ".join([f"{key}: {value}" for key, value in relation.items() if value ])
        formatted_text += "\n"

    return formatted_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Prepare the fine-tuning data for GPT-3/ChatGPT on relation extraction")

    parser.add_argument("--input", help="Input CSV file containing text and annotations", required=True)
    parser.add_argument("--output", help="Output Fine-tuning file", required=True)

    args = parser.parse_args()

    input = args.input
    output = args.output

    data = prepare_data(input, 7)

    fine_tuning_template = \
        {
            "messages": [
                {"role": "system", "content": ""},
                {"role": "user", "content": ""},
                {"role": "assistant", "content": ""}
            ]
        }
    output_data = []
    for record in data:
        text = record['text']
        materials = record['materials']
        tcs = record['tcs']
        pressures = record['pressures']
        me_methods = record['me_methods']

        entities = {
            "materials": materials,
            "tcs": tcs,
            "pressures": pressures,
            "me_methods": me_methods
        }

        answer = {}
        relations = []
        for id in range(0, len(materials)):
            record = {
                "material": materials[id],
                "tc": tcs[id]
            }
            if pressures[id] not in FORBIDDEN_VALUES:
                record['pressure'] = pressures[id] if pressures[id] else ""
            if me_methods[id] not in FORBIDDEN_VALUES:
                record['me_methods'] = me_methods[id] if me_methods[id] else ""

            relations.append(record)

        answer['relations'] = relations

        entities['pressures'] = [pressure for pressure in entities['pressures'] if pressure]
        entities['me_methods'] = [method for method in entities['me_methods'] if method]

        answer_as_text = format_as_text(answer)
        output_data.append({
            "messages": [
                {
                    "role": "system",
                    "content": PROMPT_TEMPLATE_CHAT_SYSTEM
                },
                {"role": "user",
                 "content": PromptTemplate(
                     template=PROMPT_TEMPLATE_CHAT_HUMAN_STRATEGY_AGGREGATED,
                     input_variables=['text', 'entities']
                 ).format_prompt(text=text, entities=json.dumps(entities))
                 .to_string()},
                {"role": "assistant", "content": answer_as_text}
            ]
        })

    count_all = len(data)
    count_train = math.floor(count_all * 0.70)
    count_test = count_all - count_train

    print("All:", count_all, "training:", math.floor(count_train), "test:", count_test)

    output_path = Path(output)

    train_output_file = os.path.join(output_path, "train.jsonl")
    with open(train_output_file, encoding="utf-8", mode='w') as fo:
        for record in output_data[:count_train]:
            fo.write(json.dumps(record) + "\n")

    test_output_file = os.path.join(output_path, "test.jsonl")
    with open(test_output_file, encoding="utf-8", mode='w') as fo:
        for record in output_data[count_train:]:
            fo.write(json.dumps(record) + "\n")
