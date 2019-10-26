# -*-coding:utf-8 -*-
# File :LoginView.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    LoginView    Business logic encapsulation
"""
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common_fun import Common
from driver_handler import get_driver
from logging_handler import logging


class LoginView(Common):
    # login loc
    username_loc = (By.CLASS_NAME, 'android.widget.EditText')
    password_loc = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    click_loc = (By.ID, 'com.tal.kaoyan:id/login_login_btn')
    into_loc = (By.ID, 'com.tal.kaoyan:id/task_no_task')

    # person_info loc
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    button_myself = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')

    # offline info loc
    commitBtn = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    # logout loc
    settingBtn = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButtonWraper')
    logoutBtn = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')
    tip_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    def login(self, username, password):
        self.check_cancelBtn()
        self.check_skipBtn()
        sleep(1)
        try:
            username_input = self.find_element(*self.username_loc)
        except NoSuchElementException:
            logging.info("=====account input does not exist in page =====")
        else:
            username_input.send_keys(username)
            logging.info("=====input username:{}====".format(username))

        try:
            password_input = self.find_element(*self.password_loc)
        except NoSuchElementException:
            logging.info("=====password input does not exist in page =====")
        else:
            password_input.send_keys(password)
            logging.info("=====input password:{}====".format(password))

        try:
            login_btn = self.find_element(*self.click_loc)
        except NoSuchElementException:
            logging.info("=====login btn does not exist in page =====")
        else:
            login_btn.click()
            logging.info("=====click to login====")
        try:
            into_btn = self.find_element(*self.into_loc)
        except NoSuchElementException:
            logging.info("=====into info does not exist in page =====")
        else:
            into_btn.click()
            logging.info("=====Welcome to kaoyanbang====")

    def check_account_alert(self):
        """check if there is user logoff info"""
        logging.info("=====check account logoff alert=====")
        try:
            element = self.driver.find_element(*self.commitBtn)
        except NoSuchElementException:
            pass
        else:
            logging.info("=====click commitBtn=====")
            element.click()

    def check_login_status(self):
        """check login status"""
        logging.info("=====check login status=====")

        self.check_market_ad()
        self.check_account_alert()

        try:

            self.driver.find_element(*self.button_myself).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('login Fail!')
            self.getScreenShot('login Fail')
            return False
        else:
            logging.info("=====login success=====")
            self.logout_action()
            return True

    def logout_action(self):
        """logout action"""
        try:
            element = self.driver.find_element(*self.settingBtn)
        except NoSuchElementException:
            pass
        else:
            logging.info("=====click setting button=====")
            element.click()

        try:
            element = self.driver.find_element(*self.logoutBtn)
        except NoSuchElementException:
            pass
        else:
            logging.info("=====click logout=====")
            element.click()

        try:
            element = self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            pass
        else:
            logging.info("=====click commit button=====")
            element.click()


def main():
    """test class LoginView"""
    driver = get_driver()
    login_action = LoginView(driver)
    account = ('george9527', 'george9527')
    login_action.login(account[0], account[1])
    print(login_action.check_login_status())


if __name__ == "__main__":
    main()
