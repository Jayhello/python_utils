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
            # d_info.pop(key)
            # del d_info[key]
            pass
    print 'after del'

    for key in d_info.iterkeys():
        print key, d_info[key]


def iter_dict_remove():
    """remove item in dict while iteration it"""
    d_info = {'aa': -1, 'bb': 0, 'cc': 1, 'dd': 2}

    for k, v in d_info.items():
        print k, v
        if v < 0:
            del d_info[k]

    print 'after del'

    for key in d_info.iterkeys():
        print key, d_info[key]

if __name__ == '__main__':
    # lst_2_dict()
    # iter_dict()
    # iter_dict_remove()

    s_lst={}
    s_lst['worker_1'] = [1, 2, 3]
    s_lst['worker_2'] = [1, 2, 3]
    print s_lst
    # d_info = {}
    # if d_info is None:
    #     print 'none'
    # else:
    #     # 0
    #     print len(d_info)
    lst = [1, 2, 3]

    pass
