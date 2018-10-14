# coding:utf-8

import SimpleHTTPServer


def test_translate_path():
    url = "http://yy.com/ai/xy/"
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler(None, None, None)

    print handler.translate_path(url)


if __name__ == '__main__':

    # ----- test translate path -----
    if 1:
        test_translate_path()
    # ----- end -----

    pass
