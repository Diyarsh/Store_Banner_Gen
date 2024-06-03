import os
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/openai-gpt"
HUGGING_FACE_API_KEY = "YOUR_HUGGING_FACE_API_KEY"


def generate_banner_text(store_name, store_concept):
    prompt = f"Create a concise and intriguing store banner text using the following inputs: Store Name: {store_name} Store Concept: {
        store_concept}. The banner text should be a single phrase no longer than 50 characters. It must be original and must not include any copyright-infringing elements. The output should be only the phrase, with no preface or additional text."
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    response = requests.post(HUGGING_FACE_API_URL,
                             headers=headers, json={"inputs": prompt})
    response_json = response.json()

    try:
        generated_text = response_json[0]['generated_text'].strip()
        sentences = generated_text.split('. ')
        for sentence in sentences:
            if len(sentence) <= 50:
                return sentence.strip()
        return "Error: Generated text is not within the required length or format."
    except Exception as e:
        return f"Error: Unexpected response format: {response_json}"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    store_name = request.form.get('store_name')
    store_concept = request.form.get('store_concept')
    banner_text = generate_banner_text(store_name, store_concept)
    return render_template('index.html', banner_text=banner_text)


if __name__ == '__main__':
    app.run(debug=True)
