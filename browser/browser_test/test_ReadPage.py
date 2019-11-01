from config.config import *
from browser.browser_page.PubMethod import PubMethod
from browser.browser_page.ReadPage import *
from browser.browser_page.SearchPanelPage import *
from browser.browser_page.HomePage import *
from base_function.base import Base

import allure




@allure.feature("测试阅读模式")
#可以让执行每个case前，都执行一遍指定的fixture
@pytest.mark.usefixtures("driver_setup")
class TestReadPage():

    @pytest.fixture(scope="function")
    def ReadPage_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.read = ReadPage(self.driver)
        self.searchpanel = SearchPanelPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.clearApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")


    @allure.story('测试阅读模式')
    def test001ReadPage(self, ReadPage_init):
        '''
        1、清除数据后首次打开浏览器，弹出隐私政策窗口
        2、点击“同意”，弹出权限窗口
        3、点击权限弹窗“始终允许”按钮
        '''

        # 清除数据后首次进入浏览器，点击隐私弹窗同意按钮
        self.pubmethod.clickPrivacyAgree()
        # 点击权限弹窗“始终允许”按钮，进入浏览器
        self.pubmethod.clickPermissionAgree()
        # 点击首页搜索框
        self.home.clickHomeSearch()
        # 搜索框输入m.80txt.com
        self.searchpanel.inputNumber()
        # 点击搜索
        self.searchpanel.clickSearchInto()
        # 点击小说三村人间
        self.read.clickSCRJ()
        # 点击开始阅读
        self.read.clickRead()
        # 点击章节--1、写在连载前
        self.read.clickChapter()
        # 断言是否会弹出阅读模式提示框
        self.base.assertTrue(SEARCHPANEL_READ_IMG)