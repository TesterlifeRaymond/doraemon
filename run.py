# -*- coding: utf-8 -*-
"""
@File: run
@Author: Ray
@: 2018-01-29 15:14:46
@Version: 1.0
"""
import click
import os
import unittest
from BeautifulReport import BeautifulReport
from src.lib import CreateCases

CREATE_CASES_FILE_STATUS = CreateCases.CreateCase()


@click.command()
@click.option('--cases', default='src/testcases/', help="case file path")
@click.option('--pattern', default='*.py', help="get cases file pattern")
@click.option('--report', default='src/report/', help="generator report in path")
def run(cases, pattern, report):
    test_suite = unittest.defaultTestLoader.discover(cases, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path=report)
    disfiles = os.listdir(cases)
    for file in disfiles:
        if os.path.isfile(cases + file):
            os.remove(cases + file)
    # 每次执行测试后 回收掉所有自动生成的测试文件


if __name__ == '__main__':
    run()
