from commons.reader import load_texts_and_classes_generic


def prepare_data(input):
    text_data, _ = load_texts_and_classes_generic(input)
    prompt_batch = []

    # Preparing data
    for record in text_data:
        id = record[0]
        filename = record[1]
        paragraph_idx = record[2]
        text = record[3]

        prompt_data = {
            "id": id,
            "filename": filename,
            "pid": paragraph_idx,
            "text": text,
        }

        prompt_batch.append(prompt_data)

    return prompt_batch

