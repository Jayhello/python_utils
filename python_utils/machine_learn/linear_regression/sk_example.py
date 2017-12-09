# coding:utf-8

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
sns.set()


def get_data():
    rng = np.random.RandomState(1)
    x = 10 * rng.rand(50)
    y = 2 * x - 5 + rng.randn(50)
    # plt.scatter(x, y)
    # plt.show()
    return x, y


def lr_fit():
    x, y = get_data()
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    xfit = np.linspace(0, 10, 1000)
    yfit = model.predict(xfit[:, np.newaxis])

    print "Model slope: ", model.coef_[0]
    print "Model intercept:", model.intercept_

    plt.scatter(x, y)
    plt.plot(xfit, yfit)
    plt.show()

if __name__ == '__main__':
    lr_fit()
    # get_data()
    pass
