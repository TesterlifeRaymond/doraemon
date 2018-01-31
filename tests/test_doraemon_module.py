"""
@Version: 1.0
@Project: doraemon
@Author: Raymond
@Data: 2018/1/31 下午4:01
@File: test_doraemon_module.py.py
@License: MIT
"""

import unittest

from src.lib import CasesContainer


class DoraemonTest(unittest.TestCase):
    def setUp(self):
        """ pass """

    def tearDown(self):
        """ pass """

    def test_doraemon_is_ok(self):
        self.assertIsNotNone(CasesContainer)
