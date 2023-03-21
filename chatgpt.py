import openai
import os
os.environ['api_key'] = "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"

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


