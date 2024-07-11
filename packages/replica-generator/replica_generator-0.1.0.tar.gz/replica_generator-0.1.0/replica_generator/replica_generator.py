# replica_generator.py

import torch
from transformers import CLIPTextModel, CLIPTokenizer
from diffusers import StableDiffusionPipeline
from IPython.display import Image, display

class ReplicaGenerator:
    def __init__(self, model_name_1, model_name_2, device="cuda"):
        self.device = device

        # Load the text-to-image embedding model (CLIP)
        self.tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")
        self.text_encoder = CLIPTextModel.from_pretrained("openai/clip-vit-base-patch32")

        # Load the generator models
        self.G1 = StableDiffusionPipeline.from_pretrained(model_name_1).to(self.device)
        self.G2 = StableDiffusionPipeline.from_pretrained(model_name_2).to(self.device)

    def generate_image(self, model, prompt, seed):
        # Encode the prompt
        inputs = self.tokenizer(prompt, return_tensors="pt")
        text_embeddings = self.text_encoder(**inputs).last_hidden_state

        # Generate the image
        generator = torch.Generator(self.device).manual_seed(seed)
        image = model(prompt, num_inference_steps=50, generator=generator).images[0]
        return image

    def generate_and_save_images(self, prompt, seed, path1, path2):
        # Generate the first image with G1
        image1 = self.generate_image(self.G1, prompt, seed)
        image1.save(path1)

        # Generate the replica image with G2
        image2 = self.generate_image(self.G2, prompt, seed)
        image2.save(path2)

    def display_image(self, image_path):
        # Display the image
        display(Image(filename=image_path))
