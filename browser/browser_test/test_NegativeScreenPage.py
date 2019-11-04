import allure
import pytest
from base_function.base import *
from browser.browser_page.AddToHomePage import *
from browser.browser_page.HomePage import *
from browser.browser_page.NegativeScreenPage import *
from browser.browser_page.PubMethod import *
from browser.browser_element.AddToHome import *
from browser.browser_page.SearchPanelPage import *


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
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")

    @allure.story('测试负一屏-》精选页打开网站、添加书签')
    @pytest.mark.P1
    def test001AddToHomeWebsite(self, negative_init):
        # 进入负一屏
        self.home.clickHomeOnPage(MYCOLLECTION)
        # 删除"hao123"书签
        self.negativescreen.deleteBookmark(HAO123)
        # 点击“添加”
        self.negativescreen.clickAddTo()
        # 在精选页面对"hao123"书签点击"添加"
        self.addtohome.clickAddToHome(2)
        # 点击"hao123"进入网页
        self.addtohome.clickAddToHomeWebsite(HAO123)
        # 断言是否进入"hao123"网页
        self.base.assertTrue(HAO123, timeout=5)
        # 返回上一层到负一屏
        self.pubmethod.clickBack()
        # 断言是否存在"hao123"书签
        self.base.assertTrue(HAO123, timeout=3)

    @allure.story('测试负一屏-》分类页打开网站、添加书签')
    @pytest.mark.P1
    def test002AddToHomeWebsite(self, negative_init):
        # 进入负一屏
        self.home.clickHomeOnPage(MYCOLLECTION)
        # 删除"凤凰网"书签
        self.negativescreen.deleteBookmark(IFENG_SIMPLIFIED)
        # 进入分类-》资讯头条
        self.negativescreen.clickAddTo()
        self.addtohome.clickAddToHomeClassify()
        self.addtohome.clickAddToHomeReader()
        # 对"凤凰网"书签点击"添加"
        self.addtohome.clickAddToHome(1)
        # 点击"凤凰网"进入网页
        self.addtohome.clickAddToHomeWebsite(IFENG_SIMPLIFIED)
        # 断言是否进入"凤凰网"网页
        self.base.assertTrue(IFENG_TRADITIONAL, timeout=5)
        # 返回上一层到负一屏
        self.pubmethod.clickBack()
        # 断言是否存在"凤凰网"书签
        self.base.assertTrue(IFENG_SIMPLIFIED, timeout=3)

    @allure.story('测试负一屏-》历史页打开网站、添加书签')
    @pytest.mark.P0
    def test003AddToHomeWebsite(self, negative_init):
        # 进入负一屏
        self.home.clickHomeOnPage(MYCOLLECTION)
        # 点击搜索框
        self.home.clickHomeSearch()
        # 搜索框'm.baidu.com'
        self.base.elementSetText(SEARCHPANEL_WEBSITE, 'm.baidu.com', '搜索框输入"m.baidu.com"')
        self.searchpanel.clickSearchInto()
        # 返回上一层到负一屏
        self.pubmethod.clickBack()
        # 在负一屏点击"添加"
        self.negativescreen.clickAddTo()
        # 进入历史
        self.addtohome.clickAddToHomeHistory()
        # 断言是否存在"百度一下"网页
        self.base.assertTrue(BAIDU_TEXT, timeout=3)
        # 对第1个网页点击"添加"
        self.addtohome.clickAddToHome(1)
        # 点击"百度一下"进入网页
        self.addtohome.clickAddToHomeWebsite(BAIDU_TEXT)
        # 断言是否进入"百度一下"网页
        self.base.assertTrue(BAIDU_TEXT, timeout=3)

    @allure.story('测试负一屏-》自定义页打开网站')
    @pytest.mark.P0
    def test004AddToHomeWebsite(self, negative_init):
        # 进入负一屏
        self.home.clickHomeOnPage(MYCOLLECTION)
        # 在负一屏点击"添加"
        self.negativescreen.clickAddTo()
        # 点击"hao123"进入网页
        self.addtohome.clickAddToHomeWebsite()
        # 断言是否进入"hao123"网页
        self.base.assertTrue(HAO123, timeout=3)







