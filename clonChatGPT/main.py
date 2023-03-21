from flask import Flask, render_template, request
import openai

# import os
# os.environ['api_key'] = "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"

app = Flask(__name__)
openai.api_key =  "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"
conversations = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.form['question']:
        question = 'Yo: '+ request.form['question']

        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = question,
            temperature = 0.9,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0.6
        )

        answer = 'AI: '+ response.choices[0].text.strip()

        conversations.append(question)
        conversations.append(answer)

        return render_template('index.html', chat = conversations )
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)
