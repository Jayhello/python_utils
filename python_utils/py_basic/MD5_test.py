# _*_ coding:utf-8 _*_
import md5
import sha
import hashlib


def test_md5():
    content = 'hello xy, are you ok?'
    print hashlib.md5(content).hexdigest()
    print hashlib.sha1(content).hexdigest()


if __name__ == '__main__':
    test_md5()
    pass
