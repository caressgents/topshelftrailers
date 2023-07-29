from chatbot import generate_response

# Now you can call generate_response from your main script.
# Let's test it with a sample message.
messages = [
    {'role': 'user', 'content': 'Hi, where is your business located?'}
]
response = generate_response(messages)
print(response)
