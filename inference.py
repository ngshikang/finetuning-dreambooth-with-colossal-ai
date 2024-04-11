import torch
from diffusers import DiffusionPipeline, UNet2DConditionModel

pipeline_model = 'lykon/absolutereality'
unet_model_id = "weights"

print(f"Loading pipeline... from {pipeline_model}")
pipe = DiffusionPipeline.from_pretrained(pipeline_model, torch_dtype=torch.float16).to("cuda")

print(f"Loading unet model... from {unet_model_id}")
pipe.unet = UNet2DConditionModel.from_pretrained(unet_model_id, torch_dtype=torch.float16).to("cuda")

torch.manual_seed(100)

prompt = "a portrait image of celebritymale"
image = pipe(prompt, num_inference_steps=50, guidance_scale=10).images[0]

image.save("output.png")
