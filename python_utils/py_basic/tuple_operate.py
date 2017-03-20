# _*_ coding:utf-8 _*_


def list_2_tuple():
    lst = ['python', 12, True, [1, 2]]
    tp = tuple(lst)
    print tp
    # ('python', 12, True, [1, 2])
    tp = tuple(tuple(item) for item in lst)
    print tp

if __name__ == '__main__':
    list_2_tuple()
