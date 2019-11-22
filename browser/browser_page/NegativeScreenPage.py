from base_function.base import Base
from browser.browser_element.AddToHome import *
from browser.browser_element.NegativeScreen import *
from browser.browser_page.AddToHomePage import *
from time import sleep


class NegativeScreenPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)
        self.addtohome = AddToHomePage(driver)

    # 在负一屏点击元素 —— LJX
    def clickNegative(self, element):
        if self.base.elementIsExit(element):
            self.base.clickByElement(element, '浏览器负一屏的{}'.format(element))
        else:
            self.assertFalse(element)

    # 在负一屏删除书签 —— LJX
    def deleteBookmark(self, element):
        if self.base.elementIsExit(element):
            self.base.long_clickByElement(element, '负一屏"{}"书签'.format(element), 1)
            if self.base.elementIsExit(DELETE_TEXT):
                self.base.clickByElement(DELETE_TEXT, '删除按钮')
            else:
                self.assertFalse(DELETE_TEXT)
        else:
            pass

    # 当负一屏不存在某个书签，进入“添加到主页”添加该书签到负一屏 —— LJX
    def addMeizuCommunity(self, element):
        if self.base.elementIsExit(element) is False:
            self.clickNegative(NAGATIVE_SCREEN_ADD_TEXT)
            if self.base.elementIsExit(element):
                self.base.clickByElementRight(element, ADD_ID, 'right')
                self.base.usePhone('back')
            else:
                self.assertFalse(element)
        else:
            pass

    # 在负一屏长按单个书签 —— LJX
    def longClickNegativeBookmark(self, element):
        if self.base.elementIsExit(element):
            self.base.long_clickByElement(element, '负一屏的{}'.format(element), 1)
        else:
            self.assertFalse(element)

    # 负一屏书签编辑页面设置输入框文本 —— LJX
    def setText(self, element, text):
        if self.base.elementIsExit(element):
            self.base.elementSetText(element, text, text)
            sleep(1)
        else:
            self.assertFalse(element)

    # 长按负一屏书签，获取顶部标题 —— LJX
    def getNegativeActionBar(self):
        if self.base.elementIsExit(ACTION_BAR):
            return self.base.elementText(ACTION_BAR, '顶部标题')
        else:
            self.assertFalse(ACTION_BAR)

    # 合并2个书签 —— LJX
    def newFolder(self, element1, element2):
        if self.base.elementIsExit(AUTOMATION_FILE) is False:
            self.addMeizuCommunity(TUNIU)
            self.addMeizuCommunity(BAIDU_NEWS)
            self.base.dragElementToElement(element1, element2)
        else:
            self.long_clickByElement(AUTOMATION_FILE, '负一屏的{}'.format(AUTOMATION_FILE), 1)
            if self.base.elementIsExit(DELETE_FILE):
                self.clickNegative(DELETE_FILE)
            else:
                self.assertFalse(DELETE_FILE)
            self.clickNegative(DELETE_CONFIRM)

    # 拖拽文件夹 —— LJX
    def dragFolder(self, element, position):
        if self.base.elementIsExit(element):
            self.base.dragByElement(element, position)
        else:
            self.assertFalse(element)

    # 获取文件夹坐标信息 —— LJX
    def folderBottom(self, element):
        if self.base.elementIsExit(element):
            self.base.getInfoBottom(element)
        else:
            self.assertFalse(element)




