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
    def other_init(self, scope="function"):
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

        yield
        logging.info("****用例执行结束****")
        logging.info("")


    # 新建多窗口且浏览多窗口内容，打开多窗口页面  ——LCM
    @allure.story('测试新建多窗口且浏览多窗口内容')
    def test001NewWindowsTab(self, other_init):
        '''
        1、进入浏览器，点击导航网站-》更多
        2、点击多窗口按钮
        3、点击新建多窗口按钮（新建3个多窗口tab）
        4、滑动浏览多窗口tab页
        5、点击多窗口中tab页进入网页浏览
        6、断言首页导航网站-》更多 -》小视频
        '''
        # self.pubmethod.clickBack()
        # 进入浏览器，点击导航网站-》更多
        self.more.clickDaoHang(HOME_BUSINESS_MORE_TEXT)
        # 点击多窗口按钮
        self.windowstab.clickWindowsTab()
        # 点击新建多窗口按钮（新建多个多窗口tab）
        self.windowstab.newWindowsTab()
        # 滑动浏览多窗口tab页
        self.windowstab.scrollToWindowsTab()
        # 点击多窗口中tab页进入网页浏览
        self.windowstab.openWindowsTabPage()
        # 断言首页导航网站-》更多 -》小视频
        self.base.assertTrue(SMALL_VIDEO, timeout=5)


    # 关闭所有的多窗口  ——LCM
    @allure.story('测试多窗口浏览tab页关闭所有的多窗口')
    def test002CloseAllWindowsTab(self,other_init):
        '''
        1、进入浏览器，点击导航网站-》更多
        2、点击多窗口按钮
        3、点击新建多窗口按钮，点击打开导航网站-》更多，重复新建3个多窗口
        4、关闭所有的多窗口
        5、断言首页导航网站-》安居客
        '''
        self.home.clickHome()
        # 进入浏览器，点击导航网站-》更多
        self.more.clickDaoHang(HOME_BUSINESS_MORE_TEXT)
        # 点击多窗口按钮
        self.windowstab.clickWindowsTab()
        # 点击新建多窗口按钮
        self.windowstab.newWindowsTab()
        # 关闭所有的多窗口
        self.windowstab.closeAllWindowsTab()
        # 断言首页导航网站-》安居客
        self.base.assertTrue(HOME_ANJUKE, timeout=5)

    # 多窗口浏览tab页上滑关闭多窗口  ——LCM
    @allure.story('测试多窗口浏览tab页上滑关闭一个多窗口')
    def test003CloseOneWindowsTab(self,other_init):
        '''
        1、进入浏览器，点击导航网站-》更多
        2、点击多窗口按钮
        3、点击新建多窗口按钮，点击打开导航网站-》更多，重复新建3个多窗口
        4、获取新建的多窗口数量
        5、上滑关闭2个多窗口
        6、获取删除多窗口后的数量
        7、断言多窗口数量是否减少
        '''
        # 进入浏览器，点击导航网站-》更多
        self.more.clickDaoHang(HOME_BUSINESS_MORE_TEXT)
        # 点击多窗口按钮
        self.windowstab.clickWindowsTab()
        # 点击新建多窗口
        self.windowstab.newWindowsTab()
        # 获取新建的多窗口数量
        winNumBefore = self.windowstab.getWindowsNum()
        # 上滑关闭2个多窗口
        self.windowstab.closeOneWindowsTab()
        # 点击多窗口中tab页进入网页浏览
        self.windowstab.openWindowsTabPage()
        # 获取删除多窗口后的数量
        NumAfter = self.windowstab.getWindowsNum()
        # 断言新建多窗口时的数量和删除多窗口后的数量
        assert winNumBefore != NumAfter


    # 长按menu_more按钮，关闭多窗口  ——LCM
    @allure.story('测试长按menu_more按钮，点击“X”关闭多窗口')
    def test004LongPressCloseWindowsTab(self,other_init):
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
        # 进入浏览器，点击导航网站-》更多
        self.more.clickDaoHang(HOME_BUSINESS_MORE_TEXT)
        # 点击多窗口按钮
        self.windowstab.clickWindowsTab()
        # 点击新建多窗口按钮
        self.windowstab.newWindowsTab()
        # 点击多窗口中tab页进入网页浏览
        self.windowstab.openWindowsTabPage()
        # 获取新建的多窗口数量
        winNumBefore = self.windowstab.getWindowsNum()
        # 点击长按menu_more按钮后，上滑到显示的“X”按钮，放开删除当前窗口
        self.windowstab.longPressCloseWindowsTab()
        # 获取删除多窗口后的数量
        NumAfter = self.windowstab.getWindowsNum()
        # 断言新建多窗口时的数量和删除多窗口后的数量
        assert winNumBefore != NumAfter






