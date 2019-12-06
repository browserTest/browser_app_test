import allure
import pytest
from base_function.base import *
from browser.browser_page.HomePage import *
from browser.browser_page.PubMethod import *
from browser.browser_page.WindowsTabPage import *


@allure.feature("魅族浏览器多窗口相关测试")
@pytest.mark.usefixtures("driver_setup")
class TestWindowsTabPage():

    @pytest.fixture()
    def window_init(self, scope="function"):
        self.base = Base(self.driver)
        self.more = MorePage(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.windowstab = WindowsTabPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.base.unlock()
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHome()
        self.home.clickHomeOnPage(HOME_PAGE)
        yield
        logging.info("****用例执行结束****")
        logging.info("")


    # 新建多窗口且浏览多窗口内容，打开多窗口页面  ——LCM
    @allure.story('测试新建多窗口且浏览多窗口内容')
    def test001NewWindowsTab(self, window_init):
        '''
        1、进入浏览器，点击导航网站-》更多
        2、点击多窗口按钮
        3、点击新建多窗口按钮（新建3个多窗口tab）
        4、滑动浏览多窗口tab页
        5、断言首页导航网站-》更多 -》搜索框中的默认关键字：输入关键字
        6、点击多窗口中tab页进入网页浏览
        7、断言多窗口数量不相等
        '''
        self.more.clickDaoHang(HOME_BUSINESS_MORE_TEXT)
        winNumBefore = self.windowstab.getWindowsNum()
        self.windowstab.clickWindowsTab()
        self.windowstab.newWindowsTab(2)
        self.windowstab.scrollToWindowsTab()
        self.windowstab.openWindowsTabPage()
        self.base.assertTrue(DEFAULT_WORD)
        NumAfter = self.windowstab.getWindowsNum()
        self.base.assertEqual(winNumBefore,NumAfter,False)

    # 关闭所有的多窗口  ——LCM
    @allure.story('测试多窗口浏览tab页关闭所有的多窗口')
    def test002CloseAllWindowsTab(self,window_init):
        '''
        1、进入浏览器，点击导航网站-》更多
        2、点击多窗口按钮
        3、点击新建多窗口按钮，点击打开导航网站-》更多，新建3个多窗口
        4、关闭所有的多窗口
        5、断言多窗口数量为：1
        '''
        self.more.clickDaoHang(HOME_BUSINESS_MORE_TEXT)
        self.windowstab.clickWindowsTab()
        self.windowstab.newWindowsTab(2)
        # 获取新建的多窗口数量
        winNumBefore = self.windowstab.getWindowsNum()
        self.windowstab.closeAllWindowsTab()
        # 获取删除多窗口后的数量
        NumAfter = self.windowstab.getWindowsNum()
        # 断言多窗口数量为：1
        self.base.assertEqual(winNumBefore,NumAfter,False)

    # 多窗口浏览tab页上滑关闭多窗口  ——LCM
    @allure.story('测试多窗口浏览tab页上滑关闭一个多窗口')
    def test003CloseOneWindowsTab(self,window_init):
        '''
        1、进入浏览器，点击导航网站-》更多
        2、点击多窗口按钮
        3、点击新建多窗口按钮，点击打开导航网站-》更多，重复新建3个多窗口
        4、获取新建的多窗口数量
        5、上滑关闭2个多窗口
        6、获取删除多窗口后的数量
        7、断言多窗口数量是否减少
        '''
        self.more.clickDaoHang(HOME_BUSINESS_MORE_TEXT)
        self.windowstab.clickWindowsTab()
        self.windowstab.newWindowsTab(2)
        winNumBefore = self.windowstab.getWindowsNum()
        self.windowstab.closeOneWindowsTab()
        self.windowstab.openWindowsTabPage()
        NumAfter = self.windowstab.getWindowsNum()
        # 断言新建多窗口时的数量和删除多窗口后的数量
        self.base.assertEqual(winNumBefore,NumAfter,False)


    # 长按menu_more按钮，关闭多窗口  ——LCM
    @allure.story('测试长按menu_more按钮，点击“X”关闭多窗口')
    def test004LongPressCloseWindowsTab(self,window_init):
        '''
        1、进入浏览器，点击导航网站-》更多
        2、点击多窗口按钮
        3、点击新建多窗口按钮，点击打开导航网站-》更多，重复新建3个多窗口
        4、点击多窗口中tab页进入网页浏览
        5、获取新建的多窗口数量
        6、长按并且上滑到 “X” 位置后放开，关闭当前窗口
        7、获取删除多窗口后的数量
        8、断言多窗口数量是否减少
        '''
        self.more.clickDaoHang(HOME_BUSINESS_MORE_TEXT)
        self.windowstab.clickWindowsTab()
        self.windowstab.newWindowsTab(2)
        self.windowstab.openWindowsTabPage()
        winNumBefore = self.windowstab.getWindowsNum()
        # 点击长按menu_more按钮后，上滑到显示的“X”按钮，放开删除当前窗口
        self.windowstab.longPressCloseWindowsTab()
        NumAfter = self.windowstab.getWindowsNum()
        # 断言新建多窗口时的数量和删除多窗口后的数量
        self.base.assertEqual(winNumBefore,NumAfter,False)






