
from base_function.base import Base
from browser.browser_element.More import *



class MorePage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击网址导航页面中12个导航位置
    def clickDaoHang(self, element):
        '''
        :param element: 元素名称
        :return:
        '''
        if self.base.elementIsExit(element):
            self.base.clickByElement(element, "网址导航-》{}".format(element))
        else:
            self.base.assertFalse(element)

