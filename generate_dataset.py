import os
import json
import argparse
import pandas as pd


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_root', type=str,
                        default="dataset")
    parser.add_argument('--train_file', type=str,
                        default="Batch_answers - train_data (no-blank).csv")
    parser.add_argument('--test_file', type=str,
                        default="Batch_answers - test_data(no_label).csv")
    parser.add_argument('--text_type', type=str, default="all")
    parser.add_argument('--summary_type', type=str, default="q")

    return parser.parse_args()


def generate_dataset(df, mode, text_type, summary_type):
    data_list = []
    for i in range(len(df)):
        if text_type == 'q':
            text = df["q"][i]
        elif text_type == 'r':
            text = df["r"][i]
        else:
            text = df["q"][i] + " [SEP] " + df["r"][i] + " [SEP] " + df["s"][i]

        if mode == "train":
            if summary_type == "q":
                summary = df["q'"][i]
            elif summary_type == "r":
                summary = df["r'"][i]
            else:
                summary = df["q'"][i] + " [SEP] " + df["r'"][i] + df["s"][i]
            
            data_list.append(dict(text=text, summary=summary))

        else:  # mode == "test"
            data_list.append(dict(text=text))

    return data_list


def save_json(data_list, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(data_list, open(path, "w"), indent=4)
    return


if __name__ == '__main__':
    args = parse_arguments()
    train_df = pd.read_csv(os.path.join(args.data_root, args.train_file))
    test_df  = pd.read_csv(os.path.join(args.data_root, args.test_file))

    train_list = generate_dataset(train_df, "train", args.text_type, args.summary_type)
    test_list  = generate_dataset(test_df, "test", args.text_type, args.summary_type)

    save_json(train_list, os.path.join(args.data_root, f"train_dataset_{args.text_type}_{args.summary_type}.json"))
    save_json(test_list,  os.path.join(args.data_root, f"test_dataset_{args.text_type}_{args.summary_type}.json"))
