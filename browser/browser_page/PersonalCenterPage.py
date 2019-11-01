import pytest
from base_function.base import Base
from browser.browser_element.ToolbarPanel import *
from base_function.driver import Driver
from browser.browser_element.PubElement import *
from browser.browser_element.MyCollection import *

class PersonalCenterPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击个人中心页--我的账号图标   ---wmw
    def clickFlymemeA(self):
        if self.base.elementIsExit(PERSONAL_CENTER_FLYME_ME_A):
            self.base.clickByElement(PERSONAL_CENTER_FLYME_ME_A, "我的账号图标")
        else:
            self.assertFalse(PERSONAL_CENTER_FLYME_ME_A)
