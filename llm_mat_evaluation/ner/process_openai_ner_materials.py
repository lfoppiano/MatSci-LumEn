import argparse
import csv
import os
from pathlib import Path
from typing import List, Optional

import dotenv
from langchain.schema import OutputParserException

from commons.ner import prepare_data
from llm_mat_evaluation.properties.process_openai_ner_properties import extract_entities, _parse_json
from commons.openai import CHATS

dotenv.load_dotenv(override=True)

from langchain.output_parsers import PydanticOutputParser
from pydantic import Field, BaseModel
from tqdm import tqdm

from commons.reader import get_last_id

PROMPT_TEMPLATE_CHAT_SYSTEM = """Use the following pieces of context to answer the users question. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
----------------\n{text}"""

PROMPT_TEMPLATE_CHAT_USER_MATERIALS_SIMPLE = """Extract all materials expressed in any way (formula, sample name, material name, etc). Avoid repetition if you can."""

PROMPT_TEMPLATE_CHAT_USER_MATERIALS_COMPLEX = """What are the superconductors materials mentioned in the text? 
Only provide the mention of the materials. Avoid repetition. 

The material can be expressed as follow:
- chemical formula with variables not substituted, like La(1-x)Fe(x),
- chemical formula with substitution variable like Zr 5 X 3 (X = Sb, Pb, Sn, Ge, Si and Al)
- with complete or partial abbreviations like (TMTSF) 2 PF 6,
- doping rates represented as variables (x, y or other letters) appearing in the material names. These values can be used to complement the material variables (e.g. LaFexO1-x).
- doping rates as percentages, like 4% Hdoped sample or 14% Cu doped sample
- material chemical form with no variables e.g. LaFe03NaCl2 where the doping rates are included in the name
- chemical substitution or replacements, like (A is a random variable, can be any symbol): A = Ni, Cu, A = Ni, Ni substituted (which means A = Ni)
- chemical substitution with doping ratio, like (A is a random variable, can be any symbol): A = Ni and x = 0.2

If you don't know the answer, just answer None, don't try to make up an answer."""


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


class MaterialsOutputParser(BaseModel):
    name: str = Field(description="Materials names, chemical formulas, etc. ")


class ListOfMaterialsOutputParser(BaseModel):
    materials: List[MaterialsOutputParser]

    @staticmethod
    def parse_to_list(obj):
        return [material.name for material in obj.materials]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Implementation NER with LLM (GPT3) on Superconductors materials")

    parser.add_argument("--input-text", help="Input CSV/TSV file containing text", required=True)
    parser.add_argument("--model", choices=CHATS.keys(), default="chatgpt")
    parser.add_argument("--output", help="Output CSV file or directory", required=True)
    args = parser.parse_args()

    input = args.input_text
    output = args.output
    model = args.model

    llm = CHATS[model]

    if 'pl_tags' in llm:
        llm.pl_tags.append("evaluation")
        llm.pl_tags.append("ner")

    input_path = Path(input)

    if os.path.isdir(str(output)):
        output_path = os.path.join(output, "{}.{}.output.csv".format(input_path.stem, model))
    else:
        output_path = Path(output)

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

            try:
                output_data_materials_parsed = extract_entities(text, PROMPT_TEMPLATE_CHAT_USER_MATERIALS_COMPLEX, llm,
                                                                output_parser_class=ListOfMaterialsOutputParser)

            except OutputParserException as ope:
                output_data_raw = extract_entities(text, PROMPT_TEMPLATE_CHAT_USER_MATERIALS_COMPLEX, llm)
                if output_data_raw and output_data_raw == "None":
                    continue
                output_parser = PydanticOutputParser(pydantic_object=ListOfMaterialsOutputParser)
                parsed_output = _parse_json(output_data_raw, llm, output_parser=output_parser)
                output_data_materials_parsed = ListOfMaterialsOutputParser.parse_to_list(parsed_output)

            fwm.writerows(
                [[id, filename, paragraph_id, result] for result in output_data_materials_parsed])
