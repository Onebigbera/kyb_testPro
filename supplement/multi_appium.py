# -*-coding:utf-8 -*-
# File :multi_appium.py
# Author:George
# Date : 2019/10/27
# motto: Someone always give up while someone always try!
"""
    使用Python脚本启动单个appium服务：
        host：127.0.0.1
        port：4723
    查看端口占用情况
    netstat -ano |findstr 端口号  || taskkill -f -pid appium进程id
    netstat -ano | grep 端口号  || kill -9 appium进程id
"""
import subprocess
from time import ctime


def appium_start(host, port):
    '''启动appium server'''
    bootstrap_port = str(port + 1)
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)

    print('%s at %s' % (cmd, ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open('./appium_log/' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)


# if __name__ == '__main__':
#     host = '127.0.0.1'
#     port = 4723
#     appium_start(host, port)

# 多个appium服务启动非常简单，只需在执行环境使用循环调用即可。
if __name__ == '__main__':
    host = '127.0.0.1'
    for i in range(2):
        port = 4723 + 2 * i
        appium_start(host, port)
