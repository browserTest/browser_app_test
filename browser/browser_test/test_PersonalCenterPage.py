from config.config import *
from browser.browser_page.PubMethod import PubMethod
from browser.browser_page.HomePage import *
from browser.browser_page.ToolBarPanelPage import *
from browser.browser_page.PersonalCenterPage import *
import allure





@allure.feature("测试个人中心页面")
@pytest.mark.usefixtures("driver_setup")
class TestPersonalCenterPage():

    @pytest.fixture(scope="function")
    def personalCenter_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod= PubMethod(self.driver)
        self.toolbarpanel = ToolBarPanelPage(self.driver)
        self.personalcenter = PersonalCenterPage(self.driver)
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
    @allure.story('测试个人中心账号登录页')
    def test001PersonalCenterPage(self, personalCenter_init):
        '''
        1、点击工具菜单
        2、点击工具面板--我的图标
        3、未登录时，点击我的图标
        4、断言页面是否为登录账号页面
        '''
        self.home.clickMore()
        self.toolbarpanel.clickFlymeme()
        self.personalcenter.clickFlymemeB()
        self.base.assertTrue(PERSONAL_CENTER_REGISTER)

    # ---wmw  --未完成
    @allure.story('测试个人中心账号，进入评论详情，检查页面显示是否正常')
    def test002PersonalCenterPage(self, personalCenter_init):
        '''
        1、点击工具菜单
        2、点击工具面板--我的图标
        3、判断账号是否登陆
        4、点击我的消息
        5、默认点击第一条消息
        '''
        self.home.clickMore()
        self.toolbarpanel.clickFlymeme()
        self.personalcenter.elementIsLandFlymeme()
        # 此处有bug，为了确保当前页面账号更新已登陆成功，故多点几次我的消息
        self.personalcenter.clickMyMessages()
        self.personalcenter.clickMyMessages()
        self.personalcenter.clickMyMessages()
        self.personalcenter.clickPraisedMyMessages()





