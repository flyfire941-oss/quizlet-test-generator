import requests
import os

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xl"
headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def generate_ai_tasks(words, level):
    word_list = ", ".join([w[0] for w in words])

    prompt = f"""
Create ESL exercises for students.

Level: {level} (A1, A2, B1, B2)
Words to use: {word_list}

Instructions:
1. Writing: generate 2 simple questions. Student should answer using the given words. Each answer 3–5 sentences.
2. Speaking: generate 3 discussion questions using the words.
3. Do NOT use Present Participles or vague "this" questions.
4. Keep sentences short and simple.

Output in plain text.
"""

    try:
        output = query({
            "inputs": prompt,
            "parameters": {"max_length": 300}
        })
        return output[0]["generated_text"]

    except:
        # fallback если AI не отвечает
        fallback = f"Use these words:\n\n{word_list}\n\nWrite 5 sentences with these words."
        return fallback
