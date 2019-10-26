# -*-coding:utf-8 -*-
# File :get_config.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    get config from yaml data
"""
import os
from appium import webdriver
import yaml
from logging_handler import logging


def get_driver():
    """
    :return: driver instance
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    print(base_dir)
    app_path = '/'.join([base_dir, 'app', 'kaoyan3.1.0.apk'])
    print(app_path)
    config_file = '/'.join([base_dir, 'config', 'desired_capability.yaml'])
    print(config_file)
    with open(config_file, 'r', encoding='utf-8') as f:
        config = yaml.load(f)
        desired_capability = {
            'platformName': config['platformName'],
            'deviceName': config['deviceName'],
            'app': config['app'],
            'appPackage': config['appPackage'],
            'appActivity': config['appActivity'],
            # to recover previous settings
            'noReset': config['noReset'],
            # to set unicode  if used chinese
            'unicodeKeyboard': config['unicodeKeyboard'],
            # reset keyboard
            'resetKeyboard': config['resetKeyboard']
        }

        url = 'http' + '://' + str(config['ip']) + ":" + str(config['port']) + '/wd/hub'
        logging.info("=====Begin to connect phone=====")
        driver = webdriver.Remote(url, desired_capability)
        logging.info("=====starting app,please wait=====")
        driver.implicitly_wait(3)
        logging.info("=====wait to page refresh=====")
        return driver


if __name__ == "__main__":
    get_driver()
