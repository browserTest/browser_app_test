import pytest
from base_function.base import Base
from browser.browser_element.SetUp import *
from base_function.driver import Driver
from browser.browser_element.PubElement import *
from browser.browser_element.CollectionAndHistory import *
from browser.browser_element.SearchPanel import *

class SetUpPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击魅族头条设置   ---wmw
    def clickMeizuHeadlinesSettings(self):
        if self.base.elementIsExit(SETUP_ID):
            self.base.clickByElement(MEIZU_HEAD, "魅族头条设置")
        else:
            self.assertFalse(SETUP_ID)

    # 点击简版显示   ---wmw
    def clickSimple(self):
        if self.base.elementIsExit(SETUP_SIMPLE):
            self.base.clickByElement(SETUP_SIMPLE, "简版显示")
        else:
            self.assertFalse(SETUP_SIMPLE)


    # 点击简版显示--更多   ---wmw
    def clickSetUpMore(self):
        if self.base.elementIsExit(SETUP_MORE):
            self.base.clickByElement(SETUP_MORE, "简版显示--更多")
        else:
            self.assertFalse(SETUP_MORE)

    # 点击清除浏览数据   ---wmw
    def clickClearCoolkies(self):
        if self.base.elementIsExit(CLEAR_DATA):
            self.base.clickByElement(CLEAR_DATA, "清除浏览数据")
        else:
            self.assertFalse(CLEAR_DATA)

    # 点击清除浏览数据--Cookies    ---wmw
    def clickCookies(self):
        if self.base.elementIsExit(SETUP_COOKIES):
            self.base.clickByElement(SETUP_COOKIES, "Cookies")
        else:
            self.assertFalse(SETUP_COOKIES)

    # 点击清除浏览数据--账号密码    ---wmw
    def clickAccountsAndPasswords(self):
        if self.base.elementIsExit(SETUP_ACCOUNTS_AND_PASSWORDS):
            self.base.clickByElement(SETUP_ACCOUNTS_AND_PASSWORDS, "账号密码")
        else:
            self.assertFalse(SETUP_ACCOUNTS_AND_PASSWORDS)

    # 点击清除浏览数据--地理位置授权    ---wmw
    def clickLocationAccess(self):
        if self.base.elementIsExit(SETUP_LOCATION_ACCESS):
            self.base.clickByElement(SETUP_LOCATION_ACCESS, "地理位置授权")
        else:
            self.assertFalse(SETUP_LOCATION_ACCESS)

    # 点击清除浏览数据按钮    ---wmw
    def clickClearData(self):
        if self.base.elementIsExit(SETUP_CLEAR_DATA):
            self.base.clickByElement(SETUP_CLEAR_DATA, "清除数据按钮")
        else:
            self.assertFalse(SETUP_CLEAR_DATA)

    # 点击完成按钮    ---wmw
    def clickDone(self):
        if self.base.elementIsExit(SETUP_DONE):
            self.base.clickByElement(SETUP_DONE, "完成按钮")
        else:
            self.assertFalse(SETUP_DONE)

    # 点击搜索引擎   ---wmw
    def clickSearchEngine(self):
        if self.base.elementIsExit(SEARCH_ENGINE):
            self.base.clickByElement(SEARCH_ENGINE, "搜索引擎")
        else:
            self.assertFalse(SEARCH_ENGINE)

    # 点击百度   --wmw
    def clickBaidu(self):
        if self.base.elementIsExit(SETUP_BAIDU):
            self.base.clickByElement(SETUP_BAIDU, "百度")
        else:
            self.assertFalse(SETUP_BAIDU)

    #搜索框输入123  --wmw
    def inputNumber(self):
        if self.base.elementIsExit(SEARCHPANEL_TEXT):
            self.base.elementSetText(SEARCHPANEL_TEXT, "123","搜索框输入123")
        else:
            self.assertFalse(SEARCHPANEL_TEXT)

    # 搜索框输入百度  --wmw
    def inputbaidu(self):
        if self.base.elementIsExit(SEARCHPANEL_TEXT):
            self.base.elementSetText(SEARCHPANEL_TEXT,'www.baidu.com', "搜索框输入百度")
        else:
            self.assertFalse(SEARCHPANEL_TEXT)

    # 点击广告屏蔽   ---wmw
    def clickBlockAds(self,element):
        if self.base.elementIsExit(element):
            if self.obtainBlockAdsSwitch(element) == "关闭":
                return
            else:
                self.base.clickByElementRight(element, SETUP_SWITCH, direction='right')
        else:
            self.assertFalse(element)

    # 点击恢复默认设置   ---wmw
    def clickResetToDefault(self):
        if self.base.elementIsExit(SETUP_RESET_TEXT):
            self.base.clickByElement(SETUP_RESET_TEXT, "恢复默认设置")
        else:
            self.assertFalse(SETUP_RESET_TEXT)


    # 点击恢复默认设置---恢复    --wmw
    def clickReset(self):
        if self.base.elementIsExit(SETUP_RESET):
            self.base.clickByElement(SETUP_RESET, "恢复")
        else:
            self.assertFalse(SETUP_RESET)

    # # 获取广告屏蔽开关状态    ---wmw
    # def obtainBlockAdsSwitch(self):
    #     if self.base.elementIsExit(SETUP_ID):
    #         return self.base.elementText(SETUP_SWITCH, "开关状态",0)
    #     else:
    #         self.assertFalse(SETUP_ID)

    # 获取广告屏蔽开关状态    ---wmw
    def obtainBlockAdsSwitch(self, element):
        if self.base.elementIsExit(SETUP_ID):
            return self.base.ObtianRightelementText(element, SETUP_SWITCH, direction='right')
        else:
            self.assertFalse(SETUP_ID)

    # 获取精选内容推送开关状态    ---wmw
    def obtainSwipeLeftRightSwitch(self, element):
        if self.base.elementIsExit(SETUP_ID):
            return self.base.ObtianRightelementText(element, SETUP_SWITCH, direction='right')
        else:
            self.assertFalse(SETUP_ID)


    # # 获取精选内容推送开关状态    ---wmw
    # def obtainSwipeLeftRightSwitch(self):
    #     if self.base.elementIsExit(SETUP_ID):
    #         return self.base.elementText(SETUP_SWITCH, "开关状态",3)
    #     else:
    #         self.assertFalse(SETUP_ID)

    # 点击精选内容推送  ---wmw
    def clickSwipeLeftRight(self,element):
        if self.base.elementIsExit(element):
            if self.obtainSwipeLeftRightSwitch(element) == "关闭":
                return
            else:
                self.base.clickByElementRight(element, SETUP_SWITCH, direction='right')
        else:
            self.assertFalse(element)


    # 点击允许   ---wmw
    def clickAllow(self):
        if self.base.elementIsExit(SETUP_ALLOW):
            self.base.clickByElement(SETUP_ALLOW, "允许")
        else:
            self.assertFalse(SETUP_ALLOW)

    # 点击360 ————LCM
    def click360(self):
        if self.base.elementIsExit(SETUP_360):
            self.base.clickByElement(SETUP_360, "360")
        else:
            self.assertFalse(SETUP_360)
