# -*-coding:utf-8 -*-
# File :check_port.py
# Author:George
# Date : 2019/10/27
# motto: Someone always give up while someone always try!
"""
    在使用命令启动appium时如果端口被占用，如果手动关闭是不是太Low，使用Python中的模块去自动检测并且关闭端口占用进程
"""
import os
import socket


def check_port(host, port):
    """检测端口是否被占用"""
    # 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        s.shutdown(2)
    except OSError as mes:
        print("{} is available!".format(port))
        print(mes)
        return True
    else:
        print('{} is already in use'.format(port))
        return False


def release_port(port):
    """释放指定的端口"""
    # 查找对应端口的pid
    cmd_find = 'netstat -aon | findstr %s' % port
    print(cmd_find)

    # 返回命令执行后的结果
    result = os.popen(cmd_find).read()
    print(result)

    if str(port) and 'LISTENING' in result:
        # 获取端口对应的pid进程
        i = result.index('LISTENING')
        # 从字符串中解析出进程号
        start = i + len('LISTENING') + 7
        end = result.index('\n')
        pid = result[start:end]

        # 关闭被占用端口的pid
        cmd_kill = 'taskkill -f -pid %s' % pid
        print(cmd_kill)
        os.popen(cmd_kill)

    else:
        print('port %s is available !' % port)


if __name__ == "__main__":
    host = '127.0.0.1'
    # port = 9999
    port = 4723
    check_port(host, port)
    release_port(4723)
