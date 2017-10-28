# _*_ coding:utf-8 _*_
"""
Data set from
https://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data

"""
import numpy as np
from sklearn.naive_bayes import GaussianNB, BernoulliNB
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score


def sk_demo_1():
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    Y = np.array([1, 1, 1, 2, 2, 2])
    clf = GaussianNB()
    clf.fit(X, Y)
    test_item = np.array([[-0.8, -1]])
    print clf.predict(test_item)
    # [1]
    print clf.get_params()


def load_diabetes_data():
    path = '../dataset/bayes/pima-indians-diabetes.txt'
    df = pd.read_csv(path, header=None)
    print df.head()
    # the below get 9 columns, not 8 why?
    # x = np.array(df.ix[:, 0:8])
    x = np.array(df.ix[:, 0:7])
    print x.shape, x[0]
    y = np.array(df.ix[:, 8])
    print y.shape, y[0]

    return train_test_split(x, y, test_size=0.33, random_state=40)


def sk_nb_diabetes():
    x_train, x_test, y_train, y_test = load_diabetes_data()
    clf = GaussianNB()


def sk_bernoulli_demo():
    x = np.random.randint(2, size=(6, 100))
    y = np.array([1, 2, 3, 4, 4, 5])
    clf = BernoulliNB()
    clf.fit(x, y)
    # print clf.predict(x[2:3])
    print clf.predict(x[2])

if __name__ == '__main__':
    # sk_demo_1()
    # load_diabetes_data()
    sk_bernoulli_demo()
    pass
