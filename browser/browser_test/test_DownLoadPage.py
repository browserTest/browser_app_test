import allure
import pytest
from base_function.base import *
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


    @allure.story('测试长按网页链接，点击“下载链接”，显示下载弹框，点击取消')
    def test001DownWebPage(self,down_init):
        '''
        1、打开浏览器，点击底部工具栏菜单menu_more按钮
        2、点击“设置”进入设置页面
        3、设置搜索引擎为“360”
        4、mback返回上一级页面（首页）
        5、点击“搜索框”，点击“搜索”按钮，访问网页，在页面内等待2秒
        6、使用百度文字识别 API 识别并获取图片中文字
        7、长按网页链接，显示长按菜单弹框
        8、点击“下载链接”按钮，显示下载弹框
        9、断言“下载弹框”中的名称
        10、点击下载弹框中的“取消”按钮
        11、再次通过百度文字识别 API 识别并获取图片中文字
        12、断言显示“下载弹框”前和取消“下载弹框”后的元素相等
        '''
        self.home.clickMore()
        self.tool.clickToolsPanel(SET_UP)
        self.set.clickSearchEngine(2)
        self.set.click360()
        self.pubmethod.clickBack()
        self.home.clickHomeSearch()
        self.search.clickSearchInto()
        sleep(2)
        beforetitle = self.pubmethod.getBaiduApiText(SEARCHPANEL_TEXT)
        self.down.longLink()
        self.down.clickDownLink()
        self.base.assertTrue(DOWNLOAD_NAME)
        self.down.clickCancelButton()
        aftertitle = self.pubmethod.getBaiduApiText(SEARCHPANEL_TEXT)
        self.base.assertEqual(beforetitle,aftertitle,True)

    @allure.story('测试长按网页链接下载，断言下载完成后的小红点')
    def test002DownWebPage(self,down_init):
        '''
        1、点击“搜索框”
        2、点击“搜索”按钮，访问网页，在页面内等待2秒
        3、长按网页链接，显示长按菜单弹框
        4、点击“下载链接”按钮，显示下载弹框
        5、在下载弹框中点击“下载”按钮
        6、点击底部工具栏菜单menu_more按钮，显示工具面板，等待5秒
        6、断言工具面板中下载完成后的“小红点”
        '''
        self.home.clickHomeSearch()
        self.search.clickSearchInto()
        sleep(2)
        self.down.longLink()
        self.down.clickDownLink()
        self.down.clickDownButton()
        self.home.clickMore()
        sleep(5)
        self.base.assertTrue(HOME_MORE_TIP)

    @allure.story('测试长按网页链接下载，下载完成后，断言下载管理中下载的文件存在')
    def test003DownWebPage(self, down_init):
        '''
        1、点击“搜索框”，
        2、点击“搜索”按钮，访问网页，在页面内等待2秒
        3、长按网页链接，显示弹框，点击“下载链接”按钮，显示下载弹框
        4、获取下载弹框中的标题名称
        5、在下载弹框中点击“下载”按钮
        6、点击底部工具栏菜单menu_more按钮，显示工具面板，等待5秒
        7、点击“下载管理”打开下载页面
        7、获取下载管理中下载好的文件名称标题
        8、断言“下载管理”页面中的下载文件名称与之前下载中的文件名称相等
        '''
        self.home.clickMore()
        self.tool.clickToolsPanel(DOWNLOAD_MANAGER)
        self.down.longPressElement()
        # 点击全选、删除下载文件按钮
        self.down.clickChoose()
        self.pubmethod.clickBack()
        self.home.clickHomeSearch()
        self.search.clickSearchInto()
        sleep(2)
        self.down.longLink()
        self.down.clickDownLink()
        beforeDownTitle = self.down.getDownTitle(DOWNLOAD_NAME)
        self.down.clickDownButton()
        self.home.clickMore()
        sleep(5)
        self.tool.clickToolsPanel(DOWNLOAD_MANAGER)
        afterDownTitle = self.down.getDownTitle(DOWN_LOAD_MANAGE_TITLE)
        self.base.assertEqual(beforeDownTitle, afterDownTitle, True)


    @allure.story('测试应用下载')
    def test004DownAppPage(self, down_init):
        '''
        1、点击“搜索框”
        2、输入“QQ”，点击“搜索”按钮
        3、点击页面中的“高速下载”
        4、显示下载弹框
        5、在下载弹框中点击“下载”按钮
        6、点击底部工具栏菜单menu_more按钮，显示工具面板
        7、点击“下载管理”打开下载页面
        8、断言下载中的状态
        '''
        self.home.clickHomeSearch()
        self.down.inputApp()
        self.search.clickSearchInto()
        self.down.clickAppDown()
        self.base.assertTrue(DOWNLOAD_NAME)
        self.down.clickDownButton()
        self.home.clickMore()
        self.tool.clickToolsPanel(DOWNLOAD_MANAGER)
        self.base.assertTrue(DOWN_LOAD_PROGRESS)












