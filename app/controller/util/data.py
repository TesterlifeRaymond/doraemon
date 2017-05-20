
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-20 08:10:44
# @FileName:  data.py
# @Project: base_test
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-21 07:28:59
"""
from json import loads
from requests import Session


class Base:
    """ 父类 """
    def __init__(self):
        """ init """
        self.session = Session()

    def request(self, method, uri, data, data_type=None):
        """ request active """
        if data is None or data is False or data == '' or data == 0 or data == "None":
            data = '{}'
        if method in ['get', 'GET']:
            request = self.session.get(url=uri, params=loads(data)).json()
            return request
        if data_type == 'json':
            return self.session.post(url=uri, json=loads(data)).json()
        return self.session.post(url=uri, data=loads(data)).json()


class UserRequestData(Base):
    """ 获取用户请求信息 """
    def __init__(self):
        """ 初始化用户请求类 """
        Base.__init__(self)

    def user_get_request_api(self, uri, data):
        """ http get method """
        return self.request('get', uri, data)

    def user_post_reques_api(self, url, data, data_type=None):
        """ http post method """
        return self.request('post', url, data, data_type)
