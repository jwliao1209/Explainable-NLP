export CUDA_VISIBLE_DEVICES=0

python run_summarization.py \
    --do_predict \
    --model_name_or_path old/outputs/checkpoint-14000 \
    --test_file old/test_dataset.json \
    --output_dir prediction_bin9 \
    --predict_with_generate \
    --text_column text \
    --summary_column text \
    --per_device_eval_batch_size 30 \
    --num_beams 9
