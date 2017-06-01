
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    active.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ray <liujinjia@testerlife.com>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/31 15:49:03 by ray               #+#    #+#              #
#    Updated: 2017/05/31 15:49:03 by ray              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from json import loads
from functools import update_wrapper
from . import use_http
from ...constructor.use_case_operation import UseCaseOperation


def test_case_runner(function):
    """ all test case runner wrapper """
    def wrap(*args):
        """ wrap """
        func_name = function.__qualname__.split('_')[-1]
        case_info = UseCaseOperation.query_test_case_info(func_name=func_name, type=0)
        if 'GET' in func_name or 'GET' not in func_name and 'POST' not in func_name:
            response = use_http.user_get_request_api(case_info.get('uri'), case_info.get('body'))
        else:
            response = use_http.user_post_reques_api(case_info.get('uri'), case_info.get('body'))
        if isinstance(response, str):
            response = loads(response)

        kwassert = case_info.get('kwassert')
        if len(kwassert.split('=')) > 2:
            data = kwassert.split('&')
            result = dict([(item.split('=')) for item in data])
            return function(*args, response=response, kwassert=result)
        return function(*args, response=response, kwassert=case_info.get('kwassert'))
    return update_wrapper(wrap, function)


def test_case_parse(function):
    """ test case reponse parse """
    def wrap(*args, **kwargs):
        """ parse wrap """
        response = kwargs.get('response')
        kwassert = kwargs.get('kwassert')
        exec_text = []

        if isinstance(kwassert, dict):
            for key, value in kwassert.items():
                text = ("self.assertEqual(response.get('{}'), '{}')".format(key, value))
                exec_text.append(text)
            return function(*args, response=response, exec_text=exec_text)
        return function(*args, response=response, kwassert=kwassert)
    return update_wrapper(wrap, function)
