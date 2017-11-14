# _*_ coding:utf-8 _*_


def test_except_scope():
    try:
        v = 'test scope'
        raise Exception
    except Exception as e:
        # if v is locals():
        #     print v
        print v

if __name__ == '__main__':
    test_except_scope()
    pass
