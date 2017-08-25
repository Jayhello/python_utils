import urllib
import cv2
import numpy as np


def url_img_cv():
    url = "http://yysnapshot.bs2src9.yy.com/636be6fc25410c5208d4c4ba5a22e2365768ec52?height=960&interval=12465&file=636be6fc25410c5208d4c4ba5a22e2365768ec52&width=544&bucket=yysnapshot&yid=7399736121338363914&day=20170817"
    try:
        url_response = urllib.urlopen(url)
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)
        cv2.imshow('URL Image', img)
        cv2.waitKey()
    except Exception, e:
        print e
    finally:
        print 'no use line, nothing to be cleared'
        # can't return None in this scope, because this file is certainly to be executed
        # return None

if __name__ == '__main__':
    url_img_cv()
