from base_function.base import Base
from browser.browser_element.NegativeScreen import *


class NegativeScreenPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击负一屏添加按钮
    def clickAddTo(self):
        if self.base.elementIsExit(NAGATIVE_SCREEN_ADD_TEXT):
            self.base.clickByElement(NAGATIVE_SCREEN_ADD_TEXT, '浏览器负一屏添加按钮')
        else:
            self.assertFalse(NAGATIVE_SCREEN_ADD_TEXT)

