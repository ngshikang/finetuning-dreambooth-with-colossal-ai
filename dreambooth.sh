HF_DATASETS_OFFLINE=1
TRANSFORMERS_OFFLINE=1
DIFFUSERS_OFFLINE=1

torchrun --nproc_per_node 1 --standalone train_dreambooth_colossalai.py \
  --pretrained_model_name_or_path="lykon/absolutereality"  \
  --instance_data_dir="data" \
  --output_dir="./weights" \
  --instance_prompt="celebritymale" \
  --resolution=512 \
  --plugin="gemini" \
  --train_batch_size=1 \
  --learning_rate=12e-6 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --num_class_images=200 \
  --num_train_epochs=10

python inference.py > inference.txt 2>&1
python inference_new.py > inference_new.txt 2>&1
python inference_original.py > inference_original.txt 2>&1

