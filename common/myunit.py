# -*-coding:utf-8 -*-
# File :myunit.py
# Author:George
# Date : 2019/10/26
# motto: Someone always give up while someone always try!
"""
    basic handler for setUP and tearDown
    instance a driver to launch app and close it
"""
import unittest
from driver_handler import get_driver
from logging_handler import logging
from time import sleep


class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info("=====setUp=====")
        self.driver = get_driver()

    def tearDown(self):
        logging.info("=====tearDown=====")
        sleep(5)
        self.driver.close_app()
