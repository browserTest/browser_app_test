from asyncio import sleep

import pytest

from browser.browser_element.WindowsTabElement import *
from browser.browser_page.MorePage import *
from browser.browser_page.SharePage import *


class WindowsTabPage(Base):
    def __init__(self, driver):
        self.base = Base(driver)
        self.more = MorePage(driver)

    # 点击底部工具栏中的多窗口按钮
    def clickWindowsTab(self):
        if self.base.elementIsExit(WINDOWS_TAB_BUTTON):
            self.base.clickByElement(WINDOWS_TAB_BUTTON, '点击底部工具栏中的多窗口按钮，进入多窗口浏览Tab页面')
        else:
            self.assertFalse(WINDOWS_TAB_BUTTON)

    # 新建多窗口、滑动多窗口tab并浏览多窗口页面
    def newWindowsTab(self):
        # 判断多窗口数量
        if self.base.elementIsExit(WINDOWS_TAB_NUM):
            # 新建多窗口数量
            num = 2
            for j in range(num):
                # 在多窗口浏览Tab页面，点击新建多窗口按钮
                self.base.clickByElement(NEW_WINDOWS_TAB, '在多窗口浏览Tab页面，点击新建多窗口按钮')
                # 点击导航栏中的安居客
                self.more.clickDaoHang(HOME_BUSINESS_MORE_TEXT)
                # 调用打开底部工具栏图标按钮，打开多窗口浏览Tab页
                self.clickWindowsTab()
        else:
            self.assertFalse(WINDOWS_TAB_NUM)


    # 滑动多窗口
    def scrollToWindowsTab(self):
        if self.base.elementIsExit(CLOSE_WINDOWS_TAB):
            # 滑动浏览多窗口
            self.base.swipe('left')
            self.base.swipe('right')
            self.base.swipe('left')
        else:
            self.assertFalse(CLOSE_WINDOWS_TAB)



    # 打开多窗口tab中的页面
    def openWindowsTabPage(self):
        # 判断多窗口浏览页中固定定位位置是否存在
        if self.base.elementIsExit(WINDOWS_POSITION):
            # 点击打开浏览的多窗口页面
            self.base.clickByElement(WINDOWS_POSITION, '点击打开多窗口中的浏览Tab页面')
        else:
            self.assertFalse(WINDOWS_POSITION)


    # 关闭所有的多窗口
    def closeAllWindowsTab(self):
        # 判断多窗口的数量
        if self.base.elementIsExit(CLOSE_WINDOWS_TAB):
            self.base.clickByElement(CLOSE_WINDOWS_TAB,'关闭所有的多窗口Tab')
        else:
            self.assertFalse(CLOSE_WINDOWS_TAB)


    # 向上滑动关闭一个多窗口
    def closeOneWindowsTab(self):
        # 判断多窗口的数量
        if self.base.elementIsExit(WINDOWS_TAB_NUM):
            self.base.dragByElement(WINDOWS_POSITION,WINDOWS_POSITION_AFTER,2)
        else:
            self.assertFalse(WINDOWS_TAB_NUM)

    # 长按底部 menu_more 按钮，显示X按钮，点击X按钮关闭多窗口
    def longPressCloseWindowsTab(self):
        if self.base.elementIsExit(WINDOWS_TAB_NUM):
            self.base.swipeByElement(PRESS_MENUMORE_CLOSEWINDOWS, '点击长按menu_more显示的X按钮，关闭当前窗口')
        else:
            self.assertFalse(WINDOWS_TAB_NUM)


    # 获取多窗口数量
    def getWindowsNum(self):
        if self.base.elementIsExit(WINDOWS_TAB_NUM):
            return self.base.elementText(WINDOWS_TAB_NUM,'获取多窗口数量')
        else:
            self.assertFalse(WINDOWS_TAB_NUM)


