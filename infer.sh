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
