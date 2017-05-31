
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-31 14:19:09
# @FileName:  test_app_controller_util_data.py
# @Project: doraemon
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-31 14:38:20
"""
from unittest import TestCase
from app.controller.util.data import UserRequestData


class TestUserRequestData(TestCase):
    """ test case class """

    def test_request_get_method(self):
        """ method is get """
        response = UserRequestData().user_get_request_api(
            'http://op.juhe.cn/onebox/news/words',
            '{"key": "e53c5f18346ba5e40309fdf7574ee25b", "dtype": ""}'
        )
        self.assertEqual(response.get('error_code'), 0)
        self.assertEqual(type(response), dict)

    def test_request_post_method(self):
        """ method is post """
        response = UserRequestData().user_get_request_api(
            'http://op.juhe.cn/onebox/news/words',
            '{"key": "e53c5f18346ba5e40309fdf7574ee25b", "dtype": ""}'
        )
        self.assertEqual(response.get('error_code'), 0)
        self.assertEqual(type(response), dict)
