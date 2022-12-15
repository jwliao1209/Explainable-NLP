export CUDA_VISIBLE_DEVICES=0

python run_summarization.py \
    --do_train \
    --model_name_or_path t5-small \
    --train_file dataset/train_dataset_qr_q.json \
    --output_dir checkpoint/t5_base_qr_q_bs4 \
    --per_device_train_batch_size=4 \
    --gradient_accumulation_steps=4 \
    --predict_with_generate \
    --text_column text \
    --summary_column summary \
    --adafactor \
    --learning_rate 1e-3 \
    --warmup_ratio 0.1