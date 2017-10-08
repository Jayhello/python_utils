# _*_ coding:utf-8 _*_

"""
operator about collection
"""

from collections import Counter


def counter_usage():
    lst = ['class_1', 'class_2', 'class_1', 'class_1', 'class_1', 'class_2']

    print Counter(lst).most_common()
    # [('class_1', 4), ('class_2', 2)]

    print Counter(lst).most_common(1)
    # [('class_1', 4)]

    print Counter(lst).most_common(1)[0][0]
    # class_1


if __name__ == '__main__':
    counter_usage()
    pass
