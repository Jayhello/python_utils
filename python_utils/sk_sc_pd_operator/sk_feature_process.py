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
    # load the iris datasets
    dataset = datasets.load_iris()
    # create a base classifier used to evaluate a subset of attributes
    model_lr = LogisticRegression()
    # create the RFE model and select 3 attributes
    rfe = RFE(model_lr, 3)
    rfe = rfe.fit(dataset.data, dataset.target)
    # summarize the selection of the attributes
    print rfe.support_
    # [False  True  True  True]
    print rfe.ranking_
    # [2 1 1 1]
    print sorted(zip(map(lambda x: round(x, 4), rfe.ranking_), dataset.feature_names))
    # [(1.0, 'petal length (cm)'), (1.0, 'petal width (cm)'), (1.0, 'sepal width (cm)'), (2.0, 'sepal length (cm)')]


def feature_importance():
    from sklearn.ensemble import ExtraTreesClassifier

    dataset = datasets.load_iris()
    model = ExtraTreesClassifier()
    model.fit(dataset.data, dataset.target)
    print zip(dataset.feature_names, map(lambda x: round(x, 2), model.feature_importances_))
    # [('sepal length (cm)', 0.13), ('sepal width (cm)', 0.07), ('petal length (cm)', 0.35), ('petal width (cm)', 0.45)]


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


def test_pearsonr():
    from scipy.stats import pearsonr
    arr1 = np.arange(0, 12)
    arr2 = np.arange(5, 17)
    print pearsonr(arr1, arr2)

    x = np.arange(-1, 1, 30)
    y = x
    print pearsonr(x, y)


def rfr_feature_select():
    from sklearn.datasets import load_boston
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.cross_validation import cross_val_score, ShuffleSplit

    boston = load_boston()
    X = boston["data"]
    Y = boston["target"]
    names = boston["feature_names"]

    rf = RandomForestRegressor(n_estimators=20, max_depth=4)
    scores = []
    for i in range(X.shape[1]):
        score = cross_val_score(rf, X[:, i:i + 1],
                                Y, scoring="r2", cv=ShuffleSplit(len(X), 3, .3))
        scores.append((round(np.mean(score), 3), names[i]))

    print sorted(scores, reverse=True)


if __name__ == '__main__':
    feature_importance()
    # rfr_feature_select()
    # test_pearsonr()
    # test_binarizer()
    # test_normalizer()
    # test_min_max_scaler()
    # test_standard_scaler()
    # sk_feature_ref_v2()
    # sk_feature_ref()
    pass
