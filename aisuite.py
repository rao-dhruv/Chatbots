import aisuite as ai
client = ai.Client()
message = [
    {"role": "system", "content": "Talk using private English"},
    {"role": "user", "content": "Tell me a joke"},
]

response = client.chat.completions.create(model="llama3", messages=message, temperature=0.75)
print(response.choices[0].message.content)