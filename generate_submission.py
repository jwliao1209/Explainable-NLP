import os
import pandas as pd


def read_txt(path):
    data_list = []
    f = open(path)
    for line in f.readlines():
        data_list.append(line.strip('\n'))
    
    f.close()

    return data_list

def split_q_and_r(data_list, test_q, test_r, rs):
    q_list, r_list = [], []

    for line, q, r in zip(data_list, test_q, rs):
        output = line.strip('\n').strip('"DISAGREE"').strip('"AGREE"').split('[SEP]')
        # if len(output) > 1:
        #     q_list.append(output[0])
        #     r_list.append(output[1])
        # else:
        #     q_list.append(output[0])
        #     r_list.append("")
        q_list.append(output[0])
        r_list.append(r)


    return q_list, r_list


if __name__ == '__main__':
    test_data = pd.read_csv('dataset/Batch_answers - test_data(no_label).csv')
    # file_path = 'prediction_t5_base_beam10/generated_predictions.txt'
    # test_list = read_txt(file_path)
    r_list = read_txt('prediction_t5_base_qr_r_bs8_beam1/generated_predictions.txt')
    q_list = read_txt('prediction_t5_base_qr_q_bs8_beam1/generated_predictions.txt')
    # q_list, r_list = split_q_and_r(test_list, test_data["q"], test_data["r"], r_list)
    df = pd.DataFrame({'id': test_data["id"], 'q': q_list, 'r': r_list})
    os.makedirs('submission', exist_ok=True)
    df.to_csv('submission/submission_t5_base_qr_q_r_bs8_beam1_correct.csv', index=False)
