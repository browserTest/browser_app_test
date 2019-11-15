import allure
from browser.browser_page.AddToHomePage import *
from browser.browser_page.CollectionAndHistoryPage import *
from browser.browser_page.HomePage import *
from browser.browser_page.NegativeScreenPage import *
from browser.browser_page.PubMethod import *
from browser.browser_page.SearchPanelPage import *
from browser.browser_page.ToolBarPanelPage import *
from browser.browser_page.NewsPage import *


@allure.feature("测试收藏/历史相关功能")
@pytest.mark.usefixtures("driver_setup")
class TestNegativePage():

    @pytest.fixture(scope="function")
    def collectionAndHistory_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.negativescreen = NegativeScreenPage(self.driver)
        self.addtohome = AddToHomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.searchpanel = SearchPanelPage(self.driver)
        self.toolbarpanel = ToolBarPanelPage(self.driver)
        self.collectionandhistory = CollectionAndHistoryPage(self.driver)
        self.news = NewsPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")

    @allure.story('测试取消清空历史功能')
    @pytest.mark.P0
    def test001CleanUpHistoryCancel(self, collectionAndHistory_init):
        '''
        1、先判断是否存在历史数据，不存在则造一条历史数据，存在则不处理
        2、点击工具栏中more菜单，再点击工具面板的“清空历史”，清空历史的弹框选择取消
        3、断言存在历史数据
        '''
        # 监听地理位置弹框，点击“始终允许”
        self.base.browserWatcher()
        # 制造一条历史数据
        self.collectionandhistory.makeHistory()
        # 点击工具面板的“清空历史”，弹框选择取消
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(CLEAN_UP_HISTORY)
        self.toolbarpanel.clickToolsPanel(CLEAN_UP_CANCEL)
        # 再次进入工具面板的“清空历史”，断言页面不存在“暂无历史数据”元素
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(HISTORY)
        self.base.assertTrue(HISTORY_PAGE, False, timeout=3)


    @allure.story('测试确认清空历史功能')
    @pytest.mark.P0
    def test002CleanUpHistory(self, collectionAndHistory_init):
        '''
        1、先判断是否存在历史数据，不存在则造一条历史数据，存在则不处理
        2、点击工具栏中more菜单，再点击工具面板的“清空历史”，清空历史的弹框选择取消
        3、断言存在历史数据
        '''
        # 监听地理位置弹框，点击“始终允许”
        self.base.browserWatcher()
        # 制造一条历史数据
        self.collectionandhistory.makeHistory()
        # 点击工具面板的“清空历史”，弹框选择取消
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(CLEAN_UP_HISTORY)
        self.toolbarpanel.clickToolsPanel(CLEAN_UP)
        # 再次进入工具面板的“清空历史”，断言页面不存在“暂无历史数据”元素
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(HISTORY)
        self.base.assertTrue(HISTORY_PAGE, timeout=3)


    @allure.story('收藏一篇文章，收藏夹下显示该文章；取消收藏后，收藏夹下不显示该文章')
    @pytest.mark.P1
    def test003CollectArticle(self, collectionAndHistory_init):
        '''
        1、先判断是否存在历史数据，不存在则造一条历史数据，存在则不处理
        2、点击工具栏中more菜单，再点击工具面板的“清空历史”，清空历史的弹框选择取消
        3、断言存在历史数据
        '''
        self.home.clickInformation()
        self.news.dropScrollNews()
        self.news.clickOpenNewsArticle()
        # 获取文章详情页的标题
        ArticleDetailsTitle = self.news.getArticleDetailsTitle()
        print(ArticleDetailsTitle)
        self.news.clickArticleCollectPosition()
        # 返回上一层，进入我的收藏
        self.pubmethod.clickBack()
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        # 获取我的收藏页第1条记录的标题
        CollectionTitle = self.collectionandhistory.getCollectionTitle()
        print(CollectionTitle)
        self.base.assertEqual(ArticleDetailsTitle, CollectionTitle, True)
        # 点击进入我的收藏第1条记录，取消收藏
        self.collectionandhistory.clickCollection(COLLECTION_ID)
        self.news.clickArticleCollectPosition()
        # 返回上一层，重新进入我的收藏
        self.pubmethod.clickBack()
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        CollectionTitle = self.collectionandhistory.getCollectionTitle()
        print(CollectionTitle)
        self.base.assertEqual(ArticleDetailsTitle, CollectionTitle, True)










