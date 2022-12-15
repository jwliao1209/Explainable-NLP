# Interpretive_Information_Labeling_for_NLP


## Getting the code
You can download all the files in this repository by cloning this repository:  
```
git clone https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP.git
```


## Setting the environment
To set the environment, you can run this command:
```
pip install -r requirements.txt
```

The requirements.txt include the following package:
```
accelerate >= 0.12.0
datasets >= 1.8.0
sentencepiece != 0.1.92
protobuf
rouge-score
nltk
py7zr
torch >= 1.3
evaluate
```


## Dataset and Checkpoint
You can download the dataset and checkpoint from our Google Drive:
https://drive.google.com/drive/folders/1aeQFAZWjX1iHJKx1bLSuhTdI46HdPmHa?usp=sharing


## Prepared dataset
To generate the dataset, you can run this command:
```
python generate_dataset.py
```


## Training
To train the model, you can run this command:
```
bash train.sh
```


## Inference
To inference the model, you can run this command:
```
python infer.sh
```


## Generate submission file
To generate the submission, you can run this command:
```
generate_submission.py
```


## Reproducing submission
To reproduce our submission, please do the following steps:
1. [Getting the code](https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP/#Getting-the-code)
2. [Install the package](https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP/blob/main/requirements.txt)
3. [Download the dataset and checkpoint](https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP/#Dataset-and-Checkpoint)
4. [Inference](https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP/#Inference)


## Citation
```
@misc{
    title  = {interpretive_information_labeling_for_nlp},
    author = {Jia-Wei Liao},
    url    = {https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP},
    year   = {2022}
}
```
