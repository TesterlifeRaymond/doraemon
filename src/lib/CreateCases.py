# -*- coding: utf-8 -*-
"""
@ Version : ??
@ Author  : liujinjia
@ File    : create_case.py
@ Project : base_test
@ Create Time: 2017-05-19 17:26
"""
import os
import json
import types
from .LogHandler import LogHandler
from ..config import config

logger = LogHandler(__name__)


class FileMeta(config.GetDictParam):
    """ read file headers and content.txt """

    def __init__(self):
        self.headers, self.content = None, None

    def __enter__(self):
        """
            context enter methods
        @param : value
        @return: TODO
        """
        self.headers = open(config.HEADERS_TEMPLATE_PATH, encoding='utf-8')
        self.head = self.headers.read()
        self.content = open(config.CONTENT_TEMPLATE_PATH, encoding='utf-8')
        self.cont = self.content.read()
        return self

    def make_headers(self, class_name: str, func_name, desc: str) -> None:
        """
            make test cases headers
        :return:
        """
        filepath = config.TESTCASES_PATH + class_name + '.py'
        if not os.path.exists(filepath):
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(self.head.format(class_name, class_name))

        with open(filepath, 'a', encoding='utf-8') as file:
            file.write(self.cont.format(func_name, desc))

    def generating_template(self) -> types.GeneratorType:
        """
            通过context manager管理上下文读写并关闭文件
        @param : value
        @return: TODO
        """
        tags = json.loads(repr(config.TestCaseLoader()))
        for item in tags:
            for class_name, body in item.items():
                if len(body) > 1:
                    for key, value in body.items():
                        func_name = key
                        desc = self.get_value(value, "desc")
                        body = value
                        yield config.CasesContainer({
                            "class_name": class_name,
                            "methods_name": func_name,
                            "desc": desc,
                            "body": body
                        }), self.make_headers
                else:
                    for func_name, _body in body.items():
                        yield config.CasesContainer({
                            "class_name": class_name,
                            "methods_name": func_name,
                            "desc": _body.get('desc'),
                            "body": _body
                        }), self.make_headers

    def __exit__(self, exc_type, exc_value, traceback):
        """ close all files """
        self.headers.close()
        self.content.close()


class CreateCase:
    """ Automatic case generating metaclass """
    data = []
    with FileMeta() as file:
        for item in file.generating_template():
            obj, func = item
            func(
                obj.body['class_name'],
                obj.body['methods_name'],
                obj.body['desc'])
            data.append(obj.body)

    def __iter__(self) -> iter:
        return iter(self.data)

    def __call__(self):
        return next(self.data)

    def __repr__(self) -> str:
        return json.dumps(self.data)
