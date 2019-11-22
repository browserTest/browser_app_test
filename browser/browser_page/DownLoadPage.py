
from base_function.base import Base
from browser.browser_element.DownLoadElement import *
from browser.browser_element.SearchPanel import *


class DownPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 长按下载网页
    def longLink(self):
        if self.base.elementIsExit(SEARCH_PAGE_REFRASH):
            self.base.long_clickByElement(LONG_SEARCH_PAGR_LINK,'长按搜索结果页网页链接')
        else:
            self.assertFalse(SEARCH_PAGE_REFRASH)

    # 点击长按弹框中的“下载链接”按钮
    def clickDownLink(self):
        if self.base.elementIsExit(LONG_PRESS_BOX):
            self.base.clickByElement(DOWNLINK,'点击长按菜单弹框中的“下载链接”按钮')
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

    # 长按下载管理页面中的文件————LCM
    def longPressElement(self):
        if self.base.elementIsExit(DOWN_LOAD_MANAGE_TITLE):
            if self.base.elementIsExit(DOWN_LOAD_MANAGE_TITLE):
                self.base.long_clickByElement(DOWN_LOAD_MANAGE_TITLE,'长按下载管理页面中的文件')
            else:
                self.assertFalse(DOWN_LOAD_MANAGE_TITLE)
        else:
            self.base.usePhone('back')

    # 点击操作下载管理页面中的文件————LCM
    def clickChoose(self):
        # 判断“全选”按钮存在，则点击全选
        if self.base.elementIsExit(DOWN_LOAD_MANAGE_CHOOSE):
            self.base.clickByElement(DOWN_LOAD_MANAGE_CHOOSE,'选择下载管理页面中的文件')
            self.clickDeleteAllFile()
        # 判断“全不选”按钮存在，则点击“删除”
        elif self.base.elementIsExit(DOWN_LOAD_MANAGE_CHOOSEONE):
            self.clickDeleteAllFile()
        else:
            self.assertFalse(DOWN_LOAD_MANAGE_CHOOSE)


    # 下载管理页面中点击删除按钮————LCM
    def clickDeleteAllFile(self):
        if self.base.elementIsExit(DOWN_LOAD_MANAGE_RENAME):
            # 点击删除按钮
            self.base.clickByElement(DOWN_LOAD_MANAGE_DELETE_SELECTED, '点击删除按钮')
            self.clickDelete()
        else:
            self.assertFalse(DOWN_LOAD_MANAGE_RENAME)


    # 下载管理页面中点击删除所有的文件————LCM
    def clickDelete(self):
        if self.base.elementIsExit(DOWN_LOAD_MANAGE_DELETE):
            # 点击删除全部文件
            self.base.clickByElement(DOWN_LOAD_MANAGE_DELETE, '点击删除下载管理页面中的文件')
        else:
            self.assertFalse(DOWN_LOAD_MANAGE_DELETE_SELECTED)

