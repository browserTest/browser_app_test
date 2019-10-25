
from base_function.base import Base
from browser.browser_element.Home import *
from browser.browser_element.ShareElement import *
from browser.browser_element.ToolbarPanel import *


class SharePage(Base):

    def __init__(self, driver):
        self.base = Base(driver)


    """点击导航网站中的”安居客“，进入网站—————LCM"""
    def clickAnjuke(self):
        if self.base.clickByElementIdAndText(HOME_BUSINESS_ID):
            self.base.clickByElement(HOME_ANJUKE, '点击浏览器首页安居客网站')
        else:
            self.assertFalse(HOME_BUSINESS_ID)



    """点击网页链接进行分享————LCM"""
    def clickShare(self):
        # 点击分享按钮，调起分享面板
        self.base.clickByElement(SHARE_ID,'点击分享按钮')
        # 判断分享面板中的便签是否存在
        if self.base.elementIsExit(SHARE_PAGE):
            # 点击分享到便签应用
            self.base.clickByElement(SHARE_PAGE, '点击分享到便签')
        else:
            self.assertFalse(SHARE_PAGE)



    '''点击底部工具栏中的退出按钮————LCM'''
    def clickOut(self,packagename):
        self.base.clickByElement(HOME_MORE,'点击menu_more菜单')
        self.base.clickByElement(OUT,'点击工具面板中的退出，直接退出浏览器')

    '''点击权限弹框中的始终允许'''
    def clickAllow(self):
        self.base.clickByElement(ALLOW,'点击浏览器权限弹框始终允许')