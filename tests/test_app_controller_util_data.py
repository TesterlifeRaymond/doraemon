
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_app_controller_util_data.py                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ray <liujinjia@testerlife.com>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/31 17:35:52 by ray               #+#    #+#              #
#    Updated: 2017/05/31 17:35:52 by ray              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
