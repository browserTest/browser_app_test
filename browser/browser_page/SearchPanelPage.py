import pytest
from base_function.base import Base
from browser.browser_element.SearchPanel import *
from base_function.driver import Driver
from browser.browser_element.PubElement import *
from browser.browser_element.MyCollection import *

class SearchPanelPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击搜索按钮
    def clickSearch(self):
        if self.base.elementIsExit(SEARCHPANEL_SEARCH):
            self.base.clickByElement(SEARCHPANEL_SEARCH, "搜索")
        else:
            self.assertFalse(SEARCHPANEL_SEARCH)

    # 点击搜索历史热词(默认点击第一个)
    def clickSearchHistory(self):
        if self.base.elementIsExit(SEARCHPANEL_SEARCHHISTORY):
            self.base.clickByElement(SEARCHPANEL_SEARCHHISTORY, "搜索历史热词")
        else:
            self.assertFalse(SEARCHPANEL_SEARCHHISTORY)

    # 点击换一换
    def clickAnotherChange(self):
        if self.base.elementIsExit(SEARCHPANEL_ANOTHERCHANGE):
            self.base.clickByElement(SEARCHPANEL_ANOTHERCHANGE, "换一换")
        else:
            self.assertFalse(SEARCHPANEL_ANOTHERCHANGE)



    # 获取第一个搜索热词
    def clickHotWords(self):
        return self.base.elementText(SEARCHPANEL_HOTWORDS)

    # 点击清空
    def clickEmpty(self):
        if self.base.elementIsExit(SEARCHPANEL_EMPTY):
            self.base.clickByElement(SEARCHPANEL_EMPTY, "清空")
        else:
            self.assertFalse(SEARCHPANEL_EMPTY)

