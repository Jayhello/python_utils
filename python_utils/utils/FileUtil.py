# _*_ coding:utf-8 _*_
from os import listdir
from os.path import isfile, join
import glob
import os
import errno


def make_dir_not_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


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


def all_subdir_join():
    """
    more details of sub dir search visits
    https://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
    :return:
    """
    base_dir = 'F:/ad_samples/train_samples/others/'
    sub_dir_lst = glob.glob(base_dir + "*")
    # ['F:/dir1', 'F:/dir2']
    new_sub_dir = [os.path.join(base_dir, item + '_flip') for item in os.listdir(base_dir)]
    # ['F:/dir1_flip', 'F:/dir2_flip']
    # find all the .c files in the dir of src
    glob.glob(os.path.join('src', '*.c'))

    # find all the .c files in the one level subdir of src
    glob.glob(os.path.join('src', '*', '*.c'))
    # print os.listdir(base_dir)
    # ['dir1', 'dir2']
    # print glob.glob(base_dir + "*")
    # ['F:/dir1', 'F:/dir2']


def batch_rename():
    """
    added 2017/8/17, rename dir hello.jpg
    :return:
    """
    # base_dir = 'F:/ad_samples/test_samples/'
    base_dir = 'F:/ad_samples/test_samples_2/'
    base_dir = 'F:/ad_samples/img_voice_test/tencent_img/'
    sub_dir_list = glob.glob(base_dir + '*')
    # print sub_dir_list ['F:/dir1', 'F:/dir2']
    for dir_item in sub_dir_list:
        files = glob.glob(dir_item + '/*.jpg')
        # files = os.listdir(dir_item)
        # os.chdir(dir_item)
        i = 0
        if len(files) == 0:
            continue
        for f in files:
            # fname = 'xx' + str(i)
            os.rename(f, os.path.join(dir_item, str(i) + '.jpg'))
            i += 1


def get_file_name():
    file_path = 'E:/img/10.jpg'
    print os.path.basename(file_path)
    # 10.jpg

    head, tail = os.path.split(file_path)
    print head, tail
    # E:/img 10.jpg

    print os.path.splitext(file_path)
    # ('E:/img/10', '.jpg')
    print os.path.splitext(file_path)[0]
    # E:/img/10

    base = os.path.basename(file_path)
    # 10.jpg
    print os.path.splitext(base)
    # ('10', '.jpg')
    print os.path.splitext(base)[0]
    # 10

g_val = 3

if __name__ == '__main__':
    batch_rename()
    # get_file_name()
    # print get_all_files_name_in_dir('E:/rectimg')
    # print [1, 2, 0] * 3
    # print g_val
    pass
