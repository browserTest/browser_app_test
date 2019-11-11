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

        1、清除数据后首次进入浏览器，点击隐私弹窗同意按钮
        2、点击权限弹窗“始终允许”按钮，进入浏览器
        3、点击首页搜索框
        4、搜索框输入m.80txt.com
        5、点击搜索
        6、点击小说三村人间
        7、点击开始阅读
        8、点击章节
        9、断言是否会弹出阅读模式提示框
        10、点击允许
        11、断言是否进入阅读模式
        12、点击地址栏阅读模式按钮，退出阅读模式
        13、断言点击地址栏阅读模式按钮，是否正常退出阅读模式
        14、点击地址栏阅读模式按钮，进入阅读模式
        15、断言点击地址栏阅读模式按钮，是否正常进入阅读模式

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
