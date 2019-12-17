from browser.browser_element.NewsElement import NEWS_PAGE_MOREMENU, NEWS_CHANNEL_MILITARY, NEWS_ALL_COMMENTS, \
    NEWS_INPUT_COMMENTS, NEWS_CHANNEL_CONSTELLATION
from browser.browser_page.NewsPage import NewsPage
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
        self.news = NewsPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.mbackToHomeOrNegative()
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

    # ---wmw
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
        self.personalcenter.clickMyMessages()
        self.personalcenter.clickPraisedMyMessages()
        afterMessagesTxt = self.pubmethod.getBaiduApiText(PERSONAL_CENTER_COMMENT_DETAILS)
        self.personalcenter.clickCommentary()
        beforeMessagesTxt = self.pubmethod.getBaiduApiText(NEWS_PAGE_MOREMENU)
        self.base.assertEqual(afterMessagesTxt, beforeMessagesTxt, True)

    @allure.story('测试个人中心账号，进入评论详情，检查页面显示是否正常')
    def test003PersonalCenterPage(self, personalCenter_init):
        '''
        1、点击工具菜单
        2、点击工具面板--我的图标
        3、判断账号是否登陆
        4、点击我的评论
        5、默认点击第一条消息
        '''
        self.home.clickMore()
        self.toolbarpanel.clickFlymeme()
        self.personalcenter.elementIsLandFlymeme()
        self.personalcenter.clickMyComment()
        afterCommentTxt = self.pubmethod.getBaiduApiText(PERSONAL_CENTER_MY_COMMENT_A)
        self.personalcenter.clickPraisedMyComment()
        beforeCommentTxt = self.pubmethod.getBaiduApiText(NEWS_PAGE_MOREMENU)
        self.base.assertEqual(afterCommentTxt, beforeCommentTxt, True)

    @allure.story('测试小游戏是否正常打开')
    def test004PersonalCenterPage(self,personalCenter_init):
        '''
        1、点击工具栏面板头像图标，进入个人中心
        2、点击小游戏
        '''
        self.home.clickMore()
        self.toolbarpanel.clickFlymeme()
        self.personalcenter.clickMiniGame()
        self.base.browserWatcher()
        self.pubmethod.clearApp(HOT_GAME)


    @allure.story('测试资讯文章评论是否提交正常')
    def test005RefreshNewsOpenArticle(self,personalCenter_init):
        '''
        1、清除浏览器数据,进入军事频道
        2、点击第一篇文章进入文章详情页，点击评论输入内容
        3、断言页面是否存在输入内容
        4、在个人中心评论页面删除之前输入的测试评论内容，断言测试评论不存在
        '''
        self.pubmethod.clearApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        # 清除数据后首次进入浏览器，点击隐私弹窗同意按钮
        self.pubmethod.clickPrivacyAgree()
        # 点击权限弹窗“始终允许”按钮，进入浏览器
        # self.pubmethod.clickPermissionAgree()
        self.base.browserWatcher()
        sleep(5)
        self.home.clickInformation()
        # 点击“倒三角”进入频道管理页面
        self.news.clickNewsTriangle()
        sleep(2)
        # 点击“星座”频道打开，进入资讯流列表
        self.news.clickNewsChannel(NEWS_CHANNEL_CONSTELLATION)

        self.news.dropScrollNews()
        self.news.clickOpenNewsArticle()
        self.base.scrollToElement(NEWS_ALL_COMMENTS)
        self.news.clickCommentBox()
        self.news.inputFocalPositionText()
        self.news.clickRelease()
        self.base.assertTrue(NEWS_INPUT_COMMENTS)
        sleep(4)
        # 点击mback
        self.pubmethod.clickBack()
        self.home.clickMore()
        self.toolbarpanel.clickFlymeme()
        self.personalcenter.clickMyComment()
        self.personalcenter.clickDelete()
        self.personalcenter.clickDeleteBox()
        self.pubmethod.clickBack()
        self.personalcenter.clickMyComment()
        self.base.assertTrue(NEWS_INPUT_COMMENTS, False)


    @allure.story('测试修改输入法')
    def test006PersonalCenterPage(self, personalCenter_init):
        '''
            1、修改输入法
        '''
        # 点击mback
        self.pubmethod.clickBack()
        self.pubmethod.startApp(MEIZU_SETTINGS)
        self.base.scrollToElement(LANGUAGE_AND_TIME)
        sleep(5)
        self.personalcenter.clickLanguageAndTime()
        self.personalcenter.clickInputMethod()
        self.personalcenter.clickSettingButton()
        self.personalcenter.clickSouGou()
        self.base.assertTrue(INPUT_BABIT)


    @allure.story('测试退出账号')
    def test007PersonalCenterPage(self, personalCenter_init):
        '''
            1、退出Flyme账号
        '''
        self.home.clickMore()
        self.toolbarpanel.clickFlymeme()
        self.personalcenter.clickOutAccount()
        self.base.assertTrue(PERSONAL_CENTER_NOT_LOGGED_IN)




