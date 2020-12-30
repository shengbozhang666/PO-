import unittest
from selenium import webdriver
from PO002.Web_page.mukesch import sous
from PO002.Web_data import mukes as mu
from PO002.Web_bage.logger import logger
from time import sleep
from ddt import ddt,data,unpack,file_data

@ddt()
class test_sousou(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info('<=====开始执行搜索用例======>')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get(mu.url)
        cls.s = sous(cls.driver)
        cls.s.test_sch('进入搜索页面')

    @data(*mu.su)
    def test_s(self,data):
        self.s=sous(self.driver)
        self.s.test_sch2(data['gjzi'])
        self.cs = self.driver.find_element_by_xpath(data['yuansu']).text
        sleep(1)
        self.s.css(self.cs,data['check'])


    @classmethod
    def tearDownClass(cls):
        # 后置：关闭浏览器
        cls.driver.quit()
        logger.info('<=======测试结束======>')



if __name__=="__main__":
    unittest.main() #执行用例#