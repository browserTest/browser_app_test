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
    def more_init(self, scope="function"):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.more = MorePage(self.driver)
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


    @allure.story('测试网址导航页面1-头条跳转')
    @pytest.mark.P3
    def test001MorePage(self, more_init):
        '''
        1、在浏览器首页点击导航栏中"更多"按钮，进入到浏览器网址导航页面
        2、点击"头条"
        3、断言是否跳转到"头条"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》头条
        self.more.clickDaoHang(TOUTIAO)
        self.base.assertTrue(TOUTIAO_PAGE)



    @allure.story('测试网址导航页面搜狐跳转')
    @pytest.mark.P1
    def test002MorePage(self, more_init):
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



    @allure.story('测试网址导航页面8-京东跳转')
    @pytest.mark.P1
    def test003MorePage(self, more_init):
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



    @allure.story('测试网址导航页面11-聚划算跳转')
    @pytest.mark.P1
    def test004MorePage(self, more_init):
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

    @allure.story('测试网址导航页面4-同城跳转')
    @pytest.mark.P1
    def test005MorePage(self, more_init):
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

    @allure.story('测试网址导航页面6-找房子跳转')
    @pytest.mark.P1
    def test006MorePage(self, more_init):
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

    @allure.story('测试网址导航页面2-在线商城跳转')
    def test007MorePage(self, more_init):
        '''
        1、在浏览器首页点击导航栏中"在线商城"按钮，进入到浏览器网址导航页面
        2、点击"在线商城"
        3、断言是否跳转到"在线商城"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》在线商城
        self.more.clickDaoHang(MALL)
        self.base.assertTrue(MALL_PAGE)

    @allure.story('测试网址导航页面3-二手市场跳转')
    def test008MorePage(self, more_init):
        '''
        1、在浏览器首页点击导航栏中"二手市场"按钮，进入到浏览器网址导航页面
        2、点击"二手市场"
        3、断言是否跳转到"二手市场"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》二手市场
        self.more.clickDaoHang(FLEA_MARKET)
        self.base.assertTrue(FLEA_MARKET_PAGE)

    @allure.story('测试网址导航页面5-安居客跳转')
    def test009MorePage(self, more_init):
        '''
        1、在浏览器首页点击导航栏中"安居客"按钮，进入到浏览器网址导航页面
        2、点击"安居客"
        3、断言是否跳转到"安居客"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》安居客
        self.more.clickDaoHang(ANJUKE)
        self.base.assertTrue(ANJUKE_PAGE)

    @allure.story('测试网址导航页面7-爱淘宝跳转')
    def test010MorePage(self, more_init):
        '''
        1、在浏览器首页点击导航栏中"爱淘宝"按钮，进入到浏览器网址导航页面
        2、点击"爱淘宝"
        3、断言是否跳转到"爱淘宝"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》爱淘宝
        self.more.clickDaoHang(AITAOBAO)
        self.base.assertTrue(AITAOBAO_PAGE)

    @allure.story('测试网址导航页面9-天猫跳转')
    def test011MorePage(self, more_init):
        '''
        1、在浏览器首页点击导航栏中"天猫"按钮，进入到浏览器网址导航页面
        2、点击"天猫"
        3、断言是否跳转到"天猫"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》天猫
        self.more.clickDaoHang(TIANMAO)
        self.base.assertTrue(TIANMAO_PAGE)

    @allure.story('测试网址导航页面10-拼多多跳转')
    def test012MorePage(self, more_init):
        '''
        1、在浏览器首页点击导航栏中"拼多多"按钮，进入到浏览器网址导航页面
        2、点击"拼多多"
        3、断言是否跳转到"拼多多"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》拼多多
        self.more.clickDaoHang(PINDUODUO)
        self.base.assertTrue(PINDUODUO_PAGE)

    @allure.story('测试网址导航页面12-招聘跳转')
    def test013MorePage(self, more_init):
        '''
        1、在浏览器首页点击导航栏中"招聘"按钮，进入到浏览器网址导航页面
        2、点击"招聘"
        3、断言是否跳转到"招聘"页面

        '''
        # 点击导航栏-》更多
        self.home.clickBusinessMore()
        # 点击网址导航-》招聘
        self.more.clickDaoHang(ZHAOPIN)
        self.base.assertTrue(ZHAOPIN_PAGE)