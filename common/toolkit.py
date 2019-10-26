# -*-coding:utf-8 -*-
# File :toolkit.py
# Author:George
# Date : 2019/10/26
# motto: Someone always give up while someone always try!
"""
    common toolkit such as find the lase report and send the report to others
"""
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.logging_handler import logging


def send_mail(latest_report_path):
    """
    发送最近生成的测试报告
    :param latest_report_path:最近生成文件的路径
    :return:
    """
    fr = open(latest_report_path, "rb")
    mail_content = fr.read()
    fr.close()

    smtpServer = "smtp.163.com"

    account = "onebigbera@163.com"
    password = "george9527"

    sender = "onebigbera@163.com"
    receiver = "onebigbera@163.com"

    subject = "考研帮app自动化测试报告"
    msg = MIMEText(mail_content, "html", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = sender
    msg["To"] = receiver

    smtp = smtplib.SMTP_SSL(smtpServer, 465)
    smtp.helo(smtpServer)
    smtp.ehlo(smtpServer)
    smtp.login(account, password)
    try:
        logging.info("===开始发送邮件===")
        smtp.sendmail(sender, receiver, msg.as_string())
    except BaseException as e:
        logging.info(e)
    logging.info("===邮件发送完成===")


def send_mail_with_report(report_path):
    """

    :param report_path:
    :return:
    """
    smtpServer = "smtp.163.com"
    account = "onebigbera@163.com"
    password = "george9527"
    sender = "onebigbera@163.com"
    receiver = "onebigbera@163.com"

    # instantiation an mail object
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    content = "<html><h4>亲爱的领导:<br>  " \
              "您好，下面是app自动化测试报告，请查收！</br></h4><p><span>下面为app测试报告，请查看！</span></p" \
              "></html> "
    subject = '寒冷的季节，温暖的是人心 ^_^ !'
    message["Subject"] = Header(subject, 'utf-8')

    # attach the content
    message.attach(MIMEText(content, 'html', 'utf-8'))

    # instantiation attachment object
    html_path = report_path
    # get attachment stream
    attachment_1 = MIMEText(open(html_path).read(), 'base64', 'utf-8')

    # set property
    attachment_1['Content-Type'] = 'application/octet-stream'
    attachment_1['Content-Disposition'] = 'attachment; filename="report.html"'

    message.attach(attachment_1)

    smtp = smtplib.SMTP_SSL(smtpServer, 465)
    try:
        smtp.helo(smtpServer)
        smtp.ehlo(smtpServer)
        smtp.login(account, password)
    except BaseException as e:
        logging.info(e)

    try:
        print("Begin to send >>>")
        smtp.sendmail(sender, receiver, message.as_string())
        logging.info("Send finished...")
    except BaseException as e:
        logging.info(e)


def latest_report(report_dir):
    """
    在汇报目录下寻找最新的测试报告的函数
    :param report_dir:
    :return: 返回最近生成文件的路径
    """
    lists = os.listdir(report_dir)
    # lambda 函数返回的是report_dir目录下文件fn的创建时间 sort 函数中按照key=fn创建时间进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + "\\" + fn))
    logging.info("===最近生成的汇报文件为:%s===" % lists[-1])

    # 用 os.path.join()方法将最近生成文件的路径拼接起来
    file = os.path.join(report_dir, lists[-1])
    logging.info("最近生成的文件路径为: %s" % file)
    return file


def main():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    report_dir = '/'.join((root_dir, 'reports'))
    file = latest_report(report_dir)
    send_mail(file)
    # send_mail_with_report(file)


if __name__ == "__main__":
    main()
