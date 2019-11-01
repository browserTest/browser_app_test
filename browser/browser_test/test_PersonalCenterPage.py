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
from browser.browser_page.ToolBarPanelPage import *
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
        self.toolbarpanel = ToolBarPanelPage(self.driver)
        self.personalcenter = PersonalCenterPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")

'''
    # ---wmw
    @allure.story('测试个人中心账号登录页')
    def test001PersonalCenterPage(self, PersonalCenter_init):

        # 点击工具菜单
        self.home.clickMore()
        #点击我的账号图标
        self.toolbarpanel.clickFlyme_me()
        # 查找未登录是否存在
        if self.base.elementIsExit(PERSONAL_CENTER_NOT_LOGGED_IN):
            # 存在未登录，点击我的账号图标
            self.personalcenter.clickFlymemeA()
            self.base.assertTrue(PERSONAL_CENTER_REGISTER)
        else:
            # 点击mback返回首页
            self.pubmethod.clickBack()
            # 点击资讯
            self.home.clickInformation()
'''


