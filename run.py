"""
@ Version : ??
@ Author  : liujinjia
@ File    : run.py
@ Project : base_test
@ Create Time: 2017-05-19 15:54
"""
# from app.constructor.use_case_operation import UseCaseOperation
import time
import unittest

from app.config import config
from app.constructor.create_case import CreateCase
from app.constructor.use_case_operation import UseCaseOperation
from app.controller.util import BSTestRunner
from app.controller.util.xtest import TestReport, dict_encode_test_results

case_path = CreateCase.create_unittest_files().get('case_path')
report_path = 'app/report/report.html'


def load_tests(loader, tests, pattern):
    """
    Discover and load all unit tests in all files named
    ``test_*.py`` in ./src/app/
    """
    start_time = time.time()  # 测试启动的时刻点
    suite = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py')
    if config.SWITCH:
        test_result = unittest.TextTestRunner().run(suite)  # 运行测试套件，并返回测试结果
        total_time = time.time() - start_time  # 测试过程整体的耗时
        test_res_dict = dict_encode_test_results(
            test_result,
            run_time=total_time,
            pro_version='1.0'  # 当前被测试的系统的版本号,依据目前系统的信息，如果服务端提供接口，则可以做成自动化的
        )
        test_report = TestReport()
        auth_res = test_report.get_api_auth()
        if auth_res:
            test_report.post_unit_test_data(test_res_dict)
        else:
            raise PermissionError('auth error...')
    else:
        with open(report_path, 'wb') as files:
            runner = BSTestRunner.BSTestRunner(
                files,
                title='TestReport_{0}'.format(int(time.time())),
                description=u'自动化生成用例测试'
            )
            runner.run(suite)

if __name__ == '__main__':
    try:
        unittest.main()
    except TypeError:
        UseCaseOperation.clear_test_data()
