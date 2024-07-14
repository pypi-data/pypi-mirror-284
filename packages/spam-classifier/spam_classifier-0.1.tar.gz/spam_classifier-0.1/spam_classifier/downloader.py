import os
import requests

MODEL_URL = 'https://huggingface.co/NeuroSpaceX/spam-classifier-model/resolve/main/spam_classifier_model.h5'
TOKENIZER_URL = 'https://huggingface.co/NeuroSpaceX/spam-classifier-model/resolve/main/tokenizer.pickle'

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'spam_classifier_model.h5')
TOKENIZER_PATH = os.path.join(os.path.dirname(__file__), 'tokenizer.pickle')

def download_file(url, dest):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(dest, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

def download_model_and_tokenizer():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model...")
        download_file(MODEL_URL, MODEL_PATH)
    if not os.path.exists(TOKENIZER_PATH):
        print("Downloading tokenizer...")
        download_file(TOKENIZER_URL, TOKENIZER_PATH)

download_model_and_tokenizer()