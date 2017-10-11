# _*_ coding:utf-8 _*_

"""
data set from:
http://archive.ics.uci.edu/ml/datasets/banknote+authentication
http://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt
"""

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.tree import export_graphviz
import subprocess


def visualize_tree(tree, feature_name, dot_file):
    """Create tree png using graphviz.
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    dot_file -- dot file name and path
    """
    with open("tree.dot", 'w') as f:
        export_graphviz(tree, out_file=f,
                        feature_names=feature_name)

    dt_png = "dt.png"
    command = ["dot", "-Tpng", dot_file, "-o", dt_png]
    try:
        subprocess.check_call(command)
    except Exception as e:
        print e
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")


def iris_demo():
    clf = tree.DecisionTreeClassifier()
    iris = load_iris()
    # iris.data属性150*4,iris.target 类别归一化为了0,1,2(150*1)
    clf = clf.fit(iris.data, iris.target)
    dot_file = 'tree.dot'
    tree.export_graphviz(clf, out_file=dot_file)
    visualize_tree(clf, iris.feature_names, dot_file)

    # (graph,) = pydot.graph_from_dot_file('tree.dot')
    # graph.write_png('somefile.png')


if __name__ == '__main__':
    iris_demo()
    pass
