import requests
import json

url="http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

conversation_history = []

def delete_context():
    del conversation_history[:]

def generate_response(prompt):
    # conversation history so that LLM has context for new prompts
    conversation_history.append(prompt)

    full_prompt = "\n".join(conversation_history)

    data = {
        "model": "llama2:7b",
        "stream": False,
        "prompt": full_prompt,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        conversation_history.append(actual_response)
        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None