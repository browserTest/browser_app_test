from base_function.base import Base
from browser.browser_element.NegativeScreen import *
from time import sleep


class NegativeScreenPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击负一屏添加按钮-LJX
    def clickAddTo(self):
        if self.base.elementIsExit(NAGATIVE_SCREEN_ADD_TEXT):
            self.base.clickByElement(NAGATIVE_SCREEN_ADD_TEXT, '浏览器负一屏添加按钮')
        else:
            self.assertFalse(NAGATIVE_SCREEN_ADD_TEXT)

    # 删除负一屏书签-LJX
    def deleteBookmark(self, element):
        if self.base.elementIsExit(element):
            self.base.long_clickByElement(element, '负一屏"{}"书签'.format(element), 1)
            self.assertFalse(element)
            self.base.clickByElement(DELETE_TEXT, '删除按钮')
            self.assertFalse(DELETE_TEXT)


