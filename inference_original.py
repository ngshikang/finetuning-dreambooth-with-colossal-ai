import torch
from diffusers import DiffusionPipeline

model_id = "lykon/absolutereality"
print(f"Loading model... from {model_id}")

pipe = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

prompt = "a portrait image of a celebrity male named Tom Cruirse"
image = pipe(prompt, num_inference_steps=50, guidance_scale=15).images[0]

image.save("output_original.png")
