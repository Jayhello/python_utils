# coding: utf-8

"""
Ubuntu file server like http server, by python SimpleHTTPServer, or nginx.

This file is used to create url list into txt file.
All the urls are the ubuntu dir files like jpg.
"""

import os
import glob
import random
import hashlib
import string


def write_lst_2txt(lst, f_path):
    """
    Write list to txt file.
    :param lst: list type ['url1', 'url2', ....]
    :param f_path: str type path
    :return: None
    """
    with open(f_path, 'w') as fp:
        for line in lst:
            fp.write("%s\n" % line)


def simple_show():
    base_dir = '/data6/video_img_classify/'

    lst_sub_dir = ['dance', 'life_record', '']

    print glob.glob(base_dir + "*")

    # just show first 5 line
    print glob.glob("./10_15__selected/*.jpg")[:5]


def create_url_file():
    base_dir = './10_15__selected/'
    lst_jpg_path = glob.glob(base_dir + "*.jpg")

    base_url = 'http://14.17.103.232:8000'

    lst_jpg_path = [base_url + path[1:] for path in lst_jpg_path]

    print lst_jpg_path[:2]

    txt_path = './people_url_v1.txt'
    write_lst_2txt(lst_jpg_path, txt_path)


def create_url_recursive():
    base_dir = '/data6/video_img_classify/'

    lst_url = []
    base_url = 'http://14.17.103.232:80'

    lst_sub_dir = ['dance', 'life_record', 'talent', 'extraimg', 'music']

    for sub_dir in lst_sub_dir:
        tmp_dir = "./" + sub_dir
        tmp_lst_path = glob.glob(tmp_dir + "/*/*.jpg")

        print 'now get dir: %s, all: %s' % (tmp_dir, len(tmp_lst_path))

        if 0 == len(tmp_lst_path):
            continue

        tmp_lst_path = random.sample(tmp_lst_path, min(20000, len(tmp_lst_path)))

        tmp_lst_url = map(lambda x: base_url + x[1:], tmp_lst_path)

        print 'random choice url: %s' % random.choice(tmp_lst_url)

        lst_url.extend(tmp_lst_url)

    txt_path = 'person_url_txt_all.txt'
    print 'now write all the url size: %s to %s.....' % (len(lst_url), txt_path)
    write_lst_2txt(lst_url, txt_path)


def get_file_md5(f_path):
    """
    Get md5 of a file
    :param f_path: file path
    :return: md5
    """
    md5 = hashlib.md5()
    with open(f_path, 'rb') as f:
        for block in iter(lambda: f.read(128), ""):
            md5.update(block)

    return md5.hexdigest()


def get_random_str(n=25, src=string.digits+string.lowercase+string.uppercase):

    return ''.join([random.choice(src) for _ in xrange(n)])


def create_url_recursive_v2():
    from os import listdir
    from os.path import isfile, join

    base_dir = '/data6/short_video/short_video_India_images/'
    base_url = 'http://14.17.103.232:8000/'

    d_dir_lst = {
        'dance': ['FolkDance', 'GestureDance', 'HipDance', 'InMyFeelings', 'LatinDance', 'ModernDance', 'OtherDances'],
        'fashion': ['BeautyMakeUp', 'DressCollocation', 'SpecialEffectMakeUp'],
        'film': ['MovieClip'],
        'interesting_classification': ['Dubbing', 'Blame', 'Clip'],
        'life_record': ['ChatQuotation'],
        'music': ['Bbox', 'Guitar', 'Rap', 'Sing'],
        'selfie': ['BeautySelfie', 'FunnySelfie', 'MouthShapeSelfie', 'MusicRhythmSelfie', 'OrdinarySelfie',
                   'PartySelfie', 'PersonalPhotoRotation', 'PlayCoolSelfie', 'SelfLove', 'ShootingSkills'],

        'sprout': ['ChildrenHighFaceValue', 'OrdinaryChildren']
    }

    lst_url = []
    for name in d_dir_lst.keys():
        print "now getting dir: %s" % name
        lst_sub_dir = d_dir_lst[name]
        for sub_dir in lst_sub_dir:
            tmp_dir = base_dir + name + "/" + sub_dir
            tmp_lst_path = glob.glob(tmp_dir + "/*.jpg")

            n = len(tmp_lst_path) / 10
            print "   -----dub dir: %s, get %s" % (sub_dir, n * 3)
            if n == 0:continue

            tmp_lst_path = tmp_lst_path[::10]  # get every 10 elements

            tmp_lst_url = []
            for path in tmp_lst_path:
                md5 = get_random_str()
                url = base_url + path[len(base_dir):]
                vedio_name = path[path.rfind('/') + 1: path.rfind('_')]
                tmp_lst_url.append(vedio_name + ", " + url + ", " + md5)

                # tmp_lst_path = map(lambda path: base_url + path[len(base_dir):] + ","+get_file_md5(path),
                #                tmp_lst_path)

            lst_url.extend(tmp_lst_url)

    print "done get all %s" % len(lst_url)
    print "head 3 is %s" % lst_url[:3]

    txt_path = 'race_people_sample.txt'
    write_lst_2txt(lst_url, txt_path)


if __name__ == '__main__':

    if 1:
        create_url_recursive_v2()

    if 0:
        print get_random_str()

    if 0:
        create_url_recursive()

    if 0:
        create_url_file()

    if 0:
        simple_show()

    if 0:
        path = "./10_15__selected/abc.jpg"
        path = path[1:]
        print path

    if 0:
        lst = range(100)
        print lst[::10]
        s= 'http://14.17.103.232:8000/life_record/ChatQuotation/3800048381981aa1bc9061384c69e4291a993454f2_047.jpg'
        print s[s.rfind('/') + 1: s.rfind('_')]
pass
