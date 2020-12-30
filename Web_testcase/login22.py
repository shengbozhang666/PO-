from PO002.Web_page.huarunlogin import test_LoginPage
import  unittest
from selenium import webdriver
from PO002.Web_bage import logger
from POOOO_test.base1 import Base1
log=logger.Logger1()
from PO002.Web_data import huarunlo as du

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 前置：打开浏览器，登录网页
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://sale-test.saas.crland.com.cn/login')

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    def test_login_2_success(self):
        log.info("*********登录用例：正常场景-登录成功*********")
        # 步骤：登录页面-登录操作
        self.LoginPage=test_LoginPage(self.driver)
        self.LoginPage.test_login2(du.success_data['user'],du.success_data['pwd'])


    @classmethod
    def tearDownClass(cls):
        # 后置：关闭浏览器
        print('完成')
        cls.driver.quit()
