# coding:utf-8

import pandas as pd
import numpy as np


def split_1():
    df = pd.DataFrame({'lst1': range(5),
                       'lst2': range(5)[::-1]},
                      columns=['lst1', 'lst2'])

    print df
    #    lst1  lst2
    # 0     0     4
    # 1     1     3
    # 2     2     2
    # 3     3     1
    # 4     4     0

    train = df.sample(frac=0.8, random_state=200)
    print train
    #    lst1  lst2
    # 3     3     1
    # 4     4     0
    # 0     0     4
    # 1     1     3

    test = df.drop(train.index)
    print test
    #    lst1  lst2
    # 2     2     2


def split_2():
    from sklearn.model_selection import train_test_split

    df = pd.DataFrame({'lst1': range(5),
                       'lst2': range(5)[::-1]},
                      columns=['lst1', 'lst2'])

    print df
    #    lst1  lst2
    # 0     0     4
    # 1     1     3
    # 2     2     2
    # 3     3     1
    # 4     4     0

    train, test = train_test_split(df, test_size=0.2)

    print train
    #    lst1  lst2
    # 2     2     2
    # 0     0     4
    # 4     4     0
    # 1     1     3

    print test
    #    lst1  lst2
    # 3     3     1

if __name__ == '__main__':
    split_2()
    # split_1()
    pass
