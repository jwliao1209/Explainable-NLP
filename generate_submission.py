import os
import argparse
import pandas as pd


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_root', type=str,
                        default="dataset")
    parser.add_argument('--pred_root', type=str,
                        default="prediction")
    parser.add_argument('--submit_root', type=str,
                        default="submission")
    parser.add_argument('--submit_name', type=str,
                        default="submission.csv")
    parser.add_argument('--test_file', type=str,
                        default="Batch_answers - test_data(no_label).csv")
    parser.add_argument('--q_file', type=str,
                        default="t5_small_qr_q_bs4_beam1")
    parser.add_argument('--r_file', type=str,
                        default="t5_small_qr_r_bs4_beam1")
    parser.add_argument('--summary_type', type=str, default="sep")

    return parser.parse_args()


def read_txt(path):
    data_list = []
    f = open(path)
    for line in f.readlines():
        data_list.append(line.strip('\n'))
    
    f.close()

    return data_list

def split_q_and_r(data_list, output="q"):
    out_list = []
    for data in zip(data_list):
        output = data.strip('\n').strip('"DISAGREE"').strip('"AGREE"').split('[SEP]')
        if output == "q":
            out_list.append(output[0])
        else:
            if len(out_list) > 1:
                out_list.append(output[1])
            else:
                out_list.append("")

    return out_list


if __name__ == '__main__':
    args = parse_arguments()
    test_df = pd.read_csv(os.path.join(args.data_root, args.test_file))
    pred_q = read_txt(os.path.join(args.pred_root, args.q_file, "generated_predictions.txt"))
    pred_r = read_txt(os.path.join(args.pred_root, args.r_file, "generated_predictions.txt"))

    if args.summary_type == "all":
        pred_q = split_q_and_r(pred_q, "q")
        pred_r = split_q_and_r(pred_r, "r")

    test_pred_df = pd.DataFrame({"id": test_df["id"], "q": pred_q, "r": pred_r})
    os.makedirs(args.submit_root, exist_ok=True)
    test_pred_df.to_csv(os.path.join(args.submit_root, args.submit_name), index=False)
