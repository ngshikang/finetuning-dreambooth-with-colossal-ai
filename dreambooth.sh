python train_dreambooth.py \
    --pretrained_model_name_or_path="lykon/absolutereality" \
    --instance_data_dir="hugh" \
    --output_dir="weights" \
    --instance_prompt="a portrait image of a celebrity male named Tom Cruirse" \
    --resolution=512 \
    --train_batch_size=1 \
    --gradient_accumulation_steps=1 \
    --learning_rate=5e-5 \
    --lr_scheduler="cosine" \
    --lr_warmup_steps=0 \
    --num_train_epochs=10 \
    --num_class_images=200 \
