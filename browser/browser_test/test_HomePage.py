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



@allure.feature("测试首页")
@pytest.mark.usefixtures("driver_setup")
class TestHomePage():

    @pytest.fixture()
    def home_init(self, scope="function"):
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


    @allure.story('测试小红点不存在')
    def test001HomePage(self, home_init):
        self.home.clickMore()
        self.base.assertTrue(HOME_MORE_TIP, timeout = 5)


    # @allure.story('测试正常进入到我的收藏页面')
    # def test002MyCollection(self, home_init):
    #     self.home.clickMore()
    #     self.base.assertTrue("dkjkdsjfksdkfslkfsfs")














