import os
from openai import OpenAI
from django.conf import settings

# Initialize OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def ask_favorite_foods(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",  # or "gpt-4o" if you have access
        messages=[
            {"role": "system", "content": "You are a friendly chatbot that asks about food preferences and reply positively to their answers and donot ask questions back."},
            {"role": "assistant", "content": "What are your three favourite foods?"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
