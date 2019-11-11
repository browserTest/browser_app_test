import pytest
from base_function.base import Base
from browser.browser_element.SetUp import *
from base_function.driver import Driver
from browser.browser_element.PubElement import *
from browser.browser_element.MyCollection import *
from browser.browser_element.SearchPanel import *

class SetUpPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击魅族头条设置   ---wmw
    def clickMeizuHeadlinesSettings(self,instance):
        if self.base.elementIsExit(SETUP_ID):
            self.base.clickByElementIdAndInstance(SETUP_ID, "魅族头条设置",instance)
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
    def clickClearCoolkies(self,instance):
        if self.base.elementIsExit(SETUP_ID):
            self.base.clickByElementIdAndInstance(SETUP_ID, "清除浏览数据",instance)
        else:
            self.assertFalse(SETUP_ID)

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
    def clickSearchEngine(self,instance):
        if self.base.elementIsExit(SETUP_ID):
            self.base.clickByElementIdAndInstance(SETUP_ID, "搜索引擎",instance)
        else:
            self.assertFalse(SETUP_ID)

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
    def clickBlockAds(self,instance):
        if self.base.elementIsExit(SETUP_ID):
            self.base.clickByElementIdAndInstance(SETUP_ID, "广告屏蔽",instance)
        else:
            self.assertFalse(SETUP_ID)

    # 点击恢复默认设置   ---wmw
    def clickResetToDefault(self,instance):
        if self.base.elementIsExit(SETUP_ID):
            self.base.clickByElementIdAndInstance(SETUP_ID, "恢复默认设置",instance)
        else:
            self.assertFalse(SETUP_ID)


    # 点击恢复默认设置---恢复    --wmw
    def clickReset(self):
        if self.base.elementIsExit(SETUP_RESET):
            self.base.clickByElement(SETUP_RESET, "恢复")
        else:
            self.assertFalse(SETUP_RESET)

    # 获取开关状态    ---wmw
    def clickSwitch(self):
        return self.base.elementText(SETUP_SWITCH, "开关状态")

    # 点击精选内容推送  ---wmw
    def clickSwipeLeftRight(self,instance):
        if self.base.elementIsExit(SETUP_ID):
            self.base.clickByElementIdAndInstance(SETUP_ID, "精选内容推送",instance)
        else:
            self.assertFalse(SETUP_ID)

    # 点击锁定竖屏   ---wmw
    def clickLockingVerticalScreen(self,instance):
        if self.base.elementIsExit(SETUP_ID):
            self.base.clickByElementIdAndInstance(SETUP_ID, "锁定竖屏",instance)
        else:
            self.assertFalse(SETUP_ID)

    # 点击允许   ---wmw
    def clickAllow(self):
        if self.base.elementIsExit(SETUP_ALLOW):
            self.base.clickByElement(SETUP_ALLOW, "允许")
        else:
            self.assertFalse(SETUP_ALLOW)