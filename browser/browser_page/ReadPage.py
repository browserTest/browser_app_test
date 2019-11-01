from base_function.base import Base
from browser.browser_element.Read import *

class ReadPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)


    # 阅读模式-点击小说三寸人间  --wmw
    def clickSCRJ(self):
        if self.base.elementIsExit(SEARCHPANEL_SCRJ):
            self.base.clickByElement(SEARCHPANEL_SCRJ, "点击小说三寸人间")
        else:
            self.assertFalse(SEARCHPANEL_SCRJ)

    # 阅读模式-点击开始阅读  --wmw
    def clickRead(self):
        if self.base.elementIsExit(SEARCHPANEL_READ):
            self.base.clickByElement(SEARCHPANEL_READ, "点击开始阅读")
        else:
            self.assertFalse(SEARCHPANEL_READ)

    # 阅读模式-点击章节--1、写在连载前  --wmw
    def clickChapter(self):
        if self.base.elementIsExit(SEARCHPANEL_CHAPTER):
            self.base.clickByElement(SEARCHPANEL_CHAPTER, "点击章节--1、写在连载前")
        else:
            self.assertFalse(SEARCHPANEL_CHAPTER)