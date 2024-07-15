import os
import re
import logging
import pickle
from huggingface_hub import list_repo_files, hf_hub_download

# Set TensorFlow log level before importing it
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 0 = all messages are logged (default behavior)
                                          # 1 = INFO messages are not printed
                                          # 2 = INFO and WARNING messages are not printed
                                          # 3 = INFO, WARNING, and ERROR messages are not printed

import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Configure TensorFlow logging to suppress further messages
logging.getLogger('tensorflow').setLevel(logging.ERROR)
logging.getLogger('absl').setLevel(logging.ERROR)  # Suppress absl warnings

REPO_ID = 'NeuroSpaceX/spam-classifier-model'
MODEL_FILENAME_TEMPLATE = 'spam_classifier_model{}.h5'
TOKENIZER_FILENAME = 'tokenizer.pickle'
MODEL_DIR = os.path.dirname(__file__)

def get_latest_model_version(repo_id):
    files = list_repo_files(repo_id)
    versions = []
    for file in files:
        match = re.match(r'spam_classifier_model(\d+\.\d+)\.h5', file)
        if match:
            versions.append(match.group(1))
    return max(versions, key=lambda s: list(map(int, s.split('.'))))

def get_current_version():
    for filename in os.listdir(MODEL_DIR):
        match = re.match(r'spam_classifier_model(\d+\.\d+)\.h5', filename)
        if match:
            return match.group(1)
    return None

def download_model_and_tokenizer():
    latest_version = get_latest_model_version(REPO_ID)
    current_version = get_current_version()

    if current_version is None or latest_version != current_version:
        print(f"New version detected: {latest_version}. Downloading model...")
        model_filename = MODEL_FILENAME_TEMPLATE.format(latest_version)
        model_path = os.path.join(MODEL_DIR, model_filename)
        
        # Remove old model file if exists
        if current_version:
            os.remove(os.path.join(MODEL_DIR, MODEL_FILENAME_TEMPLATE.format(current_version)))

        hf_hub_download(repo_id=REPO_ID, filename=model_filename, local_dir=MODEL_DIR)

        # Verify the model was downloaded
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file {model_filename} was not downloaded successfully.")
    
    if not os.path.exists(os.path.join(MODEL_DIR, TOKENIZER_FILENAME)):
        print("Downloading tokenizer...")
        hf_hub_download(repo_id=REPO_ID, filename=TOKENIZER_FILENAME, local_dir=MODEL_DIR)

class SpamClassifier:
    def __init__(self):
        download_model_and_tokenizer()
        
        latest_version = get_latest_model_version(REPO_ID)
        model_filename = MODEL_FILENAME_TEMPLATE.format(latest_version)
        model_path = os.path.join(os.path.dirname(__file__), model_filename)
        tokenizer_path = os.path.join(os.path.dirname(__file__), TOKENIZER_FILENAME)
        
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")

        if not os.path.exists(tokenizer_path):
            raise FileNotFoundError(f"Tokenizer file not found at {tokenizer_path}")
        
        self.model = tf.keras.models.load_model(model_path)
        self.compile_model()
        with open(tokenizer_path, 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        
        self.maxlen = 100
    
    def compile_model(self):
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    def predict_message(self, message):
        seq = self.tokenizer.texts_to_sequences([message])
        pad_seq = pad_sequences(seq, maxlen=self.maxlen)
        prediction = self.model.predict(pad_seq)
        return 'spam' if prediction[0][0] > 0.5 else 'not_spam'

# Example usage
if __name__ == '__main__':
    classifier = SpamClassifier()
    message = "This is a test message"
    result = classifier.predict_message(message)
    print(f"Ваше сообщение определено как: {result}")
