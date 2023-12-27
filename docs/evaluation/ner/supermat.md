## Grobid-superconductors

- Prompt: complex prompt with examples and the definitions taken from the guidelines
- Expected records: 1402 , files: 32 , input: resources/dataset/superMat/supermat-expected-holdout-material.csv

**NOTE**: This model was trained with the full SuperMat dataset, so testing with the holdout dataset will result in biased scores.
In the paper we report the scores from the original paper, which were obtained in a unbiased-way.
We report this information to show the real scores of the few-shot generated hints.  

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
| micro     | strict      | 22.57     | 13.65  | 17.01    | 1617    |
| macro     | strict      | 24.63     | 16.87  | 20.03    | 1617    |
| micro     | soft        | 26.37     | 15.94  | 19.87    | 1617    |
| macro     | soft        | 28.24     | 19.41  | 23.01    | 1617    |
| micro     | sbert_cross | 37.34     | 22.58  | 28.14    | 1617    |
| macro     | sbert_cross | 38.03     | 25.92  | 30.83    | 1617    |
| micro     | formula     | 59.49     | 35.97  | 44.83    | 1617    |
| macro     | formula     | 61.85     | 40.52  | 48.96    | 1617    |

- Predicted records: 1641 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run2//supermat-gpt35_turbo-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 22.57     | 13.90  | 17.21    | 1641    |
| macro     | strict      | 25.06     | 17.10  | 20.33    | 1641    |
| micro     | soft        | 26.29     | 16.20  | 20.05    | 1641    |
| macro     | soft        | 28.61     | 19.64  | 23.29    | 1641    |
| micro     | sbert_cross | 37.06     | 22.83  | 28.26    | 1641    |
| macro     | sbert_cross | 37.96     | 26.15  | 30.97    | 1641    |
| micro     | formula     | 59.21     | 36.48  | 45.15    | 1641    |
| macro     | formula     | 61.70     | 40.94  | 49.22    | 1641    |

- Predicted records: 1587 , files: 32 , input: resources/dataset/superMat/entities/results/run3//supermat-paragraphs-holdout.chatgpt.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 22.73     | 13.39  | 16.85    | 1587    |
| macro     | strict      | 25.41     | 16.67  | 20.13    | 1587    |
| micro     | soft        | 26.62     | 15.69  | 19.74    | 1587    |
| macro     | soft        | 29.07     | 19.21  | 23.13    | 1587    |
| micro     | sbert_cross | 37.45     | 22.07  | 27.77    | 1587    |
| macro     | sbert_cross | 38.57     | 25.10  | 30.41    | 1587    |
| micro     | formula     | 59.74     | 35.20  | 44.30    | 1587    |
| macro     | formula     | 62.83     | 39.76  | 48.70    | 1587    |

## chatgpt3.5-turbo + Few-shot with Grobid-superconductors

- Predicted records: 1887 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run1/supermat-gpt35_turbo-few-shot-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 59.21     | 57.40  | 58.29    | 1887    |
| macro     | strict      | 59.36     | 59.76  | 59.56    | 1887    |
| micro     | soft        | 70.92     | 68.75  | 69.82    | 1887    |
| macro     | soft        | 71.55     | 71.83  | 71.69    | 1887    |
| micro     | sbert_cross | 71.58     | 69.39  | 70.47    | 1887    |
| macro     | sbert_cross | 71.54     | 71.69  | 71.62    | 1887    |
| micro     | formula     | 75.79     | 73.47  | 74.61    | 1887    |
| macro     | formula     | 75.98     | 76.20  | 76.09    | 1887    |

- Predicted records: 2495 , files: 32 , input: resources/dataset/superMat/entities/results_prompt2/run2/supermat-ner-complex_prompt-holdout-few-shot.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 63.01     | 71.05  | 66.79    | 2495    |
| macro     | strict      | 64.83     | 73.35  | 68.82    | 2495    |
| micro     | soft        | 79.30     | 89.41  | 84.05    | 2495    |
| macro     | soft        | 80.05     | 90.81  | 85.09    | 2495    |
| micro     | sbert_cross | 78.73     | 88.78  | 83.45    | 2495    |
| macro     | sbert_cross | 78.99     | 89.63  | 83.98    | 2495    |
| micro     | formula     | 78.39     | 88.39  | 83.09    | 2495    |
| macro     | formula     | 79.33     | 89.91  | 84.29    | 2495    |

- Predicted records: 2448 , files: 32 , input: resources/dataset/superMat/entities/results/run3//supermat-paragraphs-holdout.chatgpt.few-shot.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| macro     | strict      | 65.02     | 73.61  | 69.05    | 2448    |
| micro     | soft        | 79.30     | 89.41  | 84.05    | 2448    |
| macro     | soft        | 80.06     | 90.88  | 85.13    | 2448    |
| micro     | sbert_cross | 78.85     | 88.90  | 83.57    | 2448    |
| macro     | sbert_cross | 79.06     | 89.78  | 84.08    | 2448    |
| micro     | formula     | 78.73     | 88.78  | 83.45    | 2448    |
| macro     | formula     | 79.59     | 90.29  | 84.60    | 2448    |

### GPT3.5-turbo Fine-tune

- Predicted: [supermat-paragraphs-holdout.chatgpt-ft-ner-simple.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Fentities%2Fresults%2Frun1%2Fsupermat-paragraphs-holdout.chatgpt-ft-ner-simple.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 68.48     | 64.29  | 66.32    | 1429    |
| macro     | strict      | 71.19     | 65.71  | 68.34    | 1429    |
| micro     | soft        | 71.47     | 67.09  | 69.21    | 1429    |
| macro     | soft        | 74.04     | 68.68  | 71.26    | 1429    |
| micro     | sbert_cross | 71.88     | 67.47  | 69.61    | 1429    |
| macro     | sbert_cross | 74.12     | 68.69  | 71.30    | 1429    |
| micro     | formula     | 79.89     | 75.00  | 77.37    | 1429    |
| macro     | formula     | 82.83     | 76.79  | 79.69    | 1429    |

- Predicted: [supermat-paragraphs-holdout.chatgpt-ft-ner-simple.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Fentities%2Fresults%2Frun2%2Fsupermat-paragraphs-holdout.chatgpt-ft-ner-simple.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 68.98     | 64.67  | 66.75    | 1429    |
| macro     | strict      | 71.45     | 66.07  | 68.66    | 1429    |
| micro     | soft        | 71.84     | 67.35  | 69.52    | 1429    |
| macro     | soft        | 74.21     | 68.98  | 71.50    | 1429    |
| micro     | sbert_cross | 72.24     | 67.73  | 69.91    | 1429    |
| macro     | sbert_cross | 74.29     | 68.98  | 71.54    | 1429    |
| micro     | formula     | 80.14     | 75.13  | 77.55    | 1429    |
| macro     | formula     | 82.91     | 77.02  | 79.85    | 1429    |

- Predicted: [supermat-paragraphs-holdout.chatgpt-ft-ner-simple.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Fentities%2Fresults%2Frun3%2Fsupermat-paragraphs-holdout.chatgpt-ft-ner-simple.output.csv)

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 68.89     | 64.41  | 66.58    | 1432    |
| macro     | strict      | 71.54     | 65.82  | 68.56    | 1432    |
| micro     | soft        | 71.90     | 67.22  | 69.48    | 1432    |
| macro     | soft        | 74.39     | 68.79  | 71.48    | 1432    |
| micro     | sbert_cross | 72.17     | 67.47  | 69.74    | 1432    |
| macro     | sbert_cross | 74.37     | 68.68  | 71.41    | 1432    |
| micro     | formula     | 80.08     | 74.87  | 77.39    | 1432    |
| macro     | formula     | 82.89     | 76.68  | 79.66    | 1432    |

## GPT 4

- Predicted records: 1103 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run1/supermat-gpt4-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 45.21     | 28.32  | 34.82    | 1103    |
| macro     | strict      | 46.77     | 32.35  | 38.25    | 1103    |
| micro     | soft        | 45.82     | 28.70  | 35.29    | 1103    |
| macro     | soft        | 47.22     | 32.66  | 38.62    | 1103    |
| micro     | sbert_cross | 49.90     | 31.25  | 38.43    | 1103    |
| macro     | sbert_cross | 51.40     | 35.00  | 41.64    | 1103    |
| micro     | formula     | 66.40     | 41.58  | 51.14    | 1103    |
| macro     | formula     | 68.45     | 46.25  | 55.20    | 1103    |

- Predicted records: 1097 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run2/supermat-gpt4-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 45.53     | 27.93  | 34.62    | 1097    |
| macro     | strict      | 46.58     | 32.11  | 38.02    | 1097    |
| micro     | soft        | 45.95     | 28.19  | 34.94    | 1097    |
| macro     | soft        | 46.87     | 32.33  | 38.26    | 1097    |
| micro     | sbert_cross | 49.90     | 30.61  | 37.94    | 1097    |
| macro     | sbert_cross | 51.01     | 34.60  | 41.23    | 1097    |
| micro     | formula     | 66.94     | 41.07  | 50.91    | 1097    |
| macro     | formula     | 68.65     | 45.92  | 55.03    | 1097    |

- Predicted records: 1108 , files: 32 , input: resources/dataset/superMat/entities/results/run3//supermat-paragraphs-holdout.gpt4.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 45.06     | 27.93  | 34.49    | 1108    |
| macro     | strict      | 46.71     | 31.96  | 37.95    | 1108    |
| micro     | soft        | 45.47     | 28.19  | 34.80    | 1108    |
| macro     | soft        | 46.98     | 32.17  | 38.19    | 1108    |
| micro     | sbert_cross | 49.59     | 30.74  | 37.95    | 1108    |
| macro     | sbert_cross | 51.69     | 34.51  | 41.39    | 1108    |
| micro     | formula     | 66.46     | 41.20  | 50.87    | 1108    |
| macro     | formula     | 69.61     | 45.95  | 55.36    | 1108    |

## GPT4 + Few-shot with Grobid-superconductors

Predicted records: 1854 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run2/supermat-gpt4.few-shot-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 61.03     | 60.33  | 60.68    | 1412    |
| macro     | strict      | 63.40     | 62.11  | 62.75    | 1412    |
| micro     | soft        | 75.35     | 74.49  | 74.92    | 1412    |
| macro     | soft        | 76.55     | 75.11  | 75.82    | 1412    |
| micro     | sbert_cross | 75.87     | 75.00  | 75.43    | 1412    |
| macro     | sbert_cross | 76.84     | 75.13  | 75.97    | 1412    |
| micro     | formula     | 77.16     | 76.28  | 76.72    | 1412    |
| macro     | formula     | 78.79     | 77.51  | 78.14    | 1412    |

- Predicted records: 1854 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run2/supermat-gpt4.few-shot-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 56.92     | 66.58  | 61.38    | 1854    |
| macro     | strict      | 58.92     | 68.83  | 63.49    | 1854    |
| micro     | soft        | 71.21     | 83.29  | 76.78    | 1854    |
| macro     | soft        | 72.30     | 84.52  | 77.93    | 1854    |
| micro     | sbert_cross | 70.67     | 82.65  | 76.19    | 1854    |
| macro     | sbert_cross | 71.38     | 83.38  | 76.91    | 1854    |
| micro     | formula     | 70.99     | 83.04  | 76.54    | 1854    |
| macro     | formula     | 72.58     | 84.86  | 78.24    | 1854    |

- Predicted records: 1826 , files: 32 , input: resources/dataset/superMat/entities/results/run3//supermat-paragraphs-holdout.gpt4.few-shot.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 58.35     | 67.73  | 62.69    | 1826    |
| macro     | strict      | 60.10     | 69.35  | 64.40    | 1826    |
| micro     | soft        | 72.42     | 84.06  | 77.80    | 1826    |
| macro     | soft        | 73.53     | 84.99  | 78.84    | 1826    |
| micro     | sbert_cross | 72.09     | 83.67  | 77.45    | 1826    |
| macro     | sbert_cross | 72.70     | 84.01  | 77.95    | 1826    |
| micro     | formula     | 72.09     | 83.67  | 77.45    | 1826    |
| macro     | formula     | 73.42     | 84.71  | 78.66    | 1826    |

## GPT4-Turbo

- Predicted records: 883 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run1/supermat-gpt4-turbo-holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 27.89     | 13.52  | 18.21    | 883     |
| macro     | strict      | 30.96     | 17.82  | 22.62    | 883     |
| micro     | soft        | 31.05     | 15.05  | 20.27    | 883     |
| macro     | soft        | 34.25     | 19.25  | 24.65    | 883     |
| micro     | sbert_cross | 45.53     | 22.07  | 29.73    | 883     |
| macro     | sbert_cross | 49.09     | 26.97  | 34.81    | 883     |
| micro     | formula     | 70.53     | 34.18  | 46.05    | 883     |
| macro     | formula     | 73.94     | 39.32  | 51.34    | 883     |

- Predicted records: 873 , files: 32 , input: resources/dataset/superMat/entities/results/run2//supermat-paragraphs-holdout.gpt4-turbo.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 27.73     | 13.27  | 17.95    | 873     |
| macro     | strict      | 30.52     | 17.63  | 22.35    | 873     |
| micro     | soft        | 30.93     | 14.80  | 20.02    | 873     |
| macro     | soft        | 33.81     | 19.07  | 24.39    | 873     |
| micro     | sbert_cross | 46.67     | 22.32  | 30.20    | 873     |
| macro     | sbert_cross | 50.67     | 27.39  | 35.56    | 873     |
| micro     | formula     | 70.67     | 33.80  | 45.73    | 873     |
| macro     | formula     | 74.28     | 39.36  | 51.46    | 873     |

- Predicted records: 878 , files: 32 , input: resources/dataset/superMat/entities/results/run3//supermat-paragraphs-holdout.gpt4-turbo.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 28.46     | 13.90  | 18.68    | 878     |
| macro     | strict      | 31.46     | 17.97  | 22.87    | 878     |
| micro     | soft        | 31.85     | 15.56  | 20.91    | 878     |
| macro     | soft        | 35.28     | 19.78  | 25.35    | 878     |
| micro     | sbert_cross | 46.74     | 22.83  | 30.68    | 878     |
| macro     | sbert_cross | 50.39     | 28.06  | 36.04    | 878     |
| micro     | formula     | 70.50     | 34.44  | 46.27    | 878     |
| macro     | formula     | 73.90     | 39.76  | 51.70    | 878     |

## GPT4-Turbo + Few-shot with Grobid-superconductors

- Predicted records: 1735 , files: 32 , input: resources/dataset/superMat/entities/results_prompt_complex/run1/supermat-gpt4-turbo-few-shot.holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 40.68     | 44.52  | 42.51    | 1735    |
| macro     | strict      | 42.73     | 47.00  | 44.77    | 1735    |
| micro     | soft        | 50.82     | 55.61  | 53.11    | 1735    |
| macro     | soft        | 52.81     | 57.53  | 55.07    | 1735    |
| micro     | sbert_cross | 54.78     | 59.95  | 57.25    | 1735    |
| macro     | sbert_cross | 56.11     | 61.20  | 58.54    | 1735    |
| micro     | formula     | 60.26     | 65.94  | 62.97    | 1735    |
| macro     | formula     | 62.29     | 68.20  | 65.11    | 1735    |

- Predicted records: 1707 , files: 32 , input: resources/dataset/superMat/entities/results/run2/supermat-paragraphs-holdout.gpt4-turbo.few-shot.output.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 40.76     | 43.62  | 42.14    | 1707    |
| macro     | strict      | 43.27     | 46.27  | 44.72    | 1707    |
| micro     | soft        | 52.32     | 55.99  | 54.10    | 1707    |
| macro     | soft        | 55.16     | 58.61  | 56.83    | 1707    |
| micro     | sbert_cross | 55.54     | 59.44  | 57.42    | 1707    |
| macro     | sbert_cross | 57.57     | 61.11  | 59.29    | 1707    |
| micro     | formula     | 60.91     | 65.18  | 62.97    | 1707    |
| macro     | formula     | 63.58     | 67.76  | 65.61    | 1707    |

- Predicted records: 1707 , files: 32 , input: resources/dataset/superMat/entities/results/run3/supermat-gpt4-turbo-few-shot.holdout-material.csv

| Avg. type | Method      | Precision | Recall | F1-score | Support |
|-----------|-------------|-----------|--------|----------|---------|
| micro     | strict      | 41.82     | 45.03  | 43.37    | 1707    |
| macro     | strict      | 44.23     | 48.15  | 46.11    | 1707    |
| micro     | soft        | 52.96     | 57.02  | 54.91    | 1707    |
| macro     | soft        | 55.63     | 60.03  | 57.74    | 1707    |
| micro     | sbert_cross | 55.81     | 60.08  | 57.86    | 1707    |
| macro     | sbert_cross | 57.68     | 62.12  | 59.82    | 1707    |
| micro     | formula     | 61.02     | 65.69  | 63.27    | 1707    |
| macro     | formula     | 63.55     | 68.61  | 65.98    | 1707    |




