# Measurements / quantities extraction

This evaluation was performed in MeasEval dataset

- Expected records: 1663 , files: 428 , input: resources/dataset/measeval/measeval-expected.csv

## Grobid-quantities (SciBERT)

- Predicted records: 1632 , files: 424 , input: [measeval-grobid-quantities.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Fmeaseval-grobid-quantities.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 55.09     | 54.19  | 54.63    | 1632    |
| macro     | strict      | 56.81     | 55.52  | 56.16    | 1632    |
| micro     | soft        | 60.23     | 59.25  | 59.74    | 1632    |
| macro     | soft        | 61.58     | 59.96  | 60.76    | 1632    |
| micro     | sbert_cross | 76.41     | 75.17  | 75.78    | 1632    |
| macro     | sbert_cross | 79.74     | 77.18  | 78.44    | 1632    |

Main discrepancies are due to the fact that grobid-quantities does not treat approximate quantities.
https://github.com/kermitt2/grobid-quantities/issues/166

### GPT 3.5 Turbo

- Predicted: [measeval-text.chatgpt.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-text.chatgpt.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 40.07     | 42.88  | 41.43    | 564     |
| macro     | strict      | 11.33     | 10.15  | 10.71    | 564     |
| micro     | soft        | 42.73     | 45.73  | 44.18    | 564     |
| macro     | soft        | 12.06     | 10.85  | 11.42    | 564     |
| micro     | sbert_cross | 51.06     | 54.65  | 52.80    | 564     |
| macro     | sbert_cross | 14.63     | 13.42  | 14.00    | 564     |

- Predicted: [measeval-text.chatgpt.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-text.chatgpt.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 39.36     | 41.22  | 40.27    | 531     |
| macro     | strict      | 10.56     | 9.17   | 9.81     | 531     |
| micro     | soft        | 41.81     | 43.79  | 42.77    | 531     |
| macro     | soft        | 11.21     | 9.81   | 10.46    | 531     |
| micro     | sbert_cross | 50.09     | 52.47  | 51.25    | 531     |
| macro     | sbert_cross | 13.64     | 12.06  | 12.80    | 531     |

- Predicted: [measeval-text.chatgpt.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-text.chatgpt.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 40.39     | 42.25  | 41.30    | 567     |
| macro     | strict      | 11.58     | 10.16  | 10.82    | 567     |
| micro     | soft        | 42.86     | 44.83  | 43.82    | 567     |
| macro     | soft        | 12.24     | 10.78  | 11.46    | 567     |
| micro     | sbert_cross | 51.85     | 54.24  | 53.02    | 567     |
| macro     | sbert_cross | 15.14     | 13.49  | 14.27    | 567     |

### GPT3.5 Turbo + Few-shot with Grobid-quantities

- Predicted records: 1450 , files: 378 , input: [measeval-chatgpt-few-shot-quantities.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-chatgpt-few-shot-quantities.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 55.90     | 54.62  | 55.25    | 1576    |
| macro     | strict      | 53.71     | 52.31  | 53.00    | 1576    |
| micro     | soft        | 60.98     | 59.58  | 60.27    | 1576    |
| macro     | soft        | 58.42     | 56.64  | 57.52    | 1576    |
| micro     | sbert_cross | 77.60     | 75.82  | 76.70    | 1576    |
| macro     | sbert_cross | 75.86     | 73.34  | 74.57    | 1576    |

- Predicted: [measeval-text.chatgpt.few-shot.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-text.chatgpt.few-shot.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 55.97     | 54.89  | 55.43    | 1574    |
| macro     | strict      | 53.81     | 52.49  | 53.14    | 1574    |
| micro     | soft        | 60.99     | 59.81  | 60.40    | 1574    |
| macro     | soft        | 58.49     | 56.81  | 57.64    | 1574    |
| micro     | sbert_cross | 77.26     | 75.76  | 76.50    | 1574    |
| macro     | sbert_cross | 75.62     | 73.29  | 74.44    | 1574    |

- Predicted: [measeval-text.chatgpt.few-shot.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-text.chatgpt.few-shot.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 55.71     | 54.43  | 55.06    | 1576    |
| macro     | strict      | 53.62     | 52.10  | 52.85    | 1576    |
| micro     | soft        | 60.72     | 59.33  | 60.02    | 1576    |
| macro     | soft        | 58.29     | 56.41  | 57.34    | 1576    |
| micro     | sbert_cross | 77.16     | 75.39  | 76.26    | 1576    |
| macro     | sbert_cross | 75.64     | 73.08  | 74.34    | 1576    |

### GPT3.5-turbo FIne tuned

- Predicted: [measeval-text.chatgpt-ft-ner-quantities.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-text.chatgpt-ft-ner-quantities.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 56.27     | 54.24  | 55.24    | 1603    |
| macro     | strict      | 58.12     | 57.87  | 57.99    | 1603    |
| micro     | soft        | 60.76     | 58.57  | 59.64    | 1603    |
| macro     | soft        | 61.85     | 61.63  | 61.74    | 1603    |
| micro     | sbert_cross | 64.38     | 62.06  | 63.20    | 1603    |
| macro     | sbert_cross | 67.53     | 67.67  | 67.60    | 1603    |

- Predicted: [measeval-text.chatgpt-ft-ner-quantities.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-text.chatgpt-ft-ner-quantities.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 56.23     | 54.24  | 55.22    | 1604    |
| macro     | strict      | 57.97     | 57.73  | 57.85    | 1604    |
| micro     | soft        | 60.85     | 58.69  | 59.75    | 1604    |
| macro     | soft        | 61.84     | 61.69  | 61.76    | 1604    |
| micro     | sbert_cross | 64.40     | 62.12  | 63.24    | 1604    |
| macro     | sbert_cross | 67.49     | 67.69  | 67.59    | 1604    |

- Predicted: [measeval-text.chatgpt-ft-ner-quantities.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-text.chatgpt-ft-ner-quantities.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 56.00     | 54.12  | 55.05    | 1607    |
| macro     | strict      | 57.98     | 57.84  | 57.91    | 1607    |
| micro     | soft        | 60.49     | 58.45  | 59.45    | 1607    |
| macro     | soft        | 61.72     | 61.61  | 61.66    | 1607    |
| micro     | sbert_cross | 64.09     | 61.94  | 63.00    | 1607    |
| macro     | sbert_cross | 67.41     | 67.63  | 67.52    | 1607    |

### GPT4

- Predicted records: 1535 , files: 390 , input: [measeval-gpt4-quantities.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-gpt4-quantities.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.89     | 56.25  | 57.54    | 1535    |
| macro     | strict      | 54.50     | 51.28  | 52.84    | 1535    |
| micro     | soft        | 61.43     | 58.68  | 60.03    | 1535    |
| macro     | soft        | 56.46     | 53.22  | 54.79    | 1535    |
| micro     | sbert_cross | 73.75     | 70.44  | 72.06    | 1535    |
| macro     | sbert_cross | 69.86     | 65.79  | 67.76    | 1535    |

- Predicted: [measeval-text.gpt4.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-text.gpt4.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 60.90     | 57.79  | 59.31    | 1504    |
| macro     | strict      | 54.18     | 51.43  | 52.77    | 1504    |
| micro     | soft        | 63.23     | 60.00  | 61.57    | 1504    |
| macro     | soft        | 56.15     | 53.32  | 54.70    | 1504    |
| micro     | sbert_cross | 75.20     | 71.36  | 73.23    | 1504    |
| macro     | sbert_cross | 69.03     | 65.29  | 67.11    | 1504    |

- Predicted: [measeval-text.gpt4.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-text.gpt4.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 60.76     | 57.21  | 58.93    | 1496    |
| macro     | strict      | 54.70     | 51.25  | 52.92    | 1496    |
| micro     | soft        | 62.83     | 59.16  | 60.94    | 1496    |
| macro     | soft        | 56.39     | 52.88  | 54.58    | 1496    |
| micro     | sbert_cross | 74.67     | 70.30  | 72.41    | 1496    |
| macro     | sbert_cross | 69.23     | 64.91  | 67.00    | 1496    |

## GPT4 + Few-shot with Grobid-quantities

- Predicted records: 1632 , files: 424 , input: [measeval-gpt4-few-shot-quantities.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-gpt4-few-shot-quantities.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.27     | 57.32  | 57.79    | 1632    |
| macro     | strict      | 58.57     | 57.07  | 57.81    | 1632    |
| micro     | soft        | 62.01     | 61.00  | 61.50    | 1632    |
| macro     | soft        | 62.07     | 60.41  | 61.23    | 1632    |
| micro     | sbert_cross | 77.33     | 76.07  | 76.69    | 1632    |
| macro     | sbert_cross | 79.22     | 76.70  | 77.94    | 1632    |

- Predicted: [measeval-text.gpt4.few-shot.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-text.gpt4.few-shot.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.34     | 57.36  | 57.85    | 1630    |
| macro     | strict      | 58.76     | 57.18  | 57.96    | 1630    |
| micro     | soft        | 62.15     | 61.10  | 61.62    | 1630    |
| macro     | soft        | 62.38     | 60.62  | 61.49    | 1630    |
| micro     | sbert_cross | 77.36     | 76.06  | 76.70    | 1630    |
| macro     | sbert_cross | 79.22     | 76.69  | 77.93    | 1630    |

- Predicted: [measeval-text.gpt4.few-shot.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-text.gpt4.few-shot.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.60     | 57.50  | 58.05    | 1628    |
| macro     | strict      | 59.12     | 57.56  | 58.33    | 1628    |
| micro     | soft        | 62.41     | 61.24  | 61.82    | 1628    |
| macro     | soft        | 62.68     | 60.96  | 61.81    | 1628    |
| micro     | sbert_cross | 77.40     | 75.95  | 76.67    | 1628    |
| macro     | sbert_cross | 79.39     | 76.64  | 77.99    | 1628    |

### GPT4-turbo

- Predicted: [measeval-text.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-text.gpt4-turbo.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 57.16     | 54.36  | 55.73    | 1515    |
| macro     | strict      | 52.26     | 49.00  | 50.58    | 1515    |
| micro     | soft        | 59.60     | 56.69  | 58.11    | 1515    |
| macro     | soft        | 54.17     | 50.85  | 52.45    | 1515    |
| micro     | sbert_cross | 72.61     | 69.05  | 70.79    | 1515    |
| macro     | sbert_cross | 68.57     | 64.35  | 66.39    | 1515    |

- Predicted: [measeval-text.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-text.gpt4-turbo.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 57.92     | 55.21  | 56.53    | 1528    |
| macro     | strict      | 53.84     | 50.83  | 52.29    | 1528    |
| micro     | soft        | 60.34     | 57.52  | 58.89    | 1528    |
| macro     | soft        | 55.85     | 52.66  | 54.21    | 1528    |
| micro     | sbert_cross | 73.04     | 69.62  | 71.29    | 1528    |
| macro     | sbert_cross | 69.82     | 65.53  | 67.61    | 1528    |

- Predicted: [measeval-text.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-text.gpt4-turbo.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 57.94     | 54.89  | 56.37    | 1512    |
| macro     | strict      | 52.64     | 49.31  | 50.92    | 1512    |
| micro     | soft        | 60.05     | 56.89  | 58.43    | 1512    |
| macro     | soft        | 54.53     | 51.01  | 52.72    | 1512    |
| micro     | sbert_cross | 72.49     | 68.67  | 70.53    | 1512    |
| macro     | sbert_cross | 68.59     | 63.68  | 66.04    | 1512    |

### GPT-4-turbo + few shot

- Predicted: [measeval-text.gpt4-turbo.few-shot.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-text.gpt4-turbo.few-shot.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.78     | 58.53  | 58.65    | 1652    |
| macro     | strict      | 60.02     | 59.20  | 59.60    | 1652    |
| micro     | soft        | 62.18     | 62.15  | 62.16    | 1658    |
| macro     | soft        | 63.29     | 61.94  | 62.61    | 1658    |
| micro     | sbert_cross | 77.12     | 76.79  | 76.96    | 1652    |
| macro     | sbert_cross | 80.06     | 78.17  | 79.10    | 1652    |

- Predicted: [measeval-text.gpt4-turbo.few-shot.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-text.gpt4-turbo.few-shot.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.75     | 58.71  | 58.73    | 1658    |
| macro     | strict      | 59.87     | 59.18  | 59.52    | 1658    |
| micro     | soft        | 62.42     | 62.39  | 62.41    | 1658    |
| macro     | soft        | 63.18     | 62.42  | 62.80    | 1658    |
| micro     | sbert_cross | 76.96     | 76.91  | 76.94    | 1658    |
| macro     | sbert_cross | 79.74     | 78.13  | 78.93    | 1658    |

- Predicted: [measeval-text.gpt4-turbo.few-shot.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-text.gpt4-turbo.few-shot.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.89     | 59.31  | 59.10    | 1671    |
| macro     | strict      | 60.18     | 59.48  | 59.83    | 1671    |
| micro     | soft        | 62.48     | 62.93  | 62.70    | 1671    |
| macro     | soft        | 63.53     | 62.69  | 63.11    | 1671    |
| micro     | sbert_cross | 76.66     | 77.22  | 76.94    | 1671    |
| macro     | sbert_cross | 80.03     | 78.40  | 79.21    | 1671    |
