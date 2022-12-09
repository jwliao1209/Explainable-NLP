export CUDA_VISIBLE_DEVICES=1

python run_summarization.py \
    --do_predict \
    --model_name_or_path checkpoint/t5_base_qr_r_bs8 \
    --test_file dataset/test_dataset_qr_r.json \
    --output_dir prediction_t5_base_qr_r_bs8_beam1 \
    --predict_with_generate \
    --text_column text \
    --summary_column text \
    --per_device_eval_batch_size 10 \
    --num_beams 1
