import pytest
from base_function.base import Base
from browser.browser_element.ToolbarPanel import *
from base_function.driver import Driver
from browser.browser_element.PubElement import *
from browser.browser_element.MyCollection import *

class ToolbarPanelPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击我的账号图标
    def clickFlymeme(self):
        if self.base.elementIsExit(FLYME_ME):
            self.base.clickByElement(FLYME_ME, "我的账号图标")
        else:
            self.assertFalse(FLYME_ME)