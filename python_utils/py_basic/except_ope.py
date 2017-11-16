# _*_ coding:utf-8 _*_


def test_except_scope():
    try:
        v = 'test scope'
        raise Exception
    except Exception as e:
        # if v is locals():
        #     print v
        print v


def test_except():
    try:
        raise 7
    except Exception as e:
        print e
        # exceptions must be old-style classes or derived from BaseException, not int


if __name__ == '__main__':
    # test_except_scope()
    test_except()
    pass
