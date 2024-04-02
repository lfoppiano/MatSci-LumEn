# MatSci-LumEn: Materials Science Large Language Models Evaluation for text and data mining

Code, data, and results described in the paper "Mining experimental data from scientific literature with Large Language
Models", http://arxiv.org/abs/2401.11052

```
@misc{foppiano2024mining,
      title={Mining experimental data from Materials Science literature with Large Language Models}, 
      author={Luca Foppiano and Guillaume Lambard and Toshiyuki Amagasa and Masashi Ishii},
      year={2024},
      eprint={2401.11052},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Evaluation summary

| Information                        | Task | Dataset  | Link                                            | Evaluation results                          | Evaluation data                                                                                              |
|------------------------------------|------|----------|-------------------------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Material expressions               | NER  | SuperMat | [Github](https://github.com/lfoppiano/SuperMat) | [Results](docs/evaluation/ner/supermat.md), | [predicted](resources/dataset/superMat/entities/results), [expected](resources/dataset/superMat/entities/)   |
| Properties                         | NER  | MeasEval | [Github](https://github.com/lfoppiano/MeasEval) | [Results](docs/evaluation/ner/measeval.md)  | [predicted](resources/dataset/measeval/results), [expected](resources/dataset/measeval)                      |
| Materials -> properties extraction | RE   | SuperMat | [Github](https://github.com/lfoppiano/SuperMat) | [Results](docs/evaluation/re/supermat.md)   | [predicted](resources/dataset/superMat/relations/results), [expected](resources/dataset/superMat/relations/) |

Fine-tuning training data stored

- [NER fine tuning materials](resources/dataset/superMat/entities/ft)
- [NER fine tuning properties](resources/dataset/quantities/ft)
- [RE fine tuning materials-properties](resources/dataset/superMat/relations/ft)

## Getting started

### Set-up environment

```shell
conda create --name lumen python=3.9
conda activate lumen 
```

```shell
pip install -r requirements.txt 
```

### Formula matching

The algorithm requires the [material-parser](https://github.com/lfoppiano/material-parsers) project.

### Scripts

Scripts must be run as python modules, using the parameter `-m` and the package path.

#### Processing

**Formula matching evaluation**

- Script: [formula_matching-eval.py](llm_mat_evaluation%2Fre%2Fformula_matching-eval.py)
    - Description: Evaluate the formula matching, displaying the gain F1 and the new matches as compared with the strict
      matching
    - Usage:
        ```
        usage: formula_matching-eval.py [-h] --predicted PREDICTED --expected EXPECTED [--verbose] [--base-url BASE_URL]
        
        Evaluation of the formula matching, as compared with the strict matching: how many element that are not matching with strict matching, are actually matching with formula?
        
        optional arguments:
        -h, --help            show this help message and exit
        --predicted PREDICTED
        Predicted dataset
        --expected EXPECTED   Expected dataset
        --verbose             Enable tons of prints
        --base-url BASE_URL   Formula matcher base url
        ```

**NER**:

- Script: [process_openai_ner_materials.py](llm_mat_evaluation%2Fner%2Fprocess_openai_ner_materials.py)
    - Description: Implementation NER with LLM on materials
    - Usage:
      ```
        usage: process_openai_ner_materials.py [-h] --input-text INPUT_TEXT
        [--model {chatgpt,chatgpt-ft-re,chatgpt-ft_shuffled-re,chatgpt-ft_shuffled-augmented-re,chatgpt-ft-ner-materials,chatgpt-ft-ner-quantities,gpt4,gpt4-turbo}]
        --output OUTPUT
        
        Data preparation for the materials extraction using OpenAI LLMs
        
        optional arguments:
        -h, --help            show this help message and exit
        --input-text INPUT_TEXT
        Input CSV/TSV file containing text
        --model {chatgpt,chatgpt-ft-re,chatgpt-ft_shuffled-re,chatgpt-ft_shuffled-augmented-re,chatgpt-ft-ner-materials,chatgpt-ft-ner-quantities,gpt4,gpt4-turbo}
        --output OUTPUT       Output CSV file or directory 
      ```
-
Script: [process_openai_few_shot_ner_materials.py](llm_mat_evaluation%2Fner%2Fprocess_openai_few_shot_ner_materials.py)
    - Description: Implementation NER with LLM on materials
    - Usage:
      ```
      usage: process_openai_few_shot_ner_materials.py [-h] --input-text INPUT_TEXT
      [--model {chatgpt,chatgpt-ft-re,chatgpt-ft_shuffled-re,chatgpt-ft_shuffled-augmented-re,chatgpt-ft-ner-materials,chatgpt-ft-ner-quantities,gpt4,gpt4-turbo}]
      [--config CONFIG] --output OUTPUT

      Data preparation for materials extraction using OpenAI LLMs

      optional arguments:
      -h, --help            show this help message and exit
      --input-text INPUT_TEXT
      Input CSV/TSV file containing text
      --model {chatgpt,chatgpt-ft-re,chatgpt-ft_shuffled-re,chatgpt-ft_shuffled-augmented-re,chatgpt-ft-ner-materials,chatgpt-ft-ner-quantities,gpt4,gpt4-turbo}
      --config CONFIG       Configuration file
      --output OUTPUT       Output CSV/TSV file

      ```

- Script: [process_openai_ner_properties.py](llm_mat_evaluation%2Fner%2Fprocess_openai_ner_properties.py)
    - Description:
    - Usage:
        ```
        usage: process_openai_ner_properties.py [-h] --input INPUT --output OUTPUT [--config CONFIG]
                                                [--model {chatgpt,chatgpt-ft-re,chatgpt-ft_shuffled-re,chatgpt-ft_shuffled-augmented-re,chatgpt-ft-ner-materials,chatgpt-ft-ner-quantities,gpt4,gpt4-turbo}]
        
        Data preparation for the properties extraction using OpenAI LLMs
        
        optional arguments:
          -h, --help            show this help message and exit
          --input INPUT         Input CSV/TSV file
          --output OUTPUT       Output file, support both JSON, CSV, or TSV
          --config CONFIG       Configuration file
          --model {chatgpt,chatgpt-ft-re,chatgpt-ft_shuffled-re,chatgpt-ft_shuffled-augmented-re,chatgpt-ft-ner-materials,chatgpt-ft-ner-quantities,gpt4,gpt4-turbo}
        ```

-
Script: [process_openai_few_shot_ner_properties.py](llm_mat_evaluation%2Fner%2Fprocess_openai_few_shot_ner_properties.py)
    - Description:
    - Usage:
      ```
        usage: process_openai_few_shot_ner_properties.py [-h] --input INPUT --output OUTPUT [--config CONFIG]
                                                         [--model {chatgpt,chatgpt-ft-re,chatgpt-ft_shuffled-re,chatgpt-ft_shuffled-augmented-re,chatgpt-ft-ner-materials,chatgpt-ft-ner-quantities,gpt4,gpt4-turbo}]
        
        Data preparation for the properties extraction using OpenAI LLMs
        
        optional arguments:
          -h, --help            show this help message and exit
          --input INPUT         Input CSV/TSV file
          --output OUTPUT       Output file, support both JSON, CSV, or TSV
          --config CONFIG       Configuration file
          --model {chatgpt,chatgpt-ft-re,chatgpt-ft_shuffled-re,chatgpt-ft_shuffled-augmented-re,chatgpt-ft-ner-materials,chatgpt-ft-ner-quantities,gpt4,gpt4-turbo}
      ```

**RE**:

- Script: [process_openai_re_supermat.py](llm_mat_evaluation%2Fre%2Fprocess_openai_re_supermat.py)
    - Description:
    - Usage:
        ```
        usage: process_openai_re_supermat.py [-h] --input INPUT
                                             [--model {chatgpt,chatgpt-ft-re,chatgpt-ft_shuffled-re,chatgpt-ft_shuffled-augmented-re,chatgpt-ft-ner-materials,chatgpt-ft-ner-quantities,gpt4,gpt4-turbo}] --output
                                             OUTPUT [--shuffle]
        
        Extract relations using the SuperMat dataset
        
        optional arguments:
          -h, --help            show this help message and exit
          --input INPUT         Input CSV/TSV file containing text
          --model {chatgpt,chatgpt-ft-re,chatgpt-ft_shuffled-re,chatgpt-ft_shuffled-augmented-re,chatgpt-ft-ner-materials,chatgpt-ft-ner-quantities,gpt4,gpt4-turbo}
          --output OUTPUT       Output CSV file or directory
          --shuffle             Shuffle entities before passing to the LLM
        ```

#### Evaluation

**NER**:

- Script: [eval_formulas.py](llm_mat_evaluation%2Fner%2Feval_formulas.py)
    - Description:
    - Usage:
        ```
        usage: eval_formulas.py [-h] --predicted PREDICTED --expected EXPECTED [--verbose] [--base-url BASE_URL]
        
        Evaluation of extracted entities for materials and properties using the novel formula matching.
        
        optional arguments:
          -h, --help            show this help message and exit
          --predicted PREDICTED
                                Predicted dataset
          --expected EXPECTED   Expected dataset
          --verbose             Enable tons of prints
          --base-url BASE_URL   Formula matcher base url
          ```

- Script: [eval_ner.py](llm_mat_evaluation%2Fner%2Feval_ner.py)
    - Description:
    - Usage:
        ```
        usage: eval_ner.py [-h] --predicted PREDICTED --expected EXPECTED --entity-type {material,property} [--matching-type {all,strict,soft,sbert_cross}] [--threshold THRESHOLD] [--verbose]
        
        Evaluation of extracted entities for materials and properties using the standard approaches.
        
        optional arguments:
          -h, --help            show this help message and exit
          --predicted PREDICTED
                                Predicted dataset
          --expected EXPECTED   Expected dataset
          --entity-type {material,property}
                                Types of entities to evaluate
          --matching-type {all,strict,soft,sbert_cross}
                                Type of matching
          --threshold THRESHOLD
                                Matching threshold
          --verbose             Enable tons of prints
        
        ```

**RE**:

- Script: [eval_re_supermat.py](llm_mat_evaluation%2Fre%2Feval_re_supermat.py)
    - Description: Evaluation script for RE using the SuperMat dataset.
    - Usage:
        ```
        usage: eval_re_supermat.py [-h] --predicted PREDICTED --expected EXPECTED [--matching-type {all,strict,soft}] [--threshold THRESHOLD] [--verbose]
        
        Evaluation extracted data
        
        optional arguments:
        -h, --help            show this help message and exit
        --predicted PREDICTED Input dataset
        --expected EXPECTED   Expected dataset
        --matching-type {all,strict,soft} Type of matching
        --threshold THRESHOLD Matching threshold
        --verbose             Enable tons of prints
        ```
