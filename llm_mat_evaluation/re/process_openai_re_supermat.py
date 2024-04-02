import random
from typing import List, Optional

import dotenv
from langchain.output_parsers import PydanticOutputParser
from langchain.schema import OutputParserException
from pydantic import BaseModel, Field

dotenv.load_dotenv(override=True)
import argparse
import csv
import os
from pathlib import Path

from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate, \
    PromptTemplate
from tqdm import tqdm

from commons.openai import chat_gpt35_turbo_prompt_layer, CHATS
from commons.reader import load_texts_and_classes_generic, group_by, get_last_line

PROMPT_TEMPLATE_CHAT_SYSTEM = """You are useful assistant, which knows about materials science, physics, chemistry and engineering.
You will be asked to compute relation extraction given a text and lists of entities. 
If you are not sure, don't try to make up your answer, just answer "None". 
"""

# This strategy ask for extracting all possible relations
PROMPT_TEMPLATE_CHAT_HUMAN_STRATEGY_AGGREGATED = """
Consider the following text in between triple quotes: 
```
{text}
```

Find the relations between lists of entities of different classes. 
Apply strictly the following rules:  
    - if material is not specified, ignore the relation block,
    - if tc is not specified in absolute values, ignore the relation block 
    
Following the lists of entities: 
{entities}
"""

PROMPT_TEMPLATE_CHAT_HUMAN_STRATEGY_AGGREGATED_WITH_EXAMPLE = """
Given a text between triple quotes and a list of entities, find the relations between entities of different classes: 
```
{text}
```

{entities}

--------
Example: 
The researchers of Mg have discovered that MgB2 is superconducting at 29 K at ambient pressure.

entities:
 materials: MgB2, Mg
 tcs: 29K
 pressure: ambient pressure
 
Result: 
 material: MgB2, 
 tc: 29K, 
 pressure: ambient pressure: 
 
--------
Apply strictly the following rules:  
    - if material is not specified, ignore the relation block,
    - if tc is not specified in absolute values, ignore the relation block 
"""

ENTITIES_CLASS = ["materials", "tcs", "pressures", "me_methods"]

FORBIDDEN_VALUES = ["null", "None", "unknown", "none", None]


class ExtractedRelationsOutputParser(BaseModel):
    material: Optional[str] = Field(
        description="Material name, formula, sample name, doping ratio with any additional variable expression"
    )
    tc: Optional[str] = Field(
        description="Superconductor critical temperature, Tc, Tc onset, Tc zero "
    )
    pressure: Optional[str] = Field(description="Applied pressure when the Tc is measured")
    me_method: Optional[str] = Field(description="Method used for measuring the Tc")


class ListOfRelations(BaseModel):
    relations: List[ExtractedRelationsOutputParser]

    @staticmethod
    def parse_to_list(obj):
        return list(filter(
            lambda r: (r.material is not None and r.material not in FORBIDDEN_VALUES) and (
                    r.tc is not None and r.tc not in FORBIDDEN_VALUES),
            [relation for relation in obj.relations]))


def prepare_data(input, index_row_text=-1):
    text_data, _ = load_texts_and_classes_generic(input)
    output_data = []

    if index_row_text >= 0:
        input_filtered = []
        for row in text_data:
            if row[index_row_text] is not None and row[index_row_text].strip() != "":
                input_filtered.append(row)
    else:
        input_filtered = text_data

    annotations_by_file = group_by(input_filtered, 1)
    for filename, records_by_file in annotations_by_file.items():

        records_by_pid = group_by(records_by_file, 1)

        for pid, records in records_by_pid.items():
            id = ""
            text = ""
            materials = []
            tcs = []
            pressures = []
            me_methods = []
            for record in records:
                id = record[0]
                text = record[5]
                materials.append(record[1])
                tcs.append(record[2])
                if len(str.strip(record[3])) > 0:
                    pressures.append(record[3])
                else:
                    pressures.append([])
                if len(str.strip(record[4])) > 0:
                    me_methods.append(record[4])
                else:
                    me_methods.append([])

            output_data.append(
                {
                    "id": id,
                    "pid": pid,
                    "filename": filename,
                    "text": text,
                    ENTITIES_CLASS[0]: materials,
                    ENTITIES_CLASS[1]: tcs,
                    ENTITIES_CLASS[2]: pressures,
                    ENTITIES_CLASS[3]: me_methods
                }
            )

    return output_data


def get_prompt(user_template, format_instructions=None) -> ChatPromptTemplate:
    system_message_prompt = SystemMessagePromptTemplate.from_template(PROMPT_TEMPLATE_CHAT_SYSTEM)
    human_message_prompt = HumanMessagePromptTemplate.from_template(user_template)

    if format_instructions:
        user_template += "\n{format_instructions}"

        human_message_prompt = HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                template=user_template,
                input_variables=['text', 'entities'],
                partial_variables={"format_instructions": format_instructions})
        )

    prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    return prompt


def extract_relations(llm, prompt_template, text, entities, output_parser_class=None):
    format_instructions = None
    if output_parser_class:
        output_parser = PydanticOutputParser(pydantic_object=output_parser_class)
        format_instructions = output_parser.get_format_instructions()

    if llm.model_name.startswith("ft:"):
        prompt_chat_template = get_prompt(prompt_template)
    else:
        prompt_chat_template = get_prompt(prompt_template, format_instructions)
    prompt_text = prompt_chat_template.format_messages(text=text, entities=entities)

    results = llm(prompt_text)

    result_text = results.content

    if output_parser_class:
        output = output_parser.parse(result_text)
        output = output_parser_class.parse_to_list(output)
    else:
        output = result_text

    return output


def _parse_json(response, llm, output_parser):
    system_message = """You are an useful assistant expert in materials science, physics, and chemistry that can process text and transform it to JSON. 
    If you are not sure, don't try to make up your answer, just answer None"""

    human_message = """Transform the text between three double quotes in JSON.\n\n\n\nText: \"\"\"{text}\"\"\"{format_instructions}."""

    system_message_prompt = SystemMessagePromptTemplate.from_template(system_message)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_message)

    prompt_template = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    prompt_text = prompt_template.format_prompt(
        text=response,
        format_instructions=output_parser.get_format_instructions()
    ).to_messages()

    results = llm(prompt_text)

    result_text = results.content

    parsed_output = output_parser.parse(result_text)

    return parsed_output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract relations using the SuperMat dataset")

    parser.add_argument("--input",
                        help="Input CSV/TSV file containing text",
                        required=True)
    parser.add_argument("--model",
                        choices=CHATS.keys(),
                        default="gpt35_turbo")
    parser.add_argument("--output",
                        help="Output CSV file or directory",
                        required=True)
    parser.add_argument("--shuffle",
                        help="Shuffle entities before passing to the LLM",
                        default=False,
                        action="store_true",
                        required=False)

    args = parser.parse_args()

    input = args.input
    output = args.output
    model = args.model
    shuffle = args.shuffle

    llm = CHATS[model]

    if 'pl_tags' in llm:
        llm.pl_tags.append("evaluation")
        llm.pl_tags.append("re")

    prepared_data = prepare_data(input, 7)

    input_path = Path(input)
    if os.path.isdir(str(output)):
        shuffled = "" if not shuffle else "shuffled."
        output_path = os.path.join(output, "{}.{}.{}.output.csv".format(input_path.stem, model, shuffled))
    else:
        output_path = Path(output)

    last_line = get_last_line(output_path)

    last_id = None
    if last_line is not None and last_line.strip() != "":
        last_id = last_line.split(",")[0].replace("\"", "")

    with (open(output_path, encoding="utf-8", mode='a') as fo):
        fw = csv.writer(fo, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        for idx, passage_record in tqdm(enumerate(prepared_data)):
            id = passage_record['id']
            if last_id and int(id) <= int(last_id):
                print("Skipping line with id", id)
                continue

            filename = passage_record['filename']
            paragraph_id = int(passage_record['pid'])
            text = passage_record['text']

            entities = []
            for ent_class in ENTITIES_CLASS:
                ents_of_class = passage_record[ent_class]
                if shuffle:
                    random.shuffle(passage_record[ent_class])
                entities_values = "', '".join(filter(lambda e: len(e) > 0, ents_of_class))
                if entities_values.strip():
                    entity_string = "{}: '{}'".format(ent_class, entities_values)
                    entities.append(entity_string)

            try:
                result = extract_relations(llm,
                                           PROMPT_TEMPLATE_CHAT_HUMAN_STRATEGY_AGGREGATED,
                                           text,
                                           "\n".join(entities),
                                           output_parser_class=ListOfRelations)
            except OutputParserException as ope:
                output_data_raw = extract_relations(llm,
                                                    PROMPT_TEMPLATE_CHAT_HUMAN_STRATEGY_AGGREGATED,
                                                    text,
                                                    "\n".join(entities))
                if output_data_raw and output_data_raw != "None":
                    output_parser = PydanticOutputParser(pydantic_object=ListOfRelations)
                    if llm.model_name.startswith("ft:"):
                        parsed_output = _parse_json(output_data_raw, chat_gpt35_turbo_prompt_layer,
                                                    output_parser=output_parser)
                    else:
                        parsed_output = _parse_json(output_data_raw, llm, output_parser=output_parser)

                    result = ListOfRelations.parse_to_list(parsed_output)

            output_rows = []
            for rel in result:
                material = rel.material
                tc = rel.tc
                pressure = rel.pressure
                me_method = rel.me_method
                if tc is None or tc == "null":
                    continue
                output_rows.append([id, filename, paragraph_id, material, tc, pressure, me_method])

            fw.writerows(output_rows)
