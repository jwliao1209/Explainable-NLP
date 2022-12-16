export CUDA_VISIBLE_DEVICES=0

python generate_dataset.py

wait

python run_summarization.py \
    --do_predict \
    --model_name_or_path checkpoint/t5_small_qr_q_bs4 \
    --test_file dataset/test_dataset_all_q.json \
    --output_dir t5_small_qr_q_bs4_beam1 \
    --predict_with_generate \
    --text_column text \
    --summary_column text \
    --per_device_eval_batch_size 10 \
    --num_beams 1

wait

python run_summarization.py \
    --do_predict \
    --model_name_or_path checkpoint/t5_small_qr_r_bs4 \
    --test_file dataset/test_dataset_all_r.json \
    --output_dir t5_small_qr_r_bs4_beam1 \
    --predict_with_generate \
    --text_column text \
    --summary_column text \
    --per_device_eval_batch_size 10 \
    --num_beams 1

wait

python run_summarization.py \
    --do_predict \
    --model_name_or_path checkpoint/t5_base_qr_q_bs4 \
    --test_file dataset/test_dataset_all_q.json \
    --output_dir t5_base_qr_q_bs4_beam1 \
    --predict_with_generate \
    --text_column text \
    --summary_column text \
    --per_device_eval_batch_size 10 \
    --num_beams 1

wait

python run_summarization.py \
    --do_predict \
    --model_name_or_path checkpoint/t5_base_qr_r_bs4 \
    --test_file dataset/test_dataset_all_r.json \
    --output_dir t5_base_qr_r_bs4_beam1 \
    --predict_with_generate \
    --text_column text \
    --summary_column text \
    --per_device_eval_batch_size 10 \
    --num_beams 1

wait

python generate_submission.py \
    --q_file t5_small_qr_q_bs4_beam1 \
    --r_file t5_small_qr_r_bs4_beam1 \
    --submit_name t5_small_qr_q_qr_r_bs4_beam1.csv

wait

python generate_submission.py \
    --q_file t5_base_qr_q_bs4_beam1 \
    --r_file t5_base_qr_r_bs4_beam1 \
    --submit_name t5_base_qr_q_qr_r_bs4_beam1.csv

wait

python aggregate_submission.py \
    --df_files t5_small_qr_q_qr_r_bs4_beam1.csv t5_base_qr_q_qr_r_bs4_beam1.csv
