import pytest
from base_function.base import Base
from browser.browser_element.ToolbarPanel import *
from base_function.driver import Driver
from browser.browser_element.PubElement import *
from browser.browser_element.MyCollection import *

class PersonalCenterPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击个人中心页--我的账号图标
    def clickFlymemeA(self):
        if self.base.elementIsExit(FLYME_ME_A):
            self.base.clickByElement(FLYME_ME_A, "我的账号图标")
        else:
            self.assertFalse(FLYME_ME_A)

    # 获取个人中心未登录文本
    def clickNotLoggedIn(self):
        return self.base.elementText(PERSONAL_CENTER_NOT_LOGGED_IN)