# -*- coding: utf-8 -*-

""" 测试工具自动生成的case """

import unittest
from app.controller.util.active import test_case_runner, test_case_parse


class 登陆接口测试(unittest.TestCase):
    """这是登陆接口测试接口测试用例"""

    def setUp(self):
        """ test setup function """

    def tearDown(self):
        """ test case tearDown function """

    @test_case_runner
    @test_case_parse
    def test_POST错误的登陆参数(self, **kwargs):
        """ POST错误的登陆参数 接口测试case """
        response, kwassert = kwargs.get('response'), kwargs.get('kwassert')

        if kwargs.get('exec_text'):
            for item in kwargs.get('exec_text'):
                exec(item)
        else:
            assert_key, assert_value = kwassert.split('=')
            self.assertEqual(response.get(assert_key), assert_value)

    @test_case_runner
    @test_case_parse
    def test_POST正确的登陆参数(self, **kwargs):
        """ POST正确的登陆参数 接口测试case """
        response, kwassert = kwargs.get('response'), kwargs.get('kwassert')

        if kwargs.get('exec_text'):
            for item in kwargs.get('exec_text'):
                exec(item)
        else:
            assert_key, assert_value = kwassert.split('=')
            self.assertEqual(response.get(assert_key), assert_value)
