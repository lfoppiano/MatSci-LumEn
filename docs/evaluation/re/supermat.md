# Evaluation of RE using SuperMat

## Zero-shot generation

```
Consider the following text in between triple quotes: 
"""
{text}
"""

Find the relations between lists of entities of different classes. 
Apply strictly the following  rules:  
    - if material is not specified, ignore the relation block,
    - if tc is not specified in absolute values, ignore the relation block 
    
Following the lists of entities: 
{entities}
```

### GPT3.5-turbo (not shuffled)

- Predicted: [supermat-paragraphs-all.gpt3.5_turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt3.5_turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.41     | 76.48  | 78.39    | 514     |
| macro     | strict        | 82.97     | 80.12  | 81.52    | 514     |
| micro     | soft          | 80.73     | 76.78  | 78.71    | 514     |
| macro     | soft          | 83.46     | 80.61  | 82.01    | 514     |

- Predicted: [supermat-paragraphs-all.gpt3.5_turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt3.5_turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.41     | 76.28  | 78.29    | 385     |
| macro     | strict        | 82.44     | 79.71  | 81.05    | 385     |
| micro     | soft          | 80.80     | 76.65  | 78.67    | 385     |
| macro     | soft          | 82.99     | 80.27  | 81.61    | 385     |

- Predicted records: 790 , files: 125 , input: resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.chatgpt.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.25     | 76.57  | 78.37    | 386     |
| macro     | strict        | 82.49     | 79.89  | 81.17    | 386     |
| micro     | soft          | 80.51     | 76.81  | 78.62    | 386     |
| macro     | soft          | 82.79     | 80.19  | 81.47    | 386     |

### GPT-3.5 turbo (shuffled)

- Predicted: [supermat-paragraphs-all.gpt3.5_turbo.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt3.5_turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.12     | 69.92  | 72.89    | 518     |
| macro     | strict        | 81.24     | 77.89  | 79.53    | 518     |
| micro     | soft          | 76.67     | 70.42  | 73.41    | 518     |
| macro     | soft          | 81.88     | 78.52  | 80.17    | 518     |

- Predicted: [supermat-paragraphs-all.gpt3.5_turbo.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt3.5_turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 72.08     | 67.11  | 69.51    | 390     |
| macro     | strict        | 78.20     | 75.11  | 76.62    | 390     |
| micro     | soft          | 73.12     | 68.08  | 70.51    | 390     |
| macro     | soft          | 79.28     | 76.18  | 77.70    | 390     |

- Predicted records: 757 , files: 125 , input: resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.chatgpt.shuffled.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 74.90     | 68.07  | 71.32    | 392     |
| macro     | strict        | 78.46     | 74.25  | 76.30    | 392     |
| micro     | soft          | 75.17     | 68.31  | 71.57    | 392     |
| macro     | soft          | 78.97     | 74.76  | 76.81    | 392     |

### GPT-3.5-turbo Fine-tuned (FT: not shuffled, EVAL: not shuffled)

- Predicted records: 127 , files: 25 , input: resources/dataset/superMat/relations/results_prompt1/run1/supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 88.98     | 88.98  | 88.98    | 80      |
| macro     | strict        | 90.42     | 89.17  | 89.79    | 80      |
| micro     | soft          | 91.34     | 91.34  | 91.34    | 80      |
| macro     | soft          | 92.08     | 90.83  | 91.45    | 80      |

- Predicted records: 127 , files: 25 , input: resources/dataset/superMat/relations/results_prompt1/run2/supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 88.98     | 88.98  | 88.98    | 80      |
| macro     | strict        | 90.42     | 89.17  | 89.79    | 80      |
| micro     | soft          | 91.34     | 91.34  | 91.34    | 80      |
| macro     | soft          | 92.08     | 90.83  | 91.45    | 80      |

- Predicted records: 127 , files: 25 , input: resources/dataset/superMat/relations/results_prompt1/run3/supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 88.98     | 88.98  | 88.98    | 80      |
| macro     | strict        | 90.42     | 89.17  | 89.79    | 80      |
| micro     | soft          | 91.34     | 91.34  | 91.34    | 80      |
| macro     | soft          | 92.08     | 90.83  | 91.45    | 80      |

### GPT-3.5-turbo Fine-tuned (FT: not-shuffled, EVAL: shuffled)

- Predicted:[supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.1.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-fine-tuning%2Fsupermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.1.output.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 47.73     | 47.73  | 47.73    | 132     |
| macro     | strict        | 54.56     | 59.72  | 57.03    | 132     |
| micro     | soft          | 48.48     | 48.48  | 48.48    | 132     |
| macro     | soft          | 54.96     | 60.12  | 57.42    | 132     |

- Predicted: [supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.2.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-fine-tuning%2Fsupermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.2.output.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 55.73     | 55.73  | 55.73    | 131     |
| macro     | strict        | 58.96     | 64.38  | 61.55    | 131     |
| micro     | soft          | 55.73     | 55.73  | 55.73    | 131     |
| macro     | soft          | 58.96     | 64.38  | 61.55    | 131     |

- Predicted: [supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.3.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-fine-tuning%2Fsupermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.3.output.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 57.72     | 55.04  | 56.35    | 123     |
| macro     | strict        | 60.04     | 65.43  | 62.62    | 123     |
| micro     | soft          | 57.72     | 55.04  | 56.35    | 123     |
| macro     | soft          | 60.04     | 65.43  | 62.62    | 123     |

### GPT-3.5-Turbo fine-tuned (FT: shuffled, EVAL: not-shuffled)

We shuffled and keep the same number of training examples for the fine-tuning

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 91.06     | 88.19  | 89.60    | 80      |
| macro     | strict        | 91.67     | 90.42  | 91.04    | 80      |
| micro     | soft          | 93.50     | 90.55  | 92.00    | 80      |
| macro     | soft          | 93.33     | 92.08  | 92.70    | 80      |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 91.06     | 88.19  | 89.60    | 80      |
| macro     | strict        | 91.67     | 90.42  | 91.04    | 80      |
| micro     | soft          | 93.50     | 90.55  | 92.00    | 80      |
| macro     | soft          | 93.33     | 92.08  | 92.70    | 80      |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 91.06     | 88.19  | 89.60    | 80      |
| macro     | strict        | 91.67     | 90.42  | 91.04    | 80      |
| micro     | soft          | 93.50     | 90.55  | 92.00    | 80      |
| macro     | soft          | 93.33     | 92.08  | 92.70    | 80      |

### GPT-3.5-Turbo fine-tuned (FT: shuffled, EVAL: shuffled)

We shuffled and keep the same number of training examples for the fine-tuning

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 92.68     | 89.76  | 91.20    | 80      |
| macro     | strict        | 92.92     | 91.67  | 92.29    | 80      |
| micro     | soft          | 95.12     | 92.13  | 93.60    | 80      |
| macro     | soft          | 94.58     | 93.33  | 93.95    | 80      |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 91.80     | 88.89  | 90.32    | 79      |
| macro     | strict        | 93.67     | 92.41  | 93.03    | 79      |
| micro     | soft          | 94.26     | 91.27  | 92.74    | 79      |
| macro     | soft          | 95.36     | 94.09  | 94.72    | 79      |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 91.06     | 88.19  | 89.60    | 80      |
| macro     | strict        | 92.50     | 91.25  | 91.87    | 80      |
| micro     | soft          | 93.50     | 90.55  | 92.00    | 80      |
| macro     | soft          | 94.17     | 92.92  | 93.54    | 80      |

### GPT-3.5-Turbo fine-tuned (FT: shuffled + augmented, EVAL: not-shuffled)

We shuffled + augment the number of training examples for the fine-tuning

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 89.60     | 91.06  | 90.32    | 77      |
| macro     | strict        | 92.56     | 92.10  | 92.33    | 77      |
| micro     | soft          | 92.00     | 93.50  | 92.74    | 77      |
| macro     | soft          | 94.29     | 93.83  | 94.06    | 77      |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 89.60     | 91.06  | 90.32    | 77      |
| macro     | strict        | 92.56     | 92.10  | 92.33    | 77      |
| micro     | soft          | 92.00     | 93.50  | 92.74    | 77      |
| macro     | soft          | 94.29     | 93.83  | 94.06    | 77      |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 89.60     | 91.06  | 90.32    | 77      |
| macro     | strict        | 92.56     | 92.10  | 92.33    | 77      |
| micro     | soft          | 92.00     | 93.50  | 92.74    | 77      |
| macro     | soft          | 94.29     | 93.83  | 94.06    | 77      |

### GPT-3.5-Turbo fine-tuned (FT: shuffled + augmented, EVAL: shuffled)

We shuffled + augment the number of training examples for the fine-tuning

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 91.13     | 91.87  | 91.50    | 77      |
| macro     | strict        | 94.59     | 93.51  | 94.04    | 77      |
| micro     | soft          | 91.94     | 92.68  | 92.31    | 77      |
| macro     | soft          | 95.02     | 93.94  | 94.48    | 77      |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 87.90     | 88.62  | 88.26    | 77      |
| macro     | strict        | 92.10     | 91.45  | 91.77    | 77      |
| micro     | soft          | 88.71     | 89.43  | 89.07    | 77      |
| macro     | soft          | 92.53     | 91.88  | 92.21    | 77      |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 89.52     | 90.24  | 89.88    | 77      |
| macro     | strict        | 93.29     | 92.21  | 92.75    | 77      |
| micro     | soft          | 91.94     | 92.68  | 92.31    | 77      |
| macro     | soft          | 95.02     | 93.94  | 94.48    | 77      |

### GPT-4 (not shuffled)

- Predicted: [supermat-paragraphs-all.gpt4.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt4.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.87     | 72.48  | 74.61    | 563     |
| macro     | strict        | 77.17     | 75.20  | 76.18    | 563     |
| micro     | soft          | 77.47     | 73.05  | 75.20    | 563     |
| macro     | soft          | 78.06     | 76.09  | 77.06    | 563     |

- Predicted: [supermat-paragraphs-all.gpt4.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt4.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.40     | 73.03  | 74.68    | 573     |
| macro     | strict        | 76.09     | 74.71  | 75.39    | 573     |
| micro     | soft          | 76.50     | 73.12  | 74.77    | 573     |
| macro     | soft          | 76.18     | 74.79  | 75.48    | 573     |

- Predicted records: 1013 , files: 142 , input: resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.gpt4.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.80     | 73.47  | 75.10    | 570     |
| macro     | strict        | 77.43     | 75.78  | 76.60    | 570     |
| micro     | soft          | 76.90     | 73.56  | 75.19    | 570     |
| macro     | soft          | 77.51     | 75.87  | 76.68    | 570     |

### GPT-4 (shuffled)

- Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 75.86     | 71.33  | 73.53    | 568     |
| macro     | strict        | 75.46     | 73.75  | 74.60    | 568     |
| micro     | soft          | 76.16     | 71.62  | 73.82    | 568     |
| macro     | soft          | 75.76     | 74.04  | 74.89    | 568     |

- Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 74.06     | 70.57  | 72.27    | 570     |
| macro     | strict        | 74.65     | 73.07  | 73.85    | 570     |
| micro     | soft          | 74.06     | 70.57  | 72.27    | 570     |
| macro     | soft          | 74.65     | 73.07  | 73.85    | 570     |

- Predicted records: 1007 , files: 142 , input: resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.gpt4.shuffled.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 75.37     | 71.60  | 73.44    | 571     |
| macro     | strict        | 75.58     | 74.18  | 74.87    | 571     |
| micro     | soft          | 75.57     | 71.79  | 73.63    | 571     |
| macro     | soft          | 75.70     | 74.30  | 75.00    | 571     |

### GPT-4-Turbo (not-shuffled)

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt4-turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 79.80     | 74.25  | 76.92    | 572     |
| macro     | strict        | 79.73     | 77.02  | 78.35    | 572     |
| micro     | soft          | 80.61     | 75.00  | 77.70    | 572     |
| macro     | soft          | 80.49     | 77.78  | 79.11    | 572     |

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt4-turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.22     | 74.55  | 77.28    | 572     |
| macro     | strict        | 80.29     | 77.49  | 78.86    | 572     |
| micro     | soft          | 81.03     | 75.31  | 78.07    | 572     |
| macro     | soft          | 81.01     | 78.21  | 79.59    | 572     |

- Predicted records: 989 , files: 142 , input: resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.gpt4-turbo.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 78.87     | 73.65  | 76.17    | 571     |
| macro     | strict        | 79.81     | 77.07  | 78.41    | 571     |
| micro     | soft          | 79.88     | 74.60  | 77.15    | 571     |
| macro     | soft          | 80.92     | 78.18  | 79.52    | 571     |

### GPT-4-Turbo (shuffled)

- Predicted: [supermat-paragraphs-all.gpt4-turbo.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt4-turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.04     | 72.44  | 76.05    | 572     |
| macro     | strict        | 79.99     | 76.80  | 78.36    | 572     |
| micro     | soft          | 80.98     | 73.28  | 76.94    | 572     |
| macro     | soft          | 80.83     | 77.64  | 79.21    | 572     |

- Predicted: [supermat-paragraphs-all.gpt4-turbo.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt4-turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.71     | 73.23  | 76.79    | 570     |
| macro     | strict        | 80.84     | 77.31  | 79.03    | 570     |
| micro     | soft          | 81.44     | 73.89  | 77.48    | 570     |
| macro     | soft          | 81.77     | 78.25  | 79.97    | 570     |

- Predicted records: 960 , files: 142 , input: resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.gpt4-turbo.shuffled.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 79.27     | 71.72  | 75.31    | 571     |
| macro     | strict        | 79.81     | 76.27  | 78.00    | 571     |
| micro     | soft          | 80.21     | 72.57  | 76.20    | 571     |
| macro     | soft          | 80.72     | 77.18  | 78.91    | 571     |

## Few-shot generation

```
Given a text between triple quotes and a list of entities, find the relations between entities of different classes: 
"""
{text}
"""

{entities}

--------
Example: 
The researchers of Mg have discovered that MgB2 is superconducting at 29 K at ambient pressure.

entities:
 materials: MgB2, Mg
 tcs: 29K
 pressure: ambient pressure
 
Result: 
 material: MgB2, 
 tc: 29K, 
 pressure: ambient pressure: 
 
--------
Apply strictly the following rules:  
    - if material is not specified, ignore the relation block,
    - if tc is not specified in absolute values, ignore the relation block 
```

### GPT-3.5-turbo (not shuffled)

- Predicted:  [supermat-paragraphs-all.chatgpt.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun1%2Fsupermat-paragraphs-all.chatgpt.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 67.97     | 65.34  | 66.63    | 428     |
| macro     | strict        | 70.51     | 69.12  | 69.81    | 428     |
| micro     | soft          | 69.27     | 66.59  | 67.90    | 428     |
| macro     | soft          | 72.03     | 70.64  | 71.33    | 428     |

- Predicted: [supermat-paragraphs-all.chatgpt.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun2%2Fsupermat-paragraphs-all.chatgpt.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 68.20     | 65.42  | 66.78    | 426     |
| macro     | strict        | 70.73     | 69.53  | 70.13    | 426     |
| micro     | soft          | 69.50     | 66.67  | 68.06    | 426     |
| macro     | soft          | 72.22     | 71.02  | 71.61    | 426     |

- Predicted: [supermat-paragraphs-all.chatgpt.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-few_shot%2Frun3%2Fsupermat-paragraphs-all.chatgpt.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 69.23     | 66.28  | 67.72    | 423     |
| macro     | strict        | 71.18     | 70.00  | 70.58    | 423     |
| micro     | soft          | 70.19     | 67.20  | 68.67    | 423     |
| macro     | soft          | 72.32     | 71.14  | 71.73    | 423     |

### GPT-3.5-turbo (shuffled)

- Predicted: [supermat-paragraphs-all.chatgpt.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun1%2Fsupermat-paragraphs-all.chatgpt.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 63.97     | 62.00  | 62.97    | 431     |
| macro     | strict        | 69.07     | 67.27  | 68.15    | 431     |
| micro     | soft          | 66.08     | 64.05  | 65.05    | 431     |
| macro     | soft          | 71.15     | 69.35  | 70.24    | 431     |

- Predicted: [supermat-paragraphs-all.chatgpt.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun2%2Fsupermat-paragraphs-all.chatgpt.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 66.02     | 61.68  | 63.77    | 428     |
| macro     | strict        | 68.85     | 67.44  | 68.14    | 428     |
| micro     | soft          | 67.23     | 62.81  | 64.95    | 428     |
| macro     | soft          | 70.16     | 68.77  | 69.46    | 428     |

- Predicted: [supermat-paragraphs-all.chatgpt.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-few_shot%2Frun3%2Fsupermat-paragraphs-all.chatgpt.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 62.24     | 59.24  | 60.71    | 431     |
| macro     | strict        | 67.67     | 66.28  | 66.96    | 431     |
| micro     | soft          | 63.93     | 60.85  | 62.35    | 431     |
| macro     | soft          | 69.45     | 68.06  | 68.75    | 431     |

### GPT-4 (not shuffled)

- Predicted: [supermat-paragraphs-all.gpt4.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun1%2Fsupermat-paragraphs-all.gpt4.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.57     | 76.51  | 78.49    | 576     |
| macro     | strict        | 82.98     | 81.00  | 81.98    | 576     |
| micro     | soft          | 80.57     | 76.51  | 78.49    | 576     |
| macro     | soft          | 82.98     | 81.00  | 81.98    | 576     |

- Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun2%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 81.29     | 77.21  | 79.20    | 578     |
| macro     | strict        | 83.25     | 81.21  | 82.22    | 578     |
| micro     | soft          | 81.39     | 77.30  | 79.29    | 578     |
| macro     | soft          | 83.31     | 81.27  | 82.28    | 578     |

- Predicted: [supermat-paragraphs-all.gpt4.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-few_shot%2Frun3%2Fsupermat-paragraphs-all.gpt4.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.90     | 77.05  | 78.93    | 576     |
| macro     | strict        | 83.55     | 81.35  | 82.43    | 576     |
| micro     | soft          | 80.90     | 77.05  | 78.93    | 576     |
| macro     | soft          | 83.55     | 81.35  | 82.43    | 576     |

### GPT-4 (shuffled)

- Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun1%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 79.41     | 75.02  | 77.15    | 575     |
| macro     | strict        | 82.97     | 80.65  | 81.79    | 575     |
| micro     | soft          | 79.50     | 75.12  | 77.25    | 575     |
| macro     | soft          | 83.03     | 80.71  | 81.85    | 575     |

- Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun2%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 79.72     | 75.56  | 77.59    | 576     |
| macro     | strict        | 82.28     | 80.53  | 81.39    | 576     |
| micro     | soft          | 80.02     | 75.84  | 77.87    | 576     |
| macro     | soft          | 82.45     | 80.70  | 81.57    | 576     |

- Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-few_shot%2Frun3%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.14     | 75.35  | 77.67    | 575     |
| macro     | strict        | 82.33     | 80.22  | 81.26    | 575     |
| micro     | soft          | 80.14     | 75.35  | 77.67    | 575     |
| macro     | soft          | 82.33     | 80.22  | 81.26    | 575     |

### GPT-4-Turbo (not-shuffled)

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun1%2Fsupermat-paragraphs-all.gpt4-turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 83.44     | 77.47  | 80.34    | 550     |
| macro     | strict        | 86.69     | 83.68  | 85.16    | 550     |
| micro     | soft          | 84.69     | 78.63  | 81.54    | 550     |
| macro     | soft          | 88.02     | 85.01  | 86.49    | 550     |

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun2%2Fsupermat-paragraphs-all.gpt4-turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 84.10     | 77.68  | 80.76    | 551     |
| macro     | strict        | 87.24     | 83.65  | 85.41    | 551     |
| micro     | soft          | 85.46     | 78.94  | 82.07    | 551     |
| macro     | soft          | 88.75     | 85.17  | 86.92    | 551     |

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-few_shot%2Frun3%2Fsupermat-paragraphs-all.gpt4-turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 84.01     | 77.68  | 80.72    | 550     |
| macro     | strict        | 87.06     | 83.93  | 85.47    | 550     |
| micro     | soft          | 85.37     | 78.94  | 82.03    | 550     |
| macro     | soft          | 88.33     | 85.21  | 86.74    | 550     |

### GPT-4-Turbo (shuffled)

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun1%2Fsupermat-paragraphs-all.gpt4-turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 82.01     | 74.15  | 77.89    | 549     |
| macro     | strict        | 86.09     | 82.35  | 84.18    | 549     |
| micro     | soft          | 83.51     | 75.51  | 79.31    | 549     |
| macro     | soft          | 87.39     | 83.66  | 85.49    | 549     |

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun2%2Fsupermat-paragraphs-all.gpt4-turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 84.11     | 76.71  | 80.24    | 551     |
| macro     | strict        | 87.46     | 83.55  | 85.46    | 551     |
| micro     | soft          | 85.49     | 77.97  | 81.56    | 551     |
| macro     | soft          | 88.88     | 84.94  | 86.87    | 551     |

- Predicted: [supermat-paragraphs-all.gpt4-turbo.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-few_shot%2Frun3%2Fsupermat-paragraphs-all.gpt4-turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 82.31     | 74.86  | 78.41    | 553     |
| macro     | strict        | 85.69     | 82.06  | 83.84    | 553     |
| micro     | soft          | 84.32     | 76.69  | 80.32    | 553     |
| macro     | soft          | 87.62     | 83.95  | 85.74    | 553     |
