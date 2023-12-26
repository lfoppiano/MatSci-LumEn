import argparse
import csv
import os
from pathlib import Path

import dotenv
from document_qa.grobid_processors import GrobidQuantitiesProcessor
from grobid_quantities.quantities import QuantitiesAPI
from langchain.output_parsers import PydanticOutputParser
from langchain.schema import OutputParserException

from commons.grobid.grobid_client_generic import GrobidClientGeneric
from commons.openai import CHATS
from llm_mat_evaluation.ner.process_openai_ner_properties import prepare_data, extract_entities, \
    PROMPT_TEMPLATE_CHAT_USER_QUANTITIES, ListOfQuantitiesOutputParser, _parse_json

dotenv.load_dotenv(override=True)

from tqdm import tqdm

from commons.reader import get_last_id


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Data preparation for the extraction quantities using using OpenAI LLM")

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

    config = GrobidClientGeneric().load_yaml_config_from_file(config_file)
    quantities_client = QuantitiesAPI(config['quantities']['server'], check_server=True)
    grobid_quantities_processor = GrobidQuantitiesProcessor(quantities_client)

    input_path = Path(input)
    output_path = Path(output)
    if os.path.isdir(str(output)):
        output_path = os.path.join(output, "{}.{}.few-shot.output.csv".format(input_path.stem, model))
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
                skip_quantities = True

            filename = example['filename']
            paragraph_id = int(example['pid'])
            text = example['text']

            hints = [entity['text'] for entity in grobid_quantities_processor.extract_quantities(text)]

            try:
                output_data_quantities = extract_entities(text, PROMPT_TEMPLATE_CHAT_USER_QUANTITIES, llm,
                                                          output_parser_class=ListOfQuantitiesOutputParser, hints=hints)
            except OutputParserException as ope:
                output_data_quantities_raw = extract_entities(text, PROMPT_TEMPLATE_CHAT_USER_QUANTITIES, llm, hints=hints)
                if output_data_quantities_raw.startswith("I don't know") or output_data_quantities_raw.startswith("None"):
                    continue
                output_parser = PydanticOutputParser(pydantic_object=ListOfQuantitiesOutputParser)
                parsed_output = _parse_json(output_data_quantities_raw, llm, output_parser=output_parser)
                output_data_quantities = ListOfQuantitiesOutputParser.parse_to_list(parsed_output)

            fwq.writerows([[id, filename, paragraph_id, result] for result in output_data_quantities])
