# -*- coding: utf-8 -*-

""" 测试工具自动生成的case """

import unittest
from app.controller.util.active import test_case_runner, test_case_parse


class 豆瓣(unittest.TestCase):
    """这是豆瓣接口测试用例"""

    def setUp(self):
        """ test setup function """

    def tearDown(self):
        """ test case tearDown function """

    @test_case_runner
    @test_case_parse
    def test_查询用户信息0(self, **kwargs):
        """ 查询用户信息0 接口测试case """
        response, kwassert = kwargs.get('response'), kwargs.get('kwassert')

        if kwargs.get('exec_text'):
            for item in kwargs.get('exec_text'):
                exec(item)
        else:
            assert_key, assert_value = kwassert.split('=')
            self.assertEqual(response.get(assert_key), assert_value)

    @test_case_runner
    @test_case_parse
    def test_查询用户信息1(self, **kwargs):
        """ 查询用户信息1 接口测试case """
        response, kwassert = kwargs.get('response'), kwargs.get('kwassert')

        if kwargs.get('exec_text'):
            for item in kwargs.get('exec_text'):
                exec(item)
        else:
            assert_key, assert_value = kwassert.split('=')
            self.assertEqual(response.get(assert_key), assert_value)

    @test_case_runner
    @test_case_parse
    def test_POST查询用户信息2(self, **kwargs):
        """ POST查询用户信息2 接口测试case """
        response, kwassert = kwargs.get('response'), kwargs.get('kwassert')

        if kwargs.get('exec_text'):
            for item in kwargs.get('exec_text'):
                exec(item)
        else:
            assert_key, assert_value = kwassert.split('=')
            self.assertEqual(response.get(assert_key), assert_value)
