# -*- coding: utf-8 -*-

""" 测试工具自动生成的case """

import unittest
from src.lib import Wraps


class TestJuheApi(unittest.TestCase):
    """这是TestJuheApi接口测试用例"""

    def setUp(self):
        """ test setup function """

    def tearDown(self):
        """ test case tearDown function """

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_post_methods(self, *args, **kwargs):
        """通过post方法请求聚合微信精选接口, 并拿到正确的返回结果"""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_get_methods(self, *args, **kwargs):
        """通过get方法请求聚合微信精选接口."""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_post_methods(self, *args, **kwargs):
        """通过post方法请求聚合微信精选接口, 并拿到正确的返回结果"""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_get_methods(self, *args, **kwargs):
        """通过get方法请求聚合微信精选接口."""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_post_methods(self, *args, **kwargs):
        """通过post方法请求聚合微信精选接口, 并拿到正确的返回结果"""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_get_methods(self, *args, **kwargs):
        """通过get方法请求聚合微信精选接口."""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_post_methods(self, *args, **kwargs):
        """通过post方法请求聚合微信精选接口, 并拿到正确的返回结果"""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_get_methods(self, *args, **kwargs):
        """通过get方法请求聚合微信精选接口."""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))
