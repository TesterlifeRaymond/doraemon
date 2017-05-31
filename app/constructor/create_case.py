# -*- coding: utf-8 -*-
"""
@ Version : ??
@ Author  : liujinjia
@ File    : create_case.py
@ Project : base_test
@ Create Time: 2017-05-19 17:26
"""
from os import listdir, remove

from ..config import config, message
from .use_case_operation import UseCaseOperation


class FileMeta:
    """ read file headers and content.txt """
    old_cases = listdir(config.CREATE_CASE_PATH)
    del_files = [remove(config.CREATE_CASE_PATH + item) for item in old_cases if item not in [
        '__init__.py', '__pycache__']]
    headers = open(config.CASE_HEADER_PATH, 'rb')
    content = open(config.CASE_CONTENT_PATH, 'rb')

    @classmethod
    def __close__(cls):
        """ close all files """
        cls.headers.close()
        cls.content.close()


class CreateCase:
    """ Automatic case generating metaclass """

    @classmethod
    def import_files_case_to_sqlite(cls):
        """ 将case_file文件中的全部数据导入sqlite """
        with open('case_file/case.txt', 'rb') as file:
            for item in file:
                item = item.decode()
                params = item.replace('\n', '').split('   ')
                params_dict = dict(
                    uri=params[0],
                    class_name=params[1],
                    func_name=params[2],
                    body=params[3],
                    kwassert=params[4]
                )
                query_info = UseCaseOperation.query_test_case_info(
                    uri=params_dict.get('uri'),
                    func_name=params_dict.get('func_name'),
                    type=0
                )

                if query_info.get('uri') == params_dict.get('uri') \
                        and query_info.get('func_name') == params_dict.get('func_name'):
                    return message.CASE_ALREADY_EXISTS
                UseCaseOperation.add_test_case(**params_dict)

    @classmethod
    def get_case_class_name(cls):
        """ get all class case class name """
        cls.import_files_case_to_sqlite()
        all_case_info = UseCaseOperation.query_test_case_info(type=0)
        class_enu = set()
        for value in all_case_info.values():
            if value.get('class_name'):
                class_enu.add(value.get('class_name'))
        return class_enu

    @classmethod
    def get_case_function_name(cls):
        """ Get all the function names under the same name """
        result = {}
        for class_name in cls.get_case_class_name():
            case_info = UseCaseOperation.query_test_case_info(
                class_name=class_name, type=0)
            if not isinstance(list(case_info.keys())[0], int):
                result.update({class_name: case_info.get('func_name')})
            else:
                case_name = [value.get('func_name')
                             for key, value in case_info.items()]
                result.update({class_name: case_name})
        return result

    @classmethod
    def create_unittest_files(cls):
        """ 通过 get_case_function_name 函数传递回来的class_name 和 function_name 批量生成测试用例文件 """
        headers = FileMeta.headers.read().decode()
        content = FileMeta.content.read().decode()

        for key, value in cls.get_case_function_name().items():
            if not isinstance(value, list):
                with open(
                    config.CREATE_CASE_PATH + 'test_' + key.lower() + '.py',
                    'w',
                    encoding='utf-8'
                ) as file:
                    file.write(headers.format(key, key))
                    file.write(content.format('test_' + value, value))

            else:
                with open(
                    config.CREATE_CASE_PATH + 'test_' + key.lower() + '.py',
                    'a',
                    encoding='utf-8'
                ) as file:
                    file.write(headers.format(key, key))
                    for item in value:
                        file.write(content.format('test_' + item, item))
        FileMeta.__close__()
        return dict(msg=message.CASE_CREATE_OVER, case_path=config.CREATE_CASE_PATH)
