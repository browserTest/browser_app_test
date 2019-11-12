
import pytest,allure
from config.config import *
from browser.browser_page.HomePage import HomePage
from browser.browser_page.PubMethod import PubMethod
from browser.browser_element.PubElement import *
from browser.browser_page.MorePage import MorePage
from browser.browser_page.SharePage import *


@allure.feature("魅族浏览器分享功能测试")
@pytest.mark.usefixtures("driver_setup")
class TestSharePage():

    @pytest.fixture(scope="function")
    def share_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.more = MorePage(self.driver)
        self.share = SharePage(self.driver)
        # self.zixun = ZiXunInformationPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.base.unlock()
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.home.clickHome()
        self.home.clickHomeOnPage(HOME_PAGE)
        yield
        logging.info("****用例执行结束****")
        logging.info("")


    @allure.story('测试分享网页到便签')
    @pytest.mark.P0
    def test001ShareWebPage(self, share_init):
        '''
        1、进入浏览器，点击导航网站-》安居客
        2、在安居客网页中点击底部-》工具栏图标按钮
        3、点击底部工具栏-》点击分享按钮
        4、点击分享面板-》便签按钮到便签
        5、断言便签应用中是否存在分享的内容
        '''
        self.more.clickDaoHang(HOME_ANJUKE)
        self.home.clickMore()
        self.share.clickWebPageShare()
        self.share.clickNotes()
        self.base.assertTrue(SHARE_TEXT, timeout = 5)

