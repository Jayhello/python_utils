# _*_ coding:utf-8 _*_


def get_line_lst(filename):
    """
    return list of every line in file
    :param filename the file to be readed
        like '../dataset/dataset.txt':
    :return like [['line1 1'], ['line2 2']]:
    """
    lst = []
    with open(filename) as fp:
        for line in fp:
            lst.append(line)

    return lst

