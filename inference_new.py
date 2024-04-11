import torch
from diffusers import DiffusionPipeline, UNet2DConditionModel

pipeline_model = 'lykon/absolutereality'
unet_model_id = "weights"

print(f"Loading pipeline... from {pipeline_model}")
pipe = DiffusionPipeline.from_pretrained(pipeline_model, torch_dtype=torch.float16).to("cuda")

print(f"Loading unet model... from {unet_model_id}")
pipe.unet = UNet2DConditionModel.from_pretrained(unet_model_id, torch_dtype=torch.float16, use_safetensors =False).to("cuda")

torch.manual_seed(1)

prompt = "celebritymale in the swimming pool"

image = pipe(prompt, num_inference_steps=50, guidance_scale=15).images[0]

image.save("output1.png")
