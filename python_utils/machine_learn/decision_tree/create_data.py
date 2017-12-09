# coding:utf-8

import numpy as np


def get_loan_data_lh():
    """
    this data is from li hang's book
    the feature is
    age(0->young, 1->middle-aged, 2->old),
    have work(0->have, 1-not have),
    have house(0->have, 1-not have),
    loan level(0->just so so, 1->good, 2->very good)
    """
    x = np.array([
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
        [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 2, 2, 2, 1, 1, 2, 0]
    ])

    x = x.T
    y = np.array([0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0])
    return x, y


def get_data():
    x = [[0, 0, 0, 0, 'N'],
         [0, 0, 0, 1, 'N'],
         [1, 0, 0, 0, 'Y'],
         [2, 1, 0, 0, 'Y'],
         [2, 2, 1, 0, 'Y'],
         [2, 2, 1, 1, 'N'],
         [1, 2, 1, 1, 'Y']]

    y = ['outlook', 'temperature', 'humidity', 'windy']
    return x, y

if __name__ == '__main__':

    pass
