"""
@ Version : ??
@ Author  : liujinjia
@ File    : connect.py
@ Project : base_test
@ Create Time: 2017-05-19 15:48
"""

from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///app/constructor/constructor.sqlite',
                       encoding='utf8',
                       convert_unicode=True,
                       # echo=True
                       )
session = sessionmaker(engine)
Base = declarative_base()


class TestCase(Base):
    """ 数据库 user 表 model"""
    __tablename__ = 'test_case'

    id = Column(Integer, primary_key=True)
    uri = Column(String)
    class_name = Column(String)
    func_name = Column(String)
    body = Column(String)
    kwassert = Column(String)
    type = Column(String, default=0)

    def __init__(self, uri, class_name, func_name, body, kwassert):
        """ pass """
        self.uri = uri
        self.class_name = class_name
        self.func_name = func_name
        self.body = body
        self.kwassert = kwassert

    def __repr__(self):
        """ 调用类返回的结构 """
        return '<Case(module={})>'.format(self.func_name)

Base.metadata.create_all(bind=engine)