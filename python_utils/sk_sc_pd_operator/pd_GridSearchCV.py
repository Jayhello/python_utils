# coding:utf-8

import numpy as np
import pandas as pd
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def test_grid_search_cv():
    iris = datasets.load_iris()
    parameters = {'kernel': ('linear', 'rbf'),
                  'C': [1, 2, 4], 'gamma': [0.125, 0.25, 0.5, 1, 2, 4]}

    svr = svm.SVC()
    clf = GridSearchCV(svr, parameters, n_jobs=-1)
    clf.fit(iris.data, iris.target)
    cv_result = pd.DataFrame.from_dict(clf.cv_results_)
    with open('cv_result.csv', 'w') as f:
        cv_result.to_csv(f)

    print('The parameters of the best model are: ')
    print(clf.best_params_)

    y_pred = clf.predict(iris.data)
    print(classification_report(y_true=iris.target, y_pred=y_pred))


def grid_search_cv_graph():
    iris = datasets.load_digits()
    X = iris.data
    Y = iris.target

    C_lst = [1, 10, 100, 1000]
    gamma_lst = [0.125, 0.25, 0.5, 1, 2, 4]
    gamma_lst = [1e-3, 1e-4]

    parameters = {'C': C_lst, 'gamma': gamma_lst}

    # parameters = {'kernel': ('linear', 'rbf'),
    #               'C': C_lst, 'gamma': gamma_lst}

    clf_ = svm.SVC()
    clf = GridSearchCV(clf_, parameters, cv=2, n_jobs=-1)
    clf.fit(X, Y)

    print clf.best_params_
    print clf.best_score_

    print clf.cv_results_

    # scores = [x[1] for x in clf.grid_scores_]
    scores = clf.cv_results_['mean_test_score']
    print scores
    scores = np.array(scores).reshape(len(C_lst), len(gamma_lst))

    for ind, i in enumerate(C_lst):
        plt.plot(gamma_lst, scores[ind], label='C: ' + str(i))

    plt.legend()
    plt.xlabel('Gamma')
    plt.ylabel('Mean score')
    plt.show()

if __name__ == '__main__':
    # test_grid_search_cv()
    grid_search_cv_graph()
    pass
