import os
import requests

MODEL_URL = 'https://huggingface.co/NeuroSpaceX/spam-classifier-model/resolve/main/spam_classifier_model.h5'
TOKENIZER_URL = 'https://huggingface.co/NeuroSpaceX/spam-classifier-model/resolve/main/tokenizer.pickle'

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'spam_classifier_model.h5')
TOKENIZER_PATH = os.path.join(os.path.dirname(__file__), 'tokenizer.pickle')

MODEL_ETAG_PATH = os.path.join(os.path.dirname(__file__), 'model_etag.txt')
TOKENIZER_ETAG_PATH = os.path.join(os.path.dirname(__file__), 'tokenizer_etag.txt')

def download_file(url, dest):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(dest, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return response.headers.get('ETag')

def get_saved_etag(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return f.read().strip()
    return None

def save_etag(path, etag):
    with open(path, 'w') as f:
        f.write(etag)

def check_and_download(url, dest, etag_path):
    current_etag = get_saved_etag(etag_path)
    headers = {'If-None-Match': current_etag} if current_etag else {}
    
    response = requests.head(url, headers=headers)
    response.raise_for_status()
    
    new_etag = response.headers.get('ETag')
    
    if new_etag != current_etag:
        print(f"New version detected for {os.path.basename(dest)}. Downloading...")
        new_etag = download_file(url, dest)
        save_etag(etag_path, new_etag)
    else:
        print(f"No new version for {os.path.basename(dest)}. Current version is up-to-date.")

def download_model_and_tokenizer():
    check_and_download(MODEL_URL, MODEL_PATH, MODEL_ETAG_PATH)
    check_and_download(TOKENIZER_URL, TOKENIZER_PATH, TOKENIZER_ETAG_PATH)

download_model_and_tokenizer()
