import argparse
import csv
import os
from pathlib import Path
from typing import List, Optional

import dotenv
dotenv.load_dotenv(override=True)

from langchain import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema import OutputParserException
from pydantic import Field, BaseModel

from commons.ner import prepare_data
from commons.openai import CHATS

from tqdm import tqdm

from commons.reader import get_last_id

PROMPT_TEMPLATE_CHAT_SYSTEM = """Use the following pieces of context to answer the users question. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
----------------\n{text}"""

PROMPT_TEMPLATE_CHAT_USER_QUANTITIES = """Quantity is either a Count, consisting of a value, or a Measurement, 
consisting of a value and usually a unit. A Quantity can additionally include optional Modifiers like tolerances.
Include relevant text that indicates the application of a modifier, such as "between" "less than" "approximately", 
or symbols such as ">" or "~" if they are contiguous with the span. Ignore them if they are separated by additional text.
 
Example: "The soda can's volume was 355 ml", the quantity is "355 ml".

Extract all the Quantities in the text. If you don't know the answer, just answer None, don't try to make up an answer."""


class QuantitiesOutputParser(BaseModel):
    quantity: Optional[str] = Field(description="Quantity")
    name: Optional[str] = Field(description="Measurement name or property it refers to")


class ListOfQuantitiesOutputParser(BaseModel):
    quantities: List[QuantitiesOutputParser]

    @staticmethod
    def parse_to_list(obj):
        return [quantity.quantity for quantity in obj.quantities]

class ListOfQuantitiesFtOutputParser(BaseModel):
    quantities: List[str]

    @staticmethod
    def parse_to_list(obj):
        return obj.quantities


def get_prompt(user_template, format_instructions=None, hints=None) -> ChatPromptTemplate:
    system_message_prompt = SystemMessagePromptTemplate.from_template(PROMPT_TEMPLATE_CHAT_SYSTEM)
    human_message_prompt = HumanMessagePromptTemplate.from_template(user_template)
    if hints:
        user_template += "\nHere some examples appearing in the text: " + str(hints)

    if format_instructions:
        user_template += "\n{format_instructions}"

        human_message_prompt = HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                template=user_template,
                input_variables=[],
                partial_variables={"format_instructions": format_instructions})
        )

    prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    return prompt


def extract_entities(text, prompt_template, llm, output_parser_class=None, hints=None):
    format_instructions = None
    if output_parser_class:
        output_parser = PydanticOutputParser(pydantic_object=output_parser_class)
        format_instructions = output_parser.get_format_instructions()

    prompt_chat_template = get_prompt(prompt_template, format_instructions, hints=hints)
    prompt_text = prompt_chat_template.format_messages(text=text)
    # print("Nb Tokens", chat.get_num_tokens_from_messages(prompt_text))

    results = llm(prompt_text)

    if output_parser_class:
        output = output_parser.parse(results.content)
        output = output_parser_class.parse_to_list(output)
    else:
        output = results.content

    return output


def _parse_json(response, llm, output_parser):
    system_message = "You are an useful assistant expert in materials science, physics, and chemistry " \
                     "that can process text and transform it to JSON."
    human_message = """Transform the text between three double quotes in JSON.\n\n\n\n
        {format_instructions}\n\nText: \"\"\"{text}\"\"\""""

    system_message_prompt = SystemMessagePromptTemplate.from_template(system_message)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_message)

    prompt_template = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    results = llm(
        prompt_template.format_prompt(
            text=response,
            format_instructions=output_parser.get_format_instructions()
        ).to_messages()
    )
    parsed_output = output_parser.parse(results.content)

    return parsed_output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Data preparation for the properties extraction using OpenAI LLMs")

    parser.add_argument("--input", help="Input CSV/TSV file", required=True)
    parser.add_argument("--output", help="Output file, support both JSON, CSV, or TSV", required=True)
    parser.add_argument("--config", help="Configuration file", default="resources/config/config.yaml")
    parser.add_argument("--model", choices=CHATS.keys(), default="chatgpt")

    args = parser.parse_args()

    input = args.input
    output = args.output
    config_file = args.config
    model = args.model

    llm = CHATS[model]

    if 'pl_tags' in llm:
        llm.pl_tags.append("evaluation")
        llm.pl_tags.append("ner")
        llm.pl_tags.append("quantities")

    input_path = Path(input)
    output_path = Path(output)

    if os.path.isdir(str(output)):
        output_path = os.path.join(output, "{}.{}.output.csv".format(input_path.stem, model))
    else:
        output_path = Path(output)

    last_id_quantities = get_last_id(Path(output_path))

    data_input = prepare_data(input)

    with open(output_path, encoding="utf-8", mode='a') as foq:
        fwq = csv.writer(foq, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for idx, example in tqdm(enumerate(data_input), desc="record"):
            id = example['id']

            id_n = int(id)
            if last_id_quantities > 0 and id_n <= int(last_id_quantities):
                print("Skip quantity", id_n)
                continue

            filename = example['filename']
            paragraph_id = int(example['pid'])
            text = example['text']

            output_parser_class = ListOfQuantitiesFtOutputParser if llm.model_name.startswith("ft:") else ListOfQuantitiesOutputParser
            try:
                output_data_quantities = extract_entities(text, PROMPT_TEMPLATE_CHAT_USER_QUANTITIES, llm,
                                                          output_parser_class=output_parser_class)
            except OutputParserException as ope:
                output_data_quantities_raw = extract_entities(text, PROMPT_TEMPLATE_CHAT_USER_QUANTITIES, llm)
                if output_data_quantities_raw.startswith("I don't know") or output_data_quantities_raw.startswith("None"):
                    continue
                output_parser = PydanticOutputParser(pydantic_object=output_parser_class)
                parsed_output = _parse_json(output_data_quantities_raw, llm, output_parser=output_parser)
                output_data_quantities = output_parser_class.parse_to_list(parsed_output)

            fwq.writerows([[id, filename, paragraph_id, result] for result in output_data_quantities])
