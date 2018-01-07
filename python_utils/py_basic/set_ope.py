# -*- coding:utf-8 -*-
"""
python unique list -> set usage
"""


def define_set():
    """2 ways of defining set"""
    set_1 = set([1, 2, 3])
    print type(set_1)
    print set_1

    set_2 = {2, 3, 2}
    print type(set_2)
    # <type 'set'>
    print set_2
    # set([2, 3])

    a = set((1, 2, 3, 4))
    b = set([3, 4, 5, 6])
    print a | b  # Union
    # {1, 2, 3, 4, 5, 6}
    print a & b  # Intersection
    # {3, 4}
    print a < b  # Subset
    # False
    print a - b  # Difference
    # {1, 2}
    print a ^ b  # Symmetric Difference
    # {1, 2, 5, 6}


def set_basic_usage():
    s1 = set()

    s1.add('abc')
    s1.add('abc')
    s1.add(123)
    s1.add(777)
    print (s1)

    if 123 in s1:
        print ' find it and remove it'
        s1.remove(123)
    print s1


def dict_val_set():
    dic_val_set = {}
    dic_val_set['abc'] = set([123])
    dic_val_set['abc'].add(456)
    dic_val_set['abc'].add(123)
    print dic_val_set
    # {'abc': set([456, 123])}
    dic_val_set['ddd'] = set()
    dic_val_set['ddd'].add(123)

    for k in dic_val_set.keys():
        if 123 in dic_val_set[k]:
            print dic_val_set[k]


def set_remove():
    # s_src = {1, 3, 5, 7}
    s_src = {1}
    # s2 = {1, 3, 2}
    s2 = [1, 3, 2]
    # raise error
    # print s_src.remove(*s2)
    try:
        s_src.remove(*s2)
    except Exception as e:
        print e
        # print s_src
        print s_src - s2

    # print s_src | s2
    # set([1, 2, 3, 5, 7])
    # print s_src & s2
    # set([1, 3])


def set_lst():
    s1 = {1, 2, 3}
    lst_1 = []
    # set to list
    lst_1 += s1

    print s1
    print lst_1


def dict_key_to_set():
    d = {'111': 1, 'aaa': 111}
    s1 = set(d.keys())
    print s1
    # set(['111', 'aaa'])

    s2 = {'111', 111}
    print s1 & s2


def set_diff():
    s1 = {1, 3}
    s2 = {1, 2, 4}

    print s1 - s2
    print s1.difference(s2)
    # set([3])


def set_hash():
    lst = [1, 555, 372, 6, 6, 372, 222]
    h_set = set(lst)
    print h_set  # unordered
    # set([1, 555, 372, 222, 6])

if __name__ == '__main__':
    set_hash()
    # set_diff()
    # dict_key_to_set()
    # set_lst()
    # set_remove()
    # define_set()
    # dict_val_set()
    # set_basic_usage()
    # print min(3, 4, -1)
    # import time
    # import random
    # timestamp = int(time.time())
    # print random.randint(0, 1000000) + timestamp
    pass
