## Grobid-superconductors

- Prompt: complex prompt with examples and the definitions taken from the guidelines
- Expected records: 1402 , files: 32 , input: resources/dataset/superMat/supermat-expected-holdout-material.csv

- **BIASED MODEL - PLEASE IGNORE**

- Predicted records: 1912 , files: 32 , input: resources/dataset/superMat/output/supermat-grobid-holdout-material.csv

| Method          | Precision | Recall | F1-score |
|-----------------|-----------|--------|----------|
| strict          | 80.87     | 93.69  | 86.81    |
| soft            | 83.87     | 97.16  | 90.03    |
| sbert           | 84.20     | 97.55  | 90.39    |
| sbert_cross     | 83.87     | 97.16  | 90.03    |
| formula +strict | 82.54     | 95.62  | 88.60    |

## chatgpt-3.5-turbo

- Predicted records: 1617 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run1/supermat-gpt35_turbo-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 22.57     | 18.10  | 20.09    | 1402    |
| macro     | strict      | 24.63     | 20.09  | 22.13    | 1402    |
| micro     | soft        | 38.82     | 31.13  | 34.55    | 1402    |
| macro     | soft        | 39.31     | 33.18  | 35.99    | 1402    |
| micro     | sbert_cross | 46.62     | 37.39  | 41.50    | 1402    |
| macro     | sbert_cross | 47.63     | 38.78  | 42.75    | 1402    |
| micro     | formula     | 53.59     | 42.98  | 47.70    | 1617    |
| macro     | formula     | 55.59     | 45.14  | 49.82    | 1617    |

- Predicted records: 1641 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run2//supermat-gpt35_turbo-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 22.57     | 18.38  | 20.26    | 1402    |
| macro     | strict      | 25.06     | 20.82  | 22.74    | 1402    |
| micro     | soft        | 38.51     | 31.37  | 34.57    | 1402    |
| macro     | soft        | 39.34     | 33.87  | 36.40    | 1402    |
| micro     | sbert_cross | 46.17     | 37.61  | 41.45    | 1402    |
| macro     | sbert_cross | 47.33     | 39.40  | 43.00    | 1402    |
| micro     | formula     | 53.21     | 43.34  | 47.77    | 1641    |
| macro     | formula     | 55.37     | 45.88  | 50.18    | 1641    |

- Predicted records: 1587 , files: 32 , input: resources/dataset/superMat/entities/results/run3//supermat-paragraphs-holdout.chatgpt.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 22.73     | 18.23  | 20.23    | 1402    |
| macro     | strict      | 25.41     | 20.53  | 22.72    | 1402    |
| micro     | soft        | 39.18     | 31.42  | 34.87    | 1402    |
| macro     | soft        | 40.15     | 33.07  | 36.27    | 1402    |
| micro     | sbert_cross | 46.32     | 37.15  | 41.23    | 1402    |
| macro     | sbert_cross | 47.67     | 38.32  | 42.49    | 1402    |
| micro     | formula     | 53.68     | 43.06  | 47.78    | 1587    |
| macro     | formula     | 56.35     | 45.36  | 50.26    | 1587    |

## chatgpt3.5-turbo + Few-shot with Grobid-superconductors

- Predicted records: 1887 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run1/supermat-gpt35_turbo-few-shot-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 59.21     | 61.56  | 60.36    | 1402    |
| macro     | strict      | 59.36     | 63.33  | 61.28    | 1402    |
| micro     | soft        | 72.50     | 75.38  | 73.91    | 1402    |
| macro     | soft        | 72.92     | 77.56  | 75.17    | 1402    |
| micro     | sbert_cross | 74.08     | 77.02  | 75.52    | 1402    |
| macro     | sbert_cross | 74.34     | 78.97  | 76.59    | 1402    |
| micro     | formula     | 72.76     | 75.65  | 74.18    | 1887    |
| macro     | formula     | 73.15     | 77.69  | 75.35    | 1887    |

- Predicted records: 2495 , files: 32 , input: resources/dataset/superMat/entities/results_prompt2/run2/supermat-ner-complex_prompt-holdout-few-shot.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 63.01     | 72.15  | 67.27    | 1402    |
| macro     | strict      | 64.83     | 74.40  | 69.28    | 1402    |
| micro     | soft        | 79.86     | 91.45  | 85.27    | 1402    |
| macro     | soft        | 80.46     | 92.48  | 86.05    | 1402    |
| micro     | sbert_cross | 80.09     | 91.71  | 85.51    | 1402    |
| macro     | sbert_cross | 80.62     | 92.70  | 86.24    | 1402    |
| micro     | formula     | 76.24     | 87.31  | 81.40    | 2495    |
| macro     | formula     | 77.40     | 88.95  | 82.77    | 2495    |

- Predicted records: 2448 , files: 32 , input: resources/dataset/superMat/entities/results/run3//supermat-paragraphs-holdout.chatgpt.few-shot.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 63.24     | 72.41  | 67.51    | 1402    |
| macro     | strict      | 65.02     | 74.67  | 69.51    | 1402    |
| micro     | soft        | 79.98     | 91.58  | 85.39    | 1402    |
| macro     | soft        | 80.53     | 92.63  | 86.16    | 1402    |
| micro     | sbert_cross | 80.32     | 91.97  | 85.75    | 1402    |
| macro     | sbert_cross | 80.78     | 92.97  | 86.45    | 1402    |
| micro     | formula     | 76.58     | 87.69  | 81.76    | 2448    |
| macro     | formula     | 77.67     | 89.34  | 83.10    | 2448    |

### GPT3.5-turbo Fine-tune

- Predicted: [supermat-paragraphs-holdout.chatgpt-ft-ner-simple.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Fentities%2Fresults%2Frun1%2Fsupermat-paragraphs-holdout.chatgpt-ft-ner-simple.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 67.65     | 58.36  | 62.66    | 1429    |
| macro     | strict      | 69.94     | 60.25  | 64.74    | 1429    |
| micro     | soft        | 74.45     | 64.23  | 68.97    | 1429    |
| macro     | soft        | 76.46     | 66.03  | 70.86    | 1429    |
| micro     | sbert_cross | 75.10     | 64.78  | 69.56    | 1429    |
| macro     | sbert_cross | 77.52     | 66.85  | 71.79    | 1429    |
| micro     | formula     | 74.45     | 64.23  | 68.97    | 1429    |
| macro     | formula     | 77.25     | 66.29  | 71.35    | 1429    |

- Predicted: [supermat-paragraphs-holdout.chatgpt-ft-ner-simple.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Fentities%2Fresults%2Frun2%2Fsupermat-paragraphs-holdout.chatgpt-ft-ner-simple.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 68.25     | 58.80  | 63.18    | 1429    |
| macro     | strict      | 70.39     | 60.62  | 65.14    | 1429    |
| micro     | soft        | 74.94     | 64.56  | 69.36    | 1429    |
| macro     | soft        | 76.80     | 66.33  | 71.19    | 1429    |
| micro     | sbert_cross | 75.58     | 65.12  | 69.96    | 1429    |
| macro     | sbert_cross | 77.87     | 67.16  | 72.12    | 1429    |
| micro     | formula     | 74.81     | 64.45  | 69.24    | 1429    |
| macro     | formula     | 77.50     | 66.54  | 71.60    | 1429    |

- Predicted: [supermat-paragraphs-holdout.chatgpt-ft-ner-simple.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Fentities%2Fresults%2Frun3%2Fsupermat-paragraphs-holdout.chatgpt-ft-ner-simple.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 68.04     | 58.73  | 63.04    | 1432    |
| macro     | strict      | 70.28     | 60.72  | 65.15    | 1432    |
| micro     | soft        | 74.74     | 64.52  | 69.25    | 1432    |
| macro     | soft        | 76.71     | 66.39  | 71.18    | 1432    |
| micro     | sbert_cross | 75.52     | 65.18  | 69.97    | 1432    |
| macro     | sbert_cross | 77.88     | 67.28  | 72.19    | 1432    |
| micro     | formula     | 74.61     | 64.40  | 69.13    | 1432    |
| macro     | formula     | 77.41     | 66.60  | 71.60    | 1432    |

## GPT 4

- Predicted records: 1103 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run1/supermat-gpt4-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 61.03     | 64.18  | 62.57    | 1402    |
| macro     | strict      | 63.40     | 65.51  | 64.44    | 1402    |
| micro     | soft        | 76.00     | 79.92  | 77.91    | 1402    |
| macro     | soft        | 77.16     | 79.75  | 78.43    | 1402    |
| micro     | sbert_cross | 77.81     | 81.82  | 79.76    | 1402    |
| macro     | sbert_cross | 78.69     | 81.09  | 79.87    | 1402    |
| micro     | formula     | 61.10     | 49.34  | 54.60    | 1103    |
| macro     | formula     | 63.03     | 52.48  | 57.28    | 1103    |

- Predicted records: 1097 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run2/supermat-gpt4-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 45.53     | 36.68  | 40.63    | 1402    |
| macro     | strict      | 46.58     | 38.88  | 42.39    | 1402    |
| micro     | soft        | 52.60     | 42.38  | 46.94    | 1402    |
| macro     | soft        | 52.94     | 44.11  | 48.12    | 1402    |
| micro     | sbert_cross | 58.63     | 47.24  | 52.32    | 1402    |
| macro     | sbert_cross | 59.29     | 49.45  | 53.93    | 1402    |
| micro     | formula     | 61.54     | 49.58  | 54.92    | 1097    |
| macro     | formula     | 63.08     | 52.88  | 57.53    | 1097    |

- Predicted records: 1108 , files: 32 , input: resources/dataset/superMat/entities/results/run3//supermat-paragraphs-holdout.gpt4.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 45.06     | 36.20  | 40.15    | 1402    |
| macro     | strict      | 46.71     | 39.27  | 42.67    | 1402    |
| micro     | soft        | 52.26     | 41.98  | 46.56    | 1402    |
| macro     | soft        | 53.30     | 44.65  | 48.59    | 1402    |
| micro     | sbert_cross | 58.64     | 47.11  | 52.25    | 1402    |
| macro     | sbert_cross | 60.44     | 50.36  | 54.95    | 1402    |
| micro     | formula     | 60.29     | 48.43  | 53.71    | 1108    |
| macro     | formula     | 63.07     | 52.83  | 57.50    | 1108    |

## GPT4 + Few-shot with Grobid-superconductors

Predicted records: 1854 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run2/supermat-gpt4.few-shot-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 61.03     | 64.18  | 62.57    | 1402    |
| macro     | strict      | 63.40     | 65.51  | 64.44    | 1402    |
| micro     | soft        | 76.00     | 79.92  | 77.91    | 1402    |
| macro     | soft        | 77.16     | 79.75  | 78.43    | 1402    |
| micro     | sbert_cross | 77.81     | 81.82  | 79.76    | 1402    |
| macro     | sbert_cross | 78.69     | 81.09  | 79.87    | 1402    |
| micro     | formula     | 74.71     | 78.56  | 76.59    | 1412    |
| macro     | formula     | 76.20     | 78.86  | 77.51    | 1412    |

- Predicted records: 1854 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run2/supermat-gpt4.few-shot-holdout-material.csv

| Avg. type | Method  | Precision | Recall | F1-score | Support |
|-----------|---------|-----------|--------|----------|---------|
| micro     | strict  | 56.92     | 67.97  | 61.96    | 1402    |
| macro     | strict  | 58.92     | 70.51  | 64.20    | 1402    |
| micro     | soft    | 71.86     | 85.81  | 78.22    | 1402    |
| macro     | soft    | 72.87     | 87.08  | 79.34    | 1402    |
| micro     | sbert   | 73.39     | 87.63  | 79.88    | 1402    |
| macro     | sbert   | 74.37     | 88.84  | 80.96    | 1402    |
| micro     | formula | 68.48     | 81.77  | 74.54    | 1854    |
| macro     | formula | 70.10     | 83.83  | 76.35    | 1854    |

- Predicted records: 1826 , files: 32 , input: resources/dataset/superMat/entities/results/run3//supermat-paragraphs-holdout.gpt4.few-shot.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.35     | 69.05  | 63.25    | 1402    |
| macro     | strict      | 60.10     | 70.91  | 65.06    | 1402    |
| micro     | soft        | 72.97     | 86.35  | 79.09    | 1402    |
| macro     | soft        | 74.02     | 87.35  | 80.13    | 1402    |
| micro     | sbert_cross | 73.96     | 87.52  | 80.17    | 1402    |
| macro     | sbert_cross | 74.95     | 88.26  | 81.06    | 1402    |
| micro     | formula     | 69.67     | 82.44  | 75.52    | 1826    |
| macro     | formula     | 71.15     | 83.97  | 77.03    | 1826    |

## GPT4-Turbo

- Predicted records: 883 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run1/supermat-gpt4-turbo-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 27.89     | 19.92  | 23.25    | 1402    |
| macro     | strict      | 30.96     | 23.82  | 26.93    | 1402    |
| micro     | soft        | 45.00     | 32.14  | 37.50    | 1402    |
| macro     | soft        | 48.29     | 37.24  | 42.05    | 1402    |
| micro     | sbert_cross | 55.00     | 39.29  | 45.83    | 1402    |
| macro     | sbert_cross | 58.94     | 44.75  | 50.88    | 1402    |
| micro     | formula     | 64.47     | 46.05  | 53.73    | 883     |
| macro     | formula     | 67.94     | 51.36  | 58.50    | 883     |

- Predicted records: 873 , files: 32 , input: resources/dataset/superMat/entities/results/run2//supermat-paragraphs-holdout.gpt4-turbo.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 27.73     | 19.62  | 22.98    | 1402    |
| macro     | strict      | 30.52     | 23.23  | 26.38    | 1402    |
| micro     | soft        | 46.13     | 32.64  | 38.23    | 1402    |
| macro     | soft        | 49.26     | 37.10  | 42.33    | 1402    |
| micro     | sbert_cross | 54.93     | 38.87  | 45.52    | 1402    |
| macro     | sbert_cross | 59.00     | 43.65  | 50.18    | 1402    |
| micro     | formula     | 64.27     | 45.47  | 53.26    | 873     |
| macro     | formula     | 67.67     | 50.02  | 57.52    | 873     |

- Predicted records: 878 , files: 32 , input: resources/dataset/superMat/entities/results/run3//supermat-paragraphs-holdout.gpt4-turbo.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 28.46     | 20.53  | 23.85    | 1402    |
| macro     | strict      | 31.46     | 23.74  | 27.06    | 1402    |
| micro     | soft        | 45.69     | 32.96  | 38.29    | 1402    |
| macro     | soft        | 49.32     | 37.74  | 42.76    | 1402    |
| micro     | sbert_cross | 55.61     | 40.11  | 46.61    | 1402    |
| macro     | sbert_cross | 59.71     | 45.02  | 51.34    | 1402    |
| micro     | formula     | 64.23     | 46.33  | 53.83    | 878     |
| macro     | formula     | 67.45     | 50.78  | 57.94    | 878     |

## GPT4-Turbo + Few-shot with Grobid-superconductors

- Predicted records: 1735 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run1/supermat-gpt4-turbo-few-shot.holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 40.68     | 48.01  | 44.04    | 1402    |
| macro     | strict      | 42.73     | 50.83  | 46.43    | 1402    |
| micro     | soft        | 55.48     | 65.47  | 60.06    | 1402    |
| macro     | soft        | 57.15     | 67.06  | 61.71    | 1402    |
| micro     | sbert_cross | 58.39     | 68.91  | 63.22    | 1402    |
| macro     | sbert_cross | 59.95     | 70.32  | 64.72    | 1402    |
| micro     | formula     | 57.11     | 67.40  | 61.83    | 1735    |
| macro     | formula     | 58.84     | 69.84  | 63.87    | 1735    |

- Predicted records: 1707 , files: 32 , input: resources/dataset/superMat/entities/results/run2/supermat-paragraphs-holdout.gpt4-turbo.few-shot.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 40.76     | 46.85  | 43.59    | 1402    |
| macro     | strict      | 43.27     | 49.52  | 46.18    | 1402    |
| micro     | soft        | 56.73     | 65.21  | 60.68    | 1402    |
| macro     | soft        | 59.29     | 67.14  | 62.97    | 1402    |
| micro     | sbert_cross | 59.24     | 68.08  | 63.35    | 1402    |
| macro     | sbert_cross | 61.21     | 69.25  | 64.98    | 1402    |
| micro     | formula     | 57.93     | 66.58  | 61.95    | 1707    |
| macro     | formula     | 60.27     | 68.91  | 64.30    | 1707    |

- Predicted records: 1707 , files: 32 , input: resources/dataset/superMat/entities/results/run3/supermat-gpt4-turbo-few-shot.holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 41.82     | 48.49  | 44.91    | 1707    |
| macro     | strict      | 44.23     | 51.84  | 47.74    | 1707    |
| micro     | soft        | 56.99     | 66.07  | 61.20    | 1707    |
| macro     | soft        | 59.27     | 68.37  | 63.49    | 1707    |
| micro     | sbert_cross | 59.12     | 68.54  | 63.49    | 1707    |
| macro     | sbert_cross | 61.11     | 70.46  | 65.46    | 1707    |
| micro     | formula     | 57.94     | 67.17  | 62.21    | 1707    |
| macro     | formula     | 60.25     | 70.14  | 64.82    | 1707    |



