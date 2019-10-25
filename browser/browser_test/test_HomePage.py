from base_function.driver import *
import pytest
from config.config import *
from browser.browser_page.HomePage import HomePage
from browser.browser_page.PubMethod import PubMethod
from browser.browser_element.PubElement import *
from base_function.base import Base
from browser.browser_element.Home import *
import allure
from browser.browser_element.MyCollection import *



@allure.feature("测试资讯流页面")
@pytest.mark.usefixtures("driver_setup")
class TestHomePage():

    @pytest.fixture(scope="function")
    def home_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")


    @allure.story('测试资讯流页面存在相应text')
    def test001HomePage(self, home_init):
        '''+
        1、点击地址栏more按钮
        2、点击back
        3、向下滑动页面进入到资讯流列表页
        4、向下滑动查找text
        '''
        self.home.clickMore()
        # sleep(2)
        self.pubmethod.clickBack()
        self.pubmethod.scrollPage(2)
        # self.pubmethod.clickHome()
        # self.pubmethod.scrollPageToElement('火爆动作片，话没说几句就开打，下手凶狠，血战到底')
        self.base.assertTrue('火爆动作片，话没说几句就开打，下手凶狠，血战到底', timeout = 5)


    # @allure.story('测试正常进入到我的收藏页面')
    # def test002MyCollection(self, home_init):
    #     self.home.clickMore()
    #     self.base.assertTrue("dkjkdsjfksdkfslkfsfs")














