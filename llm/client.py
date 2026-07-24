from openai import OpenAI
from config import settings

client = OpenAI(
    base_url=settings.base_url,
    api_key=settings.api_key
)

def chat(messages):

    response = client.chat.completions.create(
        model=settings.model,
        messages=messages,
        temperature=0
    )

    return response.choices[0].message.content

