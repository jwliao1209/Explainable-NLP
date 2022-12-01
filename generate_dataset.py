import os
import json
import numpy as np
import pandas as pd


def generate_dataset(df, mode):
    data_list = []
    for i in range(len(df)):
        if mode == 'train':
            text = train_df["q"][i] + " [SEP] " + train_df["r"][i] + " [SEP] " + train_df["s"][i]
            summary = train_df["q'"][i] + " [SEP] " + train_df["r'"][i] + train_df["s"][i]
            data_list.append(dict(text=text, summary=summary))
        else:
            text = train_df["q"][i] + " [SEP] " + train_df["r"][i] + " [SEP] " + train_df["s"][i]
            data_list.append(dict(text=text))

    return data_list


def save_json(data_list, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(data_list, open(path, "w"), indent=4)
    return


if __name__ == '__main__':
    train_df = pd.read_csv('dataset/Batch_answers - train_data (no-blank).csv')
    test_df  = pd.read_csv('dataset/Batch_answers - test_data(no_label).csv')

    train_list = generate_dataset(train_df, "train")
    test_list = generate_dataset(test_df, "train")

    save_json(train_list, "dataset/train_dataset.json")
    save_json(train_list, "dataset/test_dataset.json")
