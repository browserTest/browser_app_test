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

    # 判断历史是否有数据，没有则造一条“百度一下”数据 -- LJX
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

    # 获取我的收藏第1条记录的标题 -- LJX
    def getCollectionTitle(self):
        if self.base.elementIsExit(COLLECTION_ID):
            strText = self.base.elementText(COLLECTION_ID, '获取资讯详情页的文章标题')
            return strText
        else:
            self.assertFalse(COLLECTION_ID)

    # 我的收藏页面点击元素 -- LJX
    def clickCollection(self, element):
        if self.base.elementIsExit(element):
            self.base.clickByElement(element, '浏览器我的收藏页面的{}'.format(element))
        else:
            self.assertFalse(element)
