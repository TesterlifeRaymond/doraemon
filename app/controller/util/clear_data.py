
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-20 10:39:45
# @FileName:  clear_data.py
# @Project: base_test
# @Last Modified by:   jinjialiu
# @Last Modified time: 2017-05-20 10:50:27
"""

from functools import update_wrapper
from ...config.tables import BaseSqlite


class CleaerTestCase(BaseSqlite):
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
            self.session.query(self.table.type == 0).update({self.table.type: 1})
            self.session.commit()
            return self.session.query(self.table).filter_by(type=0).first()
        return update_wrapper(wrapper, function)
