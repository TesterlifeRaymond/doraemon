
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-20 08:10:44
# @FileName:  data.py
# @Project: base_test
# @Last Modified by:   jinjialiu
# @Last Modified time: 2017-05-20 10:59:04
"""
from requests import Session


class Base:
    """ 父类 """
    def __init__(self):
        """ init """
        self.session = Session()

    def request(self, method, uri, data, data_type=None):
        """ request active """
        if method in ['get', 'GET']:
            request = self.session.get(url=uri, params=data).json()
            return request
        if data_type == 'json':
            return self.session.post(url=uri, json=data).json()
        return self.session.post(url=uri, data=data).json()


class UserRequestData(Base):
    """ 获取用户请求信息 """
    def __init__(self):
        """ 初始化用户请求类 """
        Base.__init__(self)

    def user_get_request_api(self, uri, data):
        """ http get method """
        return self.request('get', uri + data, "")

    def user_post_reques_api(self, url, data, data_type=None):
        """ http post method """
        return self.request('post', url, data)
