"""Run this model in Python

> pip install openai
"""
import os
from openai import OpenAI

model_name = "gpt-4o-mini"


client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": "日本の山を高い順に5つ挙げてください。",
        }
    ],
    model=model_name,
    temperature=1,
    max_tokens=4096,
    top_p=1
)

print(response.choices[0].message.content)
