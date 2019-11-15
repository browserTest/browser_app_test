import allure
import pytest
from base_function.base import *
from browser.browser_element.ToolbarPanel import *
from browser.browser_page.DownLoadPage import *
from browser.browser_page.HomePage import *
from browser.browser_page.MorePage import *
from browser.browser_page.PubMethod import *
from browser.browser_page.SearchPanelPage import *
from browser.browser_page.SetUpPage import *
from browser.browser_page.ToolBarPanelPage import *


@allure.feature("魅族浏览器下载功能测试")
@pytest.mark.usefixtures("driver_setup")
class TestDownPage():

    @pytest.fixture()
    def down_init(self,scope="function"):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.more = MorePage(self.driver)
        self.search = SearchPanelPage(self.driver)
        self.tool = ToolBarPanelPage(self.driver)
        self.set = SetUpPage(self.driver)
        self.down = DownPage(self.driver)
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

    @allure.story('测试网页下载')
    def test001DownWebPage(self,down_init):
        '''
        1、打开浏览器，点击底部工具栏菜单menu_more按钮
        2、点击“设置”进入设置页面
        3、设置搜索引擎为“360”
        4、mback返回上一级页面（首页）
        5、点击“搜索框”，点击“搜索”按钮，访问网页，在页面内等待2秒
        6、长按网页链接，显示弹框，点击“下载链接”按钮，显示下载弹框
        7、断言“下载弹框”中的名称
        8、点击下载弹框中的“取消”按钮
        9、长按网页链接，显示弹框，点击“下载链接”按钮，显示下载弹框
        10、在下载弹框中点击“下载”按钮
        11、点击底部工具栏菜单menu_more按钮，显示工具面板，等待5秒
        12、断言工具面板中下载完成后的“小红点”
        13、点击“下载管理”打开下载页面
        14、断言“下载管理”页面中的下载的文件名称
        '''
        self.home.clickMore()
        self.tool.clickToolsPanel(SET_UP)
        self.set.clickSearchEngine(1)
        self.set.click360()
        self.pubmethod.clickBack()
        self.home.clickHomeSearch()
        self.search.clickSearchInto()
        sleep(2)
        self.down.longLink()
        self.down.clickDownLink()
        self.base.assertTrue(DOWNLOAD_NAME)
        self.down.clickCancelButton()
        self.down.longLink()
        self.down.clickDownLink()
        beforeDownTitle = self.down.getDownTitle(DOWNLOAD_NAME)
        self.down.clickDownButton()
        self.home.clickMore()
        sleep(5)
        self.base.assertTrue(HOME_MORE_TIP)
        self.tool.clickToolsPanel(DOWNLOAD_MANAGER)
        afterDownTitle = self.down.getDownTitle(DOWN_LOAD_TITLE)
        self.base.assertEqual(beforeDownTitle,afterDownTitle,True)


    @allure.story('测试应用下载')
    def test002DownAppPage(self, down_init):
        '''
        1、打开浏览器，点击底部工具栏菜单menu_more按钮
        2、点击“设置”进入设置页面
        3、设置搜索引擎为“360”
        4、mback返回上一级页面（首页）
        5、点击“搜索框”，输入“QQ”，点击“搜索”按钮
        6、点击页面中的“高速下载”
        7、显示下载弹框
        '''
        self.home.clickMore()
        self.tool.clickToolsPanel(SET_UP)
        self.set.clickSearchEngine(1)
        self.set.click360()
        self.pubmethod.clickBack()
        self.home.clickHomeSearch()
        self.down.inputApp()
        self.search.clickSearchInto()
        self.down.clickAppDown()
        self.base.assertTrue(DOWNLOAD_NAME)
        self.down.clickCancelButton()
        self.down.clickAppDown()
        self.down.clickDownButton()











