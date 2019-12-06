from base_function.driver import *
import pytest
from config.config import *
from browser.browser_page.HomePage import HomePage
from browser.browser_page.PubMethod import PubMethod
from browser.browser_element.PubElement import *
from browser.browser_page.MorePage import MorePage
from base_function.base import Base
from browser.browser_element.Home import *
import allure
from browser.browser_element.CollectionAndHistory import *
from browser.browser_page.SharePage import *



@allure.feature("测试资讯流页面")
@pytest.mark.usefixtures("driver_setup")
class TestHomePage():

    @pytest.fixture(scope="function")
    def home_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.share = SharePage(self.driver)
        self.more = MorePage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.home.clickHome()
        self.home.clickHomeOnPage(HOME_PAGE)
        yield
        logging.info("****用例执行结束****")
        logging.info("")


    @allure.story('测试资讯流页面存在相应text')
    def test001HomePage(self, home_init):
        '''
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


    @allure.story('测试资讯流广告')
    def test002HomePage(self, home_init):

        #点击资讯
        self.home.clickInformation()

        self.home.clickInformation()
        sleep(5)
        self.base.scrollToElement('广告')
        #self.base.clickByElement('广告')
        self.home.clickAdvertisement()

    @allure.story('测试前进后退')
    def test003HomePage(self, home_init):
        '''
        1、打开首页导航栏的安居客网址
        2、点击安居客首页的“新房”
        3、手势后退至安居客首页，再手势前进至“新房”页面
        '''
        self.share.clickAnjuke()
        self.home.clickNewHouse()
        self.home.right_swipe()
        self.base.assertTrue(ANJUKE_SEARCH)
        self.home.left_swipe()
        self.base.assertTrue(NEWHOUSE_SEARCH)


    @allure.story('测试爱淘宝能否正常打开')
    def test004HomePage(self, home_init):
        '''
        1、点击"爱淘宝"
        2、断言是否跳转到"爱淘宝"页面
        '''
        # 点击网址导航-》爱淘宝
        self.more.clickDaoHang(AITAOBAO)
        self.base.assertTrue(AITAOBAO_PAGE)

    @allure.story('测试搜索能否正常打开')
    def test005HomePage(self, home_init):
        '''
        1、点击"搜索"
        2、断言是否跳转到"搜索"页面
        '''
        # 点击网址导航-》搜索
        self.more.clickDaoHang(WEB_SEARCH)
        self.base.browserWatcher()
        self.base.assertTrue(WEB_SEARCH_PAGE)

    @allure.story('测试聚划算能否正常打开')
    def test006HomePage(self, home_init):
        '''
        1、点击"聚划算"
        2、断言是否跳转到"聚划算"页面
        '''
        # 点击网址导航-》聚划算
        self.more.clickDaoHang(JHS)
        self.base.assertTrue(JHS_PAGE)

    @allure.story('测试天猫能否正常打开')
    def test007HomePage(self, home_init):
        '''
        1、点击"天猫"
        2、断言是否跳转到"天猫"页面
        '''
        # 点击网址导航-》天猫
        self.more.clickDaoHang(TIANMAO)
        self.base.assertTrue(TIANMAO_PAGE)

    @allure.story('测试同城能否正常打开')
    def test008HomePage(self, home_init):
        '''
        1、点击"同城"
        2、断言是否跳转到"同城"页面
        '''
        # 点击网址导航-》同城
        self.more.clickDaoHang(TONGCHEN)
        self.base.assertTrue(TONGCHEN_PAGE)

    @allure.story('测试京东能否正常打开')
    def test009HomePage(self, home_init):
        '''
        1、点击"京东"
        2、断言是否跳转到"京东"页面
        '''
        # 点击网址导航-》京东
        self.more.clickDaoHang(JD)
        self.base.assertTrue(JD_PAGE)

    @allure.story('测试招聘能否正常打开')
    def test010HomePage(self, home_init):
        '''
        1、点击"招聘"
        2、断言是否跳转到"招聘"页面
        '''
        # 点击网址导航-》招聘
        self.more.clickDaoHang(ZHAOPIN)
        self.base.assertTrue(ZHAOPIN_PAGE)

    @allure.story('测试拼多多能否正常打开')
    def test011HomePage(self, home_init):
        '''
        1、点击"拼多多"
        2、断言是否跳转到"拼多多"页面
        '''
        # 点击网址导航-》拼多多
        self.more.clickDaoHang(PINDUODUO)
        self.base.assertTrue(PINDUODUO_PAGE)

    @allure.story('测试安居客能否正常打开')
    def test012HomePage(self, home_init):
        '''
        1、点击"安居客"
        2、断言是否跳转到"安居客"页面
        '''
        # 点击网址导航-》安居客
        self.more.clickDaoHang(ANJUKE)
        self.base.assertTrue(ANJUKE_PAGE)

    @allure.story('测试今日头条能否正常打开')
    def test013HomePage(self, home_init):
        '''
        1、点击"今日头条"
        2、断言是否跳转到"今日头条"页面
        '''
        # 点击网址导航-》今日头条
        self.more.clickDaoHang(TOUTIAO)
        self.base.assertTrue(TOUTIAO_PAGE)

    @allure.story('测试小说能否正常打开')
    def test014HomePage(self, home_init):
        '''
        1、点击"热门小说"
        2、断言是否跳转到"小说"页面
        '''
        # 点击导航栏-》更多
        self.more.clickDaoHang(HOT_NOVEL)
        self.base.browserWatcher()
        self.base.assertTrue(NOVEL_BOOKSHELF)














