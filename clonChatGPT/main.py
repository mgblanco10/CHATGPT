from flask import Flask, render_template, request
import openai

import os
os.environ['api_key'] = "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"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)
