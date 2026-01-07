# professional_story_generator.py
# Generative AI Story Generator

from transformers import pipeline

def generate_story(title, total_lines):
    generator = pipeline("text-generation", model="gpt2")

    words_per_line = 14
    story_lines = []

    seed_text = (
        f"{title} is a story that explores emotions, challenges, "
        f"and meaningful experiences that shape human life. "
    )

    current_text = seed_text

    while len(story_lines) < total_lines:
        result = generator(
            current_text,
            max_length=200,
            temperature=0.85,
            top_p=0.95,
            num_return_sequences=1
        )

        generated_text = result[0]["generated_text"]
        new_words = generated_text.replace(current_text, "").split()

        current_line = []

        for word in new_words:
            current_line.append(word)

            if len(current_line) >= words_per_line:
                story_lines.append(" ".join(current_line))
                current_line = []

            if len(story_lines) >= total_lines:
                break

        current_text = generated_text[-300:]

    return "\n".join(story_lines)


def main():
    print("Professional Story Generator using Generative AI")
    print("=" * 50)

    title = input("Enter the story name (title): ")
    lines_required = int(input("Enter number of lines required: "))

    print("\nGenerating story...\n")

    story = generate_story(title, lines_required)

    print(f"STORY TITLE: {title}\n")
    print(story)


if __name__ == "__main__":
    main()
