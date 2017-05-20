"""
@ Version : ??
@ Author  : liujinjia
@ File    : add_case.py
@ Project : base_test
@ Create Time: 2017-05-19 16:06
"""
from functools import update_wrapper
from ...config.tables import BaseSqlite


class AddCaseWrapper(BaseSqlite):
    """ 这是一个装饰器， 用于对TestCase函数进行获取及存储 , 该类继承BaseSqlite类"""
    def __init__(self, table):
        """ 初始化， params参数为装饰器接受参数
        该参数为 sqlite 中数据表的表名
        """
        self.table = self.table_enu.get(table)

    def __call__(self, function):
        """ 装饰器主方法, function为被挂在该装饰器的函数对象"""
        def wrapper(*args, **kwargs):
            """ wrapper function， 用于对装饰器进行操作"""
            data = self.table(**kwargs)
            self.session.add(data)
            self.session.commit()
            return self.session.query(self.table).filter_by(**kwargs).first()
        return update_wrapper(wrapper, function)
