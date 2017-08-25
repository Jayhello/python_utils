# _*_ coding:utf-8 _*_
"""
This file about some operator of base64 in python.
eg. image to base64 string, and then the base64 string to image
For a http issue, we may want to send image directly not url, for sake of
unvisited url by other server
cited from https://stackoverflow.com/questions/3715493/encoding-an-image-file-with-base64
"""
import base64
import requests


def img_base64():
    img_path = 'F:/img_test/dl_img_text_recognition/online_1.jpg'
    with open(img_path, 'rb') as img_file:
        b64_str = base64.b64encode(img_file.read())
        print len(b64_str)
        # 55932
        print b64_str
        # /9j/4AAQSkZ.............


def img_url_base64():
    url = 'http://i2.chinanews.com/simg/hd/2017/05/15/b3e10469cc0b4b84b2e9cedbb800cd3a.jpg'
    url = 'http://yysnapshot.bs2ctl7.yy.com/68a14b739dac400d1d1898327478a556b52260ec?height=720&interval=12402&file=68a14b739dac400d1d1898327478a556b52260ec&width=1280&bucket=yysnapshot&yid=7841950807447568392&day=20170820&t=1503163828000&streamid=7841950807452359080&id=3228019745205722527&size2=320&p=1'
    url = 'http://imgcache.qq.com/open_proj/proj_qcloud_v2/gateway/portal/css/img/home/qcloud-logo-dark.png'
    b64_str = base64.b64encode(requests.get(url).content)
    print len(b64_str)
    print b64_str


if __name__ == '__main__':
    # img_base64()
    img_url_base64()
    pass
