# _*_ coding:utf-8 _*_
import datetime
import calendar
from dateutil import rrule


def get_all_day_v1():
    from datetime import datetime
    d1 = '20171030'
    d2 = '20171102'
    for dt in rrule.rrule(rrule.DAILY,
                          dtstart=datetime.strptime(d1, '%Y%m%d'),
                          until=datetime.strptime(d2, '%Y%m%d')):
        print dt.strftime('%Y%m%d')

    # 20171030 20171031 20171101 20171102


def get_all_day_v2():
    d1 = datetime.date(2017, 10, 30)
    d2 = datetime.date(2017, 11, 2)
    delta = d2 - d1
    print delta.days
    # 3
    days = [d1 + datetime.timedelta(days=x) for x in range((d2-d1).days + 1)]
    for day in days:
        print(day.strftime('%Y%m%d'))

    # 20171030 20171031 20171101 20171102


def tb_partition_sql():
    """
    mysql partition table by day in month
    :return:
    """
    sql = """PARTITION p%s VALUES LESS THAN (TO_DAYS('%s')) ENGINE = InnoDB,"""
    d1 = datetime.date(2017, 12, 1)
    d2 = datetime.date(2017, 12, 31)
    days = [d1 + datetime.timedelta(days=x) for x in range((d2-d1).days + 2)]
    # print len(days)
    for i in xrange(len(days) - 1):
        s1 = days[i].strftime('%Y%m%d')
        s2 = days[i + 1].strftime('%Y-%m-%d')
        print sql % (s1, s2)

    # PARTITION p20171201 VALUES LESS THAN (TO_DAYS('2017-12-02')) ENGINE = InnoDB,
    # ...........
    # PARTITION p20171231 VALUES LESS THAN (TO_DAYS('2018-01-01')) ENGINE = InnoDB,

if __name__ == '__main__':
    # get_all_day_v1()
    # get_all_day_v2()
    tb_partition_sql()
    pass
