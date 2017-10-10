# _*_ coding:utf-8 _*_

"""
use sklearn to do knn prediction

data set from: https://archive.ics.uci.edu/ml/datasets/Iris
mainly cited from the below blog:
https://kevinzakka.github.io/2016/07/13/k-nearest-neighbor/
"""

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split, cross_val_score
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
    # loading training data
    path = '../dataset/knn/iris_data.txt'
    df = pd.read_csv(path, header=None, names=names)
    # print df.head()
    x = np.array(df.ix[:, 0: 4])
    y = np.array(df['class'])

    print x.shape, y.shape
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=40)
    return train_test_split(x, y, test_size=0.33, random_state=40)


def predict():
    x_train, x_test, y_train, y_test = load_data()
    k = 3
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    pred = knn.predict(x_test)
    print accuracy_score(y_test, pred)


def cross_validation():
    x_train, x_test, y_train, y_test = load_data()
    k_lst = list(range(1, 30))
    lst_scores = []

    for k in k_lst:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, x_train, y_train, cv=10, scoring='accuracy')
        lst_scores.append(scores.mean())

    # changing to misclassification error
    MSE = [1 - x for x in lst_scores]
    optimal_k = k_lst[MSE.index(min(MSE))]
    print "The optimal number of neighbors is %d" % optimal_k
    # plot misclassification error vs k
    # plt.plot(k_lst, MSE)
    # plt.ylabel('Misclassification Error')
    plt.plot(k_lst, lst_scores)
    plt.xlabel('Number of Neighbors K')
    plt.ylabel('correct classification rate')
    plt.show()

if __name__ == '__main__':
    # load_data()
    predict()
    # cross_validation()
    pass
