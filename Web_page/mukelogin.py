from POOOO_test.base1 import Base1
from time import sleep
from PO002.Web_bage.logger import MyLogging
lo=MyLogging('登录测试')
from PO002.Web_bage.logger import logger
class test_mukelogin(Base1.BasePage1):

    def css(self,c,e):
        if c==e:
            logger.info('通过')
            lo.info('通过')
        else:
            logger.info("失败")
            lo.info("失败")

    def test_mikulo(self,user,paw):
        lo.info('点击按钮')
        self.click(*self.lo)
        sleep(1)
        lo.info('输入姓名')
        self.input_text(user,*self.mukeuser)
        lo.info('输入账号')
        self.input_text(paw,*self.mukepaw)
        lo.info('点击登录')
        self.click(*self.mukebuttn)






