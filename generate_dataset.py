import os
import json
import numpy as np
import pandas as pd


def generate_dataset(df, mode):
    data_list = []
    for i in range(len(df)):
        if mode == 'train':
            text = df["q"][i] + " [SEP] " + df["r"][i] + " [SEP] " + df["s"][i]
            # summary = df["q'"][i] + " [SEP] " + df["r'"][i] + df["s"][i]
            # text = df["q"][i]
            summary = df["r'"][i]
            data_list.append(dict(text=text, summary=summary))
        else:
            text = df["q"][i] + " [SEP] " + df["r"][i] + " [SEP] " + df["s"][i]
            # text = df["q"][i]
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
    test_list = generate_dataset(test_df, "test")

    save_json(train_list, "dataset/train_dataset_qr_r.json")
    save_json(test_list, "dataset/test_dataset_qr_r.json")
