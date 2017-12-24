# coding: utf-8

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set() # use Seaborn styles


def titanic_1():
    titanic = sns.load_dataset('titanic')
    print titanic.head()
    #    survived  pclass     sex   age  ......
    #           0       0    male    22
    # 1         1       1  female  38.0
    # 2         1       3  female  26.0
    # 3         1       1  female  35.0
    # 4         0       3    male  35.0

    print titanic.groupby('sex')[['survived']].mean()
    #         survived
    # sex
    # female  0.742038
    # male    0.188908

    print titanic.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack()
    # class      First    Second     Third
    # sex
    # female  0.968085  0.921053  0.500000
    # male    0.368852  0.157407  0.135447

    print titanic.pivot_table('survived', index='sex', columns='class')
    # class      First    Second     Third
    # sex
    # female  0.968085  0.921053  0.500000
    # male    0.368852  0.157407  0.135447

    age = pd.cut(titanic['age'], [0, 18, 80])
    print titanic.pivot_table('survived', ['sex', age], 'class')
    # class               First    Second     Third
    # sex    age
    # female (0, 18]   0.909091  1.000000  0.511628
    #        (18, 80]  0.972973  0.900000  0.423729
    # male   (0, 18]   0.800000  0.600000  0.215686
    #        (18, 80]  0.375000  0.071429  0.133663

    print titanic.pivot_table(index='sex', columns='class',
                              aggfunc={'survived': sum, 'fare': 'mean'})

    print titanic.pivot_table('survived', index='sex', columns='class', margins=True)
    # class      First    Second     Third       All
    # sex
    # female  0.968085  0.921053  0.500000  0.742038
    # male    0.368852  0.157407  0.135447  0.188908
    # All     0.629630  0.472826  0.242363  0.383838


def births_demo():
    path = 'E:/python_code/births.csv'
    births = pd.read_csv(path)
    print births.head()
    #     year  month day gender  births
    # 0  1969      1   1      F    4046
    # 1  1969      1   1      M    4440
    # 2  1969      1   2      F    4454
    # 3  1969      1   2      M    4548
    # 4  1969      1   3      F    4548

    births['decade'] = 10 * (births['year'] // 10)
    print births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')
    # gender         F         M
    # decade
    # 1960     1753634   1846572
    # 1970    16263075  17121550
    # 1980    18310351  19243452
    # 1990    19479454  20420553
    # 2000    18229309  19106428

    births.pivot_table('births', index='year', columns='gender', aggfunc='sum').plot()

    plt.ylabel('total births per year')
    plt.show()

    # create a datetime index from the year, month, day
    births.index = pd.to_datetime(10000 * births.year +
                                  100 * births.month +
                                  births.day, format='%Y%m%d')

    births['dayofweek'] = births.index.dayofweek
    births.pivot_table('births', index='dayofweek',
                       columns='decade', aggfunc='mean').plot()

    plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])

    plt.ylabel('mean births by day')
    plt.show()

if __name__ == '__main__':
    births_demo()
    # titanic_1()
    pass
