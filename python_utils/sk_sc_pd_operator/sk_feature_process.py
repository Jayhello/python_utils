# coding:utf-8

from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import numpy as np


def get_dummy_data():
    x = np.array([[-1, 1, -1, 1, -1, 1],
                  [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
                  [0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
                  ])

    x = x.T
    y = np.array([0, 0, 1, 1, 0, 0])

    return x, y


def sk_feature_ref():
    dataset = datasets.load_iris()

    model_lr = LogisticRegression()

    rfe = RFE(model_lr, 3)
    rfe = rfe.fit(dataset.data, dataset.target)

    print rfe.support_
    print rfe.ranking_
    print sorted(zip(map(lambda x: round(x, 4), rfe.ranking_), dataset.feature_names))


def sk_feature_ref_v2():
    X, Y = get_dummy_data()
    names = ['f1', 'f2', 'f3']

    model_lr = LogisticRegression()

    rfe = RFE(model_lr, 2)
    rfe = rfe.fit(X, Y)

    print rfe.support_
    print rfe.ranking_
    print sorted(zip(map(lambda x: round(x, 4), rfe.ranking_), names))


def test_standard_scaler():
    from sklearn.preprocessing import StandardScaler
    arr = [-2, -1, 0, 1, 2]
    print StandardScaler().fit_transform(arr)
    # [-1.414-0.707 0  0.707 1.414]


def test_min_max_scaler():
    from sklearn.preprocessing import MinMaxScaler
    arr = np.array([0, 1, 2, 3, 4])
    print MinMaxScaler().fit_transform(arr)
    # [ 0.    0.25  0.5   0.75  1.  ]


def test_normalizer():
    from sklearn.preprocessing import Normalizer
    arr = np.array([[3, -1],
                    [-4, 2]])

    print Normalizer().fit_transform(arr)
    # [[ 0.9486833  -0.31622777]
    #  [-0.89442719  0.4472136 ]]


def test_binarizer():
    from sklearn.preprocessing import Binarizer
    arr = np.array([0, 1, 2, 3, 4])
    print Binarizer(threshold=2).fit_transform(arr)
    # [[0 0 0 1 1]]

if __name__ == '__main__':
    # test_binarizer()
    # test_normalizer()
    # test_min_max_scaler()
    # test_standard_scaler()
    # sk_feature_ref_v2()
    sk_feature_ref()
    pass
