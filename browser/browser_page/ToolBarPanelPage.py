from base_function.base import Base
from browser.browser_element.ToolbarPanel import *
from browser.browser_page.HomePage import *




class ToolBarPanelPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)
        self.home = HomePage(driver)

    # 点击底部工具栏的位置
    def clickToolsPanel(self ,element):
        '''
        :param element: 元素名称
        :return:
        '''
        if self.base.elementIsExit(element):
            self.base.clickByElement(element, "工具面板-》{}".format(element))
        else:
            self.base.assertFalse(element)
            

    # 点击我的图标 ---wmw
    def clickFlymeme(self):
        if self.base.elementIsExit(SET_UP):
            self.base.clickByElement(FLYME_ME, '我的图标')
        else:
            self.assertFalse(SET_UP)

    # 点击设置  --wmw
    def clickSetUp(self):
        if self.base.elementIsExit(SET_UP):
            self.base.clickByElement(SET_UP, "设置")
        else:
            self.assertFalse(SET_UP)

    # 清空历史 -- LJX
    def cleanHistory(self):
        self.home.clickMore()
        self.clickToolsPanel(CLEAN_UP_HISTORY)
        self.clickToolsPanel(CLEAN_UP)



