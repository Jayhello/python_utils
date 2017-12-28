# coding:utf-8

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
sns.set()


def hist_1():
    d = {"label": np.random.choice([0, 1, 2], size=1000),
         "values": np.random.randint(0, 10, size=1000)}

    df = pd.DataFrame(d)

    # df['label'].plot.hist(orientation='horizontal', cumulative=True)
    fig, axes = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True)
    df.hist(column="values", by="label", ax=axes)
    plt.suptitle('Your Title Here', x=0.5, y=1.05, ha='center', fontsize='xx-large')
    fig.text(0.5, 0.04, 'common X', ha='center')
    fig.text(0.04, 0.5, 'common Y', va='center', rotation='vertical')
    plt.show()

if __name__ == '__main__':
    hist_1()
    pass
