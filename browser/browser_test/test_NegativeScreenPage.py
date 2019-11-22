import allure
from browser.browser_page.AddToHomePage import *
from browser.browser_page.NegativeScreenPage import *
from browser.browser_page.PubMethod import *
from browser.browser_element.AddToHome import *
from browser.browser_page.SearchPanelPage import *
from browser.browser_page.ToolBarPanelPage import *
from browser.browser_page.WindowsTabPage import *

@allure.feature("测试负一屏页面")
@pytest.mark.usefixtures("driver_setup")
class TestNegativePage():

    @pytest.fixture(scope="function")
    def negative_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.negativescreen = NegativeScreenPage(self.driver)
        self.addtohome = AddToHomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.searchpanel = SearchPanelPage(self.driver)
        self.toolbarpanel = ToolBarPanelPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.windowstab = WindowsTabPage(self.driver)
        yield
        logging.info("****用例执行结束****")
        logging.info("")

    @allure.story('测试负一屏-》精选页打开网站、添加书签 —— LJX')
    @pytest.mark.P1
    def test001AddToHomeWebsite(self, negative_init):
        '''
        1、进入负一屏，删除“hao123”书签
        2、进入精选页，添加“hao123”书签，点击进入“hao123”网站，断言页面是否存在'hao123导航-上网从这里开始'元素
        3、返回上一层到负一屏，断言负一屏是否存在“hao123”书签
        '''
        # 进入负一屏，删除"hao123"书签，点击“添加”，进入精选页
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteBookmark(HAO123)
        self.negativescreen.clickNegative(NAGATIVE_SCREEN_ADD_TEXT)
        # 在精选页面对"hao123"书签点击"添加"，点击"hao123"进入网页
        self.addtohome.clickAddToHome(2)
        self.addtohome.clickAddToHomeWebsite(HAO123)
        # 断言是否进入"hao123导航-上网从这里开始"网页
        self.base.assertTrue(HAO123WEB, timeout=5)
        # 返回上一层到负一屏，断言是否存在"hao123"书签
        self.pubmethod.clickBack()
        self.base.assertTrue(HAO123, timeout=3)

    @allure.story('测试负一屏-》分类页打开网站、添加书签 —— LJX')
    @pytest.mark.P1
    def test002AddToHomeWebsite(self, negative_init):
        '''
        1、进入负一屏，删除“凤凰网”书签
        2、进入精选页，添加“凤凰网”书签，点击进入“凤凰网”网站，断言页面是否存在'手机鳳凰網'元素
        3、返回上一层到负一屏，断言负一屏是否存在“凤凰网”书签
        '''
        # 进入负一屏，删除"凤凰网"书签，进入分类-》资讯头条
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteBookmark(IFENG_SIMPLIFIED)
        self.negativescreen.clickNegative(NAGATIVE_SCREEN_ADD_TEXT)
        self.addtohome.clickAddToHomeTab(CLASSFICATION_TEXT)
        self.addtohome.clickAddToHomeTab(INFORMATION_TEXT)
        # 对"凤凰网"书签点击"添加"，点击"凤凰网"进入网页
        self.addtohome.clickAddToHome(1)
        self.addtohome.clickAddToHomeWebsite(IFENG_SIMPLIFIED)
        # 断言是否进入"凤凰网"网页
        self.base.assertTrue(IFENG_TRADITIONAL, timeout=8)
        # 返回上一层到负一屏，断言是否存在"凤凰网"书签
        self.pubmethod.clickBack()
        self.base.assertTrue(IFENG_SIMPLIFIED, timeout=3)

    @allure.story('测试负一屏-》历史页打开网站、添加书签 —— LJX')
    @pytest.mark.P1
    def test003AddToHomeWebsite(self, negative_init):
        '''
        1、进入负一屏，删除“百度一下”书签
        2、进入精选页，添加“凤凰网”书签，点击进入“凤凰网”网站，断言页面是否存在'手机鳳凰網'元素
        3、返回上一层到负一屏，断言负一屏是否存在“凤凰网”书签
        '''
        # 进入负一屏，删除“百度一下”书签
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteBookmark(BAIDU_TEXT)
        # 点击搜索框
        self.home.clickHomeSearch()
        # 搜索框'm.baidu.com'
        self.base.elementSetText(SEARCHPANEL_WEBSITE, 'm.baidu.com', '搜索框输入"m.baidu.com"')
        self.searchpanel.clickSearchInto()
        # 返回上一层到负一屏
        self.pubmethod.clickBack()
        # 在负一屏点击"添加"
        self.negativescreen.clickNegative(NAGATIVE_SCREEN_ADD_TEXT)
        # 进入历史
        self.addtohome.clickAddToHomeTab(HISTORY_TEXT)
        # 断言是否存在"百度一下"网页
        self.base.assertTrue(BAIDU_TEXT, timeout=3)
        # 对第1个网页点击"添加"
        self.addtohome.clickAddToHome(1)
        # 点击"百度一下"进入网页
        self.addtohome.clickAddToHomeWebsite(BAIDU_TEXT)
        # 断言是否进入"百度一下"网页
        self.base.assertTrue(BAIDU_TEXT, timeout=3)

    @allure.story('测试负一屏-》自定义页打开网站 —— LJX')
    @pytest.mark.P1
    def test004AddToHomeWebsite(self, negative_init):
        '''
        1、清空历史数据
        2、进入负一屏-》自定义添加
        '''
        # 进入负一屏，删除“百度一下”书签
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteBookmark(BAIDU_SEARCH)
        # 在负一屏点击"添加"
        self.negativescreen.clickNegative(NAGATIVE_SCREEN_ADD_TEXT)
        # 进入自定义
        self.addtohome.clickAddToHomeTab(DIY_TEXT)
        # 点击网址
        self.addtohome.clickAddToHomeTab(DIY_URL_ID)
        # 网址输入'baidu',点击联想词“百度搜索”，再点击“添加”
        self.base.elementSetText(DIY_URL_ID, 'baidu', '网址输入"m.baidu.com"')
        self.addtohome.clickAddToHomeTab(BAIDU_THINK)
        self.addtohome.clickAddToHomeTab(ADD_TO_TEXT)
        # 断言是否进入"百度一下"网页
        self.base.assertTrue(BAIDU_SEARCH, timeout=3)

    @allure.story('添加书签后，在负一屏点击默认图标和任一手动添加图标，正常跳转 —— LJX')
    @pytest.mark.P1
    def test005AddBookmark(self, negative_init):
        '''
        1、进入负一屏，删除"魅族社区"书签
        2、进入精选页，添加“魅族社区”书签，返回上一层到负一屏，断言负一屏是否存在“魅族社区”书签，点击进入“魅族社区”网站，断言页面是否存在'魅族社区'元素
        3、点击进入“网址导航”网站，断言页面是否存在'网址导航'元素
        '''
        # 进入负一屏，删除"魅族社区"书签
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteBookmark(MEIZU_COMMUNITY)
        self.negativescreen.clickNegative(NAGATIVE_SCREEN_ADD_TEXT)
        self.addtohome.clickToBookmark(3)
        # 返回上一层到负一屏，断言是否存在"魅族社区"书签
        self.pubmethod.clickBack()
        self.base.assertTrue(MEIZU_COMMUNITY, timeout=3)
        # 负一屏点击“魅族社区”书签，断言是否正常跳转
        self.negativescreen.clickNegative(MEIZU_COMMUNITY)
        self.base.assertTrue(MEIZU_COMMUNITY, timeout=8)
        sleep(2)
        self.pubmethod.clickBack()
        # 负一屏点击“网址导航”书签，断言是否正常跳转
        self.negativescreen.clickNegative(WEBSITE_GUIDE)
        self.base.assertTrue(WEBSITE_GUIDE, timeout=3)

    @allure.story('长按负一屏图标：新窗口打开功能正常 —— LJX')
    @pytest.mark.P1
    def test006NegativeNewWindowOpen(self, negative_init):
        '''
        1、当负一屏不存在“魅族社区”书签，则进入精选页添加“魅族社区”
        2、进入负一屏，获取当前窗口数量，长按“魅族社区”书签，选择新窗口打开，断言正常打开
        3、获取当前窗口数量，断言窗口数量+1
        '''
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.addMeizuCommunity(MEIZU_COMMUNITY)
        # 获取当前多窗口数量
        winNumBefore = self.windowstab.getWindowsNum()
        self.negativescreen.longClickNegativeBookmark(MEIZU_COMMUNITY)
        self.negativescreen.clickNegative(NEW_WINDOW_OPEN)
        # 获取新窗口打开后的窗口数量
        winNumAfter = self.windowstab.getWindowsNum()
        self.base.assertTrue(MEIZU_COMMUNITY, timeout=8)
        self.base.assertEqual(int(winNumBefore)+1, int(winNumAfter), True, timeout=3)

    @allure.story('长按负一屏图标：删除功能正常 —— LJX')
    @pytest.mark.P1
    def test007NegativeDelete(self, negative_init):
        '''
        1、当负一屏不存在“魅族社区”书签，则进入精选页添加“魅族社区”
        2、进入负一屏，长按“魅族社区”书签，选择删除，断言负一屏不存在“魅族社区”书签
        '''
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.addMeizuCommunity(MEIZU_COMMUNITY)
        self.negativescreen.longClickNegativeBookmark(MEIZU_COMMUNITY)
        self.negativescreen.clickNegative(DELETE_TEXT)
        self.base.assertTrue(MEIZU_COMMUNITY, False, timeout=3)

    @allure.story('长按负一屏图标：编辑功能正常 —— LJX')
    @pytest.mark.P1
    def test008NegativeEdit(self, negative_init):
        '''
        1、如果负一屏存在“豆瓣”，删除“豆瓣”
        1、当负一屏不存在“魅族社区”书签，则进入精选页添加“魅族社区”
        2、进入负一屏，长按“魅族社区”书签，选择编辑，编辑成豆瓣网站
        3、返回负一屏，断言负一屏存在“魅族社区”书签
        '''
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteBookmark(DOUBAN_NAME)
        self.negativescreen.addMeizuCommunity(MEIZU_COMMUNITY)
        self.negativescreen.longClickNegativeBookmark(MEIZU_COMMUNITY)
        self.negativescreen.clickNegative(EDIT)
        self.negativescreen.setText(WEBSITE_NAME, DOUBAN_NAME)
        self.negativescreen.setText(WEBSITE_URL, DOUBAN_URL)
        self.negativescreen.clickNegative(EDIT_CONFIRM)
        self.base.assertTrue(DOUBAN_NAME, True, timeout=3)
        self.negativescreen.clickNegative(DOUBAN_NAME)
        self.base.assertTrue(DOUBAN_NAME, timeout=8)

    @allure.story('长按负一屏图标：发送至桌面功能正常 —— LJX')
    @pytest.mark.P1
    def test009NegativeSendToDesk(self, negative_init):
        '''
        1、当桌面存在“魅族社区”，则删除“魅族社区”
        1、进入浏览器，当负一屏不存在“魅族社区”书签，则进入精选页添加“魅族社区”
        2、进入负一屏，长按“魅族社区”书签，选择发送至桌面，断言桌面存在“魅族社区”书签
        '''
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.deleteBookmark(MEIZU_COMMUNITY, TOP_OF_LAUNCHER)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.addMeizuCommunity(MEIZU_COMMUNITY)
        self.negativescreen.longClickNegativeBookmark(MEIZU_COMMUNITY)
        self.negativescreen.clickNegative(ADD_TO_DESK)
        sleep(2)
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.base.assertTrue(MEIZU_COMMUNITY, True, timeout=3)

    @allure.story('长按负一屏图标：多选功能正常 —— LJX')
    @pytest.mark.P1
    def test010NegativeMultiSelect(self, negative_init):
        '''
        1、当负一屏不存在“魅族社区”书签，则进入精选页添加“魅族社区”
        2、进入负一屏，长按“魅族社区”书签，选择删除，断言负一屏不存在“魅族社区”书签
        '''
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.longClickNegativeBookmark(ONLINE_STORE)
        self.negativescreen.clickNegative(SELECT_MORE)
        actionBarBefore =self.negativescreen.getNegativeActionBar()
        print(actionBarBefore)
        # ACTION_BAR
        self.negativescreen.clickNegative(SELECT)
        actionBarAfter = self.negativescreen.getNegativeActionBar()
        print(actionBarAfter)
        self.base.assertEqual(actionBarBefore, actionBarAfter, False, timeout=3)
        self.negativescreen.clickNegative(SELECT_CANCEL)
        self.base.assertTrue(SELECT_CANCEL, False, timeout=3)


    @allure.story('长按拖拽负一屏图标，可正常合并文件夹 —— LJX')
    @pytest.mark.P1
    def test011NegativeMergeFile(self, negative_init):
        '''
        1、当负一屏不存在“魅族社区”书签，则进入精选页添加“魅族社区”
        2、进入负一屏，长按“魅族社区”书签，选择删除，断言负一屏不存在“魅族社区”书签
        '''
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.addMeizuCommunity(TUNIU)
        self.negativescreen.addMeizuCommunity(BAIDU_NEWS)
        self.negativescreen.newFolder(BAIDU_NEWS, TUNIU)
        self.negativescreen.longClickNegativeBookmark(FILE)
        self.negativescreen.clickNegative(RERAME_FILE)
        self.negativescreen.setText(RERAME_FILE_ID, AUTOMATION_FILE)
        sleep(1)
        self.negativescreen.clickNegative(DELETE_CONFIRM)
        self.base.assertTrue(AUTOMATION_FILE, timeout=3)

    @allure.story('长按文件夹，删除文件夹功能正常 —— LJX')
    @pytest.mark.P1
    def test012NegativeDeleteFile(self, negative_init):
        '''
        1、当负一屏不存在“魅族社区”书签，则进入精选页添加“魅族社区”
        2、进入负一屏，长按“魅族社区”书签，选择删除，断言负一屏不存在“魅族社区”书签
        '''
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.longClickNegativeBookmark(AUTOMATION_FILE)
        self.negativescreen.clickNegative(DELETE_FILE)
        self.negativescreen.clickNegative(DELETE_CONFIRM)
        self.base.assertTrue(AUTOMATION_FILE, False, timeout=3)

    @allure.story('长按文件夹，移动文件夹功能正常 —— LJX')
    @pytest.mark.P1
    def test013NegativeMoveFile(self, negative_init):
        '''
        1、当负一屏不存在“魅族社区”书签，则进入精选页添加“魅族社区”
        2、进入负一屏，长按“魅族社区”书签，选择删除，断言负一屏不存在“魅族社区”书签
        '''
        self.home.clickHomeOnPage(MYCOLLECTION)
        bottomBefore = self.negativescreen.folderBottom(AUTOMATION_FILE)
        self.negativescreen.dragFolder(AUTOMATION_FILE, DRAG_FILE_POSITION)
        bottomAfter = self.negativescreen.folderBottom(AUTOMATION_FILE)
        self.base.assertEqual(bottomBefore, bottomAfter, False, timeout=3)









