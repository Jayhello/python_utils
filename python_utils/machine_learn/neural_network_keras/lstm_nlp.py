# _*_ coding:utf-8 _*_

"""
This file is about using lstm to do nlp problem,
classify sentiment of movie review
"""
import numpy as np
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence


def generate_data():
    # load the dataset but only keep the top n words, zero the rest
    top_words = 5000
    (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)
    # truncate and pad input sequences
    max_review_length = 500
    X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
    X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)


if __name__ == '__main__':
    generate_data()
    pass
