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
        # 制造一条历史数据
        self.collectionandhistory.makeHistory(1)
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
        # 制造一条历史数据
        self.collectionandhistory.makeHistory(1)
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
        1、进入资讯流的健康频道，下拉刷新，获取第1篇文章第标题，并收藏该文章，进入收藏夹获取第1条记录的标题，断言两个标题相等
        2、在收藏夹点击进入第1条记录详情，取消收藏，返回到收藏夹，获取第1条记录第标题，断言标题不相等
        '''
        # 进入资讯流，进入频道管理选择健康频道，下拉刷新
        self.home.clickInformation()
        self.news.clickNewsTriangle()
        self.news.clickNewsChannel(NEWS_CHANNEL_HEALTH)
        self.news.dropScrollNews()
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
        1、先删除"自动化测试"文件夹，点击搜索框，进入搜索面板，点击搜索，进入搜索结果页
        2、添加收藏，编辑收藏文件夹，新增一个文件夹，并选择添加到该文件夹下
        3、进入收藏夹该新增文件夹下，断言是否存在1条记录
        '''
        # 先删除“自动化测试”文件夹
        # self.collectionandhistory.deleteCollectFolder()
        # 点击搜索面板第1个热词，进入搜索结果页
        self.home.clickHomeSearch()
        self.searchpanel.clickSearchInto()
        # 添加到收藏夹，编辑位置信息，新建"自动化测试"文件夹并收藏到该文件夹下
        self.home.clickMore()
        sleep(1)
        self.toolbarpanel.clickToolsPanel(ADD_COLLECTION)
        self.collectionandhistory.clickAddCollectFolder(COLLECT_EDIT_ID)
        sleep(1)
        try:
            self.collectionandhistory.clickAddCollectFolder(COLLECT_FOLDER_POSITION)
        except Exception as e:
            logging.info('忽略点击编辑过程中的报错')

        self.collectionandhistory.clickAddCollectFolder(NEW_FOLDER_ID)
        self.collectionandhistory.inputCollectFolderName()
        try:
            self.collectionandhistory.clickAddCollectFolder(NEW_FOLDER_CONFIRM)
        except Exception as e:
            logging.info('忽略新建文件夹时点击确定出现的报错')
        try:
            self.collectionandhistory.clickAddCollectFolder(COLLECT_NEW_FOLDER_NAME)
        except Exception as e:
            logging.info('忽略点击"自动化测试"文件夹的报错')
        self.collectionandhistory.clickAddCollectFolder(COLLECT_NEW_FOLDER_POSITION)
        # 编辑网页URL、网页名称为百度网页，点击"确认"，收藏到收藏夹中
        self.collectionandhistory.setText(ADD_COLLECT_URL, COLLECT_NAME)
        self.collectionandhistory.setText(ADD_COLLECT_ADDRESS, COLLECT_URL)
        self.collectionandhistory.clickAddCollectFolder(CONFIRM_ID)
        # 等待2秒，"已添加到收藏"toast消失后才能定位到其它元素
        sleep(2)
        # 进入收藏夹新建的"自动化测试"文件夹，断言是否存在"百度一下"
        self.home.clickMore()
        sleep(1)
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        self.collectionandhistory.clickCollection(COLLECT_NEW_FOLDER_NAME)
        self.base.assertTrue(COLLECT_NAME)
        # 点击进入"百度一下"，监听地理位置弹框，断言存在'百度一下,你就知道'
        self.collectionandhistory.clickCollection(COLLECT_NAME)
        self.base.browserWatcher()
        sleep(2)
        self.base.assertTrue(BAIDU_HOME)


    @allure.story('添加一个网页到收藏/主页常用/桌面，查看是否添加到对应目录下并且点击能正常打开 —— LJX')
    @pytest.mark.P1
    def test005CollectWebPage(self, collectionAndHistory_init):
        '''
        1、点击搜索框，进入搜索面板，获取第1个热词文本，点击第1个热词，进入搜索结果页
        2、添加到收藏夹，进入收藏夹获取第1条记录文本，断言是否刚添加收藏夹的热词
        3、添加到主页常用，进入负一屏，断言当前页面是否存在刚收藏的热词元素
        4、发送到桌面，退出浏览器，断言桌面是否存在刚发送到桌面到热词元素
        '''
        # 进入搜索面板，获取第1个热词文本，并进入该热词的搜索结果页
        self.home.clickHomeSearch()
        hotSearchWord = self.searchpanel.clickHotWords()
        self.searchpanel.clickSearchHistory()
        # 添加到收藏夹
        self.home.clickMore()
        sleep(1)
        self.toolbarpanel.clickToolsPanel(ADD_COLLECTION)
        self.collectionandhistory.clickAddCollectFolder(ADD_TO_COLLECTION)
        # 等待2秒，"已添加到收藏"toast提示消失后才能定位到其它元素
        sleep(2)
        # 进入收藏夹新建的文件夹下，断言是否存在数据
        self.home.clickMore()
        sleep(1)
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        # 获取我的收藏页第1条记录的标题
        CollectionTitle = self.collectionandhistory.getCollectionTitle()
        self.base.assertEqual(hotSearchWord, CollectionTitle, True)
        # 返回上一层，重新添加收藏-》添加到主页常用
        self.collectionandhistory.clickAddCollectFolder(COLLECTION_BACK_ID)
        self.home.clickMore()
        sleep(1)
        self.toolbarpanel.clickToolsPanel(ADD_COLLECTION)
        self.collectionandhistory.clickAddCollectFolder(ADD_TO_NEGATIVE)
        # 等待2秒，"已添加到主页常用"toast提示消失后才能定位到其它元素
        self.home.clickHome()
        # 进入负一屏，断言是否存在添加到搜索热词
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.base.assertTrue(hotSearchWord, True, timeout=3)
        # 返回上一层，重新添加收藏-》发送到桌面3次
        self.pubmethod.clickBack()
        self.collectionandhistory.sendToDeskCollect()
        # 等待2秒，"已添加到主页常用"toast提示消失后才能定位到其它元素
        sleep(2)
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.base.assertTrue(hotSearchWord, True, timeout=3)

    @allure.story('我的收藏-长按单个-删除，检查是否正常删除 —— LJX')
    @pytest.mark.P1
    def test006DeleteCollectionOne(self, collectionAndHistory_init):
        '''
        1、造一条收藏记录
        2、进入首页，再进入收藏夹，获取第1条记录的标题
        3、长按1条记录，删除，断言被删除记录不存在
        '''
        # 造1条收藏记录
        self.collectionandhistory.makeCollection(1)
        # 进入首页，再进入收藏夹
        self.home.clickHomeOnPage(HOME_PAGE)
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        # 获取收藏夹第1条记录标题，然后长按删除
        CollectionTitle = self.collectionandhistory.getCollectionTitle()
        self.collectionandhistory.longClickCollection(COLLECTION_ID)
        self.collectionandhistory.clickCollectDelete()
        self.collectionandhistory.clickCollection(FRAME_DELETE_ID)
        # 断言当前页面不存在已删除到收藏记录
        self.base.assertTrue(CollectionTitle, False, timeout=3)

    @allure.story('我的收藏-长按多个-删除，检查是否正常删除 —— LJX')
    @pytest.mark.P1
    def test007DeleteCollectionMore(self, collectionAndHistory_init):
        '''
        1、造3条收藏记录
        2、进入首页，再进入收藏夹
        3、长按3条记录，删除，断言被删除的记录不存在
        '''
        # 造3条收藏记录
        self.collectionandhistory.makeCollection(3)
        # 进入首页，再进入收藏夹
        self.home.clickHomeOnPage(HOME_PAGE)
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        # 获取收藏夹第1、2、3条记录的标题
        CollectionTitleOne = self.collectionandhistory.getCollectionTitle(0)
        CollectionTitleTwo = self.collectionandhistory.getCollectionTitle(1)
        CollectionTitleThree = self.collectionandhistory.getCollectionTitle(2)
        # 删除第1、2、3条记录
        self.collectionandhistory.longClickCollection(COLLECTION_ID, 3)
        self.collectionandhistory.clickCollectDelete()
        self.collectionandhistory.clickCollection(FRAME_DELETE_ID)
        # 断言第1、2、3条记录的标题不存在
        self.base.assertTrue(CollectionTitleOne, False, timeout=3)
        self.base.assertTrue(CollectionTitleTwo, False, timeout=3)
        self.base.assertTrue(CollectionTitleThree, False, timeout=3)

    @allure.story('历史-长按1个-删除，检查是否正常删除 —— LJX')
    @pytest.mark.P1
    def test008DeleteHistoryOne(self, collectionAndHistory_init):
        '''
        1、造一条历史记录
        2、进入首页，再进入历史
        3、长按1条记录，删除，断言被删除记录不存在
        '''
        # 制造一条历史数据
        self.collectionandhistory.makeHistory(1)
        # 进入首页，再进入历史
        self.home.clickHomeOnPage(HOME_PAGE)
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(HISTORY)
        # 获取第1条记录的标题，并长按删除
        HistoryTitle = self.collectionandhistory.getHistoryTitle(1)
        self.collectionandhistory.longClickHistory(HISTORY_ID)
        self.collectionandhistory.clickHistoryDelete()
        self.collectionandhistory.clickCollection(FRAME_DELETE_ID)
        # 断言当前页面不存在已删除到历史记录
        self.base.assertTrue(HistoryTitle, False, timeout=3)

    @allure.story('历史-长按多个-删除，检查是否正常删除 —— LJX')
    @pytest.mark.P1
    def test009DeleteHistoryMore(self, collectionAndHistory_init):
        '''
        1、造3条历史记录
        2、进入首页，再进入历史
        3、长按3条记录，删除，断言被删除的3条记录不存在
        '''
        # 制造3条历史数据
        self.collectionandhistory.makeHistory(3)
        # 进入首页，再进入历史
        self.home.clickHomeOnPage(HOME_PAGE)
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(HISTORY)
        # 获取历史第1、2、3条记录的标题
        HistoryTitleOne = self.collectionandhistory.getHistoryTitle(1)
        HistoryTitleTwo = self.collectionandhistory.getHistoryTitle(2)
        HistoryTitleThree = self.collectionandhistory.getHistoryTitle(3)
        # 删除第1、2、3条记录
        self.collectionandhistory.longClickHistory(HISTORY_ID, 3)
        self.collectionandhistory.clickHistoryDelete()
        self.collectionandhistory.clickCollection(FRAME_DELETE_ID)
        # 断言第1、2、3条记录的标题不存在
        self.base.assertTrue(HistoryTitleOne, False, timeout=3)
        self.base.assertTrue(HistoryTitleTwo, False, timeout=3)
        self.base.assertTrue(HistoryTitleThree, False, timeout=3)

    @allure.story('我的收藏-长按单个-发送至桌面，检查是否成功添加至桌面且正常打开 —— LJX')
    @pytest.mark.P1
    def test10AddToDeskOne(self, collectionAndHistory_init):
        '''
        1、进入首页，再进入收藏夹
        2、长按1条记录，发送到桌面3次，断言桌面存在这条记录
        3、桌面点击这条记录，断言当前页面存在记录标题和工具入口
        '''
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        # 获取第1条记录的标题，长按第1条记录并发送到桌面3次
        CollectionTitle = self.collectionandhistory.getCollectionTitle()
        self.collectionandhistory.clickCollectAddToDesk()
        # 退出浏览器，断言是否存在该记录
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.base.assertTrue(CollectionTitle, True, timeout=3)
        # 桌面点击打开该记录，断言是否正常打开
        self.base.clickByElement(CollectionTitle, '发送到桌面的收藏')
        self.base.assertTrue(CollectionTitle, True, timeout=3)
        self.base.assertTrue(HOME_MORE, True, timeout=3)

    @allure.story('我的收藏-长按多个-发送至桌面，检查是否成功添加至桌面且正常打开 —— LJX')
    @pytest.mark.P1
    def test011AddToDeskMore(self, collectionAndHistory_init):
        '''
        1、进入首页，再进入收藏夹，长按第1、2、3条记录，发送到桌面3次，断言桌面存在这3条记录
        2、桌面点击第3条记录，断言当前页面存在记录标题和工具入口
        '''
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(MY_COLLECTION)
        # 获取前3条记录的标题，长按前3条记录并发送到桌面3次
        CollectionTitleOne = self.collectionandhistory.getCollectionTitle(0)
        CollectionTitleTwo = self.collectionandhistory.getCollectionTitle(1)
        CollectionTitleThree = self.collectionandhistory.getCollectionTitle(2)
        self.collectionandhistory.clickCollectAddToDesk(3)
        # 退出浏览器，断言是否存在该记录
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.base.assertTrue(CollectionTitleOne, True, timeout=3)
        self.base.assertTrue(CollectionTitleTwo, True, timeout=3)
        self.base.assertTrue(CollectionTitleThree, True, timeout=3)
        # 桌面点击打开第3条记录，断言是否正常打开
        self.base.clickByElement(CollectionTitleThree, '发送到桌面的收藏')
        self.base.assertTrue(CollectionTitleThree, True, timeout=3)
        self.base.assertTrue(HOME_MORE, True, timeout=3)

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
        historyTitleBefore = self.collectionandhistory.getHistoryTitle(1)
        # 返回上一层
        self.pubmethod.clickBack()
        self.home.clickMore()
        self.collectionandhistory.openNoMarking()
        # 造一条历史数据
        self.collectionandhistory.makeHistory(1)
        self.home.clickMore()
        self.toolbarpanel.clickToolsPanel(HISTORY)
        historyTitleAfter = self.collectionandhistory.getHistoryTitle(1)
        self.base.assertEqual(historyTitleBefore, historyTitleAfter, True, timeout=3)





















