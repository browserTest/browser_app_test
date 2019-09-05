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



@allure.feature("魅族浏览器网址导航页面测试")
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
        self.base.unlock()
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")


    @allure.story('测试网址导航页面头条跳转')
    @pytest.mark.P0
    def test001MorePage(self, home_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"头条"
        3、断言是否跳转到"头条"页面

        '''
        # 首次进入浏览器，根据显示页面点击home键回到主页
        self.home.clickHomeOnPage(HOME_PAGE)
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》头条
        self.more.clickDaoHang(TOUTIAO)
        self.base.assertTrue(TOUTIAO_PAGE, timeout = 15)


    @allure.story('测试网址导航页面小视频跳转')
    @pytest.mark.P0
    def test002MorePage(self, home_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"小视频"
        3、断言是否跳转到"小视频"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》小视频
        self.more.clickDaoHang(SMALL_VIDEO)
        self.base.assertTrue(SMALL_VIDEO_PAGE, timeout=15)

    @allure.story('测试网址导航页面搜狐跳转')
    @pytest.mark.P1
    def test003MorePage(self, home_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"搜狐"
        3、断言是否跳转到"搜狐"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》搜狐
        self.more.clickDaoHang(SOUHU)
        self.base.assertTrue(SOUHU_PAGE, timeout=15)

    @allure.story('测试网址导航页面漫画跳转')
    @pytest.mark.P1
    def test004MorePage(self, home_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"漫画"
        3、断言是否跳转到"漫画"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》漫画
        self.more.clickDaoHang(MANHUA)
        self.base.assertTrue(MANHUA_PAGE, timeout=15)

    @allure.story('测试网址导航页面小说跳转')
    @pytest.mark.P1
    def test005MorePage(self, home_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"小说"
        3、断言是否跳转到"小说"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》小说
        self.more.clickDaoHang(BOOK)
        self.base.assertTrue(BOOK_PAGE, timeout=15)

    @allure.story('测试网址导航页面钱包跳转')
    @pytest.mark.P1
    def test006MorePage(self, home_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"钱包"
        3、断言是否跳转到"钱包"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》钱包
        self.more.clickDaoHang(MONEY)
        self.base.assertTrue(MONEY_PAGE, timeout=15)

    @allure.story('测试网址导航页面搞笑跳转')
    @pytest.mark.P1
    def test007MorePage(self, home_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"搞笑"
        3、断言是否跳转到"搞笑"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》搞笑
        self.more.clickDaoHang(FUNNY)
        self.base.assertTrue(FUNNY_PAGE, timeout=15)

    @allure.story('测试网址导航页面京东跳转')
    @pytest.mark.P1
    def test008MorePage(self, home_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"京东"
        3、断言是否跳转到"京东"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》京东
        self.more.clickDaoHang(JD)
        self.base.assertTrue(JD_PAGE, timeout=15)

    @allure.story('测试网址导航页面中文跳转')
    @pytest.mark.P1
    def test009MorePage(self, home_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"中文"
        3、断言是否跳转到"中文"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》中文
        self.more.clickDaoHang(ZH)
        self.base.assertTrue(ZH_PAGE, timeout=15)

    @allure.story('测试网址导航页面聚划算跳转')
    @pytest.mark.P1
    def test010MorePage(self, home_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"聚划算"
        3、断言是否跳转到"聚划算"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》聚划算
        self.more.clickDaoHang(JHS)
        self.base.assertTrue(JHS_PAGE, timeout=15)

    @allure.story('测试网址导航页面同城跳转')
    @pytest.mark.P1
    def test011MorePage(self, home_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"同城"
        3、断言是否跳转到"同城"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》同城
        self.more.clickDaoHang(TONGCHEN)
        self.base.assertTrue(TONGCHEN_PAGE, timeout=15)

    @allure.story('测试网址导航页面星座跳转')
    @pytest.mark.P1
    def test012MorePage(self, home_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"找房子"
        3、断言是否跳转到"找房子"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》找房子
        self.more.clickDaoHang(FINDHOUSE)
        self.base.assertTrue(FINDHOUSE_PAGE, timeout=15)
