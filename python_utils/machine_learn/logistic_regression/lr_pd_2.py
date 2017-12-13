# coding:utf-8

"""
Data set from http://www.ats.ucla.edu/stat/data/binary.csv
"""


import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, recall_score
from sklearn import tree


def get_data():
    f_path = "../dataset/logistic_regression/UCLA_dataset.csv"
    df = pd.read_csv(f_path)
    print df.head()

    print df.describe()

    print df.std()

    print pd.crosstab(df['admit'], df['rank'], rownames=['admit'])

    # df.hist()
    # pl.show()

    # dummy_ranks = pd.get_dummies(df['rank'], prefix='rank')
    # print dummy_ranks.head()

    # train_cols = df.columns[1:]
    # lr = sm.Logit(df['admit'], df[train_cols])
    # ret = lr.fit()
    # print ret.summary()

    train, test = train_test_split(df, test_size=0.2)
    train_x, train_y = train[train.columns[1:]], train['admit']
    test_x, test_y = test[test.columns[1:]], test['admit']

    lr = LogisticRegression()
    lr.fit(train_x, train_y)

    y_pred = lr.predict(test_x)
    print accuracy_score(test_y, y_pred)

    rf = RandomForestClassifier(n_jobs=4)
    rf.fit(train_x, train_y)
    Y_pred = rf.predict(test_x)
    cnf_matrix = confusion_matrix(test_y, Y_pred)
    print cnf_matrix

    accuracy_percent = accuracy_score(test_y, Y_pred)
    print "accuracy is: %s%s" % (accuracy_percent, '%')
    recall_percent = recall_score(test_y, Y_pred)
    print "recall is: %s%s" % (recall_percent, '%')


def dummy_val_pred():
    f_path = "../dataset/logistic_regression/UCLA_dataset.csv"
    df = pd.read_csv(f_path)
    dummy_ranks = pd.get_dummies(df['rank'], prefix='rank')
    train, test = train_test_split(df, test_size=0.2)
    cols_to_keep = ['gre', 'gpa']

    train_x, train_y = train[cols_to_keep].join(dummy_ranks.ix[:, 'rank_2':]), train['admit']
    test_x, test_y = test[cols_to_keep].join(dummy_ranks.ix[:, 'rank_2':]), test['admit']

    lr = LogisticRegression()
    lr.fit(train_x, train_y)

    y_pred = lr.predict(test_x)
    cnf_matrix = confusion_matrix(test_y, y_pred)
    print cnf_matrix

    accuracy_percent = accuracy_score(test_y, y_pred)
    print "accuracy is: %s%s" % (accuracy_percent, '%')
    recall_percent = recall_score(test_y, y_pred)
    print "recall is: %s%s" % (recall_percent, '%')

    rf = RandomForestClassifier(n_jobs=4)
    rf.fit(train_x, train_y)
    Y_pred = rf.predict(test_x)
    cnf_matrix = confusion_matrix(test_y, Y_pred)
    print cnf_matrix

    accuracy_percent = accuracy_score(test_y, Y_pred)
    print "accuracy is: %s%s" % (accuracy_percent, '%')
    recall_percent = recall_score(test_y, Y_pred)
    print "recall is: %s%s" % (recall_percent, '%')

    dt = tree.DecisionTreeClassifier()
    dt = dt.fit(train_x, train_y)
    Y_pred = dt.predict(test_x)
    cnf_matrix = confusion_matrix(test_y, Y_pred)
    print cnf_matrix

    accuracy_percent = accuracy_score(test_y, Y_pred)
    print "accuracy is: %s%s" % (accuracy_percent, '%')
    recall_percent = recall_score(test_y, Y_pred)
    print "recall is: %s%s" % (recall_percent, '%')

if __name__ == '__main__':
    dummy_val_pred()
    # get_data()
    pass
