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

- Predicted records: 791 , files: 127 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt35_turbo.zero_shot.output.1.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 79.90     | 55.29  | 65.36    | 791     |
| macro     | strict        | 50.81     | 49.09  | 49.93    | 791     |
| micro     | soft          | 80.15     | 55.47  | 65.56    | 791     |
| macro     | soft          | 50.99     | 49.27  | 50.12    | 791     |

- Predicted records: 775 , files: 127 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt35_turbo.zero_shot.output.2.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.13     | 54.33  | 64.75    | 775     |
| macro     | strict        | 50.44     | 48.81  | 49.61    | 775     |
| micro     | soft          | 80.52     | 54.59  | 65.07    | 775     |
| macro     | soft          | 50.78     | 49.15  | 49.95    | 775     |

- Predicted records: 779 , files: 122 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt35_turbo.zero_shot.output.3.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.74     | 55.03  | 65.45    | 779     |
| macro     | strict        | 50.33     | 48.72  | 49.51    | 779     |
| micro     | soft          | 81.00     | 55.21  | 65.66    | 779     |
| macro     | soft          | 50.51     | 48.90  | 49.69    | 779     |

### GPT-3.5 turbo (shuffled)

- Predicted records: 771 , files: 127 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt35_turbo.zero_shot.shuffled.output.1.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.01     | 51.27  | 61.23    | 771     |
| macro     | strict        | 49.84     | 47.48  | 48.63    | 771     |
| micro     | soft          | 76.91     | 51.88  | 61.96    | 771     |
| macro     | soft          | 50.40     | 47.99  | 49.17    | 771     |

- Predicted records: 765 , files: 126 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt35_turbo.zero_shot.shuffled.output.2.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 75.82     | 50.74  | 60.80    | 765     |
| macro     | strict        | 49.61     | 47.45  | 48.51    | 765     |
| micro     | soft          | 76.34     | 51.09  | 61.22    | 765     |
| macro     | soft          | 50.03     | 47.85  | 48.91    | 765     |

- Predicted records: 789 , files: 128 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt35_turbo.zero_shot.shuffled.output.3.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.55     | 52.84  | 62.53    | 789     |
| macro     | strict        | 50.70     | 48.74  | 49.70    | 789     |
| micro     | soft          | 77.19     | 53.28  | 63.04    | 789     |
| macro     | soft          | 51.22     | 49.25  | 50.21    | 789     |

### GPT-4 (not shuffled)

-

Predicted: [supermat-paragraphs-all.gpt4.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt4.output.csv)
-
Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.87     | 66.58  | 71.35    | 990     |
| macro     | strict        | 68.86     | 67.10  | 67.97    | 990     |
| micro     | soft          | 77.47     | 67.10  | 71.92    | 990     |
| macro     | soft          | 69.65     | 67.89  | 68.76    | 990     |

-

Predicted: [supermat-paragraphs-all.gpt4.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt4.output.csv)
-
Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.40     | 67.98  | 71.94    | 1017    |
| macro     | strict        | 69.09     | 67.84  | 68.46    | 1017    |
| micro     | soft          | 76.50     | 68.07  | 72.04    | 1017    |
| macro     | soft          | 69.17     | 67.92  | 68.54    | 1017    |

- Predicted records: 1013 , files: 142 , input:
  resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.gpt4.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.80     | 68.07  | 72.17    | 1013    |
| macro     | strict        | 69.94     | 68.46  | 69.19    | 1013    |
| micro     | soft          | 76.90     | 68.15  | 72.26    | 1013    |
| macro     | soft          | 70.02     | 68.54  | 69.27    | 1013    |

### GPT-4 (shuffled)

-

Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
-
Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 75.86     | 65.97  | 70.57    | 994     |
| macro     | strict        | 67.93     | 66.38  | 67.15    | 994     |
| micro     | soft          | 76.16     | 66.23  | 70.85    | 994     |
| macro     | soft          | 68.19     | 66.65  | 67.41    | 994     |

-

Predicted: [supermat-paragraphs-all.gpt4.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt4.shuffled.output.csv)
-
Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 74.06     | 65.44  | 69.48    | 1010    |
| macro     | strict        | 67.43     | 66.01  | 66.71    | 1010    |
| micro     | soft          | 74.06     | 65.44  | 69.48    | 1010    |
| macro     | soft          | 67.43     | 66.01  | 66.71    | 1010    |

- Predicted records: 1007 , files: 142 , input:
  resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.gpt4.shuffled.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 75.37     | 66.40  | 70.60    | 1007    |
| macro     | strict        | 68.39     | 67.13  | 67.76    | 1007    |
| micro     | soft          | 75.57     | 66.58  | 70.79    | 1007    |
| macro     | soft          | 68.51     | 67.24  | 67.87    | 1007    |

### GPT-4-Turbo (not-shuffled)

-

Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt4-turbo.output.csv)
-
Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 79.80     | 69.12  | 74.07    | 990     |
| macro     | strict        | 72.27     | 69.82  | 71.02    | 990     |
| micro     | soft          | 80.61     | 69.82  | 74.82    | 990     |
| macro     | soft          | 72.96     | 70.50  | 71.71    | 990     |

-

Predicted: [supermat-paragraphs-all.gpt4-turbo.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt4-turbo.output.csv)
-
Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.22     | 69.20  | 74.31    | 986     |
| macro     | strict        | 72.78     | 70.24  | 71.49    | 986     |
| micro     | soft          | 81.03     | 69.90  | 75.06    | 986     |
| macro     | soft          | 73.44     | 70.90  | 72.15    | 986     |

- Predicted records: 989 , files: 142 , input:
  resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.gpt4-turbo.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 78.87     | 68.24  | 73.17    | 989     |
| macro     | strict        | 72.22     | 69.74  | 70.96    | 989     |
| micro     | soft          | 79.88     | 69.12  | 74.11    | 989     |
| macro     | soft          | 73.22     | 70.74  | 71.96    | 989     |

### GPT-4-Turbo (shuffled)

-

Predicted: [supermat-paragraphs-all.gpt4-turbo.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt1%2Frun1%2Fsupermat-paragraphs-all.gpt4-turbo.shuffled.output.csv)
-
Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.04     | 67.37  | 73.16    | 962     |
| macro     | strict        | 72.51     | 69.62  | 71.03    | 962     |
| micro     | soft          | 80.98     | 68.15  | 74.01    | 962     |
| macro     | soft          | 73.28     | 70.38  | 71.80    | 962     |

-

Predicted: [supermat-paragraphs-all.gpt4-turbo.shuffled.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresult_prompt1%2Frun2%2Fsupermat-paragraphs-all.gpt4-turbo.shuffled.output.csv)
-
Expected: [supermat-paragraphs-all.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fsupermat-paragraphs-all.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 80.71     | 67.72  | 73.64    | 959     |
| macro     | strict        | 73.02     | 69.84  | 71.39    | 959     |
| micro     | soft          | 81.44     | 68.33  | 74.31    | 959     |
| macro     | soft          | 73.87     | 70.68  | 72.24    | 959     |

- Predicted records: 960 , files: 142 , input:
  resources/dataset/superMat/relations/results_prompt1/run3//supermat-paragraphs-all.gpt4-turbo.shuffled.output.csv
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
```
{text}
```

{entities}
 
Use the following examples separated by "--------" to learn the task: 
--------
text 1: The researchers of Mg have discovered that MgB2 and MgB3 are superconducting at 29-31 K at ambient pressure.

entities 1:
 materials: MgB2, Mg, MgB3
 tcs: 29-31 K
 pressure: ambient pressure
 
Result 1: 
 material: MgB2, 
 tc: 29-31K, 
 pressure: ambient pressure:
 
 material: MgB3, 
 tc: 29-31K, 
 pressure: ambient pressure:

--------
Text 2: We are studying the material La 3 A 2 Ge 2 (A = Ir, Rh). The critical temperature T C = 4.7 K discovered for La 3 Ir 2 Ge 2 in this work is by about 1.2 K higher than that found for La 3 Rh 2 Ge 2.

entities 2:
 materials: La 3 A 2 Ge 2 (A = Ir, Rh), La 3 Ir 2 Ge 2, La 3 Rh 2 Ge 2
 tcs: 4.7 K, 1.2 K
 
Result 2: 
 material: La 3 Ir 2 Ge 2
 tc: 4.7 K

--------
Text 3: The experimental discovery of the high-temperature superconducting state in the compressed hydrogen and sulfur systems H2S (TC = 150 K for p = 150 GPa) and H3S (TC = 203 K for p = 150 GPa)

entities 3:
 materials: H2S, H3S
 tcs: 150 K, 203 K
 pressures: 150 GPa, 150 GPa
 
Result 3: 
 material: H2S,
 tc: 4.7 K,
 pressure: 150 GPa
 
 material: H3S,
 tc: 150 K,
 pressure: 150 GPa
--------

Apply strictly the following rules:  
    - if material is not specified, ignore the relation block,
    - if tc is not specified in absolute values, ignore the relation block 
```

### GPT-3.5-turbo (not shuffled)

- Predicted records: 1050 , files: 142 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt35_turbo.few_shot.output.1.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 76.38     | 70.17  | 73.14    | 1050    |
| macro     | strict        | 73.87     | 73.05  | 73.46    | 1050    |
| micro     | soft          | 76.95     | 70.69  | 73.69    | 1050    |
| macro     | soft          | 74.58     | 73.76  | 74.17    | 1050    |

- Predicted records: 1053 , files: 142 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt35_turbo.few_shot.output.2.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 75.78     | 69.82  | 72.68    | 1053    |
| macro     | strict        | 73.60     | 72.84  | 73.22    | 1053    |
| micro     | soft          | 76.35     | 70.34  | 73.22    | 1053    |
| macro     | soft          | 74.32     | 73.55  | 73.93    | 1053    |

- Predicted records: 1051 , files: 142 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt35_turbo.few_shot.output.3.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 75.93     | 69.82  | 72.74    | 1051    |
| macro     | strict        | 73.39     | 72.52  | 72.95    | 1051    |
| micro     | soft          | 76.78     | 70.60  | 73.56    | 1051    |
| macro     | soft          | 74.34     | 73.45  | 73.89    | 1051    |

### GPT-3.5-turbo (shuffled)

- Predicted records: 1046 , files: 142 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt35_turbo.few_shot.shuffled.output.1.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 72.66     | 66.49  | 69.44    | 1046    |
| macro     | strict        | 72.33     | 71.64  | 71.98    | 1046    |
| micro     | soft          | 73.52     | 67.28  | 70.26    | 1046    |
| macro     | soft          | 73.27     | 72.59  | 72.93    | 1046    |

Predicted records: 1026 , files: 142 , input:
resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt35_turbo.few_shot.shuffled.output.2.csv
Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 72.61     | 65.18  | 68.70    | 1026    |
| macro     | strict        | 71.43     | 70.61  | 71.02    | 1026    |
| micro     | soft          | 74.07     | 66.49  | 70.08    | 1026    |
| macro     | soft          | 72.66     | 71.85  | 72.25    | 1026    |

- Predicted records: 1032 , files: 142 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt35_turbo.few_shot.shuffled.output.3.csv
  Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 73.16     | 66.05  | 69.43    | 1032    |
| macro     | strict        | 72.67     | 71.86  | 72.27    | 1032    |
| micro     | soft          | 74.42     | 67.19  | 70.62    | 1032    |
| macro     | soft          | 73.77     | 73.00  | 73.38    | 1032    |

### GPT-4 (not shuffled)

- Predicted records: 1029 , files: 141 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt4.few_shot.output.1.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 82.41     | 74.19  | 78.08    | 1029    |
| macro     | strict        | 79.30     | 77.57  | 78.43    | 1029    |
| micro     | soft          | 82.41     | 74.19  | 78.08    | 1029    |
| macro     | soft          | 79.30     | 77.57  | 78.43    | 1029    |

- Predicted records: 1013 , files: 142 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt4.few_shot.output.2.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 83.32     | 73.84  | 78.29    | 1013    |
| macro     | strict        | 78.96     | 77.22  | 78.08    | 1013    |
| micro     | soft          | 83.51     | 74.02  | 78.48    | 1013    |
| macro     | soft          | 79.04     | 77.33  | 78.17    | 1013    |

- Predicted records: 1012 , files: 142 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt4.few_shot.output.3.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 83.50     | 73.93  | 78.42    | 1012    |
| macro     | strict        | 78.73     | 77.11  | 77.91    | 1012    |
| micro     | soft          | 83.60     | 74.02  | 78.52    | 1012    |
| macro     | soft          | 78.78     | 77.16  | 77.96    | 1012    |

### GPT-4 (shuffled)

- Predicted records: 1026 , files: 142 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt4.few_shot.shuffled.output.1.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 81.19     | 72.88  | 76.81    | 1026    |
| macro     | strict        | 78.97     | 77.00  | 77.97    | 1026    |
| micro     | soft          | 81.29     | 72.97  | 76.90    | 1026    |
| macro     | soft          | 79.02     | 77.06  | 78.03    | 1026    |

- Predicted records: 1014 , files: 142 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt4.few_shot.shuffled.output.2.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 82.15     | 72.88  | 77.24    | 1014    |
| macro     | strict        | 78.78     | 76.97  | 77.87    | 1014    |
| micro     | soft          | 82.15     | 72.88  | 77.24    | 1014    |
| macro     | soft          | 78.78     | 76.97  | 77.87    | 1014    |

- Predicted records: 1027 , files: 142 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt4.few_shot.shuffled.output.3.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 82.77     | 74.37  | 78.34    | 1027    |
| macro     | strict        | 79.28     | 77.80  | 78.53    | 1027    |
| micro     | soft          | 82.86     | 74.45  | 78.43    | 1027    |
| macro     | soft          | 79.31     | 77.82  | 78.56    | 1027    |

### GPT-4-Turbo (not-shuffled)

- Predicted records: 947 , files: 139 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt4-turbo.few_shot.output.1.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 86.48     | 71.65  | 78.37    | 947     |
| macro     | strict        | 77.82     | 74.44  | 76.10    | 947     |
| micro     | soft          | 87.54     | 72.53  | 79.33    | 947     |
| macro     | soft          | 78.67     | 75.31  | 76.96    | 947     |

- Predicted records: 951 , files: 139 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt4-turbo.few_shot.output.2.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 86.01     | 71.57  | 78.13    | 951     |
| macro     | strict        | 76.76     | 73.78  | 75.24    | 951     |
| micro     | soft          | 86.86     | 72.27  | 78.89    | 951     |
| macro     | soft          | 77.36     | 74.41  | 75.86    | 951     |

- Predicted records: 938 , files: 139 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt4-turbo.few_shot.output.3.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 86.67     | 71.13  | 78.14    | 938     |
| macro     | strict        | 76.78     | 73.35  | 75.03    | 938     |
| micro     | soft          | 87.53     | 71.83  | 78.90    | 938     |
| macro     | soft          | 77.41     | 73.98  | 75.66    | 938     |

### GPT-4-Turbo (shuffled)

- Predicted records: 925 , files: 139 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt4-turbo.few_shot.shuffled.output.1.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 86.59     | 70.08  | 77.47    | 925     |
| macro     | strict        | 76.85     | 73.30  | 75.03    | 925     |
| micro     | soft          | 87.46     | 70.78  | 78.24    | 925     |
| macro     | soft          | 77.67     | 74.10  | 75.85    | 925     |

- Predicted records: 920 , files: 138 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt4-turbo.few_shot.shuffled.output.2.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 87.17     | 70.17  | 77.75    | 920     |
| macro     | strict        | 77.24     | 73.86  | 75.51    | 920     |
| micro     | soft          | 87.93     | 70.78  | 78.43    | 920     |
| macro     | soft          | 78.03     | 74.65  | 76.31    | 920     |

- Predicted records: 917 , files: 139 , input:
  resources/dataset/superMat/relations/output/supermat-paragraphs-all.gpt4-turbo.few_shot.shuffled.output.3.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 86.15     | 69.12  | 76.70    | 917     |
| macro     | strict        | 76.25     | 72.85  | 74.51    | 917     |
| micro     | soft          | 87.02     | 69.82  | 77.48    | 917     |
| macro     | soft          | 77.08     | 73.66  | 75.33    | 917     |

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

- Predicted records: 127 , files: 25 , input:
  resources/dataset/superMat/relations/results_prompt1/run1/supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 88.98     | 80.71  | 84.64    | 127     |
| macro     | strict        | 79.49     | 78.39  | 78.93    | 127     |
| micro     | soft          | 91.34     | 82.86  | 86.89    | 127     |
| macro     | soft          | 80.95     | 79.85  | 80.40    | 127     |

- Predicted records: 127 , files: 25 , input:
  resources/dataset/superMat/relations/results_prompt1/run2/supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 88.98     | 80.71  | 84.64    | 127     |
| macro     | strict        | 79.49     | 78.39  | 78.93    | 127     |
| micro     | soft          | 91.34     | 82.86  | 86.89    | 127     |
| macro     | soft          | 80.95     | 79.85  | 80.40    | 127     |

- Predicted records: 127 , files: 25 , input:
  resources/dataset/superMat/relations/results_prompt1/run3/supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.output.csv
- Expected records: 1143 , files: 145 , input: resources/dataset/superMat/relations/supermat-paragraphs-all.csv

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 88.98     | 80.71  | 84.64    | 127     |
| macro     | strict        | 79.49     | 78.39  | 78.93    | 127     |
| micro     | soft          | 91.34     | 82.86  | 86.89    | 127     |
| macro     | soft          | 80.95     | 79.85  | 80.40    | 127     |

### GPT-3.5-turbo Fine-tuned (FT.document) (shuffled)

-

Predicted:[supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.1.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-fine-tuning%2Fsupermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.1.output.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 47.73     | 45.00  | 46.32    | 132     |
| macro     | strict        | 50.37     | 55.13  | 52.64    | 132     |
| micro     | soft          | 48.48     | 45.71  | 47.06    | 132     |
| macro     | soft          | 50.73     | 55.49  | 53.01    | 132     |

-

Predicted: [supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.2.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-fine-tuning%2Fsupermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.2.output.csv)

| Avg. type | Matching type | Precision | Recall | F1-score | Support |
|-----------|---------------|-----------|--------|----------|---------|
| micro     | strict        | 55.73     | 52.14  | 53.87    | 131     |
| macro     | strict        | 53.77     | 58.72  | 56.14    | 131     |
| micro     | soft          | 55.73     | 52.14  | 53.87    | 131     |
| macro     | soft          | 53.77     | 58.72  | 56.14    | 131     |

-

Predicted: [supermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.3.output.csv](..%2F..%2F..%2Fresources%2Fdataset%2FsuperMat%2Frelations%2Fresults-fine-tuning%2Fsupermat-paragraphs-holdout.chatgpt-ft-re-aggregated.shuffled.3.output.csv)

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

