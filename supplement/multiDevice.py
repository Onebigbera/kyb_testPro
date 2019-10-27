# -*-coding:utf-8 -*-
# File :multiDevice.py
# Author:George
# Date : 2019/10/27
# motto: Someone always give up while someone always try!
"""
    测试场景：
        连接以下2台设备，然后分别启动考研帮App
            设备1：127.0.0.1:62001
            设备2：127.0.0.1:62025
"""
from appium import webdriver
import yaml
from time import ctime
from kyb_test import KybTest

with open('desired_caps.yaml', 'r')as file:
    data = yaml.load(file)

devices_list = ['127.0.0.1:62001', '127.0.0.1:62025']


def appium_desired(udid, port):
    desired_caps = {
        'platformName': data['platformName'],
        'platformVersion': data['platformVersion'],
        'deviceName': data['deviceName'],
        'udid': udid, 'app': data['app'],
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'noReset': data['noReset']
    }

    print('appium port: %s start run %s at %s' % (port, udid, ctime()))
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)

    # 将每个driver机器的操作封装在appium_desired里面
    k = KybTest(driver)
    k.skip_update_guide()
    return driver


if __name__ == '__main__':
    appium_desired(devices_list[0], 4723)
    appium_desired(devices_list[1], 4725)
