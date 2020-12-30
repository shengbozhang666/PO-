#coding=utf-8
import unittest
from PO002.HTMLTestRunner import *
import time
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

case_path = r'C:\Users\ASUS\PycharmProjects\PO002\Web_testcase'
case_list = unittest.defaultTestLoader.discover(case_path,'test*.py')
report_path = r'C:\Users\ASUS\PycharmProjects\PO002\Web_Outputs'
now = time.strftime('%Y%m%d%H%M%S')  # 获取当前时间，是一个字符串
report_file = report_path+r'\%s_report.html' % now

with open(report_file,'wb') as f:
    runner = HTMLTestRunner(stream=f,title=u'ecshop项目自动化测试',description=u'测试环境：Windows 7 + Chrome 67')
    runner.run(case_list)

