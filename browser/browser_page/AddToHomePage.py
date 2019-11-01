from base_function.base import Base
from browser.browser_element.AddToHome import *


class AddToHomePage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击添加到主页的记录
    def clickAddToHomeWebsite(self, element_text):
        if self.base.elementIsExit(element_text):
            self.base.clickByElementIdAndText(BOOKMARK_ID, element_text, '添加到主页"{}"网站'.format(element_text))
        else:
            self.assertFalse(element_text)

    # 点击进入添加到主页-》分类
    def clickAddToHomeClassify(self):
        if self.base.elementIsExit(CLASSFICATION_TEXT):
            self.base.clickByElement(CLASSFICATION_TEXT, '添加到主页-》分类')
        else:
            self.assertFalse(CLASSFICATION_TEXT)

    # 点击进入添加到主页-》历史
    def clickAddToHomeHistory(self):
        if self.base.elementIsExit(HISTORY_TEXT):
            self.base.clickByElement(HISTORY_TEXT, '添加到主页-》历史')
        else:
            self.assertFalse(HISTORY_TEXT)

    # 点击进入添加到主页-》分类-》资讯头条
    def clickAddToHomeReader(self):
        if self.base.elementIsExit(INFORMATION_TEXT):
            self.base.clickByElement(INFORMATION_TEXT, '添加到主页-》分类-》资讯头条')
        else:
            self.assertFalse(INFORMATION_TEXT)


    # 点击添加到主页的添加按钮
    def clickAddToHome(self, instance):
        if self.base.elementIsExit(ADD_TO_TEXT):
            self.base.clickByElementClassNameAndText(ADD_TO_CLASSNAME, ADD_TO_TEXT, '负一屏精选页面添加按钮', instance)
        else:
            self.assertFalse(ADD_TO_TEXT)

