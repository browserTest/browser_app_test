import allure
from browser.browser_page.AddToHomePage import *
from browser.browser_page.CollectionAndHistoryPage import *
from browser.browser_page.HomePage import *
from browser.browser_page.NegativeScreenPage import *
from browser.browser_page.PubMethod import *
from browser.browser_page.SearchPanelPage import *
from browser.browser_page.ToolBarPanelPage import *
from browser.browser_page.NewsPage import *
from browser.browser_page.WindowsTabPage import *


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
        self.windowstab = WindowsTabPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.mbackToHomeOrNegative()
        yield
        logging.info("****用例执行结束****")
        logging.info("")

    @allure.story('测试取消清空历史功能 —— LJX')
    @pytest.mark.P1
    def test001CleanUpHistoryCancel(self, collectionAndHistory_init):
        '''
        1、先判断是否存在历史数据，不存在则造一条历史数据，存在则不处理
        2、点击工具栏中more菜单，再点击工具面板的“清空历史”，清空历史的弹框选择取消
        3、断言不存在“暂无历史记录”元素
        '''
        # 监听地理位置弹框，点击“始终允许”
        self.base.browserWatcher()
        # 当没有数历史数据时，制造一条历史数据
        self.collectionandhistory.makeHistory()
        # 点击工具面板的“清空历史”，弹框选择取消
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(CLEAN_UP_HISTORY)
        self.toolbarpanel.clickToolsPanel(CLEAN_UP_CANCEL)
        # 再次进入工具面板的“清空历史”，断言页面不存在“暂无历史数据”元素
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(HISTORY)
        self.base.assertTrue(HISTORY_PAGE, False, timeout=3)

    @allure.story('测试确认清空历史功能 —— LJX')
    @pytest.mark.P1
    def test002CleanUpHistory(self, collectionAndHistory_init):
        '''
        1、先判断是否存在历史数据，不存在则造一条历史数据，存在则不处理
        2、点击工具栏中more菜单，再点击工具面板的“清空历史”，清空历史的弹框选择确定
        3、断言存在“暂无历史记录”元素
        '''
        # 监听地理位置弹框，点击允许”
        self.base.browserWatcher()
        # 制造一条历史数据
        self.collectionandhistory.makeHistory()
        # 点击工具面板的“清空历史”，弹框选择确定
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(CLEAN_UP_HISTORY)
        self.toolbarpanel.clickToolsPanel(CLEAN_UP)
        # 再次进入工具面板的“清空历史”，断言页面存在“暂无历史数据”元素
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(HISTORY)
        self.base.assertTrue(HISTORY_PAGE, timeout=3)

    @allure.story('收藏一篇文章，收藏夹下显示该文章；取消收藏后，收藏夹下不显示该文章 —— LJX')
    @pytest.mark.P1
    def test003CollectArticle(self, collectionAndHistory_init):
        '''
        1、进入资讯流，下拉刷新，获取第1篇文章第标题，并收藏该文章，进入收藏夹获取第1条记录的标题，断言两个标题相等
        2、在收藏夹点击进入第1条记录详情，取消收藏，返回到收藏夹，获取第1条记录第标题，断言标题不相等
        '''
        # 进入资讯流，进入频道管理选择健康频道，下拉刷新
        self.home.clickInformation()
        self.news.clickNewsTriangle()
        self.news.clickNewsChannel(NEWS_CHANNEL_HEALTH)
        self.news.dropScrollNews()
        sleep(2)
        # 获取文章标题，并收藏该文章
        ArticleTitle = self.news.getNewsArticleTitle()
        self.news.clickOpenNewsArticle()
        self.news.clickArticleCollectPosition()
        # 返回上一层，进入我的收藏
        self.news.clickNewsBack()
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        # 获取我的收藏页第1条记录的标题，断言收藏的文章标题与收藏夹第1条记录的标题一致
        CollectionTitle = self.collectionandhistory.getCollectionTitle()
        self.base.assertEqual(ArticleTitle, CollectionTitle, True)
        # 点击进入我的收藏第1条记录，取消收藏
        self.collectionandhistory.clickCollection(COLLECTION_ID)
        self.news.clickArticleCollectPosition()
        # 返回上一层，重新进入我的收藏，获取第1条记录标题
        self.news.clickNewsBack()
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        CollectionTitle = self.collectionandhistory.getCollectionTitle()
        # 断言取消收藏的文章标题与收藏夹第1条记录的标题不一致
        self.base.assertEqual(ArticleTitle, CollectionTitle, False)

    @allure.story('打开网页-添加收藏-编辑-新建收藏文件夹-收藏进去-能改的都改一遍-收藏夹打开该收藏正常 —— LJX')
    @pytest.mark.P1
    def test004CollectWebToFolder(self, collectionAndHistory_init):
        '''
        1、点击搜索框，进入搜索面板，点击搜索，进入搜索结果页
        2、添加收藏，编辑收藏文件夹，新增一个文件夹，并选择添加到该文件夹下
        3、进入收藏夹该新增文件夹下，断言是否存在1条记录
        '''
        # 先删除“自动化测试”文件夹
        self.collectionandhistory.deleteCollectFolder()
        # 点击搜索面板第1个热词，进入搜索结果页
        self.home.clickHomeSearch()
        self.searchpanel.clickSearchInto()
        # 添加到收藏夹，编辑位置信息，新建"自动化测试"文件夹并收藏到该文件夹下
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(ADD_COLLECTION)
        self.toolbarpanel.clickToolsPanel(COLLECT_EDIT_ID)
        self.collectionandhistory.clickAddCollectFolder(COLLECT_FOLDER_ID)
        self.collectionandhistory.clickAddCollectFolder(NEW_FOLDER_ID)
        self.collectionandhistory.inputCollectFolderName(NEW_FOLDER_NAME_ID)
        self.collectionandhistory.clickAddCollectFolder(NEW_FOLDER_CONFIRM)
        self.collectionandhistory.clickAddCollectFolder(COLLECT_NEW_FOLDER_NAME)
        # 编辑网页URL、网页名称为百度网页，点击"确认"，收藏到收藏夹中
        self.collectionandhistory.setText(ADD_COLLECT_URL, COLLECT_NAME)
        self.collectionandhistory.setText(ADD_COLLECT_ADDRESS, COLLECT_URL)
        self.collectionandhistory.clickAddCollectFolder(CONFIRM_TEXT)
        # 等待2秒，"已添加到收藏"toast消失后才能定位到其它元素
        sleep(2)
        # 进入收藏夹新建的"自动化测试"文件夹，断言是否存在"百度一下"
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        self.collectionandhistory.clickCollection(COLLECT_NEW_FOLDER_NAME)
        self.base.assertTrue(COLLECT_NAME)
        # 点击进入"百度一下"，监听地理位置弹框，点击允许”，断言存在'百度一下,你就知道'
        self.collectionandhistory.clickCollection(COLLECT_NAME)

        sleep(2)
        self.base.assertTrue(BAIDU_HOME)

    @allure.story('添加一个网页到收藏/主页常用/桌面，查看是否添加到对应目录下并且点击能正常打开 —— LJX')
    @pytest.mark.P1
    def test005CollectWebPage(self, collectionAndHistory_init):
        # 获取第1个热词
        self.home.clickHomeSearch()
        hotSearchWord = self.searchpanel.clickHotWords()
        self.searchpanel.clickSearchHistory()
        # 添加到收藏夹
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(ADD_COLLECTION)
        self.collectionandhistory.clickAddCollectFolder(ADD_TO_COLLECTION)
        # 等待2秒，"已添加到收藏"toast提示消失后才能定位到其它元素
        sleep(2)
        # 进入收藏夹新建的文件夹下，断言是否存在数据
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        # 获取我的收藏页第1条记录的标题
        CollectionTitle = self.collectionandhistory.getCollectionTitle()
        self.base.assertEqual(hotSearchWord, CollectionTitle, True)
        # 返回上一层，重新添加收藏
        self.news.clickNewsBack()
        # 添加到主页常用
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(ADD_COLLECTION)
        self.collectionandhistory.clickAddCollectFolder(ADD_TO_NEGATIVE)
        # 等待2秒，"已添加到主页常用"toast提示消失后才能定位到其它元素
        sleep(2)
        self.home.clickHome()
        # 进入负一屏
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.base.assertTrue(hotSearchWord, True, timeout=3)
        # 返回上一层，重新添加收藏
        self.pubmethod.clickBack()
        # 添加到桌面
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(ADD_COLLECTION)
        self.collectionandhistory.clickAddCollectFolder(ADD_TO_DESKTOP)
        # 等待2秒，"已添加到主页常用"toast提示消失后才能定位到其它元素
        sleep(2)
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.base.assertTrue(hotSearchWord, True, timeout=3)

    @allure.story('我的收藏-长按单个-删除，检查是否正常删除 —— LJX')
    @pytest.mark.P1
    def test006DeleteCollectionOne(self, collectionAndHistory_init):
        '''
        1、进入收藏夹，长按1条记录，删除，断言被删除记录不存在
        '''
        # 进入收藏夹,长按
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        CollectionTitle = self.collectionandhistory.getCollectionTitle()
        print(CollectionTitle)
        self.collectionandhistory.longClickCollection(COLLECTION_ID)
        self.collectionandhistory.clickCollectDelete()
        self.collectionandhistory.clickCollection(CONFIRM_TEXT)
        self.base.assertTrue(CollectionTitle, False, timeout=3)

    @allure.story('我的收藏-长按多个-删除，检查是否正常删除 —— LJX')
    @pytest.mark.P1
    def test007DeleteCollectionMore(self, collectionAndHistory_init):
        '''
        1、进入收藏夹，长按3条记录，删除，断言被删除的记录不存在
        '''
        # 进入收藏夹,长按
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        CollectionTitle = self.collectionandhistory.getCollectionTitle(1)
        print(CollectionTitle)
        self.collectionandhistory.longClickCollection(COLLECTION_ID, 2)
        self.collectionandhistory.clickCollectDelete()
        self.collectionandhistory.clickCollection(CONFIRM_TEXT)
        self.base.assertTrue(CollectionTitle, False, timeout=3)

    @allure.story('历史-长按1个-删除，检查是否正常删除 —— LJX')
    @pytest.mark.P1
    def test008DeleteHistoryOne(self, collectionAndHistory_init):
        '''
        1、进入历史，长按1条记录，删除，断言被删除记录不存在
        '''
        # 进入历史，获取第1条记录标题
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(HISTORY)
        HistoryTitle = self.collectionandhistory.getHistoryTitle(1)
        print(HistoryTitle)
        self.collectionandhistory.longClickHistory(HISTORY_ID)
        self.collectionandhistory.clickHistoryDelete()
        self.collectionandhistory.clickCollection(CONFIRM_TEXT)
        sleep(1)
        self.base.assertTrue(HistoryTitle, False, timeout=3)

    @allure.story('历史-长按多个-删除，检查是否正常删除 —— LJX')
    @pytest.mark.P1
    def test009DeleteHistoryMore(self, collectionAndHistory_init):
        '''
        1、进入历史，长按多条记录，删除，断言被删除记录不存在
        '''
        # 进入历史，获取第1条记录标题
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(HISTORY)
        HistoryTitle = self.collectionandhistory.getHistoryTitle(2)
        print(HistoryTitle)
        self.collectionandhistory.longClickHistory(HISTORY_ID, 3)
        self.collectionandhistory.clickHistoryDelete()
        self.collectionandhistory.clickCollection(CONFIRM_TEXT)
        sleep(1)
        self.base.assertTrue(HistoryTitle, False, timeout=3)

    @allure.story('我的收藏-长按单个-发送至桌面，检查是否成功添加至桌面且正常打开 —— LJX')
    @pytest.mark.P1
    def test10AddToDeskOne(self, collectionAndHistory_init):
        '''
        1、进入收藏夹，长按1条记录，发送到桌面，断言桌面存在记录
        '''
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        CollectionTitle = self.collectionandhistory.getCollectionTitle()
        print(CollectionTitle)
        self.collectionandhistory.longClickCollection(COLLECTION_ID)
        self.collectionandhistory.clickCollectAddToDesk()
        # 等待2秒，"已添加到主页常用"toast提示消失后才能定位到其它元素
        sleep(2)
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.base.assertTrue(CollectionTitle, True, timeout=3)
        self.base.clickByElement(CollectionTitle, '发送到桌面的收藏')
        self.base.assertTrue(CollectionTitle, True, timeout=3)

    @allure.story('我的收藏-长按多个-发送至桌面，检查是否成功添加至桌面且正常打开 —— LJX')
    @pytest.mark.P1
    def test011AddToDeskMore(self, collectionAndHistory_init):
        '''
        1、进入收藏夹，长按1条记录，发送到桌面，断言桌面存在记录
        '''
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        CollectionTitle = self.collectionandhistory.getCollectionTitle(1)
        print(CollectionTitle)
        self.collectionandhistory.longClickCollection(COLLECTION_ID, 2)
        self.collectionandhistory.clickCollectAddToDesk()
        # 等待2秒，"已添加到主页常用"toast提示消失后才能定位到其它元素
        sleep(2)
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.base.assertTrue(CollectionTitle, True, timeout=3)
        self.base.clickByElement(CollectionTitle, '发送到桌面的收藏')
        self.base.assertTrue(CollectionTitle, True, timeout=3)

    @allure.story('我的收藏-长按1条记录-新窗口打开，检查是否正常打开且多窗口数量+1 —— LJX')
    @pytest.mark.P1
    def test12NewWindowOpenOne(self, collectionAndHistory_init):
        '''
        1、进入收藏夹，长按1条记录，新窗口打开，断言正常打开且新窗口数量增加
        '''
        # 收藏一个网页到收藏夹
        self.home.clickHomeSearch()
        hotSearchWord = self.searchpanel.clickHotWords()
        self.searchpanel.clickSearchHistory()
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(ADD_COLLECTION)
        self.collectionandhistory.clickAddCollectFolder(ADD_TO_COLLECTION)
        # 返回上一层
        self.pubmethod.clickBack()
        # 获取当前多窗口数量
        winNumBefore = self.windowstab.getWindowsNum()
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        # CollectionTitle = self.collectionandhistory.getCollectionTitle()
        # print(CollectionTitle)
        self.collectionandhistory.longClickCollection(COLLECTION_ID)
        self.collectionandhistory.clickCollectNewWindowOpen()
        # 新窗口打开后的窗口数量
        winNumAfter = self.windowstab.getWindowsNum()
        self.base.assertTrue(hotSearchWord, timeout=3)
        self.base.assertEqual(winNumBefore, winNumAfter, False, timeout=3)

    @allure.story('我的收藏-长按3条记录-新窗口打开，检查是否正常打开且多窗口数量+3 —— LJX')
    @pytest.mark.P1
    def test13NewWindowOpenMore(self, collectionAndHistory_init):
        '''
        1、进入收藏夹，长按多条记录，新窗口打开，断言正常打开且新窗口数量+3
        '''
        # 收藏一个网页到收藏夹
        self.home.clickHomeSearch()
        hotSearchWord = self.searchpanel.clickHotWords()
        self.searchpanel.clickSearchHistory()
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(ADD_COLLECTION)
        self.collectionandhistory.clickAddCollectFolder(ADD_TO_COLLECTION)
        # 返回上一层
        self.pubmethod.clickBack()
        # 获取当前多窗口数量
        winNumBefore = self.windowstab.getWindowsNum()
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        self.collectionandhistory.longClickCollection(COLLECTION_ID, 3)
        self.collectionandhistory.clickCollectNewWindowOpen()
        # 新窗口打开后的窗口数量
        winNumAfter = self.windowstab.getWindowsNum()
        self.base.assertTrue(hotSearchWord, timeout=3)
        self.base.assertEqual(int(winNumBefore)+3, int(winNumAfter), True, timeout=3)

    @allure.story('开启无痕模式，访问网站，不会生成历史记录 —— LJX')
    @pytest.mark.P1
    def test14NoMarking(self, collectionAndHistory_init):
        '''
        1、获取历史第1条记录标题
        2、打开无痕模式，点击一个热词进行搜索
        3、返回上一层，获取历史第1条记录标题
        4、断言历史第1条记录的标题没有改变
        '''
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(HISTORY)
        historyTitleBefore = self.collectionandhistory.getHistoryTitle()
        # 返回上一层
        self.pubmethod.clickBack()
        self.home.clickMore()
        self.collectionandhistory.openNoMarking()
        # 点击第1个热词，进入搜索结果页
        self.home.clickHomeSearch()
        self.searchpanel.clickSearchHistory()
        # 返回上一层
        self.pubmethod.clickBack()
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(HISTORY)
        historyTitleAfter = self.collectionandhistory.getHistoryTitle()
        self.base.assertEqual(historyTitleBefore, historyTitleAfter, True, timeout=3)





















