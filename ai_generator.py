from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_tasks(words, level):

    word_list = ", ".join([w[0] for w in words])

    prompt = f"""
Create ESL tasks.

Level: {level}
Words: {word_list}

1. Writing:
Write 2 simple questions. Student answers using the words.

2. Speaking:
Write 3 discussion questions using the words.

Use simple English. No vague questions.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
