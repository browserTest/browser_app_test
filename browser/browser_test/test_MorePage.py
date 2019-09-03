from base_function.driver import *
import pytest,allure
from config.config import *
from browser.browser_page.HomePage import HomePage
from browser.browser_page.PubMethod import PubMethod
from browser.browser_element.PubElement import *
from base_function.base import Base
from browser.browser_element.Home import *
from browser.browser_page.MorePage import MorePage
from browser.browser_element.More import *



@allure.feature("测试首页")
@pytest.mark.usefixtures("driver_setup")
class TestMorePage():

    @pytest.fixture()
    def home_init(self, scope="function"):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.more = MorePage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        sleep(2)
        yield
        logging.info("****用例执行结束****")
        logging.info("")


    @allure.story('测试网址导航页面头条跳转')
    def test001MorePage(self, home_init):
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》头条
        self.more.clickDaoHang(TOUTIAO)
        self.base.assertTrue(TOUTIAO_PAGE, timeout = 10)

    @allure.story('测试网址导航页面小视频跳转')
    def test002MorePage(self, home_init):
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》小视频
        self.more.clickDaoHang(SMALL_VIDEO)
        self.base.assertTrue(SMALL_VIDEO_PAGE, timeout=10)

    @allure.story('测试网址导航页面搜狐跳转')
    def test003MorePage(self, home_init):
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》搜狐
        self.more.clickDaoHang(SOUHU)
        self.base.assertTrue(SOUHU_PAGE, timeout=10)

    @allure.story('测试网址导航页面漫画跳转')
    def test004MorePage(self, home_init):
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》漫画
        self.more.clickDaoHang(MANHUA)
        self.base.assertTrue(MANHUA_PAGE, timeout=10)

    @allure.story('测试网址导航页面小说跳转')
    def test005MorePage(self, home_init):
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》小说
        self.more.clickDaoHang(BOOK)
        self.base.assertTrue(BOOK_PAGE, timeout=10)

    @allure.story('测试网址导航页面钱包跳转')
    def test006MorePage(self, home_init):
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》钱包
        self.more.clickDaoHang(MONEY)
        self.base.assertTrue(MONEY_PAGE, timeout=10)

    @allure.story('测试网址导航页面搞笑跳转')
    def test007MorePage(self, home_init):
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》搞笑
        self.more.clickDaoHang(FUNNY)
        self.base.assertTrue(FUNNY_PAGE, timeout=10)

    @allure.story('测试网址导航页面京东跳转')
    def test008MorePage(self, home_init):
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》京东
        self.more.clickDaoHang(JD)
        self.base.assertTrue(JD_PAGE, timeout=10)

    @allure.story('测试网址导航页面中文跳转')
    def test009MorePage(self, home_init):
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》中文
        self.more.clickDaoHang(ZH)
        self.base.assertTrue(ZH_PAGE, timeout=10)

    @allure.story('测试网址导航页面聚划算跳转')
    def test010MorePage(self, home_init):
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》搜狐
        self.more.clickDaoHang(JHS)
        self.base.assertTrue(JHS_PAGE, timeout=10)

    @allure.story('测试网址导航页面同城跳转')
    def test011MorePage(self, home_init):
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》搜狐
        self.more.clickDaoHang(TONGCHEN)
        self.base.assertTrue(TONGCHEN_PAGE, timeout=10)

    @allure.story('测试网址导航页面星座跳转')
    def test012MorePage(self, home_init):
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》搜狐
        self.more.clickDaoHang(XINGZUO)
        self.base.assertTrue(XINGZUO_PAGE, timeout=10)
