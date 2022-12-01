export CUDA_VISIBLE_DEVICES=5

python run_summarization.py \
    --do_train \
    --model_name_or_path t5-small \
    --train_file dataset/train_dataset.json \
    --output_dir checkpoint \
    --per_device_train_batch_size=4 \
    --gradient_accumulation_steps=4 \
    --per_device_eval_batch_size=4 \
    --eval_accumulation_steps=4 \
    --predict_with_generate \
    --text_column text \
    --summary_column summary \
    --adafactor \
    --learning_rate 1e-3 \
    --warmup_ratio 0.1