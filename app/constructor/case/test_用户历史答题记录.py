# -*- coding: utf-8 -*-

""" 测试工具自动生成的case """

import unittest
from app.controller.util.active import test_case_runner, test_case_parse


class 用户历史答题记录(unittest.TestCase):
    """这是用户历史答题记录接口测试用例"""

    def setUp(self):
        """ test setup function """

    def tearDown(self):
        """ test case tearDown function """

    @test_case_runner
    @test_case_parse
    def test_POST查询用户全部历史答题信息(self, **kwargs):
        """ POST查询用户全部历史答题信息 接口测试case """
        response, kwassert = kwargs.get('response'), kwargs.get('kwassert')

        if kwargs.get('exec_text'):
            for item in kwargs.get('exec_text'):
                exec(item)
        else:
            assert_key, assert_value = kwassert.split('=')
            self.assertEqual(response.get(assert_key), assert_value)

    @test_case_runner
    @test_case_parse
    def test_POST指定查询某次历史答题记录(self, **kwargs):
        """ POST指定查询某次历史答题记录 接口测试case """
        response, kwassert = kwargs.get('response'), kwargs.get('kwassert')

        if kwargs.get('exec_text'):
            for item in kwargs.get('exec_text'):
                exec(item)
        else:
            assert_key, assert_value = kwassert.split('=')
            self.assertEqual(response.get(assert_key), assert_value)
