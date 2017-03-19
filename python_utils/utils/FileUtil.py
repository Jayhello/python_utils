# _*_ coding:utf-8 _*_


def get_line_lst(filename):
    lst = []
    with open(filename) as fp:
        for line in enumerate(fp):
            lst.append(line)

    return lst

