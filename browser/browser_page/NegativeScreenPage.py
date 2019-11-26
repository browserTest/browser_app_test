from base_function.base import Base, logging
from browser.browser_element.AddToHome import *
from browser.browser_element.NegativeScreen import *
from browser.browser_page.AddToHomePage import *
from time import sleep


class NegativeScreenPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)
        self.addtohome = AddToHomePage(driver)

    # 在负一屏点击指定元素 —— LJX
    def clickNegative(self, element):
        if self.base.elementIsExit(element):
            self.base.clickByElement(element, '负一屏的{}'.format(element))
        else:
            self.assertFalse(element)

    # 连续3次长按指定书签，发送至桌面 —— LJX
    def sendToDeskNegative(self, element):
        if self.base.elementIsExit(element):
            for i in range(3):
                self.base.long_clickByElement(element, '负一屏的{}第{}次'.format(element, i), 1)
                self.clickNegative(ADD_TO_DESK)
                sleep(1)
        else:
            self.assertFalse(element)

    # 在负一屏上滑找到指定元素并点击元素 —— LJX
    def clickNegativeScrollUP(self, element):
        if self.base.scrollToElement(element):
            self.base.clickByElement(element, '负一屏的{}'.format(element))
        else:
            self.assertFalse(element)

    # 在负一屏下滑找到指定元素并点击元素 —— LJX
    def clickNegativeScrollDown(self, element):
        if self.base.scrollToElementDown(element):
            self.base.clickByElement(element, '负一屏的{}'.format(element))
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
        elif self.base.scrollToElement(element):
            self.base.long_clickByElement(element, '负一屏"{}"书签'.format(element), 1)
            if self.base.elementIsExit(DELETE_TEXT):
                self.base.clickByElement(DELETE_TEXT, '删除按钮')
            else:
                self.assertFalse(DELETE_TEXT)
        else:
            pass

    # 如果负一屏不存在指定书签，进入“添加到主页”添加该书签 —— LJX
    def addBookmarkToNegative(self, element):
        if self.base.elementIsExit(element) is False:
            if self.base.scrollToElement(element) is False:
                # 点击负一屏"添加"进入"添加到主页"
                self.base.clickByElement(NEGATIVE_ADD_TEXT, '添加按钮')
                if self.base.scrollToElement(element):
                    # 点击指定网站右边到添加按钮
                    self.base.clickByElementRight(element, ADD_ID, direction='right')
                    self.base.usePhone('back')
                    sleep(1)
                    self.base.scroll()
                else:
                    self.assertFalse(element)
            else:
                # 如果负一屏已存在指定书签，则不处理
                pass
        else:
            # 如果负一屏首屏已存在指定书签，则不处理
            pass

    # 在负一屏长按元素 —— LJX
    def longClickNegative(self, element):
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

    # 长按负一屏书签进入多选状态，获取并返回顶部标题 —— LJX
    def getNegativeActionBar(self):
        if self.base.elementIsExit(ACTION_BAR):
            return self.base.elementText(ACTION_BAR, '顶部标题')
        else:
            self.assertFalse(ACTION_BAR)

    # 合并2个书签 —— LJX
    def newFolder(self, element1, element2):
        if self.base.elementIsExit(AUTOMATION_FILE) is False:
            self.base.dragElementToElement(element1, element2)
        else:
            self.long_clickByElement(AUTOMATION_FILE, '负一屏的{}'.format(AUTOMATION_FILE), 1)
            if self.base.elementIsExit(DELETE_FILE):
                self.clickNegativeScrollUP(DELETE_FILE)
            else:
                self.assertFalse(DELETE_FILE)
            self.clickNegativeScrollUP(CONFIRM_TEXT)

    # 负一屏删除指定文件夹 —— LJX
    def deleteFolder(self, element):
        if self.base.elementIsExit(element):
            self.base.long_clickByElement(element, '负一屏的{}文件夹'.format(element), 1)
            if self.base.elementIsExit(DELETE_FILE):
                self.base.clickByElement(DELETE_FILE, '删除文件夹')
                if self.base.elementIsExit(CONFIRM_TEXT):
                    self.base.clickByElement(CONFIRM_TEXT, '确定')
                else:
                    self.assertFalse(CONFIRM_TEXT)
            else:
                self.assertFalse(DELETE_FILE)
        elif self.base.scrollToElement(element):
            self.base.long_clickByElement(element, '负一屏的{}文件夹'.format(element), 1)
            if self.base.elementIsExit(DELETE_FILE):
                self.base.clickByElement(DELETE_FILE, '删除文件夹')
                if self.base.elementIsExit(CONFIRM_TEXT):
                    self.base.clickByElement(CONFIRM_TEXT, '确定')
                else:
                    self.assertFalse(CONFIRM_TEXT)
            else:
                self.assertFalse(DELETE_FILE)
        else:
            pass

    # 拖拽文件夹 —— LJX
    def dragFolder(self, element, position):
        if self.base.elementIsExit(element):
            self.base.dragByElement(element, position)
        else:
            self.assertFalse(element)

    # 获取文件夹坐标信息 —— LJX
    def folderBottom(self, element):
        if self.base.elementIsExit(element):
            return self.base.getInfoBottom(element, '负一屏的{}'.format(element))
        else:
            self.assertFalse(element)




