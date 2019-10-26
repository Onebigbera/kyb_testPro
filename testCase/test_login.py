# -*-coding:utf-8 -*-
# File :test_login.py
# Author:George
# Date : 2019/10/26
# motto: Someone always give up while someone always try!
"""
    test login
    when we are debug our unittest test case we can use skip decorator to deal with it
"""
import unittest

from LoginView import LoginView
from logging_handler import logging
from myunit import StartEnd


class TestLogin(StartEnd):
    csv_file = '../data/user_account.csv'

    # @unittest.skip('skip')
    def test_login_george9527(self):
        logging.info("=====test login george9527=====")
        login_action = LoginView(self.driver)
        row = login_action.get_csv_data(self.csv_file, 1)
        login_action.login(row[0], row[1])
        self.assertEqual(login_action.check_login_status(), True)

    # @unittest.skip('skip')
    def test_login_6421(self):
        logging.info("=====test login george6421=====")
        login_action = LoginView(self.driver)
        row = login_action.get_csv_data(self.csv_file, 2)
        login_action.login(row[0], row[1])
        self.assertEqual(login_action.check_login_status(), True)

    # @unittest.skip('skip')
    def test_login_error(self):
        logging.info("=====test login with error account=====")
        login_action = LoginView(self.driver)
        row = login_action.get_csv_data(self.csv_file, 3)
        login_action.login(row[0], row[1])
        self.assertEqual(login_action.check_login_status(), False)


def main():
    test_login = TestLogin()
    test_login.test_login_george9527()


if __name__ == "__main__":
    # main()
    unittest.main()
