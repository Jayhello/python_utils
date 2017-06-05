# _*_ coding:utf-8 _*_
"""
This file is some operator about dict
"""


def lst_2_dict():
    """
    combine two list to dict
    :return:
    """
    lst1 = ['a', 'b', 'c']
    lst2 = [1, 2, 3]
    # d = {k: v for k, v in zip(lst1, lst2)}
    d = dict(zip(lst1, lst2))
    print d
    # {'a': 1, 'c': 3, 'b': 2}


if __name__ == '__main__':
    lst_2_dict()
    pass
