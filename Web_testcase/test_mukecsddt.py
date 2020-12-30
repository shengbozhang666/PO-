import unittest
from selenium import webdriver
from PO002.Web_page.mukelogin import test_mukelogin
from PO002.Web_data import muklo as mu
from PO002.Web_bage.logger import logger
from time import sleep
from ddt import ddt,data,unpack,file_data

@ddt
class Test_mukedenglu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info('<=====开始执行登录失败用例======>')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get(mu.url)


    @data(*mu.loginpawnull1)
    def test_mukelog1(self,data):
        logger.info('密码为空登录')
        self.test_mukelogin = test_mukelogin(self.driver)
        self.test_mukelogin.test_mikulo(data["user"], data["paw"])
        self.cs = self.driver.find_element_by_xpath(data['e']).text
        sleep(1)
        self.test_mukelogin.css(self.cs,data['check'])
        sleep(1)


    def tearDown(self):
        self.driver.refresh()
        logger.info('刷新页面')


    @classmethod
    def tearDownClass(cls):
        # 后置：关闭浏览器
        cls.driver.quit()
        logger.info('<=======测试结束======>')





if __name__=="__main__":
    unittest.main() #执行用例#

