# _*_ coding:utf-8 _*_
"""
This file is some operator about dict

cited:

https://stackoverflow.com/questions/613183/how-to-sort-a-dictionary-by-value
https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
http://pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
https://stackoverflow.com/questions/20464368/sort-a-dictionary-by-length-of-the-value
"""
import operator
from collections import OrderedDict


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
    # d.pop('a')
    del d['a']
    print d


def iter_dict():
    """
    RuntimeError: dictionary changed size during iteration
    iteration del error
    """
    d_info = {'aa': -1, 'bb': 0, 'cc': 1, 'dd': 2}
    for key in d_info.iterkeys():
        print key, d_info[key]
        if d_info[key] < 0:
            # RuntimeError: dictionary changed size during iteration
            d_info.pop(key)
            # del d_info[key]
            pass
    print 'after del'

    for key in d_info.iterkeys():
        print key, d_info[key]


def iter_dict_remove():
    """remove item in dict while iteration it"""
    d_info = {'aa': -1, 'bb': 0, 'cc': 1, 'dd': 2}

    # right way
    # for k, v in d_info.items():
    #     print k, v
    #     if v < 0:
    #         del d_info[k]

    for k in d_info.keys():
        print k, d_info[k]
        if d_info[k] < 0:
            del d_info[k]

    print 'after del'

    for key in d_info.iterkeys():
        print key, d_info[key]


def iter_dic_sort():
    """iter dict by sorted keys"""
    d_info = {'33': 33, '88': 88, '22': 22, '44': 44}
    for k in sorted(d_info):
        print k, d_info[k]


def dict_sort_by_value():
    dic_num = {'first': 11, 'second': 2, 'third': 33, 'Fourth': 4}

    # print all the keys
    print dic_num.keys()
    print list(dic_num)
    # ['second', 'Fourth', 'third', 'first']

    # print all the sorted keys
    print sorted(dic_num)
    # ['Fourth', 'first', 'second', 'third']

    print sorted(dic_num, key=str.lower)
    # ['first', 'Fourth', 'second', 'third']

    # print sorted values
    print sorted(dic_num.values())
    # [2, 4, 11, 33]

    # sorted by value
    sorted_val = sorted(dic_num.items(), key=operator.itemgetter(1))
    # [('second', 2), ('Fourth', 4), ('first', 11), ('third', 33)]
    print sorted_val

    # sorted by key
    sorted_key = sorted(dic_num.items(), key=operator.itemgetter(0))
    print sorted_key
    # [('Fourth', 4), ('first', 11), ('second', 2), ('third', 33)]

    dic_k_lst = {'11': [1, 2], 'ab': [3], 'cd': [0, -1, 2]}
    # Sort a dictionary by length of the value
    print sorted(dic_k_lst.items(), key=lambda item: len(item[1]))
    # [('ab', [3]), ('11', [1, 2]), ('cd', [0, -1, 2])]

    dic_k_set = {'11': {1, 2}, 'ab': {3}, 'cd': {0, -1, 2}}
    # Sort a dictionary by length of the value
    d_val_len = sorted(dic_k_set.items(), key=lambda item: len(item[1]))
    print d_val_len
    # [('ab', set([3])), ('11', set([1, 2])), ('cd', set([0, 2, -1]))]
    print d_val_len[0][1]
    # set([3])
    print len(d_val_len[0][1])
    # 1 (长度为 1)


def dic_to_lst():
    dic_k_lst = {'11': [1, 2], 'ab': [3], 'cd': [0, -1, 2]}
    lst = [(k, len(dic_k_lst[k])) for k in dic_k_lst.keys()]
    print lst
    # [('11', 2), ('ab', 1), ('cd', 3)]


def dic_count_value():
    from collections import Counter
    dic_k_lst = {'11': None, 'ab': 3, 'name': 'xy', 'none': None, 'age': 26}
    print Counter(dic_k_lst.values())
    # Counter({None: 2, 'xy': 1, 26: 1, 3: 1})

    count_none = 0
    count_not_none = 0
    for k in dic_k_lst.keys():
        if dic_k_lst[k] is None:
            count_none += 1
        else:
            count_not_none += 1

    print count_none, count_not_none
    # 2 3


def count_val_lst_len():
    d = {'T1': ['eggs', 'bacon', 'sausage'], 'T2': ['spam', 'ham', 'monty', 'python']}
    print map(len, d.values())
    # [4, 3]
    print sum(map(len, d.values()))
    # 7


def sum_dic_val():
    d_info = {'33': 1, '88': 2, '22': 3, '44': 4}
    print sum(d_info.values())
    # 10


def dict_pop():
    dic_k_lst = {'11': {1, 2}, 'ab': [3], 'cd': [0, -1, 2]}
    s1 = dic_k_lst['11']
    print s1
    # set([1, 2])
    # del dic_k_lst['11']
    dic_k_lst.pop('11')
    print s1
    # set([1, 2])
    print dic_k_lst
    # {'ab': [3], 'cd': [0, -1, 2]}


def dic_val_lst():
    dic_k_lst = {'11': [1, 2], 'ab': [3], 'cd': [0, -1, 2]}
    dic_k = {}
    for k, v in dic_k_lst.items():
        for item in v:
            dic_k[item] = k

    print dic_k


def dic_probability():
    p = {1: {1: 0.1, 2: 0.3}, 2: {1: 0.1, 2: 0.3}}
    # {1: {1: 0.1, 2: 0.3}, 2: {1: 0.1, 2: 0.3}}
    print p[2], p[2][2]
    # {1: 0.1, 2: 0.3} 0.3

if __name__ == '__main__':
    # dic_val_lst()
    # dict_pop()
    # sum_dic_val()
    # count_val_lst_len()
    # dic_count_value()
    # dic_to_lst()
    # dict_sort_by_value()
    # lst_2_dict()
    # iter_dict()
    # iter_dic_sort()
    iter_dict_remove()

    s_lst={}
    s_lst['worker_1'] = [1, 2, 3]
    s_lst['worker_2'] = [1, 2, 3]

    # s_lst['worker_2'] = [1, 2, 3]
    # print s_lst
    # s_lst.pop('worker_1')
    # print s_lst
    # d_info = {}
    # if d_info is None:
    #     print 'none'
    # else:
    #     # 0
    #     print len(d_info)
    # lst = [1, 2, 3]

    pass
