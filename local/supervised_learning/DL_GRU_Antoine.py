#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 09:50:00 2018

@author: AntoineP
"""

import pickle

from keras.layers.convolutional import MaxPooling1D
from keras.layers.convolutional import Conv1D
from keras.layers.embeddings import Embedding
from keras.optimizers import RMSprop
from keras.models import Sequential
from keras.layers import Dropout
from keras.layers import Dense
from keras.layers import LSTM
from sklearn import gridsearchCV


# Import data
xtrain, xtest, ytrain, ytest = pickle.load(open('../../../train_test_deep_learning_group7', 'rb'))


def lstm_modelization(num_class, epochs, X_train, X_test, Y_train, Y_test):
    # create the model
    num_words = 10000
    max_review_length = 500
    embedding_vecor_length = 32
    opt = RMSprop(lr=0.001, rho=0.9, epsilon=1e-6)
    model = Sequential()
    model.add(Embedding(num_words, embedding_vecor_length, input_length=max_review_length))
    model.add(Dropout(0.2))
    model.add(LSTM(50))
    model.add(Dropout(0.2))
    model.add(Dense(num_class, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    print(model.summary())
    model.fit(X_train, Y_train, epochs=epochs, batch_size=64)
    # Final evaluation of the model
    scores = model.evaluate(X_test, Y_test, verbose=0)
    print("Accuracy: %.2f%%" % (scores[1]*100))
    return model