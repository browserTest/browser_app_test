import allure
import pytest
from base_function.base import *
from browser.browser_page.AddToHomePage import *
from browser.browser_page.HomePage import *
from browser.browser_page.NegativeScreenPage import *
from browser.browser_page.PubMethod import *
from browser.browser_element.AddToHome import *


@allure.feature("测试负一屏页面")
@pytest.mark.usefixtures("driver_setup")
class TestNegativePage():

    @pytest.fixture(scope="function")
    def negative_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.negative = NegativeScreenPage(self.driver)
        self.addtohome = AddToHomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")

    @allure.story('测试负一屏添加图标-精选页')
    @pytest.mark.P0
    def test001NegativeScreenPage(self, negative_init):
        '''
        1、在浏览器首页右滑进入负一屏
        2、在负一屏点击"添加"
        3、在精选页面点击"添加"
        3、返回上一层到负一屏，断言是否存在"京东618"
        '''
        # 首次进入浏览器，根据显示页面点击home键回到主页
        self.home.clickHomeOnPage(HOME_PAGE)
        # 在浏览器首页右滑进入负一屏
        self.pubmethod.swipe_ext('right')
        # 在负一屏点击"添加"
        self.negative.clickAddTo()
        sleep(2)
        # 在精选页面点击"添加"
        self.addtohome.clickChoiceAddTo()
        # 返回上一层到负一屏
        self.clickBack()
        # 断言是否存在"京东618"
        self.base.assertTrue(JD, timeout=15)

