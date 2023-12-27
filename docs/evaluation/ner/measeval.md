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

- Predicted: [measeval-gpt35_turbo-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-gpt35_turbo-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 40.07     | 13.59  | 20.30    | 564     |
| macro     | strict      | 11.33     | 10.15  | 10.71    | 564     |
| micro     | soft        | 42.73     | 14.49  | 21.64    | 564     |
| macro     | soft        | 12.06     | 10.85  | 11.42    | 564     |
| micro     | sbert_cross | 45.39     | 15.39  | 22.99    | 564     |
| macro     | sbert_cross | 13.05     | 11.69  | 12.33    | 564     |

- Predicted: [measeval-gpt35_turbo-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-gpt35_turbo-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 39.36     | 12.57  | 19.05    | 531     |
| macro     | strict      | 10.56     | 9.17   | 9.81     | 531     |
| micro     | soft        | 41.81     | 13.35  | 20.24    | 531     |
| macro     | soft        | 11.21     | 9.81   | 10.46    | 531     |
| micro     | sbert_cross | 45.01     | 14.37  | 21.79    | 531     |
| macro     | sbert_cross | 12.36     | 10.80  | 11.53    | 531     |

- Predicted: [measeval-gpt35_turbo-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-gpt35_turbo-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 40.39     | 13.77  | 20.54    | 567     |
| macro     | strict      | 11.58     | 10.16  | 10.82    | 567     |
| micro     | soft        | 42.86     | 14.61  | 21.79    | 567     |
| macro     | soft        | 12.24     | 10.78  | 11.46    | 567     |
| micro     | sbert_cross | 45.86     | 15.63  | 23.32    | 567     |
| macro     | sbert_cross | 13.56     | 11.75  | 12.59    | 567     |

### GPT3.5 Turbo + Few-shot with Grobid-quantities

- Predicted: [measeval-gpt35_turbo-few_shot-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-gpt35_turbo-few_shot-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 55.90     | 52.98  | 54.40    | 1576    |
| macro     | strict      | 53.71     | 52.31  | 53.00    | 1576    |
| micro     | soft        | 60.98     | 57.79  | 59.34    | 1576    |
| macro     | soft        | 58.42     | 56.64  | 57.52    | 1576    |
| micro     | sbert_cross | 64.85     | 61.46  | 63.11    | 1576    |
| macro     | sbert_cross | 63.72     | 61.84  | 62.77    | 1576    |

- Predicted: [measeval-gpt35_turbo-few_shot-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-gpt35_turbo-few_shot-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 55.97     | 52.98  | 54.43    | 1574    |
| macro     | strict      | 53.81     | 52.49  | 53.14    | 1574    |
| micro     | soft        | 60.99     | 57.73  | 59.31    | 1574    |
| macro     | soft        | 58.49     | 56.81  | 57.64    | 1574    |
| micro     | sbert_cross | 64.55     | 61.09  | 62.77    | 1574    |
| macro     | sbert_cross | 63.60     | 61.83  | 62.70    | 1574    |

- Predicted: [measeval-gpt35_turbo-few_shot-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-gpt35_turbo-few_shot-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 55.71     | 52.80  | 54.21    | 1576    |
| macro     | strict      | 53.62     | 52.10  | 52.85    | 1576    |
| micro     | soft        | 60.72     | 57.55  | 59.09    | 1576    |
| macro     | soft        | 58.29     | 56.41  | 57.34    | 1576    |
| micro     | sbert_cross | 64.28     | 60.91  | 62.55    | 1576    |
| macro     | sbert_cross | 63.32     | 61.53  | 62.41    | 1576    |

### GPT3.5-turbo FIne tuned

- Predicted: [measeval-gpt35_turbo-ft-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-gpt35_turbo-ft-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 56.27     | 54.24  | 55.24    | 1603    |
| macro     | strict      | 58.12     | 57.87  | 57.99    | 1603    |
| micro     | soft        | 60.76     | 58.57  | 59.64    | 1603    |
| macro     | soft        | 61.85     | 61.63  | 61.74    | 1603    |
| micro     | sbert_cross | 64.38     | 62.06  | 63.20    | 1603    |
| macro     | sbert_cross | 67.53     | 67.67  | 67.60    | 1603    |

- Predicted: [measeval-gpt35_turbo-ft-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-gpt35_turbo-ft-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 56.23     | 54.24  | 55.22    | 1604    |
| macro     | strict      | 57.97     | 57.73  | 57.85    | 1604    |
| micro     | soft        | 60.85     | 58.69  | 59.75    | 1604    |
| macro     | soft        | 61.84     | 61.69  | 61.76    | 1604    |
| micro     | sbert_cross | 64.40     | 62.12  | 63.24    | 1604    |
| macro     | sbert_cross | 67.49     | 67.69  | 67.59    | 1604    |

- Predicted: [measeval-gpt35_turbo-ft-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-gpt35_turbo-ft-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 56.00     | 54.12  | 55.05    | 1607    |
| macro     | strict      | 57.98     | 57.84  | 57.91    | 1607    |
| micro     | soft        | 60.49     | 58.45  | 59.45    | 1607    |
| macro     | soft        | 61.72     | 61.61  | 61.66    | 1607    |
| micro     | sbert_cross | 64.09     | 61.94  | 63.00    | 1607    |
| macro     | sbert_cross | 67.41     | 67.63  | 67.52    | 1607    |

### GPT4

- Predicted: [measeval-gpt4-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-gpt4-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.89     | 54.36  | 56.54    | 1535    |
| macro     | strict      | 54.50     | 51.28  | 52.84    | 1535    |
| micro     | soft        | 61.43     | 56.70  | 58.97    | 1535    |
| macro     | soft        | 56.46     | 53.22  | 54.79    | 1535    |
| micro     | sbert_cross | 65.08     | 60.07  | 62.48    | 1535    |
| macro     | sbert_cross | 61.30     | 57.95  | 59.58    | 1535    |

- Predicted: [measeval-gpt4-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-gpt4-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 60.90     | 55.08  | 57.85    | 1504    |
| macro     | strict      | 54.18     | 51.43  | 52.77    | 1504    |
| micro     | soft        | 63.23     | 57.19  | 60.06    | 1504    |
| macro     | soft        | 56.15     | 53.32  | 54.70    | 1504    |
| micro     | sbert_cross | 66.42     | 60.07  | 63.09    | 1504    |
| macro     | sbert_cross | 60.45     | 57.47  | 58.92    | 1504    |

- Predicted: [measeval-gpt4-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-gpt4-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 60.76     | 54.66  | 57.55    | 1496    |
| macro     | strict      | 54.70     | 51.25  | 52.92    | 1496    |
| micro     | soft        | 62.83     | 56.52  | 59.51    | 1496    |
| macro     | soft        | 56.39     | 52.88  | 54.58    | 1496    |
| micro     | sbert_cross | 66.11     | 59.47  | 62.61    | 1496    |
| macro     | sbert_cross | 60.84     | 57.07  | 58.90    | 1496    |

## GPT4 + Few-shot with Grobid-quantities

- Predicted: [measeval-gpt4-few_shot-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-gpt4-few_shot-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.27     | 57.19  | 57.72    | 1632    |
| macro     | strict      | 58.57     | 57.07  | 57.81    | 1632    |
| micro     | soft        | 62.01     | 60.85  | 61.43    | 1632    |
| macro     | soft        | 62.07     | 60.41  | 61.23    | 1632    |
| micro     | sbert_cross | 65.56     | 64.34  | 64.95    | 1632    |
| macro     | sbert_cross | 66.80     | 65.29  | 66.04    | 1632    |

- Predicted: [measeval-gpt4-few_shot-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-gpt4-few_shot-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.34     | 57.19  | 57.76    | 1630    |
| macro     | strict      | 58.76     | 57.18  | 57.96    | 1630    |
| micro     | soft        | 62.15     | 60.91  | 61.52    | 1630    |
| macro     | soft        | 62.38     | 60.62  | 61.49    | 1630    |
| micro     | sbert_cross | 65.52     | 64.22  | 64.86    | 1630    |
| macro     | sbert_cross | 67.04     | 65.48  | 66.25    | 1630    |

- Predicted: [measeval-gpt4-few_shot-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-gpt4-few_shot-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.60     | 57.37  | 57.98    | 1628    |
| macro     | strict      | 59.12     | 57.56  | 58.33    | 1628    |
| micro     | soft        | 62.41     | 61.09  | 61.74    | 1628    |
| macro     | soft        | 62.68     | 60.96  | 61.81    | 1628    |
| micro     | sbert_cross | 65.60     | 64.22  | 64.90    | 1628    |
| macro     | sbert_cross | 66.98     | 65.25  | 66.10    | 1628    |

### GPT4-turbo

- Predicted: [measeval-gpt4_turbo-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-gpt4_turbo-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 57.16     | 52.07  | 54.50    | 1515    |
| macro     | strict      | 52.26     | 49.00  | 50.58    | 1515    |
| micro     | soft        | 59.60     | 54.30  | 56.83    | 1515    |
| macro     | soft        | 54.17     | 50.85  | 52.45    | 1515    |
| micro     | sbert_cross | 62.90     | 57.31  | 59.97    | 1515    |
| macro     | sbert_cross | 59.05     | 55.26  | 57.09    | 1515    |

- Predicted: [measeval-gpt4_turbo-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-gpt4_turbo-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 57.92     | 53.22  | 55.47    | 1528    |
| macro     | strict      | 53.84     | 50.83  | 52.29    | 1528    |
| micro     | soft        | 60.34     | 55.44  | 57.79    | 1528    |
| macro     | soft        | 55.85     | 52.66  | 54.21    | 1528    |
| micro     | sbert_cross | 63.87     | 58.69  | 61.17    | 1528    |
| macro     | sbert_cross | 60.80     | 57.04  | 58.86    | 1528    |

- Predicted: [measeval-gpt4_turbo-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-gpt4_turbo-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 57.94     | 52.68  | 55.18    | 1512    |
| macro     | strict      | 52.64     | 49.31  | 50.92    | 1512    |
| micro     | soft        | 60.05     | 54.60  | 57.20    | 1512    |
| macro     | soft        | 54.53     | 51.01  | 52.72    | 1512    |
| micro     | sbert_cross | 63.96     | 58.15  | 60.91    | 1512    |
| macro     | sbert_cross | 59.99     | 55.69  | 57.76    | 1512    |

### GPT-4-turbo + few shot

- Predicted: [measeval-gpt4_turbo-few_shot-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun1%2Fmeaseval-gpt4_turbo-few_shot-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.69     | 58.51  | 58.60    | 1658    |
| macro     | strict      | 59.98     | 58.77  | 59.37    | 1658    |
| micro     | soft        | 62.18     | 62.00  | 62.09    | 1658    |
| macro     | soft        | 63.29     | 61.94  | 62.61    | 1658    |
| micro     | sbert_cross | 65.80     | 65.60  | 65.70    | 1658    |
| macro     | sbert_cross | 68.75     | 67.19  | 67.96    | 1658    |

- Predicted: [measeval-gpt4_turbo-few_shot-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun2%2Fmeaseval-gpt4_turbo-few_shot-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.75     | 58.57  | 58.66    | 1658    |
| macro     | strict      | 59.87     | 59.18  | 59.52    | 1658    |
| micro     | soft        | 62.42     | 62.24  | 62.33    | 1658    |
| macro     | soft        | 63.18     | 62.42  | 62.80    | 1658    |
| micro     | sbert_cross | 66.10     | 65.90  | 66.00    | 1658    |
| macro     | sbert_cross | 68.49     | 67.45  | 67.97    | 1658    |

- Predicted: [measeval-gpt4_turbo-few_shot-properties.csv](..%2F..%2F..%2Fresources%2Fdataset%2Fmeaseval%2Fresults%2Frun3%2Fmeaseval-gpt4_turbo-few_shot-properties.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.89     | 59.17  | 59.03    | 1671    |
| macro     | strict      | 60.18     | 59.48  | 59.83    | 1671    |
| micro     | soft        | 62.48     | 62.78  | 62.63    | 1671    |
| macro     | soft        | 63.53     | 62.69  | 63.11    | 1671    |
| micro     | sbert_cross | 65.95     | 66.27  | 66.11    | 1671    |
| macro     | sbert_cross | 68.79     | 67.69  | 68.23    | 1671    |

