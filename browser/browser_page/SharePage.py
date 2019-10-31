
from base_function.base import Base
from browser.browser_element.Home import *
from browser.browser_element.ShareElement import *
from browser.browser_element.ZiXunInformationElement import *


class SharePage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击导航网站中的”安居客“，进入网站—————LCM
    def clickAnjuke(self):
        if self.base.clickByElementIdAndText(HOME_BUSINESS_ID):
            self.base.clickByElement(HOME_ANJUKE, '点击浏览器首页安居客网站')
        else:
            self.assertFalse(HOME_BUSINESS_ID)

    # 在网页中点击分享按钮————LCM
    def clickWebPageShare(self):
        # 点击分享按钮，调起分享面板
        if self.base.elementIsExit(SHARE_ID):
            self.base.clickByElement(SHARE_ID, '点击工具面板中的分享按钮')
        else:
            self.assertFalse(SHARE_ID)

    # 在资讯文章中点击分享按钮————LCM
    def clickZiXunPageShare(self):
        if self.base.elementIsExit(ZIXUN_PAGE_BACK):
            self.base.clickByElement(ZIXUN_SHARE_PAGR, '点击资讯文章详情页总的分享按钮')
        else:
            self.assertFalse(ZIXUN_PAGE_BACK)

    # 在分享面板中点击便签————LCM
    def clickNotes(self):
        # 判断分享面板中的便签是否存在
        if self.base.elementIsExit(SHARE_PAGE):
            # 点击分享到便签应用
            self.base.clickByElement(SHARE_PAGE, '点击分享到便签')
        else:
            self.assertFalse(SHARE_PAGE)

