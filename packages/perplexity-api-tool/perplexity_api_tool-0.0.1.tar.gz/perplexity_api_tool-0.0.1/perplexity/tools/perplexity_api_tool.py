from promptflow import tool
from promptflow.connections import CustomConnection
import requests


@tool
def get_perplexity_result(url, api_key, model, chat_input):
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an artificial intelligence assistant and you need to "
                    "engage in a helpful, detailed, polite conversation with a user."
                    "Even if the question is in another language, make sure to answer in Korean"
                ),
            },
            {
                "role": "user",
                "content": chat_input,
            },
        ],
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}",
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        message_content = result["choices"][0]["message"]["content"]
        return message_content
    else:
        return f"Error: {response.status_code} - {response.text}"
