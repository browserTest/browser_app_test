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

    @allure.story('测试首页12个导航位能否正常打开')
    def test004HomePage(self, home_init):
        '''
        1、获取首页12个导航位名称
        2、依次打开12个导航位（小说除外），均能正常跳转
        '''
        HOME_BUSINESS_NAME = self.home.get_HomeBusiness()
        for i in range(0,12):
            if HOME_BUSINESS_NAME[i] == "热门小说" :
                continue
            self.more.clickDaoHang(HOME_BUSINESS_NAME[i])
            self.base.browserWatcher()
            if HOME_BUSINESS_NAME[i] == "头条" :
                self.base.assertTrue(TOUTIAO)
            elif HOME_BUSINESS_NAME[i] == "安居客":
                self.base.assertTrue(ANJUKE_SEARCH)
            elif HOME_BUSINESS_NAME[i] == "酷站":
                self.base.assertTrue(KUZHAN)
            else:
                self.base.assertTrue(HOME_BUSINESS_NAME[i])
            self.pubmethod.clickBack()


    @allure.story('测试小说能否正常打开')
    def test005HomePage(self, home_init):
        '''
        1、点击"热门小说"
        2、断言是否跳转到"小说"页面
        '''
        # 点击导航栏-》更多
        self.more.clickDaoHang(HOT_NOVEL)
        self.base.browserWatcher()
        self.base.assertTrue(NOVEL_BOOKSHELF)




















