# _*_ coding:utf-8 _*_

"""
https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html
"""

from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np


def get_data():
    x, y_true = make_blobs(n_samples=300, centers=4,
                           cluster_std=0.60, random_state=0)
    plt.scatter(x[:, 0], x[:, 1], s=50)
    # plt.show()
    return x


def predict():
    x = get_data()
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(x)
    y_kmeans = kmeans.predict(x)
    # print y_kmeans
    plt.scatter(x[:, 0], x[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    print centers
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    plt.show()

if __name__ == '__main__':
    # get_data()
    predict()
    pass
