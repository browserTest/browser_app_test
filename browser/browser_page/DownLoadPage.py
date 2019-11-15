
from base_function.base import Base
from browser.browser_element.DownLoadElement import *
from browser.browser_element.SearchPanel import *


class DownPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 长按下载网页
    def longLink(self):
        if self.base.elementIsExit(SEARCH_PAGE_REFRASH):
            # text = self.base.elementSetText(LONG_SEARCH_PAGR_LINK)
            self.base.long_clickByElement(LONG_SEARCH_PAGR_LINK,'长按搜索结果页网页链接')
        else:
            self.assertFalse(SEARCH_PAGE_REFRASH)


    # 点击长按弹框中的“下载链接”按钮
    def clickDownLink(self):
        if self.base.elementIsExit(LONG_PRESS_BOX):
            self.base.clickByElement(DOWNLINK,'点击弹框中的“下载链接”按钮')
        else:
            self.assertFalse(LONG_PRESS_BOX)

    # 点击下载弹框中的“下载”按钮
    def clickDownButton(self):
        if self.base.elementIsExit(DOWNLOAD_NAME):
            self.base.clickByElement(DOWN_LOAD,'点击下载弹框中的“下载”按钮')
        else:
            self.assertFalse(DOWNLOAD_NAME)

    # 点击下载弹框中的“取消”按钮
    def clickCancelButton(self):
        if self.base.elementIsExit(DOWNLOAD_NAME):
            self.base.clickByElement(DOWN_CANCEL,'点击下载弹框中的“取消”按钮')
        else:
            self.assertFalse(DOWNLOAD_NAME)

    # 地址栏输入“QQ应用”
    def inputApp(self):
        if self.base.elementIsExit(SEARCHPANEL_ANOTHERCHANGE):
            self.base.elementSetText(SEARCHPANEL_WEBSITE, APPNAME, "输入“QQ”")
        else:
            self.assertFalse(SEARCHPANEL_ANOTHERCHANGE)


    # 地址栏输入“QQ应用”
    def clickAppDown(self):
        if self.base.elementIsExit(QQDOWN):
            self.base.clickByElement(QQDOWN, "点击“高速下载”")
        else:
            self.assertFalse(QQDOWN)

    # 获取下载弹框中的标题内容————LCM
    def getDownTitle(self,element):
        if self.base.elementIsExit(element):
            return self.base.elementText(element,'获取下载弹框中的标题内容')
        else:
            self.assertFalse(element)

