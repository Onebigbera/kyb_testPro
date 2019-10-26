# -*-coding:utf-8 -*-
# File :baseView.py
# Author:George
# Date : 2019/10/25
# motto: Someone always give up while someone always try!
"""
    BaseView class
"""


class BaseView(object):
    """BaseView"""

    def __init__(self, driver):
        """
        return driver instance
        :param driver:
        """
        self.driver = driver

    def find_element(self, *loc):
        """locate element with locator"""
        return self.driver.find_element(*loc)

    def get_window_size(self):
        """get window size"""
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        """swipe basic action"""
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)
