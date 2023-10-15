import openai

api_key = "YOUR_API_KEY"


def send_request(message):
    openai.api_key = api_key
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    response = chat_completion.choices[0].message['content']
    assert isinstance(response, object)
    return response
