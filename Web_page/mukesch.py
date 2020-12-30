from POOOO_test.base1 import Base1
from time import sleep
from PO002.Web_bage.logger import MyLogging
lo=MyLogging('搜索测试')
from PO002.Web_bage.logger import logger
class sous(Base1.BasePage1):

    def css(self, c, e):
        if c == e:
            logger.info('通过')
            lo.info('通过')
        else:
            logger.info("失败")
            lo.info('失败')

    def test_sch(self,so):
        lo.info('输入关键字搜索')
        self.input_text(so,*self.input)
        lo.info('点击搜索按钮进入搜索页面')
        self.click(*self.souann)
        sleep(1)


    def test_sch2(self,so):
        lo.info('清除输入框数据')
        self.clear_input(*self.input2)
        lo.info('输入关键字搜索')
        self.input_text(so,*self.input2)
        lo.info('点击搜索按钮')
        self.click(*self.souann2)
        sleep(1)




