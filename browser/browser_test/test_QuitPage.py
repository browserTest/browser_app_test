import allure

from browser.browser_element.ToolbarPanel import *
from browser.browser_page.HomePage import *
from browser.browser_page.PubMethod import *
from browser.browser_page.ToolBarPanelPage import *
from browser.browser_page.WindowsTabPage import *


@allure.feature("魅族浏览器测试退出功能")
@pytest.mark.usefixtures("driver_setup")
class TestQuitPage():

    @pytest.fixture()
    def quit_init(self, scope="function"):
        self.base = Base(self.driver)
        self.more = MorePage(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.windowstab = WindowsTabPage(self.driver)
        self.quit = ToolBarPanelPage(self.driver)
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


    # 点击menu_more按钮，点击退出  ——LCM
    @allure.story('测试点击底部工具栏，点击退出按钮，再打开浏览器访问网页正常')
    def test001QuitOpenBrowser(self, quit_init):
        '''
        1、进入浏览器，点击导航网站-》安居客
        2、点击多窗口
        3、添加多窗口
        4、点击浏览的窗口tab网页
        5、点击底部工具栏的 menu_more 按钮
        6、点击退出按钮
        7、打开浏览器，点击导航网站-》更多
        8、断言页面中的搜索框默认词
        '''
        self.more.clickDaoHang(HOME_ANJUKE)
        self.windowstab.clickWindowsTab()
        self.windowstab.newWindowsTab(2)
        self.windowstab.openWindowsTabPage()
        self.home.clickMore()
        self.quit.clickToolsPanel(OUT)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.more.clickDaoHang(HOME_BUSINESS_MORE_TEXT)
        # 断言进入浏览器，点击导航网站-》更多，查看页面中搜索框默认词是否存在
        self.base.assertTrue(DEFAULT_WORD)


    # 点击menu_more按钮，点击退出  ——LCM
    @allure.story('测试点击底部工具栏，点击退出按钮，再打开浏览器，查看多窗口只有一个')
    def test002QuitOpenBrowser(self, quit_init):
        '''
        1、进入浏览器
        2、点击导航网站-》安居客
        3、点击多窗口
        4、添加多窗口（新增3个多窗口）
        5、点击浏览的窗口tab网页
        6、点击底部工具栏的 menu_more 按钮
        7、点击退出按钮
        8、打开浏览器
        9、断言多窗口数量不相等
        '''
        self.more.clickDaoHang(HOME_ANJUKE)
        self.windowstab.clickWindowsTab()
        self.windowstab.newWindowsTab(2)
        self.windowstab.openWindowsTabPage()
        winNumBefore = self.windowstab.getWindowsNum()
        self.home.clickMore()
        self.quit.clickToolsPanel(OUT)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        NumAfter = self.windowstab.getWindowsNum()
        # 断言退出浏览器之前和打开浏览器之后的多窗口数量
        self.base.assertEqual(winNumBefore,NumAfter,False)


