from base_function.driver import *
import pytest
from config.config import *
from browser.browser_page.HomePage import HomePage
from browser.browser_page.PubMethod import PubMethod
from browser.browser_element.PubElement import *
from base_function.base import Base
from browser.browser_element.Home import *
from browser.browser_page.SetUpPage import *
from browser.browser_page.HomePage import *
from browser.browser_page.ToolBarPanelPage import *
from browser.browser_page.SearchPanelPage import *
from browser.browser_page.ZiXunInformationElementPage import *
import allure
from browser.browser_element.MyCollection import *





@allure.feature("测试设置页面")
@pytest.mark.usefixtures("driver_setup")
class TestSetUpPage():

    @pytest.fixture(scope="function")
    def SetUp_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.searchpanel = SearchPanelPage(self.driver)
        self.toolbarpanel = ToolBarPanelPage(self.driver)
        #self.zixuninformationelement = ZiXunInformationElementPage(self.driver)
        self.setup = SetUpPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")

    # ---wmw
    @allure.story('测试简版显示是否正常')
    def test001SetUpPage(self, SetUp_init):

        # 点击主页工具菜单
        self.home.clickMore()
        # 点击设置
        self.toolbarpanel.clickSetUp()
        # 点击魅族头条设置
        self.setup.clickMeizuHeadlinesSettings(2)
        # 点击简版显示
        self.setup.clickSimple()
        # 点击mback
        self.pubmethod.clickBack()
        # 断言页面魅族头条是否存在
        self.base.assertTrue(SETUP_MEIZU_HEADLINES)
        #
        # # 点击简版显示--更多
        # self.setup.clickSetUpMore()
        # # 提取资讯流页面第一个文章的文本信息
        # Text = self.zixuninformationelement.clickText(0)
        # # 点击工具栏资讯刷新页面
        # self.home.clickInformation()
        # #断言页面是否存刷新成功
        # self.base.assertTrue(Text)
        # # 点击第一篇文章
        # self.zixuninformationelement.clickOneArticle(0)
        # # 断言是否正常打开文章详情页


    # ---wmw
    @allure.story('测试设置清除浏览器')
    def test002SetUpPage(self, SetUp_init):

        # 点击主页工具菜单
        self.home.clickMore()
        # 点击设置
        self.toolbarpanel.clickSetUp()
        # 点击清除浏览器数据
        self.setup.clickClearCoolkies(5)
        # 点击Cookies
        self.setup.clickCookies()
        # 点击账号密码
        self.setup.clickAccountsAndPasswords()
        # 点击地理位置授权
        self.setup.clickLocationAccess()
        # 点击清除数据按钮
        self.setup.clickClearData()
        # 点击完成按钮
        self.setup.clickDone()
        # 点击mback
        self.pubmethod.clickBack()
        # 点击首页搜索框
        self.home.clickHomeSearch()
        #搜索框输入文本
        self.setup.inputbaidu()
        # 点击进入
        self.searchpanel.clickSearchInto()
        # 断言页面是否会重新提示地址位置授权
        self.base.assertTrue('地理位置权限')


    # ---wmw
    @allure.story('测试切换搜索引擎')
    def test003SetUpPage(self, SetUp_init):

        # 点击主页工具菜单
        self.home.clickMore()
        # 点击设置
        self.toolbarpanel.clickSetUp()
        # 点击搜索引擎
        self.setup.clickSearchEngine(1)
        # 点击百度
        self.setup.clickBaidu()
        # 点击mback
        self.pubmethod.clickBack()
        # 点击首页搜索框
        self.home.clickHomeSearch()
        # 搜索框输入123
        self.setup.inputNumber()
        # 点击搜索
        self.searchpanel.clickSearchInto()
        # 断言页面是否存在百度
        self.base.assertTrue('百度')






