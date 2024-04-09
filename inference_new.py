import torch
from diffusers import DiffusionPipeline

model_id = "weights"
print(f"Loading model... from {model_id}")

pipe = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

torch.manual_seed(100)

prompt = "Tom Cruirse playing a guitar"

image = pipe(prompt, num_inference_steps=50, guidance_scale=10).images[0]

image.save("output1.png")
