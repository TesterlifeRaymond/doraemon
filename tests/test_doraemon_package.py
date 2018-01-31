"""
@Version: 1.0
@Project: doraemon
@Author: Raymond
@Data: 2018/1/31 下午7:43
@File: test_doraemon_package.py
@License: MIT
"""
import unittest
from src.lib import CasesContainer


class CasesContainerCase(unittest.TestCase):
    def test_container_is_not_null(self):
        self.assertIsNotNone(CasesContainer)
