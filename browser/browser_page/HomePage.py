import pytest
from base_function.base import Base
from browser.browser_element.Home import *
from browser.browser_element.PubElement import *
from browser.browser_element.MyCollection import *


class HomePage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击工具栏中more菜单
    def clickMore(self):
        if self.base.elementIsExit(HOME_MORE):
            self.base.clickByElement(HOME_MORE, 'more菜单')
        else:
            self.assertFalse(HOME_MORE)