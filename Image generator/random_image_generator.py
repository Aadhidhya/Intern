# random_image_generator.py
# Text -> Image Generator using Stable Diffusion
# Google Colab / GPU compatible

from diffusers import StableDiffusionPipeline
import torch

def generate_image():
    # Load Stable Diffusion model
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16
    )

    # Use GPU
    pipe = pipe.to("cuda")

    # Take text input
    prompt = input("Enter text to generate image: ")

    # Generate image
    image = pipe(
        prompt,
        num_inference_steps=20,
        guidance_scale=7.5
    ).images[0]

    # Save image
    image.save("output.png")

    print("Image generated successfully!")
    print("Saved as output.png")

    # Display image (works in Colab)
    image.show()

if __name__ == "__main__":
    generate_image()
