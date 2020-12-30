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
        logger.info('<=====开始执行登录成功用例======>')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get(mu.url)



    def test_mukelog(self):
        logger.info('登录成功')
        self.test_mukelogin=test_mukelogin(self.driver)
        self.test_mukelogin.test_mikulo(mu.login_success_data['user'],mu.login_success_data['paw'])
        self.cs = self.driver.find_element('xpath','//*[@id="login-area"]/ul/li[4]/a/span').text
        sleep(1)
        self.test_mukelogin.css(self.cs,'我的课程')



    @classmethod
    def tearDownClass(cls):
        # 后置：关闭浏览器
        cls.driver.quit()
        logger.info('<=======测试结束======>')





if __name__=="__main__":
    unittest.main() #执行用例#

