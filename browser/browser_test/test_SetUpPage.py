from browser.browser_page.PubMethod import PubMethod
from browser.browser_page.SetUpPage import *
from browser.browser_page.HomePage import *
from browser.browser_page.ToolBarPanelPage import *
from browser.browser_page.SearchPanelPage import *
from browser.browser_page.ZiXunInformationPage import *
import allure






@allure.feature("测试设置页面")
@pytest.mark.usefixtures("driver_setup")
class TestSetUpPage():

    @pytest.fixture(scope="function")
    def setUp_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.searchpanel = SearchPanelPage(self.driver)
        self.toolbarpanel = ToolBarPanelPage(self.driver)
        self.setup = SetUpPage(self.driver)
        self.zixuninformation = ZiXunInformationPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.home.clickHome()
        self.home.clickHomeOnPage(HOME_PAGE)
        yield
        logging.info("****用例执行结束****")
        logging.info("")

    # ---wmw
    @allure.story('测试简版显示是否正常')
    def test001SetUpPage(self, setUp_init):

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

        # 点击简版显示--更多
        self.setup.clickSetUpMore()
        # 提取资讯流页面第一个文章的文本信息
        Text = self.zixuninformation.getZiXunArticleTitle()
        # 点击工具栏资讯刷新页面
        self.home.clickInformation()
        # 断言页面是否存刷新成功
        self.base.assertTrue(Text)
        sleep(5)
        # 打开资讯文章
        self.zixuninformation.clickOpenZiXunArticle()
        # 断言是否正常打开
        self.base.assertTrue(ZIXUN_PAGE_MOREMENU)
        # 点击mback
        self.pubmethod.clickBack()


    # ---wmw
    @allure.story('测试设置清除浏览器')
    def test002SetUpPage(self, setUp_init):
        '''

        1、点击主页工具菜单
        2、点击设置
        3、点击清除浏览器数据
        4、点击Cookies
        5、点击账号密码
        6、点击地理位置授权
        7、点击清除数据按钮
        8、点击完成按钮
        9、点击mback返回
        10、点击首页搜索框
        11、搜索框输入文本
        12、点击进入
        13、断言页面是否会重新提示地址位置授权

        '''
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
        # 搜索框输入文本"www.baidu.com"
        self.setup.inputbaidu()
        # 点击进入
        self.searchpanel.clickSearchInto()
        # 断言页面是否会重新提示地址位置授权
        self.base.assertTrue(GEOGRAPHY)
        # 点击允许
        self.setup.clickAllow()
        # self.pubmethod.clickBack()

    # ---wmw
    @allure.story('测试切换搜索引擎')
    def test003SetUpPage(self, setUp_init):
        '''

        1、点击主页工具菜单
        2、点击设置
        3、点击搜索引擎
        4、点击百度
        5、点击mback返回
        6、点击首页搜索框
        7、搜索框输入123
        8、点击搜索
        9、# 断言页面是否存在百度

        '''
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
        self.base.assertTrue(SETUP_BAIDU)

    # ---wmw
    @allure.story('测试恢复默认设置')
    def test004SetUpPage(self, setUp_init):
        '''
        1、点击主页工具菜单
        2、点击设置
        3、点击广告屏蔽
        4、获取未点击前，广告屏蔽，锁定竖屏，精选内容推送开关状态
        5、点击锁定竖屏
        6、点击精选内容推送
        7、向下滑动到恢复默认设置
        8、点击恢复默认设置
        9、点击恢复
        10、点击主页工具菜单
        11、点击设置
        12、获取点击后，广告屏蔽，锁定竖屏，精选内容推送开关状态
        13、判断点击恢复默认设置前，广告屏蔽开关状态和恢复后广告屏蔽开关状态
        '''

        # 点击主页工具菜单
        self.home.clickMore()
        # 点击设置
        self.toolbarpanel.clickSetUp()
        # 点击广告屏蔽
        self.setup.clickBlockAds(0)
        BeforeBlockAdsText = self.setup.clickSwitch()
        BeforeLockingVerticalScreen = self.setup.clickSwitch()
        BeforeSwipeLeftRight = self.setup.clickSwitch()
        # 点击锁定竖屏
        self.setup.clickLockingVerticalScreen(4)
        # 点击精选内容推送
        self.setup.clickSwipeLeftRight(6)
        # 向下滑动到恢复默认设置
        self.base.scrollToElement(SETUP_RESET_TEXT)
        # 点击恢复默认设置
        self.setup.clickResetToDefault(8)
        # 点击恢复
        self.setup.clickReset()
        # 点击主页工具菜单
        self.home.clickMore()
        # 点击设置
        self.toolbarpanel.clickSetUp()
        AfterBlockAdsText = self.setup.clickSwitch()
        AfterLockingVerticalScreen = self.setup.clickSwitch()
        AfterSwipeLeftRight = self.setup.clickSwitch()
        # 判断点击恢复默认设置前，广告屏蔽开关状态和恢复后广告屏蔽开关状态
        assert BeforeBlockAdsText != AfterBlockAdsText
        assert BeforeLockingVerticalScreen != AfterLockingVerticalScreen
        assert BeforeSwipeLeftRight != AfterSwipeLeftRight




