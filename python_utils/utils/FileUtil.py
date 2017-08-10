# _*_ coding:utf-8 _*_
from os import listdir
from os.path import isfile, join
import glob, os


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


def get_all_files_name_in_dir(dir):
    files = [f for f in listdir(dir)]
    # like ['1.jpg', '10.jpg', '2.jpg', 'dir']

    files = [f for f in listdir(dir) if isfile(join(dir, f))]
    # doesn't contain directory
    # like ['1.jpg', '10.jpg', '2.jpg']
    files = [join(dir, f) for f in listdir(dir) if isfile(join(dir, f))]
    # like ['E:/img\\1.jpg', 'E:/img\\10.jpg', 'E:/img\\2.jpg']

    files = [f for f in listdir(dir) if f.endswith('.jpg')]
    # like ['1.jpg', '10.jpg', '2.jpg']

    files = glob.glob(dir + '/*.jpg')
    # like ['E:/img\\1.jpg', 'E:/img\\10.jpg', 'E:/img\\2.jpg']
    os.chdir(dir)
    files = glob.glob('*.jpg')
    # like ['1.jpg', '10.jpg', '2.jpg']
    return files

g_val = 3

if __name__ == '__main__':
    print get_all_files_name_in_dir('E:/rectimg')
    print [1, 2, 0] * 3
    print g_val
    pass
