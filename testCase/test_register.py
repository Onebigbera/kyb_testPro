# -*-coding:utf-8 -*-
# File :test_register.py
# Author:George
# Date : 2019/10/26
# motto: Someone always give up while someone always try!
"""
    test register
"""
import random

from common.myunit import StartEnd
from businessView.registerView import RegisterView
from logging_handler import logging
import unittest
from driver_handler import get_driver


class RegisterTest(StartEnd):
    """
    test register
    """

    def test_user_register(self):
        logging.info("=====test_user_register=====")
        register = RegisterView(self.driver)

        username = 'george' + str(random.randint(5000, 8000))
        password = 'password' + str(random.randint(5000, 8000))
        email = 'george' + str(random.randint(5000, 8000)) + '@qq.com'
        logging.info(register.register_action(username, password, email))
        # self.assertTrue(register.register_action(username, password, email))
        print(register.che_register_status())
        self.assertEqual(register.che_register_status(), True)


if __name__ == "__main__":
    # unittest.main()
    # rt = RegisterTest()
    # username = 'george' + str(random.randint(5000, 8000))
    # password = 'password' + str(random.randint(5000, 8000))
    # email = 'george' + str(random.randint(5000, 8000)) + '@qq.com'
    # rt.test_user_register(username, password, email)
    unittest.main()
