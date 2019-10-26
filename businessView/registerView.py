# -*-coding:utf-8 -*-
# File :registerAction.py
# Author:George
# Date : 2019/10/25
# motto: Someone always give up while someone always try!
"""
    Register
"""
import random

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common_fun import Common
from common.logging_handler import logging
from driver_handler import get_driver


class RegisterView(Common):
    """User register"""
    register_btn = (By.ID, 'com.tal.kaoyan:id/login_register_text')
    image_choose = (By.ID, "com.tal.kaoyan:id/activity_register_userheader")
    image = (By.ID, "com.tal.kaoyan:id/item_image")
    save_btn = (By.ID, 'com.tal.kaoyan:id/save')

    user_account = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    password = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    email = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    register_save = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')
    judge_ele = (By.ID, 'com.tal.kaoyan:id/myapptitle_Title')
    into_loc = (By.ID, 'com.tal.kaoyan:id/task_no_task')

    # person info set
    year_btn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_time')
    years = (By.ID, 'android:id/text1')
    school_choose_btn = (By.ID, 'com.tal.kaoyan:id/perfectinfomation_edit_school_name')
    school_choice = (By.ID, 'com.tal.kaoyan:id/more_forum_title')
    school_choose_btn_choice = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')
    majors = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')
    major_choices = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
    major_group = (By.ID, 'com.tal.kaoyan:id/major_group_title')
    major_choice = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')
    go_btn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

    # check login status
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    button_myself = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')

    def register_action(self, account, password, email):
        self.check_cancelBtn()
        self.check_skipBtn()
        self.driver.implicitly_wait(3)

        # click register button
        try:
            register_button = self.find_element(*self.register_btn)
        except NoSuchElementException:
            logging.info("=====Register button does not exist=====")
            pass
        else:
            register_button.click()
            self.driver.implicitly_wait(2)

        # click choose image button
        try:
            images_button = self.find_element(*self.image_choose)
        except NoSuchElementException:
            logging.info("=====Images choose element does not exists=====")
            pass
        else:
            images_button.click()
            self.driver.implicitly_wait(2)

        # choose images
        try:
            image = self.driver.find_elements(*self.image)[2]
        except NoSuchElementException:
            logging.info("=====Images choose element does not exists=====")
        else:
            image.click()
            logging.info("=====choose second img=====")

        # click sava button
        try:
            save_button = self.driver.find_element(*self.save_btn)
        except NoSuchElementException:
            logging.info("=====Save button does not exists=====")
        else:
            save_button.click()
            logging.info("=====save user image=====")
            self.driver.implicitly_wait(2)

        # user account password and email
        try:
            user_account = self.find_element(*self.user_account)
        except NoSuchElementException:
            logging.info("===User account input does not exist===")
            pass
        else:
            user_account.clear()
            user_account.send_keys(account)
            logging.info("===User account is: {}".format(account))

        try:
            user_password = self.find_element(*self.password)
        except NoSuchElementException:
            logging.info("===User password input does not exist===")
            pass
        else:
            user_password.clear()
            user_password.send_keys(password)
            logging.info("===User password is: {}".format(password))

        try:
            user_email = self.find_element(*self.email)
        except NoSuchElementException:
            logging.info("===User email input does not exist===")
            pass
        else:
            user_email.clear()
            user_email.send_keys(email)
            logging.info("===User email is: {}".format(email))

        try:
            register_save = self.find_element(*self.register_save)
        except NoSuchElementException:
            logging.info("===register save btn does not exist===")
            pass
        else:
            register_save.click()
            logging.info("===click to register===")

        # judge whether alarm info
        try:
            judge_ele = self.find_element(*self.judge_ele)
        except NoSuchElementException:
            logging.info("===register fail, register too many times===")
            pass
        else:
            logging.info("===register successful begin to perfect your information===")

        self.add_register_info()
        self.che_register_status()

    def add_register_info(self):
        """perform personal information"""
        try:
            year_btn = self.find_element(*self.year_btn)
            year_btn.click()
            logging.info("===click year choice btn===")

            years = self.driver.find_elements(*self.years)
            years[2].click()
            logging.info("===select second year===")

            school_choose_btn = self.find_element(*self.school_choose_btn)
            school_choose_btn.click()
            logging.info("===start to choose school===")

            school_choice = self.driver.find_elements(*self.school_choice)
            school_choice[1].click()
            logging.info("===choose school===")

            school_choose_btn_choice = self.driver.find_elements(*self.school_choose_btn_choice)
            school_choose_btn_choice[2].click()
            logging.info("===choose second school")

            majors = self.find_element(*self.majors)
            majors.click()
            logging.info("===start to choose your major===")

            major_choices = self.driver.find_elements(*self.major_choices)
            major_choices[3].click()
            logging.info("===choose the thirds university===")

            major_group = self.driver.find_elements(*self.major_group)
            major_group[2].click()
            logging.info("===choose the second major===")

            major_choice = self.driver.find_elements(*self.major_choice)
            major_choice[2].click()
            logging.info("===choose major finished===")

            go_btn = self.find_element(*self.go_btn)
            go_btn.click()
            logging.info("===finished perform your personal information")
        except NoSuchElementException as e:
            logging.info(e)
            pass
        try:
            into_btn = self.find_element(*self.into_loc)
        except NoSuchElementException:
            logging.info("=====into info does not exist in page =====")
        else:
            into_btn.click()
            logging.info("=====Welcome to kaoyanbang====")

    def che_register_status(self):
        """check whether to skip normally"""
        self.check_market_ad()
        logging.info("=====check register status=====")

        try:
            self.driver.find_element(*self.button_myself).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('register Fail!')
            self.getScreenShot('register_Fail')
            return False
        else:
            logging.info('register success!')
            self.getScreenShot('register_success')
            return True


def main():
    """
        when debug your programming every scene is special in context
        test Register View
    """
    driver = get_driver()
    register = RegisterView(driver)
    item = random.randint(8000, 9000)
    account = ('george' + str(item), 'password' + str(item), 'george' + str(item) + '@qq.com')
    register.register_action(account[0], account[1], account[2])
    print(register.che_register_status())


if __name__ == "__main__":
    main()
