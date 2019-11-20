from base_function.base import Base
from browser.browser_element.CollectionAndHistory import HISTORY_PAGE
from browser.browser_element.Home import HOME_MORE
from browser.browser_element.SearchPanel import SEARCHPANEL_WEBSITE
from browser.browser_page.HomePage import *
from browser.browser_page.ToolBarPanelPage import *
from browser.browser_page.PubMethod import *
from browser.browser_page.SearchPanelPage import *

class CollectionAndHistoryPage(Base):

    def __init__(self, driver):
        self.home = HomePage(driver)
        self.toolbarpanel = ToolBarPanelPage(driver)
        self.pubmethod = PubMethod(driver)
        self.searchpanel = SearchPanelPage(driver)
        self.base = Base(driver)

    # 判断历史是否有数据，没有则造一条“百度一下”数据 —— LJX
    def makeHistory(self):
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(HISTORY)
        if self.base.elementIsExit(HISTORY_PAGE):
            # 返回上一层
            self.pubmethod.clickBack()
            # 点击搜索框,搜索'm.baidu.com'
            self.home.clickHomeSearch()
            self.base.elementSetText(SEARCHPANEL_WEBSITE, 'm.baidu.com', '搜索框输入"m.baidu.com"')
            self.searchpanel.clickSearchInto()
            sleep(2)
            # 返回上一层
            self.pubmethod.clickBack()
        else:
            # 返回上一层
            self.pubmethod.clickBack()

    # 获取我的收藏相应记录的标题 —— LJX
    def getCollectionTitle(self, instance=0):
        if self.base.elementIsExit(COLLECTION_ID):
            strText = self.base.elementText(COLLECTION_ID, '我的收藏记录的标题', instance)
            return strText
        else:
            self.assertFalse(COLLECTION_ID)

    # 获取历史相应记录的标题 —— LJX
    def getHistoryTitle(self, instance=0):
        if self.base.elementIsExit(HISTORY_ID):
            strText = self.base.elementText(HISTORY_ID, '我的收藏记录的标题', instance)
            return strText
        else:
            self.assertFalse(HISTORY_ID)

    # 我的收藏页面点击元素 —— LJX
    def clickCollection(self, element):
        if self.base.elementIsExit(element):
            self.base.clickByElement(element, '我的收藏页面的{}'.format(element))
        else:
            self.assertFalse(element)

    # 我的收藏页点击删除按钮 —— LJX
    def clickCollectDelete(self):
        if self.base.elementIsExit(MULTI_CHOICE):
            self.base.clickByElement(COLLECT_DELETE_BUTTON, '“删除”相对坐标')
        else:
            self.assertFalse(MULTI_CHOICE)

    # 我的收藏页点击发送至桌面按钮 —— LJX
    def clickCollectAddToDesk(self):
        if self.base.elementIsExit(MULTI_CHOICE):
            self.base.clickByElement(COLLECT_ADDTODESK_BUTTON, '“发送至桌面”相对坐标')
        else:
            self.assertFalse(MULTI_CHOICE)

    # 我的收藏页点击发送至桌面按钮 —— LJX
    def clickCollectNewWindowOpen(self):
        if self.base.elementIsExit(MULTI_CHOICE):
            self.base.clickByElement(COLLECT_NEW_WINDOW, '“新窗口打开”相对坐标')
        else:
            self.assertFalse(MULTI_CHOICE)

    # 在添加收藏页面点击元素 —— LJX
    def clickAddCollectFolder(self, element):
        if self.base.elementIsExit(element):
            self.base.clickByElement(element, '添加收藏页面的{}'.format(element))
        else:
            self.assertFalse(element)

    # 新增收藏文件夹输入框填写文本 —— LJX
    def inputCollectFolderName(self, element):
        if self.base.elementIsExit(element):
            self.base.elementSetText(element, "自动化测试", "自动化测试")
        else:
            self.assertFalse(element)

    # 删除“自动化测试”收藏文件夹 —— LJX
    def deleteCollectFolder(self):
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        if self.base.elementIsExit(COLLECT_NEW_FOLDER_NAME):
            self.base.long_clickByElement(COLLECT_NEW_FOLDER_NAME, '"自动化测试"收藏文件夹', 1)
            if self.base.elementIsExit(DELETE_FOLDER):
                self.base.clickByElement(DELETE_FOLDER, '删除文件夹')
                if self.base.elementIsExit(DELETE_CONFIRM):
                    self.base.clickByElement(DELETE_CONFIRM, '确定')
                    self.pubmethod.clickBack()
                else:
                    self.assertFalse(DELETE_CONFIRM)
            else:
                self.assertFalse(DELETE_FOLDER)
        else:
            self.pubmethod.clickBack()

    # 设置输入框文本 —— LJX
    def setText(self, element, text):
        if self.base.elementIsExit(element):
            self.base.elementSetText(element, text, text)
            sleep(1)
        else:
            self.assertFalse(element)

    # 我的收藏页面长按单条/多条记录 —— LJX
    def longClickCollection(self, element, nums=1):
        if self.base.elementIsExit(element):
            self.base.long_clickByElementIdAndInstance(element, '收藏页面的{}'.format(element))
            for i in range(1, nums):
                self.base.clickByElementIdAndInstance(element, '收藏页面的{}'.format(element), i)
        else:
            self.assertFalse(element)

    # 历史页面长按单条/多条记录 —— LJX
    def longClickHistory(self, element, nums=1):
        if self.base.elementIsExit(element):
            self.base.long_clickByElementIdAndInstance(element, '历史页面的{}'.format(element), 1)
            for i in range(2, nums):
                self.base.clickByElementIdAndInstance(element, '历史页面的{}'.format(element), i)
        else:
            self.assertFalse(element)

    # 历史页点击删除按钮 —— LJX
    def clickHistoryDelete(self):
        if self.base.elementIsExit(MULTI_CHOICE):
            self.base.clickByElement(HISTORY_DELETE_BUTTON, '删除按钮相对坐标')
        else:
            self.assertFalse(MULTI_CHOICE)


