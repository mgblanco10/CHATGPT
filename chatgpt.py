# https://github.com/openai/openai-python
# https://platform.openai.com/docs/api-reference

import openai

# https://openai.com/api
openai.api_key = "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"

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


