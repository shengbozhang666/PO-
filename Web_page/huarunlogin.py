import  unittest

import yaml

from POOOO_test.base1 import Base1
from PO002.Web_bage import logger
log=logger.Logger1()
from time import sleep
from selenium import webdriver
from PO002.Web_data import huarunlo as du


#登录页面
class test_LoginPage(Base1.BasePage1):

    def test_login2(self,username,paswdrd):
        log.info("*********登录用例：正常场景-登录成功*********")
        self.input_text(username,*self.user)
        self.input_text(paswdrd, *self.paw)
        self.click(*self.search)  #




#
# #管理页面
# class test_GuanLi(Base1.BasePage1,unittest.TestCase):
#     def __init__(self, driver):
#         super().__init__(driver)
#     def test_Account(self):
#         sleep(2)
#         self.click(*self.acount)


# if __name__ == '__main__':
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     driver.get("https://sale-test.saas.crland.com.cn/login")
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     #登录-查询用户
#     LoginPage=test_LoginPage(driver)
#     LoginPage.login()
#     # GuanLi.Account()
#     driver.quit()
#     log.info('登录成功')
