"""
@ Version : ??
@ Author  : liujinjia
@ File    : tables.py
@ Project : base_test
@ Create Time: 2017-05-19 16:09
"""
from .connect import TestCase
from . import SESSION


class BaseSqlite:
    """ sqlite 元类"""
    table_enu = {
        'test_case': TestCase
    }
    session = SESSION
