# _*_ coding:utf-8 _*_

"""
This file is about approaches of orm(object relational mapper)
in sql alchemy
"""

from basic import get_db_session
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    password = Column(String)

    @hybrid_property
    def name_pwd(self):
        return self.nickname + " " + self.password


def query_orm():
    session = get_db_session()
    user = session.query(User).first()
    print user.name_pwd

if __name__ == '__main__':
    query_orm()
