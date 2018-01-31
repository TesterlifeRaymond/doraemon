"""
@Version: 1.0
@Project: doraemon
@Author: Raymond
@Data: 2018/1/31 下午7:58
@File: test_case_manager.py
@License: MIT
"""

import unittest
from src.lib import CasesManager


class CaseManagerCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.default_path = 'cases/'

    def test_set_file_path(self):
        path = '.'
        case_mananger = CasesManager(path)
        self.assertFalse(case_mananger.path == self.default_path)

    def test_default_file_path(self):
        case_mananger = CasesManager()
        self.assertTrue(case_mananger.path == self.default_path)
