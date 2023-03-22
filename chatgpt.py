import openai
import os
print(os.environ.get('openai_api_key'))
openai.api_key = os.environ['openai_api_key']
# https://openai.com/api

# modelo entrenado que esta asociado a chapgpt
# text-davinci-003
while True:
    prompt = input ("\nIntroduce una pregunta: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003", 
                                          prompt= prompt, 
                                          max_tokens=2048)

    print(completion.choices[0].text)


# ejecutar python3 script_name.py


