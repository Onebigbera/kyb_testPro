# -*-coding:utf-8 -*-
# File :kyb_test.py
# Author:George
# Date : 2019/10/27
# motto: Someone always give up while someone always try!
"""
    再上面的场景基础之上，并发启动设备后然后执行跳过引导页面操作。
"""
from selenium.common.exceptions import NoSuchElementException


class KybTest(object):
    def __init__(self,driver):
        self.driver=driver

    def check_cancelBtn(self):
        print('check cancelBtn')

        try:
            cancelBtn = self.driver.find_element_by_id('android:id/button2')
        except NoSuchElementException:
            print('no cancelBtn')
        else:
            cancelBtn.click()

    def check_skipBtn(self):
        print('check skipBtn')

        try:
            skipBtn = self.driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
        except NoSuchElementException:
            print('no skipBtn')
        else:
            skipBtn.click()

    def skip_update_guide(self):
        self.check_cancelBtn()
        self.check_skipBtn()