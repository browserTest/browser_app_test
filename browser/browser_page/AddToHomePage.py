from time import sleep

from base_function.base import Base
from browser.browser_element.AddToHome import *


class AddToHomePage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击添加到主页的记录
    def clickAddToHomeWebsite(self, element_text):
        if self.base.elementIsExit(element_text):
            self.base.clickByElementIdAndText(BOOKMARK_ID, element_text, '添加到主页"{}"网站'.format(element_text))
            sleep(1)
        else:
            self.assertFalse(element_text)

    # 点击进入添加到主页-》元素进入页面
    def clickAddToHomeTab(self, element):
        if self.base.elementIsExit(element):
            self.base.clickByElement(element, '添加到主页"{}"页面'.format(element))
        else:
            self.assertFalse(element)

    # 点击添加到主页的添加按钮
    def clickAddToHome(self, instance):
        if self.base.elementIsExit(ADD_TO_TEXT):
            self.base.clickByElementClassNameAndText(ADD_TO_CLASSNAME, ADD_TO_TEXT, '负一屏精选页面添加按钮', instance)
        else:
            self.assertFalse(ADD_TO_TEXT)

    # 添加到主页自定义页面输入文本



