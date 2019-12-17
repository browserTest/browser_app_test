from time import sleep

from base_function.base import Base
from browser.browser_element.Read import *

class ReadPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)


    # 阅读模式-点击小说三寸人间  --wmw
    def clickBook(self):
        if self.base.elementIsExit(READ_BOOK):
            self.base.clickByElement(READ_BOOK, "点击小说封面")
        else:
            self.assertFalse(READ_BOOK)

    # 阅读模式-点击开始阅读  --wmw
    def clickRead(self):
        if self.base.elementIsExit(READ):
            self.base.clickByElement(READ, "点击开始阅读")
        else:
            self.assertFalse(READ)

    # 阅读模式-点击章节  --wmw
    def clickChapter(self):
        if self.base.elementIsExit(READ_CATALOG):
            self.base.clickByElement(READ_CHAPTER, "点击章节")
        else:
            self.assertFalse(READ_CATALOG)

    # 阅读模式-立即开启  --wmw
    def clickOpen(self):
        if self.base.elementIsExit(READ_OPEN):
            self.base.clickByElement(READ_OPEN, "我知道了")
        else:
            self.assertFalse(READ_OPEN)

    # 阅读模式地址栏按钮  --wmw
    def clickReadButton(self):
        if self.base.elementIsExit(READ_BUTTON):
            self.base.clickByElement(READ_BUTTON, "地址栏阅读模式按钮")
            sleep(4)
        else:
            self.assertFalse(READ_BUTTON)


    # 点击工具面板电脑版  --wmw
    def clickComputerButton(self):
        if self.base.elementIsExit(COMPUTER):
            self.base.clickByElement(COMPUTER, "点击工具面板电脑版")
        else:
            self.assertFalse(COMPUTER)