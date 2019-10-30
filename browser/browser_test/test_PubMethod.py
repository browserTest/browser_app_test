from base_function.driver import *
import pytest
from config.config import *
from browser.browser_page.HomePage import HomePage
from browser.browser_page.PubMethod import PubMethod
from browser.browser_element.PubElement import *
from base_function.base import Base
from browser.browser_element.Home import *
import allure
from browser.browser_element.MyCollection import *



@allure.feature("测试启动弹框")
#可以让执行每个case前，都执行一遍指定的fixture
@pytest.mark.usefixtures("driver_setup")
class TestPubMethod():

    @pytest.fixture(scope="function")
    def pubMethod_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.clearApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")

#可以在每一个测试用例加一个marker，比如pytest运行的时就只运行带有该marker的测试用例，比如@pytest.mark.P0
    @allure.story('测试隐私弹窗同意按钮')
    def test001PrivacyAgree(self, pubMethod_init):
        '''
        1、清除数据后首次打开浏览器，弹出隐私政策窗口
        2、点击“同意”，弹出权限窗口
        '''

        # 清除数据后首次进入浏览器，点击隐私弹窗同意按钮
        self.pubmethod.clickPrivacyAgree()
        self.base.assertTrue(PERMISSION_TITLE, timeout=5)

    @allure.story('测试隐私弹窗不同意按钮')
    def test002PrivacyDisagree(self, pubMethod_init):
        '''
        1、清除数据后首次打开浏览器，弹出隐私政策窗口
        2、点击“不同意”，退出
        '''

        # 清除数据后首次进入浏览器，点击隐私弹窗不同意按钮
        self.pubmethod.clickPrivacyDisagree()
        self.base.assertTrue(LAUNCHER_ID, timeout=5)

    @allure.story('测试权限弹窗拒绝按钮')
    def test003PermissionDisagree(self, pubMethod_init):
        '''
        1、清除数据后首次打开浏览器，弹出隐私政策窗口
        2、点击“同意”，弹出权限窗口
        3、点击权限弹窗“拒绝”按钮
        '''

        # 清除数据后首次进入浏览器，点击隐私弹窗同意按钮
        self.pubmethod.clickPrivacyAgree()
        # 点击权限弹窗“拒绝”按钮，进入浏览器
        self.pubmethod.clickPermissionDisagree()
        self.base.assertTrue(HOME_PAGE, timeout=5)

    @allure.story('测试权限弹窗允许按钮')
    def test004PermissionAgree(self, pubMethod_init):
        '''
        1、清除数据后首次打开浏览器，弹出隐私政策窗口
        2、点击“同意”，弹出权限窗口
        3、点击权限弹窗“始终允许”按钮
        '''

        # 清除数据后首次进入浏览器，点击隐私弹窗同意按钮
        self.pubmethod.clickPrivacyAgree()
        # 点击权限弹窗“始终允许”按钮，进入浏览器
        self.pubmethod.clickPermissionAgree()
        self.base.assertTrue(HOME_PAGE, timeout=5)
