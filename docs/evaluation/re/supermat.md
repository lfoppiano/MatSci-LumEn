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
| micro     | strict        | 80.41     | 65.70  | 72.32    | 934     |
| macro     | strict        | 67.59     | 65.26  | 66.40    | 934     |
| micro     | soft          | 80.73     | 65.97  | 72.60    | 934     |
| macro     | soft          | 67.98     | 65.66  | 66.80    | 934     |

- Predicted: [supermat-paragraphs-all.gpt3.5_turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt3.5_turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.41     | 54.59  | 65.03    | 776     |
| macro     | strict        | 50.30     | 48.63  | 49.45    | 776     |
| micro     | soft          | 80.80     | 54.86  | 65.35    | 776     |
| macro     | soft          | 50.64     | 48.97  | 49.79    | 776     |

- Predicted records: 790 , files: 125 , input: resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.chatgpt.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.25     | 55.47  | 65.60    | 790     |
| macro     | strict        | 50.46     | 48.87  | 49.65    | 790     |
| micro     | soft          | 80.51     | 55.64  | 65.80    | 790     |
| macro     | soft          | 50.64     | 49.05  | 49.84    | 790     |

### GPT-3.5 turbo (shuffled)

- Predicted: [supermat-paragraphs-all.gpt3.5_turbo.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt3.5_turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.12     | 60.80  | 67.61    | 913     |
| macro     | strict        | 66.69     | 63.94  | 65.29    | 913     |
| micro     | soft          | 76.67     | 61.24  | 68.09    | 913     |
| macro     | soft          | 67.22     | 64.46  | 65.81    | 913     |

- Predicted: [supermat-paragraphs-all.gpt3.5_turbo.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt3.5_turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 72.08     | 48.56  | 58.02    | 770     |
| macro     | strict        | 48.34     | 46.42  | 47.36    | 770     |
| micro     | soft          | 73.12     | 49.26  | 58.86    | 770     |
| macro     | soft          | 49.00     | 47.09  | 48.02    | 770     |

- Predicted records: 757 , files: 125 , input: resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.chatgpt.shuffled.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 74.90     | 49.61  | 59.68    | 757     |
| macro     | strict        | 48.74     | 46.13  | 47.40    | 757     |
| micro     | soft          | 75.17     | 49.78  | 59.89    | 757     |
| macro     | soft          | 49.06     | 46.45  | 47.72    | 757     |

### GPT-4 (not shuffled)

- Predicted: [supermat-paragraphs-all.gpt4.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt4.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.87     | 66.58  | 71.35    | 990     |
| macro     | strict        | 68.86     | 67.10  | 67.97    | 990     |
| micro     | soft          | 77.47     | 67.10  | 71.92    | 990     |
| macro     | soft          | 69.65     | 67.89  | 68.76    | 990     |

- Predicted: [supermat-paragraphs-all.gpt4.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt4.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.40     | 67.98  | 71.94    | 1017    |
| macro     | strict        | 69.09     | 67.84  | 68.46    | 1017    |
| micro     | soft          | 76.50     | 68.07  | 72.04    | 1017    |
| macro     | soft          | 69.17     | 67.92  | 68.54    | 1017    |

- Predicted records: 1013 , files: 142 , input: resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.gpt4.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.80     | 68.07  | 72.17    | 1013    |
| macro     | strict        | 69.94     | 68.46  | 69.19    | 1013    |
| micro     | soft          | 76.90     | 68.15  | 72.26    | 1013    |
| macro     | soft          | 70.02     | 68.54  | 69.27    | 1013    |

### GPT-4 (shuffled)

- Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 75.86     | 65.97  | 70.57    | 994     |
| macro     | strict        | 67.93     | 66.38  | 67.15    | 994     |
| micro     | soft          | 76.16     | 66.23  | 70.85    | 994     |
| macro     | soft          | 68.19     | 66.65  | 67.41    | 994     |

- Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 74.06     | 65.44  | 69.48    | 1010    |
| macro     | strict        | 67.43     | 66.01  | 66.71    | 1010    |
| micro     | soft          | 74.06     | 65.44  | 69.48    | 1010    |
| macro     | soft          | 67.43     | 66.01  | 66.71    | 1010    |

- Predicted records: 1007 , files: 142 , input: resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.gpt4.shuffled.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 75.37     | 66.40  | 70.60    | 1007    |
| macro     | strict        | 68.39     | 67.13  | 67.76    | 1007    |
| micro     | soft          | 75.57     | 66.58  | 70.79    | 1007    |
| macro     | soft          | 68.51     | 67.24  | 67.87    | 1007    |

### GPT-4-Turbo (not-shuffled)

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt4-turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 79.80     | 69.12  | 74.07    | 990     |
| macro     | strict        | 72.27     | 69.82  | 71.02    | 990     |
| micro     | soft          | 80.61     | 69.82  | 74.82    | 990     |
| macro     | soft          | 72.96     | 70.50  | 71.71    | 990     |

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt4-turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.22     | 69.20  | 74.31    | 986     |
| macro     | strict        | 72.78     | 70.24  | 71.49    | 986     |
| micro     | soft          | 81.03     | 69.90  | 75.06    | 986     |
| macro     | soft          | 73.44     | 70.90  | 72.15    | 986     |

- Predicted records: 989 , files: 142 , input: resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.gpt4-turbo.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 78.87     | 68.24  | 73.17    | 989     |
| macro     | strict        | 72.22     | 69.74  | 70.96    | 989     |
| micro     | soft          | 79.88     | 69.12  | 74.11    | 989     |
| macro     | soft          | 73.22     | 70.74  | 71.96    | 989     |

### GPT-4-Turbo (shuffled)

- Predicted: [supermat-paragraphs-all.gpt4-turbo.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt4-turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.04     | 67.37  | 73.16    | 962     |
| macro     | strict        | 72.51     | 69.62  | 71.03    | 962     |
| micro     | soft          | 80.98     | 68.15  | 74.01    | 962     |
| macro     | soft          | 73.28     | 70.38  | 71.80    | 962     |

- Predicted: [supermat-paragraphs-all.gpt4-turbo.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt4-turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.71     | 67.72  | 73.64    | 959     |
| macro     | strict        | 73.02     | 69.84  | 71.39    | 959     |
| micro     | soft          | 81.44     | 68.33  | 74.31    | 959     |
| macro     | soft          | 73.87     | 70.68  | 72.24    | 959     |

- Predicted records: 960 , files: 142 , input: resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.gpt4-turbo.shuffled.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 79.27     | 66.58  | 72.37    | 960     |
| macro     | strict        | 72.22     | 69.02  | 70.59    | 960     |
| micro     | soft          | 80.21     | 67.37  | 73.23    | 960     |
| macro     | soft          | 73.04     | 69.84  | 71.40    | 960     |

## Few-shot prompting

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
| micro     | strict        | 67.97     | 50.31  | 57.82    | 846     |
| macro     | strict        | 47.83     | 46.89  | 47.35    | 846     |
| micro     | soft          | 69.27     | 51.27  | 58.92    | 846     |
| macro     | soft          | 48.86     | 47.92  | 48.38    | 846     |

- Predicted: [supermat-paragraphs-all.chatgpt.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun2%2Fsupermat-paragraphs-all.chatgpt.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 68.20     | 50.48  | 58.02    | 846     |
| macro     | strict        | 47.75     | 46.94  | 47.34    | 846     |
| micro     | soft          | 69.50     | 51.44  | 59.13    | 846     |
| macro     | soft          | 48.76     | 47.95  | 48.35    | 846     |

- Predicted: [supermat-paragraphs-all.chatgpt.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-few_shot%2Frun3%2Fsupermat-paragraphs-all.chatgpt.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 69.23     | 50.39  | 58.33    | 832     |
| macro     | strict        | 47.72     | 46.93  | 47.32    | 832     |
| micro     | soft          | 70.19     | 51.09  | 59.14    | 832     |
| macro     | soft          | 48.48     | 47.69  | 48.08    | 832     |

### GPT-3.5-turbo (shuffled)

- Predicted: [supermat-paragraphs-all.chatgpt.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun1%2Fsupermat-paragraphs-all.chatgpt.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 63.97     | 47.68  | 54.64    | 852     |
| macro     | strict        | 47.17     | 45.95  | 46.55    | 852     |
| micro     | soft          | 66.08     | 49.26  | 56.44    | 852     |
| macro     | soft          | 48.60     | 47.37  | 47.98    | 852     |

- Predicted: [supermat-paragraphs-all.chatgpt.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun2%2Fsupermat-paragraphs-all.chatgpt.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 66.02     | 47.59  | 55.31    | 824     |
| macro     | strict        | 46.70     | 45.74  | 46.22    | 824     |
| micro     | soft          | 67.23     | 48.47  | 56.33    | 824     |
| macro     | soft          | 47.59     | 46.65  | 47.11    | 824     |

- Predicted: [supermat-paragraphs-all.chatgpt.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-few_shot%2Frun3%2Fsupermat-paragraphs-all.chatgpt.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 62.24     | 45.14  | 52.33    | 829     |
| macro     | strict        | 46.22     | 45.27  | 45.74    | 829     |
| micro     | soft          | 63.93     | 46.37  | 53.75    | 829     |
| macro     | soft          | 47.44     | 46.49  | 46.96    | 829     |

### GPT-4 (not shuffled)

- Predicted: [supermat-paragraphs-all.gpt4.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun1%2Fsupermat-paragraphs-all.gpt4.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.57     | 71.83  | 75.95    | 1019    |
| macro     | strict        | 75.75     | 73.94  | 74.84    | 1019    |
| micro     | soft          | 80.57     | 71.83  | 75.95    | 1019    |
| macro     | soft          | 75.75     | 73.94  | 74.84    | 1019    |

- Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun2%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 81.29     | 72.62  | 76.71    | 1021    |
| macro     | strict        | 76.26     | 74.39  | 75.31    | 1021    |
| micro     | soft          | 81.39     | 72.70  | 76.80    | 1021    |
| macro     | soft          | 76.31     | 74.44  | 75.37    | 1021    |

- Predicted: [supermat-paragraphs-all.gpt4.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-few_shot%2Frun3%2Fsupermat-paragraphs-all.gpt4.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.90     | 72.27  | 76.34    | 1021    |
| macro     | strict        | 76.27     | 74.26  | 75.25    | 1021    |
| micro     | soft          | 80.90     | 72.27  | 76.34    | 1021    |
| macro     | soft          | 76.27     | 74.26  | 75.25    | 1021    |

### GPT-4 (shuffled)

- Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun1%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 79.41     | 70.17  | 74.50    | 1010    |
| macro     | strict        | 75.60     | 73.49  | 74.53    | 1010    |
| micro     | soft          | 79.50     | 70.25  | 74.59    | 1010    |
| macro     | soft          | 75.66     | 73.54  | 74.59    | 1010    |

- Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun2%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 79.72     | 70.87  | 75.03    | 1016    |
| macro     | strict        | 75.11     | 73.51  | 74.30    | 1016    |
| micro     | soft          | 80.02     | 71.13  | 75.31    | 1016    |
| macro     | soft          | 75.27     | 73.67  | 74.46    | 1016    |

- Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-few_shot%2Frun3%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.14     | 70.60  | 75.07    | 1007    |
| macro     | strict        | 75.02     | 73.10  | 74.05    | 1007    |
| micro     | soft          | 80.14     | 70.60  | 75.07    | 1007    |
| macro     | soft          | 75.02     | 73.10  | 74.05    | 1007    |

### GPT-4-Turbo (not-shuffled)

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun1%2Fsupermat-paragraphs-all.gpt4-turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 83.44     | 70.08  | 76.18    | 960     |
| macro     | strict        | 75.56     | 72.94  | 74.23    | 960     |
| micro     | soft          | 84.69     | 71.13  | 77.32    | 960     |
| macro     | soft          | 76.72     | 74.10  | 75.39    | 960     |

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun2%2Fsupermat-paragraphs-all.gpt4-turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 84.10     | 70.34  | 76.61    | 956     |
| macro     | strict        | 76.18     | 73.05  | 74.58    | 956     |
| micro     | soft          | 85.46     | 71.48  | 77.85    | 956     |
| macro     | soft          | 77.50     | 74.37  | 75.90    | 956     |

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-few_shot%2Frun3%2Fsupermat-paragraphs-all.gpt4-turbo.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 84.01     | 70.34  | 76.57    | 957     |
| macro     | strict        | 75.88     | 73.16  | 74.50    | 957     |
| micro     | soft          | 85.37     | 71.48  | 77.81    | 957     |
| macro     | soft          | 76.99     | 74.27  | 75.61    | 957     |

### GPT-4-Turbo (shuffled)

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun1%2Fsupermat-paragraphs-all.gpt4-turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 82.01     | 67.02  | 73.76    | 934     |
| macro     | strict        | 74.90     | 71.65  | 73.24    | 934     |
| micro     | soft          | 83.51     | 68.24  | 75.11    | 934     |
| macro     | soft          | 76.04     | 72.79  | 74.38    | 934     |

- Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt2%2Frun2%2Fsupermat-paragraphs-all.gpt4-turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 84.11     | 69.47  | 76.09    | 944     |
| macro     | strict        | 76.37     | 72.96  | 74.63    | 944     |
| micro     | soft          | 85.49     | 70.60  | 77.34    | 944     |
| macro     | soft          | 77.61     | 74.17  | 75.85    | 944     |

- Predicted: [supermat-paragraphs-all.gpt4-turbo.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-few_shot%2Frun3%2Fsupermat-paragraphs-all.gpt4-turbo.shuffled.output.csv)
- Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 82.31     | 67.98  | 74.46    | 944     |
| macro     | strict        | 75.10     | 71.92  | 73.47    | 944     |
| micro     | soft          | 84.32     | 69.64  | 76.28    | 944     |
| macro     | soft          | 76.79     | 73.57  | 75.15    | 944     |

## GPT-3.5-Turbo Fine-tuned

### GPT-3.5-Turbo fine-tuned (FT.base) (not-shuffled)

We shuffled and keep the same number of training examples for the fine-tuning

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 91.06     | 80.00  | 85.17    | 123     |
| macro     | strict        | 80.59     | 79.49  | 80.03    | 123     |
| micro     | soft          | 93.50     | 82.14  | 87.45    | 123     |
| macro     | soft          | 82.05     | 80.95  | 81.50    | 123     |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 91.06     | 80.00  | 85.17    | 123     |
| macro     | strict        | 80.59     | 79.49  | 80.03    | 123     |
| micro     | soft          | 93.50     | 82.14  | 87.45    | 123     |
| macro     | soft          | 82.05     | 80.95  | 81.50    | 123     |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 91.06     | 80.00  | 85.17    | 123     |
| macro     | strict        | 80.59     | 79.49  | 80.03    | 123     |
| micro     | soft          | 93.50     | 82.14  | 87.45    | 123     |
| macro     | soft          | 82.05     | 80.95  | 81.50    | 123     |

### GPT-3.5-Turbo fine-tuned (FT.base) (shuffled)

We shuffled and keep the same number of training examples for the fine-tuning

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 92.68     | 81.43  | 86.69    | 123     |
| macro     | strict        | 81.68     | 80.59  | 81.13    | 123     |
| micro     | soft          | 95.12     | 83.57  | 88.97    | 123     |
| macro     | soft          | 83.15     | 82.05  | 82.60    | 123     |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 91.80     | 80.00  | 85.50    | 122     |
| macro     | strict        | 81.32     | 80.22  | 80.77    | 122     |
| micro     | soft          | 94.26     | 82.14  | 87.79    | 122     |
| macro     | soft          | 82.78     | 81.68  | 82.23    | 122     |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 91.06     | 80.00  | 85.17    | 123     |
| macro     | strict        | 81.32     | 80.22  | 80.77    | 123     |
| micro     | soft          | 93.50     | 82.14  | 87.45    | 123     |
| macro     | soft          | 82.78     | 81.68  | 82.23    | 123     |

### GPT-3.5-turbo Fine-tuned (FT.document) (not shuffled)

- Predicted records: 127 , files: 25 , input: resources/dataset/superMat/relations/results_prompt1/run1/supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 88.98     | 80.71  | 84.64    | 127     |
| macro     | strict        | 79.49     | 78.39  | 78.93    | 127     |
| micro     | soft          | 91.34     | 82.86  | 86.89    | 127     |
| macro     | soft          | 80.95     | 79.85  | 80.40    | 127     |

- Predicted records: 127 , files: 25 , input: resources/dataset/superMat/relations/results_prompt1/run2/supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 88.98     | 80.71  | 84.64    | 127     |
| macro     | strict        | 79.49     | 78.39  | 78.93    | 127     |
| micro     | soft          | 91.34     | 82.86  | 86.89    | 127     |
| macro     | soft          | 80.95     | 79.85  | 80.40    | 127     |

- Predicted records: 127 , files: 25 , input: resources/dataset/superMat/relations/results_prompt1/run3/supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 88.98     | 80.71  | 84.64    | 127     |
| macro     | strict        | 79.49     | 78.39  | 78.93    | 127     |
| micro     | soft          | 91.34     | 82.86  | 86.89    | 127     |
| macro     | soft          | 80.95     | 79.85  | 80.40    | 127     |

### GPT-3.5-turbo Fine-tuned (FT.document) (shuffled)

- Predicted:[supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.1.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-fine-tuning%2Fsupermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.1.output.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 47.73     | 45.00  | 46.32    | 132     |
| macro     | strict        | 50.37     | 55.13  | 52.64    | 132     |
| micro     | soft          | 48.48     | 45.71  | 47.06    | 132     |
| macro     | soft          | 50.73     | 55.49  | 53.01    | 132     |

- Predicted: [supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.2.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-fine-tuning%2Fsupermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.2.output.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 55.73     | 52.14  | 53.87    | 131     |
| macro     | strict        | 53.77     | 58.72  | 56.14    | 131     |
| micro     | soft          | 55.73     | 52.14  | 53.87    | 131     |
| macro     | soft          | 53.77     | 58.72  | 56.14    | 131     |

- Predicted: [supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.3.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-fine-tuning%2Fsupermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.3.output.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 57.72     | 50.71  | 53.99    | 123     |
| macro     | strict        | 54.10     | 58.96  | 56.43    | 123     |
| micro     | soft          | 57.72     | 50.71  | 53.99    | 123     |
| macro     | soft          | 54.10     | 58.96  | 56.43    | 123     |

### GPT-3.5-Turbo fine-tuned (FT.augmented) augmented (not-shuffled)

We shuffled + augment the number of training examples for the fine-tuning

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 89.60     | 80.00  | 84.53    | 125     |
| macro     | strict        | 78.32     | 77.93  | 78.13    | 125     |
| micro     | soft          | 92.00     | 82.14  | 86.79    | 125     |
| macro     | soft          | 79.79     | 79.40  | 79.59    | 125     |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 89.60     | 80.00  | 84.53    | 125     |
| macro     | strict        | 78.32     | 77.93  | 78.13    | 125     |
| micro     | soft          | 92.00     | 82.14  | 86.79    | 125     |
| macro     | soft          | 79.79     | 79.40  | 79.59    | 125     |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 89.60     | 80.00  | 84.53    | 125     |
| macro     | strict        | 78.32     | 77.93  | 78.13    | 125     |
| micro     | soft          | 92.00     | 82.14  | 86.79    | 125     |
| macro     | soft          | 79.79     | 79.40  | 79.59    | 125     |

### GPT-3.5-Turbo fine-tuned (FT.augmented) (shuffled)

We shuffled + augment the number of training examples for the fine-tuning

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 91.13     | 80.71  | 85.61    | 124     |
| macro     | strict        | 80.04     | 79.12  | 79.58    | 124     |
| micro     | soft          | 91.94     | 81.43  | 86.36    | 124     |
| macro     | soft          | 80.40     | 79.49  | 79.94    | 124     |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 87.90     | 77.86  | 82.58    | 124     |
| macro     | strict        | 77.93     | 77.38  | 77.65    | 124     |
| micro     | soft          | 88.71     | 78.57  | 83.33    | 124     |
| macro     | soft          | 78.30     | 77.75  | 78.02    | 124     |

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 89.52     | 79.29  | 84.09    | 124     |
| macro     | strict        | 78.94     | 78.02  | 78.48    | 124     |
| micro     | soft          | 91.94     | 81.43  | 86.36    | 124     |
| macro     | soft          | 80.40     | 79.49  | 79.94    | 124     |

