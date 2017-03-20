# _*_ coding:utf-8 _*_

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.JsonUtil import get_json_from_file


def get_db_session():
    db_config_file = '../config/mysql_config.json'
    db_js_data = get_json_from_file(db_config_file)
    db_connect = 'mysql+mysqldb://{user}:{pwd}@{host}/{db}?charset=utf8'.format(**db_js_data)
    print db_connect
    # mysql+mysqldb://root:123@localhost/springdemo?charset=utf8
    engine = create_engine(db_connect, echo=True)
    session = sessionmaker(bind=engine)
    return session()


def query_example():
    session = get_db_session()
    print session.execute('show databases').fetchall()
    # [(u'springdemo',), (u'test',), (u'world',)]
    print session.execute('select * from tb_yylive_news where id = 1').first()
    # (1L, u'http://www.bbc.com')

if __name__ == '__main__':
    # get_db_session()
    query_example()
