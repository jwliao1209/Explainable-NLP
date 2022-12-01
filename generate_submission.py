import os
import pandas as pd


def read_txt(path):
    data_list = []
    f = open(path)
    for line in f.readlines():
        data_list.append(line)
    
    f.close()

    return data_list

def split_q_and_r(data_list):
    q_list, r_list = [], []

    for line in data_list:
        output = line.strip('\n').split('[SEP]')
        if len(output) > 1:
            q_list.append(output[0])
            r_list.append(output[1])

        else:
            q_list.append(output[0])
            r_list.append("")

    return q_list, r_list


if __name__ == '__main__':
    file_path = 'prediction_bin9/generated_predictions.txt'
    test_list = read_txt(file_path)
    q_list, r_list = split_q_and_r(test_list)
    ids = pd.read_csv('dataset/Batch_answers - test_data(no_label).csv').id
    df = pd.DataFrame({'id': ids, 'q': q_list, 'r': r_list})
    os.makedirs('submission', exist_ok=True)
    df.to_csv('submission/submission3.csv', index=False)
