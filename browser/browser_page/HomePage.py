import pytest
from base_function.base import Base
from browser.browser_element.Home import *
from browser.browser_element.PubElement import *
from browser.browser_element.MyCollection import *



class HomePage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击导航栏中“更多”按钮
    def clickBusinessMore(self):
        if self.base.elementIsExit(HOME_BUSINESS_MORE_TEXT):
            self.base.clickByElementIdAndText(HOME_BUSINESS_ID, HOME_BUSINESS_MORE_TEXT, "导航栏-》更多")
        else:
            self.assertFalse(HOME_BUSINESS_MORE_TEXT)

    # 点击工具栏中more菜单
    def clickMore(self):
        if self.base.elementIsExit(HOME_MORE):
            self.base.clickByElement(HOME_MORE, '浏览器首页more菜单')
        else:
            self.assertFalse(HOME_MORE)

    # 点击工具栏中home菜单
    def clickHome(self):
        if self.base.elementIsExit(HOME_HOME):
            self.base.clickByElement(HOME_HOME, '浏览器首页home菜单')
        else:
            self.assertFalse(HOME_HOME)


    # 根据传参确认是否需要点击home按钮
    def clickHomeOnPage(self, page):
        if page == HOME_PAGE and self.base.elementIsExit(COLLECTION_FOLDER):
            self.clickHome()
        elif page == MYCOLLECTION and self.base.elementIsExit(HOME_CAMERA):
            self.clickHome()
        else:
            pass

    # 点击首页搜索框——LYX
    def clickHomeSearch(self):
        if self.base.elementIsExit(HOME_SEARCH):
            self.base.clickByElement(HOME_SEARCH,'首页搜索框')
        else:
            self.assertFalse(HOME_SEARCH)