# -*-coding:utf-8 -*-
# File :muti_appium_sync.py
# Author:George
# Date : 2019/10/27
# motto: Someone always give up while someone always try!
"""
    上面的案例还不是并发执行启动appium,因此我们需要使用多进程来实现并发启动。 同样需要引入multiprocessing多进程模块。
"""
import multiprocessing
import subprocess
from time import ctime


def appium_start(host, port):
    '''启动appium server'''

    bootstrap_port = str(port + 1)
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' --bootstrap-port ' + str(bootstrap_port)

    print('%s at %s' % (cmd, ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open('./appium_log/' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)


# 构建appium进程组
appium_process = []

# 加载appium进程
for i in range(2):
    host = '127.0.0.1'
    port = 4723 + 2 * i
    appium = multiprocessing.Process(target=appium_start, args=(host, port))
    appium_process.append(appium)

if __name__ == '__main__':
    # 并发启动appium服务
    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()
