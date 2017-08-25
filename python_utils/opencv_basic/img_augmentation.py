# _*_ coding:utf-8 _*_

"""
Deep learning image augmentation
cited from https://scottontechnology.com/flip-image-opencv-python/
http://augmentor.readthedocs.io/en/master/userguide/mainfeatures.html
"""

import cv2
import glob
import random
import os
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
import Augmentor
import path_var


def img_flip():
    # path = "F:/ad_samples/train_samples/ad_text_artifact/base_type/type_10.jpg"
    path = "F:/ad_samples/download_sample/14/8DB54D749B1D4A2D5FD3441C681D9A2C522453AC_s.jpg"
    img = cv2.imread(path)

    horizontal_img = img.copy()
    vertical_img = img.copy()
    both_img = img.copy()

    horizontal_img = cv2.flip(img, 0)
    vertical_img = cv2.flip(img, 1)
    both_img = cv2.flip(img, -1)

    cv2.imshow("original img", img)
    cv2.imshow("horizontal img", horizontal_img)
    cv2.imshow("vertical img", vertical_img)
    cv2.imshow("both flip", both_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# g_dst_dir = 'F:/ad_samples/train_samples/artifact_ad_web/'
# g_dst_dir = 'F:/ad_samples/train_samples/artifact_ad_web_2_flip/'
# class Path(object):
#     g_dst_dir = ''
# global g_dst_dir
# g_dst_dir = ''


def flip_img_save2dir(file):
    img = cv2.imread(file)

    dst_dir = path_var.g_dst_dir

    h_img = img.copy()
    v_img = img.copy()
    b_img = img.copy()

    h_img = cv2.flip(img, 0)
    v_img = cv2.flip(img, 1)
    b_img = cv2.flip(img, -1)

    # file like F:/ad_samples/train_samples/ad_text_artifact/base_type/type_10.jpg
    # get file name "type_10"
    # type_10.jpg
    base_name = os.path.basename(file)
    # type_10
    base_name = os.path.splitext(base_name)[0]

    file_name = dst_dir + base_name + "_h" + ".jpg"
    cv2.imwrite(file_name, h_img)

    file_name = dst_dir + base_name + "_v" + ".jpg"
    cv2.imwrite(file_name, v_img)

    file_name = dst_dir + base_name + '_b' + ".jpg"
    cv2.imwrite(file_name, b_img)


def do_all_flip(base_dir="F:/ad_samples/train_samples/ad_web_2/"):
    """
    flip all the images in dir, and then save them
     to another dir
    :return:
    """
    # get all files
    # base_dir = "F:/ad_samples/train_samples/ad_text/"

    # base_dir = "F:/ad_samples/download_sample/14/"
    # base_dir = "F:/ad_samples/train_samples/ad_web/"
    # files = glob.glob(base_dir + "*.jpg")
    files = glob.glob(base_dir + "/*.png")
    # like ['E:/img\\1.jpg', 'E:/img\\10.jpg']

    # start 3 process
    # pool = ProcessPool(3)
    pool = ThreadPool(3)
    rets = pool.map(flip_img_save2dir, files)
    pool.close()
    pool.join()
    print 'all images accomplish flip and save to dir'


def flip_all_in_dir():
    base_dir = 'F:/ad_samples/train_samples/others/'
    sub_dir_lst = glob.glob(base_dir + "*")
    # ['F:/dir1', 'F:/dir2']

    # print sub_dir_lst
    new_sub_dir = [os.path.join(base_dir, item + '_flip/') for item in os.listdir(base_dir)]
    # ['F:/dir1_flip', 'F:/dir2_flip']

    for dir_item, new_item in zip(sub_dir_lst[10:], new_sub_dir[10:]):
        global g_dst_dir
        if not os.path.exists(new_item):
            os.makedirs(new_item)
        # g_dst_dir = new_item
        # Path.g_dst_dir = new_item
        path_var.g_dst_dir = new_item
        print 'flip %s, flip dir %s' % (dir_item, new_item)
        do_all_flip(base_dir=dir_item)
    # print os.listdir(base_dir)
    # ['dir1', 'dir2']
    # print glob.glob(base_dir + "*")
    # ['F:/dir1', 'F:/dir2']


def augmentation():
    # path = 'F:/augment'
    # path = 'F:/ad_samples/train_samples/ad_text'

    # output_path = 'F:/ad_samples/train_samples/ad_text_artifact/augmentation'
    # output_path = 'output'

    # path = 'F:/ad_samples/train_samples/artifact_ad_web/artifact_ad_web_14_flip/'
    path = 'F:/ad_samples/train_samples/ad_text_2/'
    # path = 'F:/ad_samples/new_train_sample/'
    # output_path = 'F:/ad_samples/train_samples/artifact_ad_web/artifact_ad_web_14_aug/'
    # output_path = 'F:/ad_samples/train_samples/ad_text_rotate90/'
    # output_path = 'F:/ad_samples/new_train_sample_artifact/'
    output_path = 'F:/ad_samples/train_samples/ad_text_2_output/'

    p = Augmentor.Pipeline(path, output_directory=output_path)

    p.zoom(probability=0.1, min_factor=1.1, max_factor=1.3)
    p.flip_left_right(probability=0.1)
    p.rotate(probability=0.2, max_left_rotation=15, max_right_rotation=16)
    p.shear(probability=0.2, max_shear_left=10, max_shear_right=10)
    p.skew(probability=0.1, magnitude=0.6)
    p.skew_tilt(probability=0.2, magnitude=0.6)
    p.random_distortion(probability=0.3, grid_height=4, grid_width=4, magnitude=4)

    # p.random_distortion(probability=0.2, grid_height=4, grid_width=4, magnitude=4)
    # p.rotate90(probability=1)
    # SIZE = 4164 * 4
    # SIZE = 5 * 10
    # SIZE = 2799 * 10
    # SIZE = 2799 * 1
    # SIZE = 4148 * 3
    SIZE = 68 * 5
    p.sample(SIZE)


if __name__ == '__main__':
    # img_flip()
    # flip_all_in_dir()
    # do_all_flip()
    augmentation()
    # test single image flip and save
    # file = 'F:/ad_samples/train_samples/ad_text_artifact/base_type/type_10.jpg'
    # flip_img_save2dir(file=file)
    pass
