import pytest
from base_function.base import Base
from browser.browser_element.Home import *
from browser.browser_element.PubElement import *
from browser.browser_element.CollectionAndHistory import *
from browser.browser_element.NegativeScreen import *
from time import sleep


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
        if page == HOME_PAGE and self.base.elementIsExit(SAVED_PAGE):
            self.clickHome()
        elif page == MYCOLLECTION and self.base.elementIsExit(ARTICLE_ID):
            self.clickHome()
        else:
            pass

    # 点击首页搜索框——LYX
    def clickHomeSearch(self):
        if self.base.elementIsExit(HOME_SEARCH):
            self.base.clickByElement(HOME_SEARCH,'首页搜索框')
        else:
            self.assertFalse(HOME_SEARCH)

    # 点击资讯information   ----wmw
    def clickInformation(self):
        if self.base.elementIsExit(HOME_INFORMATION):
            self.base.clickByElement(HOME_INFORMATION,'资讯')
        else:
            self.assertFalse(HOME_INFORMATION)

    # 点击资讯广告   ----wmw
    def clickAdvertisement(self):
        if self.base.elementIsExit(HOME_ADVERTISEMENT):
            self.base.clickByElement(HOME_ADVERTISEMENT,'资讯流广告')
        else:
            self.assertFalse(HOME_ADVERTISEMENT)

    # 点击安居客首页新房入口——LYX
    def clickNewHouse(self):
        if self.base.elementIsExit(NEWHOUSE):
            self.base.clickByElement(NEWHOUSE,'安居客首页新房入口')
        else:
            self.assertFalse(NEWHOUSE)

    # 从屏幕边缘右滑手势后退——LYX
    def right_swipe(self):
        sleep(1)
        self.base.swipeByElement(RIGHTSWIPE_COORDINATE,"屏幕边缘右滑")

    # 从屏幕边缘左滑手势前进——LYX
    def left_swipe(self):
        sleep(1)
        self.base.swipeByElement(LEFTSWIPE_COORDINATE,"屏幕边缘左滑")

    # 提取首页12个导航位的名称——LYX
    def get_HomeBusiness(self):
        HOME_BUSINESS_NAME = []
        for i in range(12):
            text = self.base.elementText(HOME_BUSINESS_ID,"首页导航栏",i)
            HOME_BUSINESS_NAME.append(text)
        return HOME_BUSINESS_NAME

    # 点击安居客首页新房入口——LYX
    def clickNewHouse(self):
        if self.base.elementIsExit(NEWHOUSE):
            self.base.clickByElement(NEWHOUSE,'安居客首页新房入口')
        else:
            self.assertFalse(NEWHOUSE)

    # 点击小说精选页的推荐小说——LYX
    def clickTv_Novel(self):
        if self.base.elementIsExit(TV_NOVEL):
            self.base.clickByElement(TV_NOVEL,'小说详情页的推荐小说')
        else:
            self.assertFalse(TV_NOVEL)

    # 点击小说详情页的免费阅读——LYX
    def clickFreeRead(self):
        if self.base.elementIsExit(FREE_READ):
            self.base.clickByElement(FREE_READ,'小说详情页的免费阅读')
        else:
            self.assertFalse(FREE_READ)

