import argparse

from tqdm import tqdm

from commons.evaluation import match, MATCHING_TYPES_RE
from commons.reader import load_texts_and_classes_generic, group_by
from commons.writer import print_markdown


def match_relations(expected, predicted, matching_type, matching_threshold, model):
    matches = []
    matched_indices = set()
    if len(predicted) == 0:
        return matches

    # Iterate through copies of the lists
    for pred_index, pred_row in enumerate(predicted.copy()):
        for exp_index, exp_row in enumerate(expected.copy()):
            if exp_index in matched_indices:
                continue  # Skip already matched records in expected

            if all(((pred_val is None or str.strip(pred_val) in ('', 'unknown', 'null', 'none', 'None')) or match(exp_val, pred_val, matching_type,
                                                                                       matching_threshold, model=model))
                   for pred_val, exp_val in zip(pred_row, exp_row)):
                matches.append((pred_row, exp_row))
                matched_indices.add(exp_index)
                break

    return matches


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Evaluation extracted data")

    parser.add_argument("--predicted", help="Input dataset", required=True)
    parser.add_argument("--expected", help="Expected dataset", required=True)

    # parser.add_argument("--dataset", help="Domain on which evaluate", choices=domains_choice, required=False,
    #                     default="magdb")

    parser.add_argument("--matching-type", help="Type of matching", choices=MATCHING_TYPES_RE, default="strict")
    parser.add_argument("--threshold", help="Matching threshold", required=False, type=float, default=0.9)
    parser.add_argument("--verbose", help="Enable tons of prints", required=False, default=False, action="store_true")

    args = parser.parse_args()

    predicted_path = args.predicted
    expected_path = args.expected
    matching_type = args.matching_type
    matching_threshold = args.threshold if args.threshold <= 1.0 else args.threshold / 100
    verbose = args.verbose

    matching_types = [matching_type]
    if matching_type == "all":
        matching_types = [mt for mt in filter(lambda x: x != "all", MATCHING_TYPES_RE)]

    sbert_model = None
    if matching_type == 'sbert' or matching_type == "all":
        from sentence_transformers import CrossEncoder
        sbert_model = CrossEncoder('cross-encoder/stsb-distilroberta-base')

        if matching_type == 'sbert':
            matching_type = 'sbert_cross'
        elif matching_type == 'all':
            matching_types = list(filter(lambda mmt: mmt != "sbert", matching_types))

    predicted, _ = load_texts_and_classes_generic(predicted_path)
    files_predicted = set([str.strip(x[1]) for x in predicted])
    expected, _ = load_texts_and_classes_generic(expected_path)
    files_expected = set([str.strip(x[1]) for x in expected])

    print("Predicted records:", len(predicted), ", files:", len(files_predicted), ", input:", predicted_path)
    print("Expected records:", len(expected), ", files:", len(files_expected), ", input:", expected_path)

    predicted_by_filename = group_by(predicted, 1)
    expected_by_filename = group_by(expected, 1)

    evaluation_map = {}
    for mt in tqdm(matching_types):
        evaluation_map[mt] = evaluation_map_mt = {}
        for filename, expected_records in expected_by_filename.items():
            expected_records_by_pid = group_by(expected_records, 1)
            predicted_same_filename = predicted_by_filename[filename] if filename in predicted_by_filename else None

            evaluation_map_mt[filename] = evaluation_filename = {}

            if not predicted_same_filename:
                continue

            predicted_records_by_pid = group_by(predicted_same_filename, 1)
            for pid, pid_expected_records in expected_records_by_pid.items():

                expected_records_by_pid = [pe[1:5] for pe in pid_expected_records]
                if pid not in predicted_records_by_pid:
                    continue
                pid_predicted_records = [pr[1:5] for pr in predicted_records_by_pid[pid]]

                matching = match_relations(expected_records_by_pid, pid_predicted_records, mt, matching_threshold,
                                           model=sbert_model)

                tp = len(matching)
                fp = len(pid_predicted_records) - tp
                fn = len(pid_expected_records) - tp
                evaluation_filename[pid] = {
                    'tp': tp,
                    'fp': fp,
                    'fn': fn,
                    'matching': matching,
                    'expt': len(expected_records_by_pid),
                    'pred': len(pid_predicted_records)
                }

        # avg_macro_precision_mt = float(len(tp)) / len(predicted) * 100 if len(predicted) > 0 else 0.0
        # avg_macro_recall_mt = float(len(tp)) / len(expected) * 100 if len(expected) > 0 else 0.0

    # print(evaluation_map)

    results = []
    results.append(["Avg. type", "Matching type", "Precision", "Recall", "F1-score", "Support"])

    avg_macro_precision_by_mt = {}
    avg_macro_recall_by_mt = {}
    avg_macro_f1_by_mt = {}

    avg_micro_precision_by_mt = {}
    avg_micro_recall_by_mt = {}
    avg_micro_f1_by_mt = {}

    tp_by_mt = {}
    fp_by_mt = {}
    fn_by_mt = {}
    for mt, records_by_filename in evaluation_map.items():
        avg_macro_precision_by_mt[mt] = 0.0
        avg_macro_recall_by_mt[mt] = 0.0
        avg_macro_f1_by_mt[mt] = 0.0

        tp_by_mt[mt] = 0.0
        fp_by_mt[mt] = 0.0
        fn_by_mt[mt] = 0.0

        avg_macro_precision_by_filename = {}
        avg_macro_recall_by_filename = {}

        avg_micro_precision_by_filename = {}
        avg_micro_recall_by_filename = {}

        tp_by_filename = {}
        fp_by_filename = {}
        fn_by_filename = {}

        nb_paragraphs = 0
        for filename, records_by_pid in records_by_filename.items():
            avg_macro_precision_by_filename[filename] = 0.0
            avg_macro_recall_by_filename[filename] = 0.0

            tp_by_filename[filename] = sum([r['tp'] for pid, r in records_by_pid.items()])
            fp_by_filename[filename] = sum([r['fp'] for pid, r in records_by_pid.items()])
            fn_by_filename[filename] = sum([r['fn'] for pid, r in records_by_pid.items()])

            for pid, r in records_by_pid.items():
                avg_macro_precision_by_filename[filename] += r['tp'] / (r['tp'] + r['fp']) if (r['tp'] + r[
                    'fp']) > 0 else 0
                avg_macro_recall_by_filename[filename] += r['tp'] / (r['tp'] + r['fn']) if (r['tp'] + r[
                    'fn']) > 0 else 0
                nb_paragraphs += 1

            avg_micro_precision_by_filename[filename] = tp_by_filename[filename] / (
                        tp_by_filename[filename] + fp_by_filename[filename]) if (tp_by_filename[filename] +
                                                                                 fp_by_filename[filename]) > 0 else 0
            avg_micro_recall_by_filename[filename] = tp_by_filename[filename] / (
                        tp_by_filename[filename] + fn_by_filename[filename]) if (tp_by_filename[filename] +
                                                                                 fn_by_filename[filename]) > 0 else 0
        tp_by_mt[mt] += sum(tp_by_filename.values())
        fp_by_mt[mt] += sum(fp_by_filename.values())
        fn_by_mt[mt] += sum(fn_by_filename.values())

        avg_macro_precision_by_mt[mt] = sum(avg_macro_precision_by_filename.values()) / nb_paragraphs
        avg_macro_recall_by_mt[mt] = sum(avg_macro_recall_by_filename.values()) / nb_paragraphs
        avg_macro_f1_by_mt[mt] = 2 * (avg_macro_precision_by_mt[mt] * avg_macro_recall_by_mt[mt]) / (avg_macro_precision_by_mt[mt] + avg_macro_recall_by_mt[mt] )

        avg_micro_precision_by_mt[mt] = tp_by_mt[mt] / (tp_by_mt[mt] + fp_by_mt[mt]) if (tp_by_mt[mt] + fp_by_mt[mt]) > 0 else 0
        avg_micro_recall_by_mt[mt] = tp_by_mt[mt] / (tp_by_mt[mt] + fn_by_mt[mt]) if (tp_by_mt[mt] + fn_by_mt[mt]) > 0 else 0
        avg_micro_f1_by_mt[mt] = 2 * (avg_micro_precision_by_mt[mt] * avg_micro_recall_by_mt[mt] ) / (avg_micro_precision_by_mt[mt] + avg_micro_recall_by_mt[mt] )

        results.append(["micro", mt, avg_micro_precision_by_mt[mt], avg_micro_recall_by_mt[mt], avg_micro_f1_by_mt[mt], str(nb_paragraphs)])
        results.append(["macro", mt, avg_macro_precision_by_mt[mt], avg_macro_recall_by_mt[mt], avg_macro_f1_by_mt[mt], str(nb_paragraphs)])

    print(print_markdown(results))