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

    # 造指定条数的历史数据 —— LJX
    def makeHistory(self, nums):
        for i in range(nums):
            # 点击搜索框，搜索内容
            self.home.clickHomeSearch()
            if self.base.elementIsExit(SEARCHPANEL_WEBSITE):
                self.base.elementSetText(SEARCHPANEL_WEBSITE, SEARCH_WORD + str(i), '搜索框输入"安卓自动化测试"')
            else:
                self.assertFalse(SEARCHPANEL_WEBSITE)
            self.searchpanel.clickSearchInto()
            # 监听地理位置弹框
            self.base.browserWatcher()
            sleep(2)
            # 返回上一层
            self.pubmethod.clickBack()

    # 造指定条数的收藏数据 —— LJX
    def makeCollection(self, nums):
        for i in range(nums):
            # 点击搜索框，搜索内容并添加收藏
            self.home.clickHomeSearch()
            if self.base.elementIsExit(SEARCHPANEL_WEBSITE):
                self.base.elementSetText(SEARCHPANEL_WEBSITE, SEARCH_WORD + str(i), '搜索框输入"安卓自动化测试"')
            else:
                self.assertFalse(SEARCHPANEL_WEBSITE)
            self.searchpanel.clickSearchInto()
            # 监听地理位置弹框
            self.base.browserWatcher()
            sleep(2)
            self.home.clickMore()
            sleep(1)
            self.toolbarpanel.clickToolsPanel(ADD_COLLECTION)
            self.clickAddCollectFolder(ADD_TO_COLLECTION)
            # 返回上一层
            self.pubmethod.clickBack()


    # 获取我的收藏相应记录的标题 —— LJX
    def getCollectionTitle(self, instance=0):
        if self.base.elementIsExit(COLLECTION_ID):
            return self.base.elementText(COLLECTION_ID, '我的收藏记录的标题', instance)
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
            sleep(3)
        else:
            self.assertFalse(element)

    # 我的收藏页点击删除按钮 —— LJX
    def clickCollectDelete(self):
        if self.base.elementIsExit(MULTI_CHOICE):
            self.base.clickByElement(COLLECT_DELETE_BUTTON, '“删除”相对坐标')
        else:
            self.assertFalse(MULTI_CHOICE)

    # 收藏页长按指定条数的记录发送至桌面3次 —— LJX
    def clickCollectAddToDesk(self, num=1):
        if self.base.elementIsExit(COLLECTION_ID):
            for i in range(3):
                self.longClickCollection(COLLECTION_ID, num)
                self.base.clickByElement(COLLECT_ADDTODESK_BUTTON, '“发送至桌面”相对坐标')
                # 等待2秒，"已添加到主页常用"toast提示消失后才能定位到其它元素
                sleep(2)
        else:
            self.assertFalse(COLLECTION_ID)

    # 我的收藏页点击发送至桌面按钮 —— LJX
    def clickCollectNewWindowOpen(self):
        if self.base.elementIsExit(MULTI_CHOICE):
            self.base.clickByElement(COLLECT_NEW_WINDOW, '“新窗口打开”相对坐标')
        else:
            self.assertFalse(MULTI_CHOICE)

    # 在添加收藏页面点击元素 —— LJX
    def clickAddCollectFolder(self, element):
        if self.base.elementIsExit(element):
            sleep(1)
            self.base.clickByElement(element, '添加收藏页面的{}'.format(element))
        else:
            self.assertFalse(element)

    # 新增收藏文件夹输入框填写文本 —— LJX
    def inputCollectFolderName(self):
        if self.base.elementIsExit(NEW_FOLDER_NAME_ID):
            sleep(1)
            self.base.elementSetText(NEW_FOLDER_NAME_ID, "自动化测试", "自动化测试")
        else:
            self.assertFalse(NEW_FOLDER_NAME_ID)

    # 删除“自动化测试”收藏文件夹 —— LJX
    def deleteCollectFolder(self):
        self.home.clickMore()
        sleep(1)
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        if self.base.elementIsExit(COLLECT_NEW_FOLDER_NAME):
            self.base.long_clickByElement(COLLECT_NEW_FOLDER_NAME, '"自动化测试"文件夹', 1)
            if self.base.elementIsExit(DELETE_FOLDER):
                self.base.clickByElement(DELETE_FOLDER, '删除文件夹')
                if self.base.elementIsExit(CONFIRM_TEXT):
                    self.base.clickByElement(NEW_FOLDER_CONFIRM, '确认')
                    sleep(1)
                    self.pubmethod.clickBack()
                else:
                    self.assertFalse(CONFIRM_TEXT)
            else:
                self.assertFalse(DELETE_FOLDER)
        else:
            self.pubmethod.clickBack()

    # 设置输入框文本 —— LJX
    def setText(self, element, text):
        if self.base.elementIsExit(element):
            sleep(1)
            self.base.elementSetText(element, text, text)
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
            for i in range(2, nums+1):
                self.base.clickByElementIdAndInstance(element, '历史页面的{}'.format(element), i)
        else:
            self.assertFalse(element)

    # 历史页点击删除按钮 —— LJX
    def clickHistoryDelete(self):
        if self.base.elementIsExit(MULTI_CHOICE):
            self.base.clickByElement(HISTORY_DELETE_BUTTON, '删除按钮相对坐标')
        else:
            self.assertFalse(MULTI_CHOICE)

    # 点击无痕按钮 —— LJX
    def openNoMarking(self):
        if self.base.elementIsExit(NO_MARKING):
            self.base.clickByElement(NO_MARKING, '无痕按钮')
        else:
            self.assertFalse(NO_MARKING)

    # 连续3次把指定书签发送至桌面 —— LJX
    def sendToDeskCollect(self):
        if self.base.elementIsExit(HOME_MORE):
            for i in range(3):
                # 添加到桌面
                self.home.clickMore()
                sleep(1)
                self.toolbarpanel.clickToolsPanel(ADD_COLLECTION)
                self.base.clickByElement(ADD_TO_DESKTOP, '添加到收藏-》发送到桌面第{}次'.format(i))
                sleep(1)
        else:
            self.assertFalse(HOME_MORE)



