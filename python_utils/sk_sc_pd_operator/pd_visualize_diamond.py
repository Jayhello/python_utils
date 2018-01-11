# coding:utf-8

"""
data set from
https://github.com/tidyverse/ggplot2/blob/master/data-raw/diamonds.csv
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def load_data():
    f_path = 'E:/python_code/tc_competition/diamond/diamonds.csv'
    df_data = pd.read_csv(f_path)

    print df_data.columns

    print df_data.describe()

    print df_data['clarity'].value_counts()

    my_tab = pd.crosstab(index=df_data["clarity"],  # Make a crosstab
                     columns="count")      # Name the count column

    # my_tab.plot.bar()
    # plt.show()

    print my_tab.sum()  # # Sum the counts

    print my_tab.shape  # Check number of rows and cols

    print my_tab.iloc[1:7]  # Slice rows 1-6

    print my_tab / my_tab.sum()

    # df_data.boxplot(column="price",        # Column to plot
    #               by="clarity",         # Column to split upon
    #               figsize=(8, 8))        # Figure size

    # plt.show()
    print '=========================='
    # two-way table
    grouped = df_data.groupby(['cut', 'clarity'])
    print grouped.size()

    print '=========================='
    clarity_color_table = pd.crosstab(index=df_data["clarity"],
                                      columns=df_data["color"])

    print clarity_color_table

    clarity_color_table.plot(kind="bar",
                             figsize=(8, 8),
                             stacked=True)
    plt.show()


if __name__ == '__main__':
    load_data()
    pass
