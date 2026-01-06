# animal_sound_generator.py
# Text -> Animal Sound using Generative AI (Google Colab compatible)
# Plays sound immediately after generation

from transformers import pipeline
import soundfile as sf
import numpy as np
from IPython.display import Audio, display

def generate_animal_sound():
    # Load text-to-audio generative model
    generator = pipeline(
        "text-to-audio",
        model="facebook/musicgen-small",
        device=0  # uses GPU if available
    )

    # Take user input
    prompt = input("Enter animal sound (e.g., dog barking, cat meowing): ")

    # Generate audio
    output = generator(prompt)

    # Fix audio shape
    audio = np.squeeze(output["audio"])
    sampling_rate = output["sampling_rate"]

    # Save audio
    sf.write("animal_sound.wav", audio, sampling_rate)

    print("Animal sound generated and playing now...")

    # Play sound
    display(Audio("animal_sound.wav", autoplay=True))

if __name__ == "__main__":
    generate_animal_sound()
