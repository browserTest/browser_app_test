from base_function.driver import *
import pytest
from config.config import *
from browser.browser_page.HomePage import HomePage
from browser.browser_page.PubMethod import PubMethod
from browser.browser_element.PubElement import *
from base_function.base import Base
from browser.browser_element.Home import *
from browser.browser_page.SearchPanelPage import *
from browser.browser_page.HomePage import *
import allure
from browser.browser_element.MyCollection import *





@allure.feature("测试资讯流页面")
@pytest.mark.usefixtures("driver_setup")
class TestSearchPanelPage():

    @pytest.fixture(scope="function")
    def home_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod= PubMethod(self.driver)
        self.searchpanel = SearchPanelPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")



    @allure.story('测试搜索框')
    def test001SearchPanelPage(self, home_init):
        '''
        1、点击首页搜索框
        2、提取搜索框文本
        3、点击搜索按钮
        4、提取结果页搜索框文本
        '''
        self.home.clickHomeSearch()
        self.base.clickObtain()
        self.searchpanel.clickSearch()
        self.base.clickObtain2()

    @allure.story('测试历史面板热词是否正常跳转')
    def test002SearchPanelPage(self, home_init):
        '''
        1、点击首页搜索框
        2、点击历史面板热词(默认第一个)
        '''
        self.home.clickHomeSearch()
        self.searchpanel.clickSearchHistory()

    @allure.story('测试换一换')
    def test003SearchPanelPage(self, home_init):
        '''
        1、点击首页搜索框
        2、点击换一换
        '''
        self.home.clickHomeSearch()
        self.searchpanel.clickAnotherChange()



