import argparse
from typing import Union

import dotenv
from document_qa.grobid_processors import GrobidMaterialsProcessor
from tqdm import tqdm

from commons.evaluation import calculate_metrics
from commons.grobid_client_generic import GrobidClientGeneric

dotenv.load_dotenv(override=True)

from commons.reader import load_texts_and_classes_generic, group_by
from commons.writer import print_markdown


def get_processor():
    materials_client = GrobidClientGeneric(ping=True)
    config_materials = {
        'grobid': {
            # "server": "http://falcon.nims.go.jp/superconductors/stable",
            "server": "http://falcon.nims.go.jp/material/nlp/unstable",
            # "server": "http://localhost:8090",
            "url_mapping": {
                "processText": "/service/process/text",
                "processText_disable_linking": "/service/process/text?disableLinking=true",
                # "parseMaterial": "/service/material/parse",
                # "parseMaterials": "/service/material/multiparse",
                "parseMaterial": "/process/material",
                "parseMaterials": "/process/material",
                "ping": "/"
            }
        }
    }

    materials_client.set_config(config_materials, ping=False)
    return materials_client


def compare_compositions(compositions_expected: list, compositions_predicted: list) -> Union[bool, None]:
    for element in compositions_expected:
        if element in compositions_predicted:
            if compositions_expected[element] != compositions_predicted[element]:
                return False
        else:
            return False

    return True


def match_by_formula(expected, predicted):
    if expected and str.lower(expected[0].strip()) != str.lower(predicted[0].strip()):
        compositions_expected = expected[1]
        compositions_predicted = predicted[1]

        for composition_expected in compositions_expected:
            for composition_predicted in compositions_predicted:
                if compare_compositions(composition_expected, composition_predicted):
                    # with open("matching.3.formula.csv", 'a') as ftp:
                    #     ftp.write(f'"{predicted}","{expected}"\n')
                    return True
    else:
        return True


def get_matches(expected_entities, predicted_entities, verbose=False) -> (list, list, list):
    if verbose:
        print("-> Expected:", expected_entities, "\n-> Predicted:", predicted_entities)

    tp = []
    fp = []
    fn = []

    skip_predicted_idx = []
    skip_expected_idx = []
    for idxp, predicted_entity in enumerate(predicted_entities):
        if idxp in skip_predicted_idx:
            continue

        is_match = False
        for idxe, expected_entity in enumerate(expected_entities):

            if idxe in skip_expected_idx:
                continue

            full_object = {
                "expected": expected_entity,
                "predicted": predicted_entity
            }

            if match_by_formula(expected_entity, predicted_entity):
                tp.append(full_object)

                skip_predicted_idx.append(idxp)
                skip_expected_idx.append(idxe)
                is_match = True
                break

        if is_match is False:
            fp.append(predicted_entity)
            # with open("not_matching.formula.csv", 'a') as ftp:
            #     ftp.write(f'"{predicted_entity}"\n')

    # fn, entities I did not predict that are expected
    for idxe, expected_entity in enumerate(expected_entities):
        if idxe not in skip_expected_idx:
            fn.append(expected_entity)

    assert "FP+TP != nb of predicted", len(tp) + len(fp) == len(predicted_entities)
    assert "FP+FN != nb of expected", len(tp) + len(fn) == len(expected_entities)

    return tp, fp, fn


def evaluate(expected_dict, predicted_dict, verbose=False):
    grobid_processor = GrobidMaterialsProcessor(get_processor())

    tp_by_filename = {}
    fn_by_filename = {}
    fp_by_filename = {}
    for filename in tqdm(expected_dict.keys()):

        if verbose:
            print("==>", filename)

        if filename not in tp_by_filename:
            tp_by_filename[filename] = []

        if filename not in fn_by_filename:
            fn_by_filename[filename] = []

        if filename not in fp_by_filename:
            fp_by_filename[filename] = []

        expected_records = expected_dict[filename]

        # We remove the expected entities that cannot be parsed.
        records = [record[2] for record in expected_records]
        records_as_text = "\n".join(records)
        parsed_records = grobid_processor.parse_materials(records_as_text)
        for idx, record in enumerate(expected_records):
            record.append(parsed_records[idx])

        if filename not in predicted_dict.keys():
            continue

        predicted_records = predicted_dict[filename]

        records = [record[2] for record in predicted_records]
        records_as_text = "\n".join(records)
        parsed_records = grobid_processor.parse_materials(records_as_text)
        for idx, record in enumerate(predicted_records):
            record.append(parsed_records[idx])

        expected_records_by_pid = group_by(expected_records, 1)
        predicted_records_by_pid = group_by(predicted_records, 1)

        for pid in expected_records_by_pid.keys():
            if pid not in predicted_records_by_pid:
                continue
            predicted_in_pid = [x[1:3] for x in predicted_records_by_pid[pid]]
            expected_in_pid = [x[1:3] for x in expected_records_by_pid[pid]]

            tp, fp, fn = get_matches(expected_in_pid, predicted_in_pid, verbose)

            tp_by_filename[filename] += tp
            fp_by_filename[filename] += fp
            fn_by_filename[filename] += fn

    return tp_by_filename, fp_by_filename, fn_by_filename


def calculate_scores(expected_dict, predicted_dict, verbose):
    tp, fp, fn = evaluate(expected_dict, predicted_dict, verbose)

    return calculate_metrics(fn, fp, tp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Evaluation of extracted materials by a formula comparison")

    parser.add_argument("--predicted",
                        help="Predicted dataset",
                        required=True)
    parser.add_argument("--expected",
                        help="Expected dataset",
                        required=True)
    parser.add_argument("--verbose",
                        help="Enable tons of prints",
                        required=False,
                        default=False, action="store_true")

    args = parser.parse_args()

    predicted_path = args.predicted
    expected_path = args.expected
    verbose = args.verbose

    predicted, _ = load_texts_and_classes_generic(predicted_path)
    files_predicted = set([str.strip(x[1]) for x in predicted])
    expected, _ = load_texts_and_classes_generic(expected_path)
    files_expected = set([str.strip(x[1]) for x in expected])

    print("Predicted records:", len(predicted), ", files:", len(files_predicted), ", input:", predicted_path)
    print("Expected records:", len(expected), ", files:", len(files_expected), ", input:", expected_path)

    predicted_dict = group_by(predicted, 1)
    expected_dict = group_by(expected, 1)

    for filename in predicted_dict.keys():
        predicted_dict[filename] = [item for i, item in enumerate(predicted_dict[filename]) if
                                    item[2] not in [x[2] for x in predicted_dict[filename][:i]]]
    for filename in expected_dict.keys():
        expected_dict[filename] = [item for i, item in enumerate(expected_dict[filename]) if
                                   item[2] not in [x[2] for x in expected_dict[filename][:i]]]

    result_table = [["Avg. Type", "Method", "Precision", "Recall", "F1-score", "Support"]]

    precision_micro_avg, recall_micro_avg, f1_score_micro_avg, precision_macro_avg, recall_macro_avg, f1_score_macro_avg = calculate_scores(
        expected_dict, predicted_dict, verbose)
    result_table.append(
        ["micro", "formula", precision_micro_avg, recall_micro_avg, f1_score_micro_avg, str(len(predicted))])
    result_table.append(
        ["macro", "formula", precision_macro_avg, recall_macro_avg, f1_score_macro_avg, str(len(predicted))])

    print("\n")
    print(print_markdown(result_table))
