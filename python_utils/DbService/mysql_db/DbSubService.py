# _*_ coding:utf-8 _*_

from DbBase import DbBase


class DbSubService(DbBase):
    def __init__(self, **kwargs):
        super(DbSubService, self).__init__(**kwargs)

    def query(self):
        pass

    def count(self, tb):
        """
        :param tb:
        :return: table rows count
        """
        query_sql = ' select count(*) from %s ' % tb
        self.cursor.execute(query_sql)
        res = self.cursor.fetchone()
        print res[0]
        return res[0]

if __name__ == '__main__':
    db = DbSubService(db_config_file='../config/mysql_config.json')
    tb = 'tb_test'
    db.count(tb)
