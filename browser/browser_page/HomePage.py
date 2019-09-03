import pytest
from base_function.base import Base
from browser.browser_element.Home import *
from browser.browser_element.PubElement import *
from browser.browser_element.MyCollection import *



class HomePage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击导航栏中“更多”按钮
    def clickBusinessMore(self):
        if self.base.elementIsExit(HOME_BUSINESS_MORE_TEXT):
            self.base.clickByElementIdAndText(HOME_BUSINESS_ID, HOME_BUSINESS_MORE_TEXT, "导航栏-》更多")
        else:
            self.assertFalse(HOME_BUSINESS_MORE_TEXT)

    # 点击工具栏中more菜单
    def clickMore(self):
        if self.base.elementIsExit(HOME_MORE):
            self.base.clickByElement(HOME_MORE, '浏览器首页more菜单')
        else:
            self.assertFalse(HOME_MORE)