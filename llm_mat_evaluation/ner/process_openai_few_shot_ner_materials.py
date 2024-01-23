import argparse
import csv
import os
from pathlib import Path
from typing import List, Optional

import dotenv
dotenv.load_dotenv(override=True)
from langchain_core.exceptions import OutputParserException
from document_qa.grobid_processors import GrobidMaterialsProcessor

from commons.grobid.grobid_client_generic import GrobidClientGeneric
from commons.ner import prepare_data
from commons.openai import CHATS
from llm_mat_evaluation.ner.process_openai_ner_materials import ListOfMaterialsOutputParser, \
    PROMPT_TEMPLATE_CHAT_USER_MATERIALS_SIMPLE
from llm_mat_evaluation.ner.process_openai_ner_properties import _parse_json, extract_entities

from langchain.output_parsers import PydanticOutputParser
from pydantic import Field, BaseModel
from tqdm import tqdm

from commons.reader import get_last_id

class PropertiesOutputParser(BaseModel):
    pressure: Optional[str] = Field(description="Applied pressure condition when Tc is detected")
    tc: Optional[str] = Field(description="Superconductors critical temperature, Tc")
    tc_type: Optional[str] = Field(
        description="Type of superconductors critical temperature, Tc. E.g. onset, zero temperature, Tc0, T onset, etc...")
    me_method: Optional[str] = Field(
        description="Method used to measure the Tc or superconductors critical temperature")


class ListOfProperitesOutputParser(BaseModel):
    properties: List[PropertiesOutputParser]

    @staticmethod
    def parse_to_list(obj):
        return obj.properties


class MeMethodOutputParser(BaseModel):
    name: str = Field(description="Methods used to measure the tc")
    description: str = Field(description="Additional information related to the me_method")


class PressureOutputParser(BaseModel):
    name: str = Field(description="Applied pressures to obtain tc")
    description: str = Field(description="additional information about the applied pressure")


class TcOutputParser(BaseModel):
    value: str = Field(description="Superconductors critical temperature, Tc. Composed by value and unit.")
    description: str = Field(description="Additional information about tc")


class ListOfTcOutputParser(BaseModel):
    tcs: List[TcOutputParser]

    @staticmethod
    def parse_to_list(obj):
        return [item.value for item in obj.tcs]


class ListOfPressureOutputParser(BaseModel):
    pressures: List[PressureOutputParser]

    @staticmethod
    def parse_to_list(obj):
        return [item.name for item in obj.pressures]


class ListOfMeMethodOutputParser(BaseModel):
    me_methods: List[MeMethodOutputParser]

    @staticmethod
    def parse_to_list(obj):
        return [item.name for item in obj.me_methods]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Data preparation for materials extraction using OpenAI LLMs")

    parser.add_argument("--input-text", help="Input CSV/TSV file containing text", required=True)
    parser.add_argument("--model", choices=CHATS.keys(), default="chatgpt")
    parser.add_argument("--config", help="Configuration file", default="resources/config/config.yaml")
    parser.add_argument("--output", help="Output CSV/TSV file", required=True)
    args = parser.parse_args()

    input = args.input_text
    output = args.output
    model = args.model
    config_file = args.config

    llm = CHATS[model]

    if 'pl_tags' in llm:
        llm.pl_tags.append("evaluation")
        llm.pl_tags.append("ner")
        llm.pl_tags.append("few-shot")

    input_path = Path(input)
    if os.path.isdir(str(output)):
        output_path = os.path.join(output, "{}.{}.few-shot.output.csv".format(input_path.stem, model))
    else:
        output_path = Path(output)

    config = GrobidClientGeneric().load_yaml_config_from_file(config_file)
    materials_client = GrobidClientGeneric()
    config_materials = {
        'grobid': config['superconductors'],
        'max_retry': config['max_retry'],
        'sleep_time': config['sleep_time'],
        'coordinates': config['coordinates'],
        'batch_size': config['batch_size']
    }

    materials_client.set_config(config_materials)
    grobid_material_processor = GrobidMaterialsProcessor(materials_client)

    last_id_material = get_last_id(output_path)

    data_input = prepare_data(input)

    with open(output_path, encoding="utf-8", mode='a') as fom:
        fwm = csv.writer(fom, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for idx, example in tqdm(enumerate(data_input), desc="record"):
            id = example['id']

            id_n = int(id)
            if last_id_material > 0 and id_n <= int(last_id_material):
                print("Skip material", id_n)
                continue

            filename = example['filename']
            paragraph_id = int(example['pid'])
            text = example['text']

            hints = [entity['raw_value'] for entity in grobid_material_processor.extract_materials(text)]

            try:
                output_data_materials_parsed = extract_entities(text, PROMPT_TEMPLATE_CHAT_USER_MATERIALS_SIMPLE, llm,
                                                                output_parser_class=ListOfMaterialsOutputParser, hints=hints)
            except OutputParserException as ope:
                output_data_raw = extract_entities(text, PROMPT_TEMPLATE_CHAT_USER_MATERIALS_SIMPLE, llm, hints=hints)
                if output_data_raw and output_data_raw == "None":
                    continue
                output_parser = PydanticOutputParser(pydantic_object=ListOfMaterialsOutputParser)
                parsed_output = _parse_json(output_data_raw, llm, output_parser=output_parser)
                output_data_materials_parsed = ListOfMaterialsOutputParser.parse_to_list(parsed_output)

            fwm.writerows(
                [[id, filename, paragraph_id, result] for result in output_data_materials_parsed])
