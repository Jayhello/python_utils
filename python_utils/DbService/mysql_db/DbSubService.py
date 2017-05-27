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

    def get_liver_info(self, limit_start, limit_size):
        query = """select reported_uid,
                    sum(audit_status='S01') as audit_status_S01,
                    sum(audit_status='S02') as audit_status_S02,
                    sum(audit_status='S03') as audit_status_S03,
                    sum(audit_status='S04') as audit_status_S04,
                    sum(audit_status='S05') as audit_status_S05,
                    count(*) as audit_status_all from iboms.tb_ms_mobile_report_test
                    group by reported_uid
                    limit %s, %s""" % (limit_start, limit_size)

        self.cursor.execute(query)
        return [row for row in self.cursor]

    def bulk_update(self, lst):
        """
        batch updates
        [("new_value" , "3"),("new_value" , "6")]
        :param lst:
        :return:
        """
        query = """UPDATE Writers SET Name = %s WHERE Id = %s"""
        self.cursor.executemany(query, lst)
        self.conn.commit()


if __name__ == '__main__':
    db = DbSubService(db_config_file='../config/mysql_config.json')
    tb = 'tb_test'
    db.count(tb)
