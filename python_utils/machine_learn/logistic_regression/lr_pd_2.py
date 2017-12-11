# coding:utf-8

"""
Data set from http://www.ats.ucla.edu/stat/data/binary.csv
"""


import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np


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

    train_cols = df.columns[1:]
    lr = sm.Logit(df['admit'], df[train_cols])
    ret = lr.fit()
    print ret.summary()

if __name__ == '__main__':
    get_data()
    pass
