
import pytest,allure
from config.config import *
from browser.browser_page.HomePage import HomePage
from browser.browser_page.PubMethod import PubMethod
from browser.browser_element.PubElement import *
from base_function.base import Base
from browser.browser_page.MorePage import MorePage
from browser.browser_element.More import *
from browser.browser_page.SharePage import *
from time import sleep

from conftest import browser_watcher


@allure.feature("魅族浏览器分享功能测试")
@pytest.mark.usefixtures("driver_setup")
class TestSharePage():

    @pytest.fixture()
    def more_init(self, scope="function"):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.more = MorePage(self.driver)
        self.share = SharePage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.base.unlock()
        # 通过 menu_more 工具图标判断当前页面是否存在，确认是否在浏览器页面中
        if self.base.elementIsExit(HOME_MORE):
            # 若在浏览器页面中则点击工具栏退出按钮直接退出应用
            self.share.clickOut(BROWSER_PACKAGE_NAME)
        else:
            # 若不在浏览器应用中，则直接打开浏览器
            self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")


    @allure.story('测试分享网页到便签')
    @pytest.mark.P0
    def test001ShareNetPage(self, more_init):
        '''
        1、在浏览器首页点击导航栏中"安居客"网站，进入安居客网页页面
        2、点击底部工具栏图标
        3、点击分享按钮
        4、点击分享到便签
        5、断言便签应用中是否存在分享的内容
        '''

        # self.pubmethod.clickPrivacyAgree()
        # self.share.clickAllow()
        # 首次进入浏览器，点击导航网站-》更多安居客
        self.more.clickDaoHang(HOME_ANJUKE)
        sleep(3)
        # 在安居客网页中点击底部工具栏图标按钮
        self.home.clickMore()
        # 点击底部工具栏-》分享到便签
        self.share.clickShare()
        # 断言便签中的内容
        self.base.assertTrue(SHARE_TEXT, timeout = 15)

