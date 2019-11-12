from config.config import *
from browser.browser_page.PubMethod import PubMethod
from browser.browser_page.SearchPanelPage import *
from browser.browser_page.HomePage import *
import allure






@allure.feature("测试搜索页面")
@pytest.mark.usefixtures("driver_setup")
class TestSearchPanelPage():

    @pytest.fixture(scope="function")
    def search_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod= PubMethod(self.driver)
        self.searchpanel = SearchPanelPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.home.clickHome()
        self.home.clickHomeOnPage(HOME_PAGE)
        yield
        logging.info("****用例执行结束****")
        logging.info("")


    # ---wmw
    @allure.story('测试搜索框')
    def test001SearchPanelPage(self, search_init):
        '''
        1、点击首页搜索框
        2、提取搜索框文本
        3、点击搜索按钮
        4、断言页面是否正常跳转到对应的搜索结果页
        '''
        self.home.clickHomeSearch()
        SearchText = self.searchpanel.clickSearchText()
        self.searchpanel.clickSearchInto()
        self.base.assertTrue(SearchText)


    # ---wmw
    @allure.story('测试历史面板热词是否正常跳转')
    def test002SearchPanelPage(self, search_init):
        '''
        1、点击首页搜索框
        2、获取第一个热词文本
        3、点击历史面板热词(默认第一个)
        4、断言页面是否打开正确
        '''
        self.home.clickHomeSearch()
        OneSearchHistory = self.searchpanel.clickHotWords()
        self.searchpanel.clickSearchHistory()
        self.base.assertTrue(OneSearchHistory)

    # ---wmw
    @allure.story('测试换一换')
    def test003SearchPanelPage(self, search_init):
        '''
        1、点击首页搜索框
        2、获取第一个搜索热词
        3、点击换一换
        4、断言第一个搜索热词是否不存在
        '''
        self.home.clickHomeSearch()
        Panel = self.searchpanel.clickHotWords()
        self.searchpanel.clickAnotherChange()
        self.base.assertTrue(Panel,False,timeout=15)

    @allure.story('搜索页顶部地址栏输入，选中文字')
    def test004SearchPanelPage(self, search_init):
        '''
        1、点击首页搜索框
        2、点击输入框工具条前缀词“www.”
        3、长按并选中地址栏中的“www.”
        4、点击搜索框联想词，并打开网址
        5、点击地址栏，清空地址，显示搜索历史
        6.清空搜索历史
        '''
        # 点击首页搜索框
        self.home.clickHomeSearch()
        # 点击输入框工具条前缀词“www.”
        self.searchpanel.clickInputPanelPrefixes()
        # 拖动输入框工具条，选中地址栏文字
        self.searchpanel.swipe_InputPanel()
        # 点击搜索框，弹框消失
        self.searchpanel.clickSearchPanel()
        # 点击搜索框联想词
        self.searchpanel.clickAutomatedWord()
        # 判断是否正常打开flyme官网
        self.base.assertTrue(FLYME_WEBSITE)
        # 点击搜索框，清空地址
        self.searchpanel.clickSearchPanel()
        self.searchpanel.clearSearchPanel()
        # 判断搜索历史是否存在
        self.base.assertTrue(SEARCHHISTORY)
        # 清空搜索历史
        self.searchpanel.clearSearchHistory()
        self.base.assertTrue(SEARCHHISTORY,False)

    @allure.story('打开百度首页，滑动页面检查顶部地址栏是否高亮，点击搜索历史')
    def test005SearchPanelPage(self, search_init):
        '''
        1、点击首页搜索框，输入百度网址
        2、打开百度首页，滑动页面
        3、检查顶部地址栏是否展开
        4、检查搜索历史,长按删除
        '''
        # 点击首页搜索框
        self.home.clickHomeSearch()
        # 输入百度地址,进入百度首页
        self.searchpanel.inputBaidu()
        self.searchpanel.clickSearchInto()
        # 监听地理位置弹框，点击“始终允许”
        # self.base.browserWatcher()
        # 判断顶部地址栏是否展开
        self.base.assertTrue(ADDRESS_CONTAINER_REFRESH )
        # 向上滑动页面,收起顶部地址栏
        self.searchpanel.swipeBaidu()
        self.base.assertTrue(ADDRESS_CONTAINER_REFRESH,False)
        # 点击并清空地址栏，判断搜索历史是否存在
        self.searchpanel.clickwebsite()
        self.searchpanel.clearSearchPanel()
        self.base.assertTrue(SEARCHHISTORY)
        # 长按搜索历史中的百度网址
        self.searchpanel.long_clickSearchHistory()
        self.base.assertTrue(DELETESEARCHHISTORY)
        # 点击删除按钮
        self.searchpanel.delete_SearchHistory()
        self.base.assertTrue(DELETESEARCHHISTORY,False)

    @allure.story('搜索框输入主题美化地址，检查外部应用跳转是否正常')
    def test006SearchPanelPage(self, search_init):
        '''

        1、点击首页搜索框，输入主题美化地址
        2、弹出跳转提示，点击允许，跳转至主题美化APP
        '''
        # 点击首页搜索框
        self.home.clickHomeSearch()
        # 输入百度地址,进入百度首页
        self.searchpanel.inputCustomize()
        self.searchpanel.clickSearchInto()
        self.searchpanel.skipCustomize()
        self.base.assertTrue(CUSTOMIZE)







