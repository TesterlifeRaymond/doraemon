"""
@Version: 1.0
@Project: doraemon_recode
@Author: Raymond
@Data: 2018/1/31 上午11:49
@File: CaseManager.py
@License: MIT
"""
import os
import json
from .LogHandler import LogHandler
CASE_PATH = 'cases/'

logger = LogHandler(__name__)


class CasesManager:
    def __init__(self, path: str=None):
        self.datas = {}
        self.path = path
        if not self.path:
            self.path = CASE_PATH

    def get_all_cases(self) -> list:
        """
            返回cases 路径下全部case文件列表
        :return:
        """
        return os.listdir(self.path)

    def read_cases_json(self, file_name: str) -> str:
        """
            读取json中的case信息
        :return: json中的case信息
        """
        try:
            with open(self.path + file_name, encoding='utf-8') as file:
                return json.load(file)
        except Exception as err:
            logger.error("解析json 测试用例时出错, 出错文件: {}, 错误信息: {}".format(file_name, err))

    def make_cases_info(self) -> list:
        """
            构造完整的测试用例信息集合
        :return:
        """
        all_cases_enum = []
        for file in self.get_all_cases():
            class_name = file.split('.')[0].title().replace("_", '')
            all_cases_enum.append({class_name: self.read_cases_json(file)})
        return all_cases_enum


class CasesContainer:
    def __init__(self, body: dict):
        self.body = body

    def __repr__(self) -> str:
        return 'CasesContainer<{}:{}>'.format(
            self.body.get('class_name'),
            self.body.get('methods_name')
        )
