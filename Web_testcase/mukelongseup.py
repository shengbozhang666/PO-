import unittest
from selenium import webdriver
from PO002.Web_page.mukelogin import test_mukelogin
from PO002.Web_data import muklo as mu
from PO002.Web_bage.logger import logger
from time import sleep
class Test_mukedenglu(unittest.TestCase):

    def css(self,c,e):
        if c==e:
            logger.info('通过')
        else:
            logger.info("失败")

    def setUp(cls):
        logger.info('<=====开始执行用例======>')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get(mu.url)
        cookies = cls.driver.get_cookies()
        print(f"main: cookies = {cookies}")
        cls.driver.delete_all_cookies()


    def test_mukelog(self):
        logger.info('登录成功')
        self.test_mukelogin=test_mukelogin(self.driver)
        self.test_mukelogin.test_mikulo(mu.login_success_data['user'],mu.login_success_data['paw'])
        self.cs = self.driver.find_element('xpath','//*[@id="login-area"]/ul/li[4]/a/span')
        sleep(1)
        Test_mukedenglu.css(self, self.cs,'我的课程')


    def test_mukelog1(self):
        logger.info('密码为空登录')
        self.test_mukelogin = test_mukelogin(self.driver)
        self.test_mukelogin.test_mikulo(mu.loginpawnull[0]['user'], mu.loginpawnull[0]['paw'])
        self.cs = self.driver.find_element('xpath', '//*[@id="signup-form"]/div[2]/p').text
        sleep(1)
        Test_mukedenglu.css(self,self.cs,mu.loginpawnull[0]['check'])


    def test_mukelog2(self):
        logger.info('账号为空登录')
        self.test_mukelogin = test_mukelogin(self.driver)
        self.test_mukelogin.test_mikulo(mu.loginusernull[0]['user'], mu.loginusernull[0]['paw'])
        self.cs = self.driver.find_element('xpath','//*[@id="signup-form"]/div[1]/p').text
        sleep(1)
        Test_mukedenglu.css(self, self.cs,mu.loginusernull[0]['check'])


    def test_mukelog3(self):
        logger.info('执行登录密码错误')
        self.test_mukelogin = test_mukelogin(self.driver)
        self.test_mukelogin.test_mikulo(mu.loginmimafa[0]['user'], mu.loginmimafa[0]['paw'])
        self.cs = self.driver.find_element('xpath','//*[@id="signin-globle-error"]').text
        logger.info('获取文本成功')
        sleep(1)
        Test_mukedenglu.css(self, self.cs,mu.loginmimafa[0]['check'])


    def test_mukelog4(self):
        logger.info('执行登录账号不存在错误')
        self.test_mukelogin = test_mukelogin(self.driver)
        self.test_mukelogin.test_mikulo(mu.loginzhanghfa[0]['user'], mu.loginzhanghfa[0]['paw'])
        sleep(1)
        self.cs = self.driver.find_element('xpath','//*[@id="signin-globle-error"]').text
        print(self.cs)
        logger.info('获取文本成功')
        sleep(1)
        Test_mukedenglu.css(self, self.cs,mu.loginzhanghfa[0]['check'])




    def tearDown(cls):
        # 后置：关闭浏览器
        # pass
        logger.info('<=======测试结束======>')
        cls.driver.quit()




