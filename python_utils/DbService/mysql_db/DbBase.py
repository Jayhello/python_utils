# _*_ coding:utf-8 _*_

import MySQLdb
from utils.JsonUtil import get_json_from_file


class DbBase(object):
    def __init__(self, **kwargs):
        db_config_file = kwargs['db_config_file']
        self.config_db(db_config_file)

    def config_db(self, db_config_file):
        data = get_json_from_file(db_config_file)
        host = data['host']
        user = data['user']
        pwd = data['pwd']
        db = data['db']
        port = data['port']

        self.conn = MySQLdb.connect(host=host, port=port, user=user, passwd=pwd, db=db, charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
