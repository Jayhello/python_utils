# coding:utf-8

import numpy
import pandas as pd


def df_merge():
    df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})

    df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                        'hire_date': [2004, 2008, 2012, 2014]})

    print df1
    #     employee        group
    # 0        Bob   Accounting
    # 1       Jake  Engineering
    # 2       Lisa  Engineering
    # 3        Sue           HR

    print df2
    #   employee  hire_date
    # 0     Lisa       2004
    # 1      Bob       2008
    # 2     Jake       2012
    # 3      Sue       2014

    print pd.merge(df1, df2)
    #   employee        group  hire_date
    # 0      Bob   Accounting       2008
    # 1     Jake  Engineering       2012
    # 2     Lisa  Engineering       2004
    # 3      Sue           HR       2014


def df_merge_2():
    df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})

    df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
                                  'Engineering', 'Engineering', 'HR', 'HR'],
                        'skills': ['math', 'spreadsheets', 'coding', 'linux',
                                   'spreadsheets', 'organization']})

    print pd.merge(df1, df5)
    #   employee        group        skills
    # 0      Bob   Accounting          math
    # 1      Bob   Accounting  spreadsheets
    # 2     Jake  Engineering        coding
    # 3     Jake  Engineering         linux
    # 4     Lisa  Engineering        coding
    # 5     Lisa  Engineering         linux
    # 6      Sue           HR  spreadsheets
    # 7      Sue           HR  organization


def df_merge_3():
    df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})

    df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'salary': [70000, 80000, 120000, 90000]})

    print pd.merge(df1, df3, left_on="employee", right_on="name")
    #   employee        group  name  salary
    # 0      Bob   Accounting   Bob   70000
    # 1     Jake  Engineering  Jake   80000
    # 2     Lisa  Engineering  Lisa  120000
    # 3      Sue           HR   Sue   90000

    print pd.merge(df1, df3, left_on="employee", right_on="name").drop('name', axis=1)
    #   employee        group  salary
    # 0      Bob   Accounting   70000
    # 1     Jake  Engineering   80000
    # 2     Lisa  Engineering  120000
    # 3      Sue           HR   90000


def df_merge_4():
    df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                        'food': ['fish', 'beans', 'bread']},
                       columns=['name', 'food'])

    df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                        'drink': ['wine', 'beer']},
                       columns=['name', 'drink'])

    print pd.merge(df6, df7)
    #    name   food drink
    # 0  Mary  bread  wine

    print pd.merge(df6, df7, how='inner')
    # 0  Mary  bread  wine
    #    name   food drink
    print pd.merge(df6, df7, how='outer')
    #      name   food drink
    # 0   Peter   fish   NaN
    # 1    Paul  beans   NaN
    # 2    Mary  bread  wine
    # 3  Joseph    NaN  beer

    print pd.merge(df6, df7, how='left')
    #      name   food drink
    # 0   Peter   fish   NaN
    # 1    Paul  beans   NaN
    # 2    Mary  bread  wine
    # 3  Joseph    NaN  beer


def df_merge_5():
    df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'rank': [1, 2, 3, 4]})

    df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'rank': [3, 1, 4, 2]})

    # Overlapping Column Names: The suffixes Keyword
    print pd.merge(df8, df9, on="name")
    #    name  rank_x  rank_y
    # 0   Bob       1       3
    # 1  Jake       2       1
    # 2  Lisa       3       4
    # 3   Sue       4       2

    print pd.merge(df8, df9, on="name", suffixes=["_L", "_R"])
    #     name  rank_L  rank_R
    # 0   Bob       1       3
    # 1  Jake       2       1
    # 2  Lisa       3       4
    # 3   Sue       4       2

if __name__ == '__main__':
    df_merge_5()
    # df_merge_4()
    # df_merge_2()
    # df_merge()
    pass
