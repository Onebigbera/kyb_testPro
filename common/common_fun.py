# -*-coding:utf-8 -*-
# File :common_fun.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    Common class which inherit BaseView  use logging model to record it  basic action
"""
import csv
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from baseView.baseView import BaseView
from driver_handler import get_driver
from logging_handler import logging
import time


class Common(BaseView):
    """
    cancel_btn and skip btn
    """
    # element locator
    cancel_loc = (By.ID, 'android:id/button2')
    skip_loc = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    # advertise button
    wemedia_cacel = (By.ID, 'com.tal.kaoyan:id/view_wemedia_cacel')

    def check_cancelBtn(self):
        """
        if there is a update button cancel it then
        :return:
        """
        try:
            cancel_btn = self.find_element(*self.cancel_loc)
        except NoSuchElementException:
            logging.info("=====cancel button does not exist in page =====")
        else:
            cancel_btn.click()
            logging.info("=====Click Cancel btn====")

    def check_skipBtn(self):
        """
        to skip advertising
        :return:
        """
        try:
            skip_btn = self.find_element(*self.skip_loc)
        except NoSuchElementException:
            logging.info("=====skip button does not exist in page =====")
        else:
            skip_btn.click()
            logging.info("=====Click skip btn====")

    def get_screenSize(self):
        """
        get screen size (width, height)
        :return:
        """
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        return x, y

    def swipeLeft(self):
        """swipe left"""
        coordinate = self.get_screenSize()
        x1 = int(coordinate[0] * 0.9)
        y1 = int(coordinate[1] * 0.5)
        x2 = int(coordinate[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    @staticmethod
    def getTime():
        """get the stringify time"""
        time_now = time.strftime("%Y-%m-%d_%H_%M_%S")
        return time_now

    def getScreenShot(self, module):
        """Screen shot """
        time_now = self.getTime()
        root_dir = os.path.dirname(os.path.dirname(__file__))
        image_file = root_dir + '/screenshots/' + '{}_{}.png'.format(module, time_now)
        logging.info("=====Get {} screen shot=====".format(module))
        self.driver.get_screenshot_as_file(image_file)
        logging.info("======Screen shot end=====")

    def check_market_ad(self):
        """check advertisement"""
        logging.info("=====Check advertisement=====")
        try:
            element = self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info("=====Close market ad====")
            element.click()

    @staticmethod
    def get_csv_data(csv_file, line):
        """
        get specified line data from csv file
        :param csv_file: csv file path
        :param line: data line
        :return:
        """
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


def main():
    """
        test class Common, every time you finish your programming you should sure it stability
    """
    driver = get_driver()
    common = Common(driver)
    common.check_cancelBtn()
    common.swipeLeft()
    common.check_skipBtn()
    common.check_market_ad()
    # common.getScreenShot('launch')
    data_dir = r'F:\Appium\Projects\kyb_testPro\data\test_data.csv'
    print(common.get_csv_data(data_dir, 2))


if __name__ == "__main__":
    main()
