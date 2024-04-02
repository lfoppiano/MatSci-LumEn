import argparse
from typing import Union

import dotenv
from tqdm import tqdm

from commons.evaluation import calculate_metrics
from commons.grobid.material_parsers_client import MaterialParsersClient

dotenv.load_dotenv(override=True)

from commons.reader import load_texts_and_classes_generic, group_by
from commons.writer import print_markdown


class FormulaMatcher:
    def __init__(self, base_url="http://localhost:8090"):
        self.materials_client = MaterialParsersClient(base_url=base_url, ping=True)

    @staticmethod
    def output_info(result):
        results = []
        for position_material in result:
            compositions = []
            for material in position_material:
                if 'resolvedFormulas' in material:
                    for resolved_formula in material['resolvedFormulas']:
                        if 'formulaComposition' in resolved_formula:
                            compositions.append(resolved_formula['formulaComposition'])
                elif 'formula' in material:
                    if 'formulaComposition' in material['formula']:
                        compositions.append(material['formula']['formulaComposition'])
                if 'name' in material:
                    compositions.append(material['name'])
            results.append(compositions)
        return results

    def parse_materials(self, text):
        status, result = self.materials_client.parse_materials(text)

        if status != 200:
            result = []

        results = self.output_info(result)

        return results


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
                if type(composition_expected) is dict and type(composition_predicted) is dict:
                    if compare_compositions(composition_expected, composition_predicted):
                        return True
                elif type(composition_expected) is str and type(composition_predicted) is str:
                    return composition_expected == composition_predicted
        return False
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


def calculate_and_print_scores_and_gain(expected_dict, predicted_dict, grobid_processor, verbose):
    from llm_mat_evaluation.ner.eval_ner import evaluate
    tp_strict, fp_strict, fn_strict = evaluate(expected_dict, predicted_dict, matching_type="strict")

    not_matched_strict = {filename: [[idx, en_fp[0], en_fp[1]] for idx, en_fp in enumerate(elements)] for
                          filename, elements in fp_strict.items()}

    matching_by_filename = {filename: [value['expected'] for value in values] for filename, values in
                            tp_strict.items()}
    new_expected = {filename: [item for item in values if item[2] not in matching_by_filename[filename]] for
                    filename, values in expected_dict.items()}

    from llm_mat_evaluation.ner.eval_formulas import evaluate
    tp_formulas, fp_formulas, fn_formulas = evaluate(new_expected, not_matched_strict, grobid_processor, verbose)

    precision_micro_avg_strict, recall_micro_avg_strict, f1_score_micro_avg_strict, _, _, _ = calculate_metrics(
        tp_strict, fp_strict, fn_strict)

    new_tp_formulas = {filename: [m for m in matches] for filename, matches in tp_formulas.items()}

    for key, value in new_tp_formulas.items():
        value += tp_strict[key] if key in tp_strict else []

    precision_micro_avg_formulas, recall_micro_avg_formulas, f1_score_micro_avg_formulas, _, _, _ = calculate_metrics(
        new_tp_formulas, fp_formulas, fn_formulas)

    print("Scores: ")
    print(f"- strict, P: {precision_micro_avg_strict}, R: {recall_micro_avg_strict}, F1: {f1_score_micro_avg_strict}")
    print(f"- formulas, P: {precision_micro_avg_formulas}, R: {recall_micro_avg_formulas}, F1: {f1_score_micro_avg_formulas}")

    print("\n")
    print(print_markdown(result_table))

    print(
        f"Gain F1: {f1_score_micro_avg_formulas - f1_score_micro_avg_strict} (+{f1_score_micro_avg_formulas / f1_score_micro_avg_strict * 100})")
    print("Matches with the formula that were not matching with the strict matching: ")

    for filename, matches in tp_formulas.items():
        print(f"\t{filename}")
        for item in matches:
            print(f"\t\t{item['expected']}\n\t\t{item['predicted']}")
            print()

        print("--------")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Evaluation of the formula matching, as compared with the strict matching: "
                    "how many element that are not matching with strict matching, are actually matching with formula? ")

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
    parser.add_argument("--base-url",
                        help="Formula matcher base url",
                        default="http://localhost:8090",
                        required=False)

    args = parser.parse_args()

    predicted_path = args.predicted
    expected_path = args.expected
    verbose = args.verbose

    grobid_processor = FormulaMatcher(base_url=args.base_url)

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

    calculate_and_print_scores_and_gain(expected_dict, predicted_dict, grobid_processor, verbose)
