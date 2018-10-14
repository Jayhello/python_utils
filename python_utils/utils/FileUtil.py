# _*_ coding:utf-8 _*_
from os import listdir
from os.path import isfile, join
import glob
import os
import errno
from xlwt import *
import time


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

    The above may contains '\n', the below one line can solve it.
     open(f_path).read().split('\n')
    """
    lst = []
    with open(filename) as fp:
        for line in fp:
            lst.append(line)

    return lst


def write_lines_to_txt():
    lst = ['line1', 'line2', 'line3']

    f_path = 'output.txt'
    with open(f_path, 'w') as fp:
        for line in lst:
            fp.write("%s\n" % line)

        # or
        # fp.write("\n".join(lst))


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


def batch_rename_files_in_dir():
    """
    signal level dir
    :return:
    """
    base_dir = 'F:/ad_samples/img_voice_test/tencent_img/violence_samples/'
    file_list = glob.glob(base_dir + "*.jpg")
    i = 0
    for f in file_list:
        os.rename(f, os.path.join(base_dir, str(i) + '.jpg'))
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


def write_list_excel(file_name, title_lst, row_lst):
    # excel operator handler
    excel_handler = Workbook(encoding='utf-8')
    excel_sheet_name = time.strftime('%Y-%m-%d')
    excel_sheet = excel_handler.add_sheet(excel_sheet_name)

    # write title
    col_idx = 0
    for item in title_lst:
        excel_sheet.write(0, col_idx, item)
        col_idx += 1

    # write row contents, index->row
    row_idx = 1
    for row in row_lst:
        col_idx = 0
        for item in row:
            excel_sheet.write(row_idx, col_idx, item)
            col_idx += 1
        row_idx += 1

    # write/save excel to file
    excel_handler.save(file_name)


def test_write_list_excel():
    file = 'F:/test.xlsx'
    title_lst = ['姓名', '性别', '年龄', ]
    row_lst = [['熊大', '男', 10], ['熊2', '男', '15'], ['强哥', '男', 25]]
    write_list_excel(file, title_lst, row_lst)


g_val = 3


def del_file_is_exists(f):
    if os.path.exists(f):
        os.remove(f)


def get_file_create_time(f_path=None):
    f_path = 'F:/826.mp3'
    t = os.path.getmtime(f_path)
    print t
    # 1511842029.89
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
    # 2017-11-28 12:07:09

    now_t = int(time.time())
    print now_t, now_t - int(t)
    # 1511856026 13997


def get_relative_path():
    """
    https://stackoverflow.com/questions/8693024/how-to-remove-a-path-prefix-in-python
    :return:
    """
    full_path = '/book/html/wa/foo/bar/'
    print os.path.relpath(full_path, '/book/html')
    # wa\foo\bar


def download_from_url():
    """download file from url, and save it to path"""
    import urllib

    dw = urllib.URLopener()

    url = 'https://o-hk.ihago.net/ikxd/guest_2.png'
    f_name = 'path/filename.ext'

    # download and save file
    dw.retrieve(url, f_name)


def get_img_from_dir(base_dir='', lst_ext=['jpg', 'png', 'jpeg']):
    """Get all the jpg and png file from base_dir

        return: lst ['path/name.jpg, ...']
    """

    import glob
    lst_img = []
    for ext in lst_ext:
        # append all the jpg
        lst_img += glob.glob(base_dir + "*." + ext)

    return lst_img


def get_file_md5(f_path):
    """
    Get md5 of a file
    :param f_path: file path
    :return: md5
    """
    import hashlib

    md5 = hashlib.md5()
    with open(f_path, 'rb') as f:
        for block in iter(lambda: f.read(128), ""):
            md5.update(block)

    return md5.hexdigest()


def batch_rename_recursive():
    """
    two-level dir
    added 2017/8/17, rename dir hello.jpg
    :return:
    """
    # base_dir = 'F:/ad_samples/test_samples/'
    base_dir = 'F:/ad_samples/test_samples_2/'
    base_dir = 'E:/face_rec/short_vedio_famous_people/people_lst/'
    sub_dir_list = glob.glob(base_dir + '*')
    # print sub_dir_list ['F:/dir1', 'F:/dir2']
    for dir_item in sub_dir_list:
        dir_item = dir_item.replace('\\', '/')
        files = get_img_from_dir(dir_item)
        # files = os.listdir(dir_item)
        # os.chdir(dir_item)
        i = 0
        if len(files) == 0:
            continue
        for f in files:
            # fname = 'xx' + str(i)
            k_md5 = get_file_md5(f)
            new_name = os.path.join(dir_item, k_md5 + '.jpg')
            os.rename(f, new_name)
            i += 1


def batch_rename():
    """Batch rename file in directory to md5
    """
    base_dir = "E:/face_rec/face_det_test/whole_excluded_female_cleaned/"
    base_dir = "E:/face_rec/face_det_test/whole_excluded_male_cleaned/"
    base_dir = "E:/face_rec/face_det_test/new_task_8_28/suitable/"
    base_dir = "E:/face_rec/face_det_test/new_task_8_28/unsuitable/"
    base_dir = "E:/face_rec/yy_face_demand/cartoon_sample/cartoon_face_images/"
    base_dir = "E:/face_rec/yy_face_demand/cartoon_sample/pet_test_images/"
    base_dir = "E:/face_rec/face_det_test/new_train_data/"
    lst_img = get_img_from_dir(base_dir)
    # lst_img = get_img_from_dir(base_dir, lst_ext=['gif'])

    for path in lst_img:
        k_md5 = get_file_md5(path)
        ext = os.path.splitext(path)[1]
        # new_name = os.path.join(base_dir, k_md5 + ext)
        new_name = os.path.join(base_dir, k_md5 + '.jpg')
        # print "now rename %s -> %s" % (path, new_name)
        try:
            os.rename(path, new_name)
        except WindowsError as e:
            print "rename error:%s %s" % (e, path)


if __name__ == '__main__':
    # batch_rename()

    batch_rename_recursive()

    # get_relative_path()
    # get_file_create_time()
    # test_write_list_excel()
    # batch_rename()
    # batch_rename_files_in_dir()
    # get_file_name()
    # print get_all_files_name_in_dir('E:/rectimg')
    # print [1, 2, 0] * 3
    # print g_val
    pass
