# coding:utf-8

"""
download image from txt file, in which all the rows in txt is a url string
"""

import json
import urllib
import numpy as np
import cv2
import glob
import os
import errno
import random
from multiprocessing import Pool as ProcessPool


def make_dir_not_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def get_name_from_url(url):
    """
    Get name from url
    :param url:
    :return: str
    """
    return url[url.rfind('/') + 1:url.rfind('.')]


def read_txt(f_path=''):
    lst_lines = []

    with open(f_path) as fp:
        for line in fp:
            lst_lines.append(line[:-1])

    return lst_lines


def get_url_lst_from_csv(f_path='E:/tmp_img_select/xiongyu/SelfLove_4146.csv'):
    """
    get all the url lst
    :param f_path: csv path
    :return: ['url1', 'url2', ...]
    """
    lst_url = []
    count = 0
    with open(f_path) as fp:
        for line in fp:
            if line and line.find(',') > 0:
                lst_url.append(line.split(',')[0])
                count += 1
                # if count > 20000:  # just read 20000 line
                #     break

    return lst_url


def get_file_name(f_path):
    """
    Get file name from file path
    :param f_path:
    :return: file name
    """
    base_name = os.path.basename(f_path)
    return os.path.splitext(base_name)[0]


def dw_img_and_save(lst_url_path):
    """
    Download image from url and save it to path
    :param d_url_path: list [url, path]
    :return: None
    """
    try:
        url, img_path = lst_url_path[0], lst_url_path[1]
        if os.path.exists(img_path):  # if file exists, then don't download
            # print '%s exists, so skip it' % img_path
            return

        img = urllib.URLopener()
        img.retrieve(url, img_path)
    except Exception as e:
        print "dw %s, error %s" % (url, e)


def dw_img_from_txt():
    """Download all the files from txt with url in each line
    """
    # get all the url list, and random choice 5000

    d_path = {"female_annotation": "female_annotation",
              "male_annotation": "male_annotation",
              "mutiple_annotation": "mutiple_annotation"
              }

    base_dir = 'E:/people_detection/10_15_has_person/'

    lst_url_path = []

    for txt_name, dir_name in d_path.viewitems():

        txt_path = base_dir + txt_name + ".txt"

        lst_urls = read_txt(txt_path)
        lst_urls = random.sample(lst_urls, 8000)

        base_save_dir = base_dir + dir_name + "/"

        for url in lst_urls:
            name = get_name_from_url(url)
            img_path = base_save_dir + name + '.jpg'

            lst_url_path.append([url, img_path])

    pool = ProcessPool(5)
    results = pool.map(dw_img_and_save, lst_url_path)
    pool.close()
    pool.join()


def get_file_name_lst(base_dir='E:/SecureCRT_tmp/img_people_sample/person_det_url_box_v2_10_24/'):
    lst_file = os.listdir(base_dir)
    lst_name = [os.path.splitext(name)[0] for name in lst_file]
    # print lst_name[:5]
    return lst_name


def dw_img():
    # txt_file = 'E:/SecureCRT_tmp/img_people_sample/person_det_url_box_v2_10_24.csv'
    # lst_url = get_url_lst_from_csv(txt_file)

    txt_file = 'E:/race-classifcation/race_indian_yellow/short_video_Indonesia_images.txt'
    lst_url = read_txt(txt_file)

    print 'get %s to be download.....' % len(lst_url)

    # lst_has_dw_name = get_file_name_lst()

    base_dir = 'E:/race-classifcation/race_indian_yellow/short_video_Indonesia_images/'
    lst_url_path = []
    for url in lst_url:
        name = get_name_from_url(url)
        # if name not in lst_has_dw_name:
        img_path = base_dir + name + '.jpg'
        lst_url_path.append([url, img_path])

    print 'starting downloading %s img.....' % len(lst_url_path)

    pool = ProcessPool(5)
    result = pool.map(dw_img_and_save, lst_url_path)
    pool.close()
    pool.join()


if __name__ == '__main__':
    if 0:
        dw_img_from_txt()

    if 1:
        dw_img()

    # get_file_name_lst()
    pass
