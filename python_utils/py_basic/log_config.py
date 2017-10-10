# _*_ coding:utf-8 _*_
import logging

# log config, module name, line num, function name
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(module)s:%(lineno)s %(funcName)s %(threadName)s %(message)s",
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %I:%M:%S'
)


def test_log():
    logging.info('hello world')

if __name__ == '__main__':
    test_log()
    pass
