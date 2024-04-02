import sys
from typing import Union

from sentence_transformers import util
from sklearn.metrics import accuracy_score
from textdistance import RatcliffObershelp
from tqdm import tqdm

from commons.reader import group_by

MATCHING_TYPES = ["all", "strict", "soft", "sbert_cross"]
MATCHING_TYPES_MATERIALS = ["all", "strict", "soft", "sbert_cross", "formulas"]
MATCHING_TYPES_RE = ["all", "strict", "soft"]

DEFAULT_SOFT_MATCHING_THRESHOLDS = {
    'soft': 0.7,
    'sbert': 0.7,
    'sbert_cross': 0.7,
    'strict': None,
    'formulas': None
}


def print_metrics(tp, tn, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (fn + tp)
    f1 = 2 * precision * recall / (precision + recall)
    print("tp", tp, ", fp", fp, "tn", tn, "fn", fn)
    print("p", precision, "r", recall, "f1", f1)


def evaluate(x_all, y_all, type):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    correct = 0
    wrong = 0
    y_neg = 0
    y_pos = 0
    y_predict1 = 0

    for idx, data in enumerate(x_all):

        measurements_count, relevant_measurements_count, measurements_with_quantified_object_count, materials_count = \
            get_features(data)

        if type == "quantities2":
            y_predict = predict_quantities2(measurements_count, relevant_measurements_count,
                                            measurements_with_quantified_object_count, materials_count)
        elif type == "quantities1":
            y_predict = predict_quantities1(relevant_measurements_count)
        else:
            print("Type not valid:", type)
            sys.exit(-1)

        if y_predict == 1:
            y_predict1 += 1

        y_expected = int(y_all[idx][0])

        if y_expected == 0:
            y_neg += 1

        if y_expected == 1:
            y_pos += 1

        if y_expected == y_predict:
            correct += 1
            if y_predict == 1:
                tp += 1
            else:
                tn += 1
        else:
            # print("Wrong:", x_all[idx][0:-1], "Result (predicted/real):", y_predict, y_all[idx][0])
            wrong += 1
            if y_predict == 0:
                fn += 1
            else:
                fp += 1

    print("Total valid items:", len(x_all))
    print("Total predicted = 1:", y_predict1)
    print("Negative examples:", y_neg, "positive examples:", y_pos)
    print_metrics(tp, tn, fp, fn)


def compare_compositions(compositions_expected: list, compositions_predicted: list) -> Union[bool, None]:
    for element in compositions_expected:
        if element in compositions_predicted:
            if compositions_expected[element] != compositions_predicted[element]:
                return False
        else:
            return False

    return True


def match_by_formula(expected, predicted):
    if expected and (str.lower(expected[0].strip()) != str.lower(predicted[0].strip())
                     and str.lower(expected[0].strip().replace(" ", "")) != str.lower(
                predicted[0].strip().replace(" ", ""))):
        compositions_expected = expected[1]
        compositions_predicted = predicted[1]

        for composition_expected in compositions_expected:
            for composition_predicted in compositions_predicted:
                if type(composition_expected) is dict and type(composition_predicted) is dict:
                    if compare_compositions(composition_expected, composition_predicted):
                        # with open("matching.3.formula.csv", 'a') as ftp:
                        #     ftp.write(f'"{predicted}","{expected}"\n')
                        return True
                elif type(composition_expected) is str and type(composition_predicted) is str:
                    return composition_expected == composition_predicted
        return False
    else:
        return True


def match(expected, predicted, matching_type, matching_threshold=None, verbose=False, model=None,
          grobid_processor=None):
    expected = "" if expected is None else expected
    predicted = "" if predicted is None else predicted
    if matching_type == "strict":
        return str.lower(expected) == str.lower(predicted)
    elif matching_type == "soft" and matching_threshold is not None:
        return RatcliffObershelp().normalized_similarity(str.lower(predicted),
                                                         str.lower(expected)) >= matching_threshold
    elif matching_type == "contains":
        return str.lower(predicted) in str.lower(expected) or str.lower(expected) in str.lower(predicted)
    elif matching_type == "sbert":
        if not model:
            from sentence_transformers import SentenceTransformer
            model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings_e = model.encode(str.lower(expected), convert_to_tensor=True, show_progress_bar=False)
        embeddings_p = model.encode(str.lower(predicted), convert_to_tensor=True, show_progress_bar=False)
        cosine_scores = util.cos_sim(embeddings_e, embeddings_p)
        return cosine_scores[0][0] > matching_threshold
    elif matching_type == "sbert_cross":
        if not model:
            from sentence_transformers import CrossEncoder
            model = CrossEncoder('cross-encoder/stsb-distilroberta-base')
        return model.predict([[predicted, expected]], show_progress_bar=False) > matching_threshold
    elif matching_type == "formulas":
        if not grobid_processor:
            raise Exception("GrobidProcessor should be initialised and passed when using formulas matching. ")
        parsed_expected_records = grobid_processor.parse_material(expected)
        if not predicted:
            return False
        parsed_predicted_records = grobid_processor.parse_material(predicted)

        return match_by_formula([expected, parsed_expected_records], [predicted, parsed_predicted_records])
    else:
        print("Invalid matching type:", matching_type, ". Please check how to use it, --help")
        return 0


def get_matches(expected_entities, predicted_entities, matching_type="soft", matching_threshold=0.8, verbose=False,
                sbert=None) -> (list, list, list):
    if verbose:
        print("-> Expected:", expected_entities, "\n-> Predicted:", predicted_entities)

    tp = []
    fp = []
    fn = []

    skip_predicted_idx = []
    skip_expected_idx = []
    for idxp, predicted_entity_ in enumerate(predicted_entities):
        if idxp in skip_predicted_idx:
            continue
        predicted_entity = predicted_entity_.strip()
        is_match = False
        for idxe, expected_entity_ in enumerate(expected_entities):
            expected_entity = expected_entity_.strip()

            if idxe in skip_expected_idx:
                continue

            full_object = {
                "expected": expected_entity,
                "predicted": predicted_entity
            }

            if match(predicted_entity, expected_entity, matching_type, matching_threshold, model=sbert):
                tp.append(full_object)

                skip_predicted_idx.append(idxp)
                skip_expected_idx.append(idxe)
                is_match = True
                break

        if is_match is False:
            fp.append(predicted_entity)

    # fn, entities I did not predict that are expected
    for idxe, expected_entity in enumerate(expected_entities):
        if idxe not in skip_expected_idx:
            fn.append(expected_entity)

    assert "FP+TP != nb of predicted", len(tp) + len(fp) == len(predicted_entities)
    assert "FP+FN != nb of expected", len(tp) + len(fn) == len(expected_entities)

    return tp, fp, fn


def predict_quantities1(relevant_measurements_count):
    return 1 if relevant_measurements_count > 0 else 0


def predict_quantities2(measurements_count, relevant_measurements_count, measurements_with_quantified_object_count,
                        materials_count):
    return 1 if relevant_measurements_count > 0 \
                and measurements_with_quantified_object_count > 0 \
                and materials_count > 0 \
        else 0


def evaluate_magnetic(expected_dict, predicted_dict, matching_type, matching_threshold=None, verbose=False):
    full_matching_by_filename = {}
    partial_matching_by_filename = {}
    for filename in expected_dict.keys():

        if verbose:
            print("==>", filename)

        if filename not in full_matching_by_filename:
            full_matching_by_filename[filename] = []

        if filename not in partial_matching_by_filename:
            partial_matching_by_filename[filename] = []

        expected_records = expected_dict[filename]
        if filename not in predicted_dict.keys():
            continue

        predicted_records = predicted_dict[filename]

        expected_records_by_pid = group_by(expected_records, 1)
        predicted_records_by_pid = group_by(predicted_records, 1)

        for pid in expected_records_by_pid.keys():
            if pid not in predicted_records_by_pid:
                continue
            predicted_in_pid = predicted_records_by_pid[pid]
            expected_in_pid = expected_records_by_pid[pid]
            full_matches, partial_matches = get_matches(expected_in_pid, predicted_in_pid, matching_type,
                                                        matching_threshold)
            full_matching_by_filename[filename] += full_matches
            partial_matching_by_filename[filename] += partial_matches

    return full_matching_by_filename, partial_matching_by_filename


def get_features(data):
    measurements_count = int(data[3])
    relevant_measurements_count = int(data[4])
    measurements_with_quantified_object_count = int(data[5])
    materials_count = int(data[6])
    return measurements_count, relevant_measurements_count, measurements_with_quantified_object_count, materials_count


def calculate_matching(grouped_by_filename, matching_type, threshold, verbose, cleanup_predicted_value=None,
                       sbert_model=None, grobid_processor=None):
    predicted_all = []
    expected_all = []

    if verbose:
        print("Accuracy")

    for filename, rows in tqdm(grouped_by_filename.items(), desc="Processing file", unit="file"):
        predicted_in_file = []
        expected_in_file = []

        for row in rows:
            id = int(row[0])
            expected = row[1]
            expected_in_file.append(expected)

            predicted = row[2]

            if predicted is None:
                predicted_in_file.append("")
                is_matching = False
            else:
                if cleanup_predicted_value:
                    predicted_clean = cleanup_predicted_value(predicted)
                else:
                    predicted_clean = predicted

                is_matching = match(
                    expected,
                    predicted_clean,
                    matching_type=matching_type,
                    matching_threshold=threshold,
                    model=sbert_model,
                    grobid_processor=grobid_processor)

            ## This is a trick so that soft matching slightly different items will result in the calculation of the correct evaluation scores
            if is_matching:
                predicted_in_file.append(expected)
            else:
                predicted_in_file.append(predicted)

        if verbose:
            accuracy = accuracy_score(expected_in_file, predicted_in_file)
            print(filename, ": {:10.4f}".format(accuracy))

        expected_all.extend(expected_in_file)
        predicted_all.extend(predicted_in_file)

    return expected_all, predicted_all


def calculate_metrics(tp: dict, fp: dict, fn: dict):
    tp_n = {key: len(value) for key, value in tp.items()}
    fp_n = {key: len(value) for key, value in fp.items()}
    fn_n = {key: len(value) for key, value in fn.items()}

    precision_macro_avg_ = {}
    recall_macro_avg_ = {}

    tp_all = sum([tp_n[filename] for filename in tp_n.keys()])
    fp_all = sum([fp_n[filename] for filename in fp_n.keys()])
    fn_all = sum([fn_n[filename] for filename in fn_n.keys()])

    for filename in tp_n.keys():
        precision_macro_avg_[filename] = tp_n[filename] / (tp_n[filename] + fp_n[filename]) if tp_n[filename] + fp_n[
            filename] > 0 else 0
        recall_macro_avg_[filename] = tp_n[filename] / (tp_n[filename] + fn_n[filename]) if tp_n[filename] + fn_n[
            filename] > 0 else 0

    precision_macro_avg = (sum([precision_macro_avg_[filename] for filename in precision_macro_avg_.keys()]) /
                           len(list(precision_macro_avg_.keys())))
    recall_macro_avg = (sum([recall_macro_avg_[filename] for filename in recall_macro_avg_.keys()]) /
                        len(list(recall_macro_avg_.keys())))
    f1_score_macro_avg = 2 * (precision_macro_avg * recall_macro_avg) / (precision_macro_avg + recall_macro_avg)

    precision_micro_avg = tp_all / (tp_all + fp_all)
    recall_micro_avg = tp_all / (tp_all + fn_all)
    f1_score_micro_avg = 2 * (precision_micro_avg * recall_micro_avg) / (precision_micro_avg + recall_micro_avg)

    return precision_micro_avg, recall_micro_avg, f1_score_micro_avg, precision_macro_avg, recall_macro_avg, f1_score_macro_avg
