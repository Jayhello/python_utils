# _*_ coding:utf-8 _*_
"""
python operator module usage, cited from
https://docs.python.org/2/library/operator.html
"""

import operator


def cmp_fun():
    a, b = 5, 3
    print operator.le(a, b)
    # False
    print operator.gt(a, b)
    # True


def lst_ope():
    lst = [1, 2, 3]
    print operator.indexOf(lst, 2)
    # 1
    lst1 = [1, 2, 3, 2]
    print operator.countOf(lst1, 2)
    # 2


def cal_ope():
    lst1 = [0, 1, 2, 3]
    lst2 = [10, 20, 30, 40]
    print map(operator.mul, lst1, lst2)
    # [0, 20, 60, 120]

    print sum(map(operator.mul, lst1, lst2))
    # 200

    a, b = 1, 3
    print operator.iadd(a, b)
    # 4


def item_ope():
    s = ['h', 'e', 'l', 'l', 'o']
    print operator.getitem(s, 1)
    # e
    print operator.itemgetter(1, 4)(s)
    # ('e', 'o')

    inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
    get_count = operator.itemgetter(1)
    print map(get_count, inventory)
    # [3, 2, 5, 1]

    print sorted(inventory, key=get_count)
    # [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]


def reduce_ope():
    a = [2, 3, 4, 5]
    print reduce(lambda x, y: x + y, a)
    # 14
    print reduce(operator.add, a)
    # 14

if __name__ == '__main__':
    reduce_ope()
    # item_ope()
    # cal_ope()
    # lst_ope()
    # cmp_fun()
    pass
