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
from browser.browser_page.PersonalCenterPage import *
import allure
from browser.browser_element.MyCollection import *





@allure.feature("测试个人中心页面")
@pytest.mark.usefixtures("driver_setup")
class TestPersonalCenterPage():

    @pytest.fixture(scope="function")
    def PersonalCenter_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod= PubMethod(self.driver)
        self.personalcenter = PersonalCenterPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")

    # ---wmw
    @allure.story('测试个人中心账号登录页')
    def test001PersonalCenterPage(self, PersonalCenter_init):

        self.home.clickMore()
        self.toolbarpanel.clickFlymeme()
        # 查找未登录是否存在
        self.base.assertTrue333('未登录')