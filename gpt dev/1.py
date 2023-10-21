import os
import openai
openai.organization = "Personal"
openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.api_key)

def chat_with_gpt(prompt):
    res = openai.Completion.create(engine = 'davinci')
    return res

conversation = "hello"
resp = chat_with_gpt(conversation)
print(resp)
