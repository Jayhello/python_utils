# _*_ coding:utf-8 _*_
import md5
import sha
import hashlib


def test_md5():
    content = 'hello xy, are you ok?'
    print hashlib.md5(content).hexdigest()
    # 180d5f07d511b660f320cf2a645f1f3b
    print hashlib.sha1(content).hexdigest()
    # c25884a4688c8b1a25a619f198f91f8661b2623b


if __name__ == '__main__':
    test_md5()
    pass
