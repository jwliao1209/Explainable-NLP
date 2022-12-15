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
or
```
export CUDA_VISIBLE_DEVICES=0
python run_summarization.py \
    --do_train \
    --model_name_or_path t5-small \
    --train_file dataset/train_dataset_qr_q.json \
    --output_dir checkpoint/t5_base_qr_q_bs4 \
    --per_device_train_batch_size=4 \
    --gradient_accumulation_steps=4 \
    --predict_with_generate \
    --text_column text \
    --summary_column summary \
    --adafactor \
    --learning_rate 1e-3 \
    --warmup_ratio 0.1
```


## Inference
To inference the model, you can run this command:
```
python infer.sh
```

or

```
export CUDA_VISIBLE_DEVICES=0
python run_summarization.py \
    --do_predict \
    --model_name_or_path checkpoint/t5_small_q_bs4 \
    --test_file dataset/test_dataset_qr_q.json \
    --output_dir t5_small_qr_q_bs4_beam1 \
    --predict_with_generate \
    --text_column text \
    --summary_column text \
    --per_device_eval_batch_size 10 \
    --num_beams 1
```


## Generate submission
To generate the submission file, you can run this command:
```
generate_submission.py
```


## Aggregate submissions
To aggregate the submission files, you can run this command:
```
aggregate_submission.py
```


## Reproducing submission
To reproduce our submission, please do the following steps:
1. [Getting the code](https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP/#Getting-the-code)
2. [Setting the environment](https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP/#Setting-the-environment)
3. [Download the dataset and checkpoint](https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP/#Dataset-and-Checkpoint)
4. [Inference](https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP/#Inference)
5. [Generate submission](https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP/#Generate-submission)
6. [Aggregate submissions](https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP/#Aggregate-submissions)


## Operating System
We develop the code on Ubuntu 22.04 operating system and use python 3.9.15 version. All trainings are performed on a server with a single NVIDIA 3090 GPU.


## Acknowledgement
We thank the authors of these repositories:
- Hugging Face: https://github.com/huggingface
- pytorch-seq2seq: https://github.com/bentrevett/pytorch-seq2seq


## Citation
```
@misc{
    title  = {interpretive_information_labeling_for_nlp},
    author = {Jia-Wei Liao},
    url    = {https://github.com/Jia-Wei-Liao/Interpretive_Information_Labeling_for_NLP},
    year   = {2022}
}
```
