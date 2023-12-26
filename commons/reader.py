import csv
import os
from datetime import datetime, date
from hashlib import blake2b
from pathlib import Path

from tqdm import tqdm


def load_texts_and_classes_generic(filepath, classes_indexes=[], data_only_indexes=None, has_header=None):
    """
    Load texts and classes from a file in the following simple tab-separated format:

    id_0    text_0  class_00 ...    class_n0
    id_1    text_1  class_01 ...    class_n1
    ...
    id_m    text_m  class_0m  ...   class_nm

    text has no EOF and no tab
    By default it assumes that:
     - all columns except the class_indexes are considered for building x
    - filter_data will limit the data to the selected column indexes

    Returns:
        tuple(numpy array, numpy array): texts and classes

    Source: https://github.com/kermitt2/delft
    """
    x = []
    y = []

    delimiter = "\t"
    if filepath.endswith(".csv"):
        delimiter = ","

    with open(filepath, encoding="utf-8-sig") as f:
        if has_header is None:
            sample = f.readline()
            sample = sample + f.readline() if sample else ""
            has_header = csv.Sniffer().has_header(sample)
            f.seek(0)

        first = True
        tsvreader = csv.reader(f, delimiter=delimiter)
        for line in tsvreader:
            if has_header:
                has_header = False
                continue

            if len(line) == 0:
                continue

            classes = []
            data = []
            for col_id, column in enumerate(line):
                if col_id in classes_indexes:
                    classes.append(column)
                else:
                    if data_only_indexes:
                        if col_id in data_only_indexes:
                            data.append(column)
                    else:
                        data.append(column)

            if first:
                print("Sample input", "x: ", data, "y: ", classes)
                first = False

            x.append(data)
            y.append(classes)

    return x, y


def load_data_and_classes_generic_old(filepath, data_indexes: list, classes_indexes: list):
    """
    Load texts and classes from a file in the following simple tab-separated format:

    id_0    text_0  class_00 ...    class_n0
    id_1    text_1  class_01 ...    class_n1
    ...
    id_m    text_m  class_0m  ...   class_nm

    text has no EOF and no tab

    Returns:
        tuple(numpy array, numpy array): texts and classes


    Source: https://github.com/kermitt2/delft

    """
    x = []
    y = []

    delimiter = "\t"
    if filepath.endswith(".csv"):
        delimiter = ","

    with open(filepath) as f:
        first = True
        tsvreader = csv.reader(f, delimiter=delimiter)
        for line in tsvreader:
            if len(line) == 0:
                continue
            if len(line) < 3:
                print("Warning: number of fields in the data file too low for line:", line)
            classes = [line[i] for i in classes_indexes]
            data = [line[i] for i in data_indexes]
            if first:
                print("Sample input", "x: ", data, "y: ", classes)
                first = False
            x.append(data)
            if len(classes) == 1:
                y.append(classes[0])
            else:
                y.append(classes)

    return x, y


def group_by(input, column_idx: int):
    dict = {}
    for elem in input:
        if elem[column_idx] not in dict:
            dict[elem[column_idx]] = []
        elem_clean = elem.copy()
        elem_clean.pop(column_idx)
        dict[elem[column_idx]].append(elem_clean)
    return dict


def get_file_hash(fname):
    hash_md5 = blake2b()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_str_hash(string):
    hash_md5 = blake2b()
    hash_md5.update(string.encode("utf-8"))
    return hash_md5.hexdigest()


def is_too_short_text(text):
    return len(text.split(" ")) <= 3 or len(text) < 10


def preprocess_text(x_all, y_all, column_text_index):
    x_preprocessed = []
    y_preprocessd = []

    for idx, data in tqdm(enumerate(x_all), desc="Preprocessing"):
        text = data[column_text_index]
        if is_too_short_text(text):
            continue
        # if len(split_sentences(text)) < 3:
        #     continue

        x_preprocessed.append(data)
        y = y_all[idx]
        if type(y) == list:
            if len(y) == 1:
                y = int(y_all[idx][0])
            else:
                y = y_all[idx]

        y_preprocessd.append(y)

    return x_preprocessed, y_preprocessd


def get_last_line(path: Path) -> str:
    last_line = None
    if os.path.exists(str(path)):
        with open(path) as f:
            for line in f:
                last_line = line

    return last_line


def get_last_id(path: Path) -> int:
    last_line = get_last_line(Path(path))
    last_id = -1
    if last_line is not None and last_line.strip() != "":
        last_id = last_line.split(",")[0].replace("\"", "")

    return int(last_id)
