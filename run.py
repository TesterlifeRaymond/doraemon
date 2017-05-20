"""
@ Version : ??
@ Author  : liujinjia
@ File    : run.py
@ Project : base_test
@ Create Time: 2017-05-19 15:54
"""
# from app.constructor.use_case_operation import UseCaseOperation
import unittest
import BSTestRunner
import time
from app.constructor.create_case import CreateCase
from app.constructor.use_case_operation import UseCaseOperation

case_path = CreateCase.create_unittest_files().get('case_path')
report_path = 'app/report/report.html'


def load_tests(loader, tests, pattern):
    """
    Discover and load all unit tests in all files named
    ``test_*.py`` in ./src/app/
    """
    suite = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py')
    # runner = xmlrunner.XMLTestRunner(output=report_path, elapsed_times=False)
    # runner.run(suite)
    with open(report_path, 'wb') as files:
        runner = BSTestRunner.BSTestRunner(
            files,
            title='TestReport_{0}'.format(int(time.time())),
            description=u'自动化生成用例测试'
        )
        runner.run(suite)


def main():
    """ main function """
    try:
        unittest.main()
    except TypeError:
        print(UseCaseOperation.clear_test_data())

if __name__ == '__main__':
    main()
