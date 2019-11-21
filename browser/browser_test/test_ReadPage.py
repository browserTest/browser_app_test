from config.config import *
from browser.browser_page.PubMethod import PubMethod
from browser.browser_page.ReadPage import *
from browser.browser_page.SearchPanelPage import *
from browser.browser_page.HomePage import *
from base_function.base import Base
import allure




@allure.feature("测试阅读模式")
@pytest.mark.usefixtures("driver_setup")
class TestReadPage():

    @pytest.fixture(scope="function")
    def readPage_init(self):
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
    def test001ReadPage(self, readPage_init):
        '''

        1、清空浏览器数据，点击电脑版进入小说网页
        2、点击小说封面，开始阅读，进入章节，判断是否首次弹出阅读模式弹框
        3、点击地址栏的阅读模式按钮，判断是否正常进入/退出阅读模式

        '''
        # 清除数据后首次进入浏览器，点击隐私弹窗同意按钮
        self.pubmethod.clickPrivacyAgree()
        # 点击权限弹窗“始终允许”按钮，进入浏览器
        self.pubmethod.clickPermissionAgree()
        sleep(5)
        # 点击主页工具菜单
        self.home.clickMore()
        # 点击电脑版
        self.read.clickComputerButton()
        # 点击首页搜索框
        self.home.clickHomeSearch()
        # 搜索框输入m.80txt.la
        self.searchpanel.inputNumber()
        # 点击搜索
        self.searchpanel.clickSearchInto()
        # 点击小说封面
        self.read.clickBook()
        # 点击开始阅读
        self.read.clickRead()
        # 点击章节
        self.read.clickChapter()
        # 断言是否会弹出阅读模式提示框
        self.base.assertTrue(READ_IMG)
        # 点击允许
        self.read.clickOpen()
        # 断言是否进入阅读模式
        self.base.assertTrue(READ_IMG,False)
        # 点击地址栏阅读模式按钮，退出阅读模式
        self.read.clickReadButton()
        # 断言点击地址栏阅读模式按钮，是否正常退出阅读模式
        self.base.assertTrue(READ_NEXT)
        # 点击地址栏阅读模式按钮，进入阅读模式
        self.read.clickReadButton()
        # 断言点击地址栏阅读模式按钮，是否正常进入阅读模式
        self.base.assertTrue(READ_NEXT,False)
