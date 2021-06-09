from typing import List

import uvicorn
from fastapi import FastAPI
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = FastAPI()

vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type = 'post'
padding_type = 'post'
oov_tok = "<OOV>"

model = tf.keras.models.load_model('model.h5')

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
def input_to_model(sentence: list):
    sequences = tokenizer.texts_to_sequences(sentence)
    padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

    result = model.predict(padded)

    return {'data': result}


@app.get('/')
def get_root():
    return {'message': 'Welcome to the ML API'}
    Sentiment Analysis API
    :param data:
    :return:
    """
    result = input_to_model(data)

    return result


