from time import sleep

from base_function.base import Base
from browser.browser_element.AddToHome import *


class AddToHomePage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击添加到主页的记录 —— LJX
    def clickAddToHomeWebsite(self, element_text):
        if self.base.elementIsExit(element_text):
            self.base.clickByElementIdAndText(BOOKMARK_ID, element_text, '添加到主页"{}"网站'.format(element_text))
            sleep(1)
        else:
            self.assertFalse(element_text)

    # 点击进入添加到主页-》元素进入页面 —— LJX
    def clickAddToHomeTab(self, element):
        if self.base.elementIsExit(element):
            self.base.clickByElement(element, '添加到主页"{}"页面'.format(element))
        else:
            self.assertFalse(element)

    # 点击“添加到主页”的添加按钮 —— LJX
    def clickAddToHome(self, instance):
        if self.base.elementIsExit(ADD_TO_TEXT):
            self.base.clickByElementClassNameAndText(ADD_TO_CLASSNAME, ADD_TO_TEXT, '负一屏精选页面添加按钮', instance)
        else:
            self.assertFalse(ADD_TO_TEXT)

    # 点击“添加到主页”的添加按钮 —— LJX
    def clickToBookmark(self, instance):
        if self.base.elementIsExit(ADD_TO_CLASSNAME):
            self.base.clickByElementIdAndInstance(ADD_ID, '负一屏-》添加到主页的添加按钮', instance)
        else:
            self.assertFalse(ADD_TO_CLASSNAME)

    # 在“添加到主页”点击指定网站的添加按钮 —— LJX
    def addBookmark(self, element):
        if self.base.elementIsExit(element):
            self.base.clickByElementRight(element, ADD_ID, direction='right')
        else:
            self.assertFalse(element)




