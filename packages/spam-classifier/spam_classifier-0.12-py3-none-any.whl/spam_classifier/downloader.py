import os
import requests
import re

VERSION_URL = 'https://huggingface.co/NeuroSpaceX/spam-classifier-model/resolve/main/latest_version.txt'
BASE_MODEL_URL = 'https://huggingface.co/NeuroSpaceX/spam-classifier-model/resolve/main/'
MODEL_NAME_TEMPLATE = 'spam_classifier_model{}.h5'
TOKENIZER_URL = 'https://huggingface.co/NeuroSpaceX/spam-classifier-model/resolve/main/tokenizer.pickle'

MODEL_DIR = os.path.dirname(__file__)
MODEL_PATH_TEMPLATE = os.path.join(MODEL_DIR, MODEL_NAME_TEMPLATE)
TOKENIZER_PATH = os.path.join(MODEL_DIR, 'tokenizer.pickle')

def download_file(url, dest):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(dest, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

def get_latest_version():
    response = requests.get(VERSION_URL)
    response.raise_for_status()
    return response.text.strip()

def get_current_version():
    for filename in os.listdir(MODEL_DIR):
        match = re.match(r'spam_classifier_model(\d+\.\d+)\.h5', filename)
        if match:
            return match.group(1)
    return None

def download_model_and_tokenizer():
    latest_version = get_latest_version()
    current_version = get_current_version()

    if current_version is None or latest_version != current_version:
        print(f"New version detected: {latest_version}. Downloading model...")
        model_url = BASE_MODEL_URL + MODEL_NAME_TEMPLATE.format(latest_version)
        model_path = MODEL_PATH_TEMPLATE.format(latest_version)
        
        # Remove old model file if exists
        if current_version:
            os.remove(MODEL_PATH_TEMPLATE.format(current_version))

        download_file(model_url, model_path)
    
    if not os.path.exists(TOKENIZER_PATH):
        print("Downloading tokenizer...")
        download_file(TOKENIZER_URL, TOKENIZER_PATH)

download_model_and_tokenizer()
