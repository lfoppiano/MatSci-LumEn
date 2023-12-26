import argparse

import dotenv
from tqdm import tqdm

dotenv.load_dotenv(override=True)

from commons.evaluation import MATCHING_TYPES, match, get_matches, calculate_metrics
from commons.reader import load_texts_and_classes_generic, group_by
from commons.writer import print_markdown


def evaluate(expected_dict, predicted_dict, matching_type, matching_threshold=None, verbose=False, sbert=None):
    if not sbert:
        if matching_type == "sbert":
            from sentence_transformers import SentenceTransformer
            sbert = SentenceTransformer('all-MiniLM-L6-v2')
        elif matching_type == "sbert_cross":
            from sentence_transformers import CrossEncoder
            sbert = CrossEncoder('stsb-distilroberta-base')

    tp_by_filename = {}
    fn_by_filename = {}
    fp_by_filename = {}
    for filename in tqdm(expected_dict.keys(), desc=matching_type):

        if verbose:
            print("==>", filename)

        if filename not in tp_by_filename:
            tp_by_filename[filename] = []

        if filename not in fn_by_filename:
            fn_by_filename[filename] = []

        if filename not in fp_by_filename:
            fp_by_filename[filename] = []

        expected_records = expected_dict[filename]
        if filename not in predicted_dict.keys():
            continue

        predicted_records = predicted_dict[filename]

        expected_records_by_pid = group_by(expected_records, 1)
        predicted_records_by_pid = group_by(predicted_records, 1)

        for pid in expected_records_by_pid.keys():
            if pid not in predicted_records_by_pid:
                continue
            predicted_in_pid = [x[1] for x in predicted_records_by_pid[pid]]
            expected_in_pid = [x[1] for x in expected_records_by_pid[pid]]

            tp, fp, fn = get_matches(expected_in_pid,
                                     predicted_in_pid,
                                     matching_type,
                                     matching_threshold,
                                     sbert=sbert,
                                     verbose=verbose)
            if verbose:
                print("\t- fp: {}\n\t- fn: {}".format(fp, fn))
            tp_by_filename[filename] += tp
            fp_by_filename[filename] += fp
            fn_by_filename[filename] += fn

            # with open("not_matching.strict.csv", 'a') as ftp:
            #     for t in fp:
            #         ftp.write(f'"",{filename}, {pid}, "{t}"\n')
            # for f in fn:
            #     ftp.write(f'"",{filename}, {pid}, "{f}"\n')

    return tp_by_filename, fp_by_filename, fn_by_filename


def print_results(matches_by_filename, entity_type, matching_type, expected_count, verbose=False):
    matches = [j for v in matches_by_filename.values() if len(v) > 0 for j in v]

    accuracy_full_match = len(matches) / expected_count * 100 if expected_count > 0 else 0

    # if verbose:
    #     print("Matches by filename")
    #     for filename in matches_by_filename.keys():
    #         print("->", filename)
    #         for matches in matches_by_filename[filename]:
    #             print_match(matches)

    print("\nResults")
    print("\tMatching type:", matching_type)
    print("\tMatching", entity_type, len(matches), "\n\t\tAccuracy",
          accuracy_full_match)


def print_match(match):
    print("\t", match['expected'], "\t-> ", match['predicted'])
    print("--")


def calculate_scores(expected_dict, predicted_dict, mt, matching_threshold, verbose):
    tp, fp, fn = evaluate(expected_dict, predicted_dict, mt, matching_threshold,
                          verbose, sbert=None)
    return calculate_metrics(fn, fp, tp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Evaluation of extracted entities")

    parser.add_argument("--predicted", help="Predicted dataset", required=True)
    parser.add_argument("--expected", help="Expected dataset", required=True)

    parser.add_argument("--entity-type", help="Types of entities to evaluate",
                        choices=["material", "property"],
                        required=True,
                        default="material")

    parser.add_argument("--matching-type", help="Type of matching", choices=MATCHING_TYPES, default="all",
                        required=False)
    parser.add_argument("--threshold", help="Matching threshold", required=False, type=float, default=0.9)

    parser.add_argument("--verbose", help="Enable tons of prints", required=False, default=False, action="store_true")

    args = parser.parse_args()

    predicted_path = args.predicted
    expected_path = args.expected
    matching_type = args.matching_type
    matching_threshold = args.threshold if args.threshold <= 1.0 else args.threshold / 100
    verbose = args.verbose
    entity_type = args.entity_type

    predicted, _ = load_texts_and_classes_generic(predicted_path)
    files_predicted = set([str.strip(x[1]) for x in predicted])
    expected, _ = load_texts_and_classes_generic(expected_path)
    # if expected[0][0] == 'id':
    #     expected.pop(0)
    files_expected = set([str.strip(x[1]) for x in expected])

    print("Predicted records:", len(predicted), ", files:", len(files_predicted), ", input:", predicted_path)
    print("Expected records:", len(expected), ", files:", len(files_expected), ", input:", expected_path)

    predicted_dict = group_by(predicted, 1)
    expected_dict = group_by(expected, 1)

    if entity_type == "material":
        for filename in predicted_dict.keys():
            predicted_dict[filename] = [item for i, item in enumerate(predicted_dict[filename]) if
                                        item[2] not in [x[2] for x in predicted_dict[filename][:i]]]
        for filename in expected_dict.keys():
            expected_dict[filename] = [item for i, item in enumerate(expected_dict[filename]) if
                                       item[2] not in [x[2] for x in expected_dict[filename][:i]]]

    if matching_type == "all":
        result_table = [["Avg. type", "Method", "Precision", "Recall", "F1-score", "Support"]]

        for mt in filter(lambda m: m != 'all', MATCHING_TYPES):
            precision_micro_avg, recall_micro_avg, f1_score_micro_avg, precision_macro_avg, recall_macro_avg, f1_score_macro_avg = calculate_scores(
                expected_dict, predicted_dict, mt, matching_threshold, verbose)
            result_table.append(
                ["micro", mt, precision_micro_avg, recall_micro_avg, f1_score_micro_avg, str(len(predicted))])
            result_table.append(
                ["macro", mt, precision_macro_avg, recall_macro_avg, f1_score_macro_avg, str(len(predicted))])

        print("\n")
        print(print_markdown(result_table))
    else:
        result_table = [["Avg. type", "Method", "Precision", "Recall", "F1-score", "Support"]]

        precision_micro_avg, recall_micro_avg, f1_score_micro_avg, precision_macro_avg, recall_macro_avg, f1_score_macro_avg = calculate_scores(
            expected_dict, predicted_dict, matching_type, matching_threshold, verbose)
        result_table.append(
            ["micro", matching_type, precision_micro_avg, recall_micro_avg, f1_score_micro_avg, str(len(predicted))])
        result_table.append(
            ["macro", matching_type, precision_macro_avg, recall_macro_avg, f1_score_macro_avg, str(len(predicted))])

        print("\n")
        print(print_markdown(result_table))
