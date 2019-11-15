from base_function.base import Base
from browser.browser_element.NegativeScreen import *
from time import sleep


class NegativeScreenPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击负一屏添加按钮-LJX
    def clickAddTo(self, element):
        if self.base.elementIsExit(element):
            self.base.clickByElement(element, '浏览器负一屏的{}'.format(element))
        else:
            self.assertFalse(element)

    # 删除负一屏书签-LJX
    def deleteBookmark(self, element):
        if self.base.elementIsExit(element):
            self.base.long_clickByElement(element, '负一屏"{}"书签'.format(element), 1)
            self.assertFalse(element)
            self.base.clickByElement(DELETE_TEXT, '删除按钮')
            self.assertFalse(DELETE_TEXT)


