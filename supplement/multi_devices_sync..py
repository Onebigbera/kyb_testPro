# -*-coding:utf-8 -*-
# File :multiprocessLauchAppium.py
# Author:George
# Date : 2019/10/27
# motto: Someone always give up while someone always try!
"""
    使用多进程实现同时启动多个appium服务
"""
from appium import webdriver
import yaml
from time import ctime
import multiprocessing

with open('desired_caps.yaml', 'r') as file:
    data = yaml.load(file)

devices_list = ['127.0.0.1:62001', '127.0.0.1:62025']


def appium_desired(udid, port):
    desired_caps = {
        'platformName': data['platformName'],
        'platformVersion': data['platformVersion'],
        'deviceName': data['deviceName'],
        'udid': udid,
        'app': data['app'],
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'noReset': data['noReset']
    }

    print('appium port:%s start run %s at %s' % (port, udid, ctime()))
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver


# 构建desired进程租
desired_process = []

# 加载desied进程
for i in range(len(devices_list)):
    port = 4723 + 2 * i
    # 实例化启动appium的进程
    desired = multiprocessing.Process(target=appium_desired, args=(devices_list[i], port))
    desired_process.append(desired)

if __name__ == '__main__':
    # 启动多设备执行测试
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()
    # [desired_item.start() for desired_item in desired_process]
    # [desired_item.join() for desired_item in desired_process]
