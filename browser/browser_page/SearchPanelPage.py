import pytest
from base_function.base import Base
from browser.browser_element.SearchPanel import *
from base_function.driver import Driver
from browser.browser_element.PubElement import *
from browser.browser_element.MyCollection import *

class SearchPanelPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击搜索历史热词(默认点击第一个)   ---wmw
    def clickSearchHistory(self):
        if self.base.elementIsExit(SEARCHPANEL_SEARCHHISTORY):
            self.base.clickByElement(SEARCHPANEL_SEARCHHISTORY, "搜索历史热词")
        else:
            self.assertFalse(SEARCHPANEL_SEARCHHISTORY)

    # 点击换一换   ---wmw
    def clickAnotherChange(self):
        if self.base.elementIsExit(SEARCHPANEL_ANOTHERCHANGE):
            self.base.clickByElement(SEARCHPANEL_ANOTHERCHANGE, "换一换")
        else:
            self.assertFalse(SEARCHPANEL_ANOTHERCHANGE)

    # 点击输入框工具条前缀词“www.”——LYX
    def clickInputPanelPrefixes(self):
        if self.base.elementIsExit(INPUTPANEL_PROMPT):
            self.base.clickByElement(INPUTPANEL_PROMPT, "输入框前缀词www.")
        else:
            self.assertFalse(INPUTPANEL_PROMPT)

    # 长按地址栏中的“www.”——LYX
    def long_clickSearchPanel(self):
        if self.base.elementIsExit(SEARCHPANEL_WEBSITE):
            self.base.long_clickByElement(SEARCHPANEL_WEBSITE, "地址栏文字www")
        else:
            self.assertFalse(SEARCHPANEL_WEBSITE)

    # 拖动输入框中的工具条——LYX
    def swipe_InputPanel(self):
        if self.base.elementIsExit(INPUTPANEL_SWIPE):
            self.base.swipeByElement(INPUTPANEL_SWIPE, "left","向左拖动工具条",200)
        else:
            self.assertFalse(INPUTPANEL_SWIPE)


    # 获取第一个搜索热词    ---wmw
    def clickHotWords(self):
        return self.base.elementText(SEARCHPANEL_HOTWORDS, "第一个搜索热词")

    # 点击清空    ---wmw
    def clickEmpty(self):
        if self.base.elementIsExit(SEARCHPANEL_EMPTY):
            self.base.clickByElement(SEARCHPANEL_EMPTY, "清空")
        else:
            self.assertFalse(SEARCHPANEL_EMPTY)

    # 点击搜索框——LYX
    def clickSearchPanel(self):
        if self.base.elementIsExit(SEARCHPANEL_WEBSITE):
            self.base.clickByElement(SEARCHPANEL_WEBSITE, "搜索框")
        else:
            self.assertFalse(SEARCHPANEL_WEBSITE)

    # 点击搜索框联想词——LYX
    def clickAutomatedWord(self):
        if self.base.elementIsExit(AUTOMATED_WORD):
            self.base.clickByElement(AUTOMATED_WORD, "搜索框联想词")
        else:
            self.assertFalse(AUTOMATED_WORD)

    # 点击地址栏清空按钮——LYX
    def clearSearchPanel(self):
        if self.base.elementIsExit(SEARCHPANEL_CLEAR):
            self.base.clickByElement(SEARCHPANEL_CLEAR, "地址栏清空按钮")
        else:
            self.assertFalse(SEARCHPANEL_CLEAR)

    # 点击清空搜索历史——LYX
    def clearSearchHistory(self):
        if self.base.elementIsExit(CLEARSEARCHHISTORY):
            self.base.clickByElement(CLEARSEARCHHISTORY, "地址栏清空按钮")
        else:
            self.assertFalse(CLEARSEARCHHISTORY)

    # 地址栏输入百度——LYX
    def inputBaidu(self):
        if self.base.elementIsExit(SEARCHPANEL_WEBSITE):
            self.base.elementSetText(SEARCHPANEL_WEBSITE, "m.baidu.com","百度网址")
        else:
            self.assertFalse(SEARCHPANEL_WEBSITE)

    # 点击搜索框右侧的搜索/进入按钮——LYX
    def clickSearchInto(self):
        if self.base.elementIsExit(SEARCHPANEL_OPEN):
            self.base.clickByElement(SEARCHPANEL_OPEN,"搜索框右侧进入按钮")
        else:
            self.assertFalse(SEARCHPANEL_OPEN)

    # 搜索框输入m.80txt.com  --wmw
    def inputNumber(self):
        if self.base.elementIsExit(SEARCHPANEL_TEXT):
            self.base.elementSetText(SEARCHPANEL_TEXT, "m.80txt.com" ,"搜索框输入m.80txt.com")
        else:
            self.assertFalse(SEARCHPANEL_TEXT)

    # 滑动百度页面——LYX
    def swipeBaidu(self):
        if self.base.elementIsExit(BAIDU_LOGO):
            self.base.swipeByElement(BAIDU_LOGO,'up','滑动百度页面')
        else:
            self.assertFalse(BAIDU_LOGO)

    # 点击搜索框——LYX
    def clickwebsite(self):
        if self.base.elementIsExit(WEBSITE_PACKUP):
            self.base.clickByElement(WEBSITE_PACKUP, "百度页面收起的地址栏")
        else:
            self.assertFalse(WEBSITE_PACKUP)

    # 长按搜索历史中的百度网址——LYX
    def long_clickSearchHistory(self):
        if self.base.elementIsExit(BAIDU_WEBSITE):
            self.base.long_clickByElement(BAIDU_WEBSITE, "搜索历史中的百度网址")
        else:
            self.assertFalse(BAIDU_WEBSITE)

    # 点击搜索历史中的删除按钮——LYX
    def delete_SearchHistory(self):
        if self.base.elementIsExit(DELETESEARCHHISTORY):
            self.base.clickByElement(DELETESEARCHHISTORY,"搜索历史中的删除按钮")
        else:
            self.base.assertFalse(DELETESEARCHHISTORY)

