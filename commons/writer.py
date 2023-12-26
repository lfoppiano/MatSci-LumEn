import csv


def write_output(data, output_path, format="tsv"):
    delimiter = '\t' if format == 'tsv' else ','
    fw = csv.writer(open(output_path, encoding='utf-8', mode='w'), delimiter=delimiter, quotechar='"',
                    quoting=csv.QUOTE_ALL)
    fw.writerows(data)


def print_markdown(result_table):
    # Write table headers
    markdown = "|" + "|".join(result_table[0]) + "|" + "\n"
    markdown += "|" + "|".join(["---"] * len(result_table[0])) + "|" + "\n"

    # Write table rows
    for row in result_table[1:]:
        formatted_row = [f"{cell * 100:.2f}" if isinstance(cell, (int, float)) else str(cell) for cell in row]
        markdown += "|" + "|".join(formatted_row) + "|" + "\n"

    return markdown
