# -*-coding:utf-8 -*-
# File :run_test.py
# Author:George
# Date : 2019/10/26
# motto: Someone always give up while someone always try!
"""
    test case runner
"""
import sys
path = 'F:\\Appium\\Projects\\kyb_testPro\\'
path1 = 'F:\\Appium\\Projects\\kyb_testPro\\common\\'
path2 = 'F:\\Appium\\Projects\\kyb_testPro\\baseView\\'
path3 = 'F:\\Appium\\Projects\\kyb_testPro\\businessView\\'
path4 = 'F:\\Appium\\Projects\\kyb_testPro\\testCase\\'
path5 = 'F:\\Appium\\Projects\\kyb_testPro\\testRun\\'
# 在导入包之前就要先将项目路径添加到环境变量中，否则还是不能生效
sys.path.append(path)
sys.path.append(path1)
sys.path.append(path2)
sys.path.append(path3)
sys.path.append(path4)
sys.path.append(path5)


import unittest
from BSTestRunner import BSTestRunner
import time
from common.logging_handler import logging
import os
from common.toolkit import latest_report, send_mail_with_report


def test_case_run():
    """"""
    # get the dir of test case and test reports
    root_dir = os.path.dirname(os.path.dirname(__file__))

    # sys.path.append(root_dir)

    print(root_dir)
    testcase_dir = '/'.join((root_dir, 'testCase'))
    testrepots_dir = '/'.join((root_dir, 'reports'))
    print(testcase_dir)
    print(testrepots_dir)

    discovery = unittest.defaultTestLoader.discover(testcase_dir, pattern='test_login.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    report_name = testrepots_dir + '/' + now + 'test_report.html'

    with open(report_name, 'wb') as fw:
        runner = BSTestRunner(stream=fw, title='Kyb Test Report', description='Kyb Android kyb test report')
        logging.info("===start to run test case===")
        runner.run(discovery)
    report = latest_report(testrepots_dir)
    send_mail_with_report(report)


if __name__ == "__main__":
    test_case_run()
