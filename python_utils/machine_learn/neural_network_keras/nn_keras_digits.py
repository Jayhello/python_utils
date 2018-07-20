# _*_ coding:utf-8 _*_
"""
This file is mainly use keras to recognize digits,with
Multi-Layer perceptrons or neural network
"""
from keras.datasets import mnist
import gzip
import matplotlib.pyplot as plt
import sys
# from six.moves import cPickle
import cPickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Dropout
from keras.utils import np_utils


def load_data():
    """
    this function is used to load data
    :return:
    """
    file = '../dataset/mnist/mnist.pkl.gz'
    f = gzip.open(file, 'rb')
    if sys.version_info < (3,):
        data = cPickle.load(f)
    else:
        data = cPickle.load(f, encoding='bytes')
    f.close()
    return data


def show_image():
    """
    this function is for a test to show, server image
    :return:
    """
    (X_train, y_train), (X_validation, y_validation), (X_test, y_test) = load_data()
    # (X_train, y_train), (X_test, y_test) = mnist.load_data()
    # plot 4 images as gray scale
    plt.subplot(221)
    plt.imshow(X_train[0], cmap=plt.get_cmap('gray'))
    plt.subplot(222)
    plt.imshow(X_train[1], cmap=plt.get_cmap('gray'))
    plt.subplot(223)
    plt.imshow(X_train[2], cmap=plt.get_cmap('gray'))
    plt.subplot(224)
    plt.imshow(X_train[3], cmap=plt.get_cmap('gray'))
    # show the plot
    plt.show()


def generate_data():
    (X_train, y_train), (X_test, y_test) = load_data()

    # flatten 28*28 images to a 784 vector for each image
    print X_train.shape[1], X_train.shape[2], X_train.shape
    # X_train.shape -> (60000L, 28L, 28L)
    num_pixels = X_train.shape[1] * X_train.shape[2]
    X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32')
    X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32')

    # normalize inputs from 0-255 to 0-1
    X_train = X_train / 255
    X_test = X_test / 255

    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)
    # print y_train.shape, y_test.shape
    # y_train.shape -> (60000L, 10L), y_test.shape -> (10000L, 10L)
    num_classes = y_test.shape[1]

    return X_train, y_train, X_test, y_test


def baseline_model():
    """
    define baseline model
    :return:
    """
    # create model
    model = Sequential()

    num_pixels = 784
    # model.add(Dense(num_pixels, input_dim=num_pixels, init='normal', activation='relu'))
    model.add(Dense(num_pixels, input_dim=num_pixels, activation='relu'))
    num_classes = 10
    # model.add(Dense(num_classes, init='normal', activation='softmax'))
    model.add(Dense(num_classes, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def train_and_evaluate():
    X_train, y_train, X_test, y_test = generate_data()
    model = baseline_model()
    model.fit(X_train, y_train, validation_data=(X_test, y_test), nb_epoch=10, batch_size=200, verbose=2)
    # Final evaluation of the model
    scores = model.evaluate(X_test, y_test, verbose=0)
    print("Baseline Error: %.2f%%" % (100-scores[1]*100))


if __name__ == '__main__':
    # load_data()
    generate_data()
    # train_and_evaluate()
    pass
