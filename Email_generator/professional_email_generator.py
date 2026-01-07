# chatgpt_professional_email_generator.py
# Professional Email Generator using ChatGPT API

import os
from openai import OpenAI

def generate_professional_email(recipient, purpose):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert assistant who writes highly professional, "
                    "formal office emails suitable for corporate and academic environments."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Write a formal and professional email.\n"
                    f"Recipient: {recipient}\n"
                    f"Purpose: {purpose}\n\n"
                    f"Include a subject line, greeting, professional body, and polite closing."
                )
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


def main():
    print("Professional Email Generator (ChatGPT API)")
    print("=" * 50)

    recipient = input("Enter recipient (HR / Manager / Professor): ")
    purpose = input("Enter purpose of the email: ")

    print("\nGenerating professional email...\n")

    email = generate_professional_email(recipient, purpose)
    print(email)


if __name__ == "__main__":
    main()
