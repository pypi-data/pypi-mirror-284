import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Отключает информационные и предупреждающие сообщения

import tensorflow as tf
import logging
logging.getLogger('tensorflow').setLevel(logging.ERROR)
logging.getLogger('absl').setLevel(logging.ERROR)  # Отключает предупреждения absl

from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os
from .downloader import download_model_and_tokenizer

class SpamClassifier:
    def __init__(self):
        download_model_and_tokenizer()
        
        model_path = os.path.join(os.path.dirname(__file__), 'spam_classifier_model.h5')
        tokenizer_path = os.path.join(os.path.dirname(__file__), 'tokenizer.pickle')
        
        self.model = tf.keras.models.load_model(model_path)
        self.compile_model()  # Вызываем метод компиляции модели
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