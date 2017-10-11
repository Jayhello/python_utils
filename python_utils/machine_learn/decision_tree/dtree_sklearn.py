# _*_ coding:utf-8 _*_

"""
data set from:
http://archive.ics.uci.edu/ml/datasets/banknote+authentication
http://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt
"""

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import subprocess
import pydot

def visualize_tree(tree):
    """Create tree png using graphviz.

    Args
    ----
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    """
    with open("tree.dot", 'w') as f:
        export_graphviz(tree, out_file=f,
                        feature_names=iris.feature_names)

    command = ["dot", "-Tpng", "tree.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")

clf = tree.DecisionTreeClassifier()
iris = load_iris()
clf = clf.fit(iris.data, iris.target)
tree.export_graphviz(clf, out_file='tree.dot')
(graph,) = pydot.graph_from_dot_file('tree.dot')
graph.write_png('somefile.png')

# command = ["dot", "-Tpng", "tree.dot", "-o", "dt.png"]
# try:
#     subprocess.check_call(command)
# except:
#     exit("Could not run dot, ie graphviz, to "
#          "produce visualization")

visualize_tree(clf)



if __name__ == '__main__':

    pass
