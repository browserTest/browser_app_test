import allure
import pytest
from browser.browser_element.PubElement import *
from browser.browser_page.HomePage import *
from browser.browser_page.MorePage import *
from browser.browser_page.PubMethod import *
from browser.browser_page.ZiXunInformationPage import *


@allure.feature("魅族浏览器资讯流功能测试")
@pytest.mark.usefixtures("driver_setup")
class TestZiXunInformationPage():

    @pytest.fixture()
    def zixun_init(self,scope="function"):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.more = MorePage(self.driver)
        self.zixun = ZiXunInformationPage(self.driver)
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

    @allure.story('测试下拉刷新、上滑刷新、点击资讯按钮刷新、点击提示语刷新资讯流列表，更新资讯内容')
    def test001RefreshZiXunInfo(self,zixun_init):
        '''
        1、打开浏览器，从首页上滑进入资讯流列表
        2、获取资讯流列表的文章标题
        3、下拉刷新资讯流列表内容
        4、再次获取资讯流列表的文章标题
        5、断言刷新前和刷新后的文章标题不一样
        6、滑动页面找到'上次看到这里，点击刷新'提示语
        7、点击'上次看到这里，点击刷新'提示语，刷新资讯流内容
        8、断言刷新前和刷新后的文章标题不一样
        9、上滑刷新，刷新新的资讯文章
        10、断言刷新前的文章内容标题不存在
        '''
        self.zixun.scrollUpZiXun(1)
        beforeArticleTitle = self.zixun.getZiXunArticleTitle()
        self.zixun.dropScrollZiXun()
        afterArticleTitle = self.zixun.getZiXunArticleTitle()
        assert beforeArticleTitle != afterArticleTitle
        self.zixun.scrollUpZiXunToElement()
        self.zixun.clickZiXunRefreshNotice()
        afterRefreshArticleTitle = self.zixun.getZiXunArticleTitle()
        assert beforeArticleTitle != afterRefreshArticleTitle
        self.zixun.scrollUpZiXun(5)
        afterToArticleTitle = self.zixun.getZiXunArticleTitle()
        assert beforeArticleTitle != afterToArticleTitle



    @allure.story('测试下拉刷新资讯流列表，更新资讯内容，打开任意文章/视频联播页，文章加载正常')
    def test002RefreshZiXunInfoOpenArticle(self,zixun_init):
        '''
        1、打开浏览器
        2、从浏览器首页上滑进入资讯流列表
        3、下拉刷新资讯流列表内容
        4、点击打开资讯流列表的资讯文章详情/视频视频联播页
        5、判断打开的资讯文章，断言文章详情页顶部返回按钮是否存在，若打开视频连播页，则断言视频联播页的更多负反馈按钮
        6、mback返回上一级页面
        '''
        self.zixun.scrollUpZiXun(1)
        self.zixun.dropScrollZiXun()
        self.zixun.clickOpenZiXunArticle()
        self.pubmethod.clickBack()


    @allure.story('测试美女频道，打开标签列表、打开图片详情')
    def test003ZiXunMeiNvChannel(self,zixun_init):
        '''
        1、打开浏览器，在首页向上滑动进入资讯流列表
        2、点击资讯流列表的三角符号，进入频道管理页面
        3、点击“美女”，进入“美女”频道列表
        4、打开美女频道后，断言“女神”标签存在
        5、再点击打开“美女”频道顶部“女神”标签，进入标签列表页中
        6、断言“女神”标签名称存在
        7、点击mback返回美女列表页
        8、点击打开美女图片详情
        9、断言图片详情页顶部返回按钮存在

        '''

        self.zixun.scrollUpZiXun(1)
        self.zixun.clickZiXunTriangle()
        # 添加美女频道
        # self.zixun.addZiXunChannel(ZIXUN_CHANNEL_MEINV)
        # 打开美女频道列表
        self.zixun.clickZiXunChannel(ZIXUN_CHANNEL_MEINV)
        self.base.assertTrue(ZIXUN_MEINV_MEINV_NVSHEN)
        self.zixun.clickMeiNvLable(ZIXUN_MEINV_MEINV_NVSHEN)
        self.base.assertTrue(ZIXUN_MEINV_MEINV_NS)
        self.pubmethod.clickBack()
        self.zixun.scrollUpZiXun(1)
        self.zixun.clickMeiNvList()
        self.base.assertTrue(ZIXUN_MEINV_BACK)


    @allure.story('测试频道管理页面，新增、删除、长按、点击打开频道跳转正常等操作')
    def test004ZiXunChannelManage(self,zixun_init):
        '''
        1、打开浏览器，上滑进入资讯流列表
        2、点击倒三角符号，进入频道管理页面
        3、在我的频道管理页面，长按“头条”
        4、删除“视频、军事”频道
        5、点击“完成”按钮
        6、再添加“视频、军事”频道
        7、点击“视频”频道，进入资讯流列表
        8、断言视频频道列表中的负反馈按钮存在
        '''
        self.pubmethod.clearApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.clickPrivacyAgree()
        self.pubmethod.clickPermissionAgree()
        sleep(3)
        self.zixun.scrollUpZiXun(1)
        self.zixun.clickZiXunTriangle()
        self.zixun.longPressZiXunChannel(ZIXUN_CHANNEL_TOUTIAO)
        self.zixun.clickDeleteZiXunChannel(ZIXUN_CHANNEL_DELETE,2)
        self.zixun.clickFinishButton()
        self.zixun.addZiXunChannel(ZIXUN_CHANNEL_VIDEO)
        self.zixun.addZiXunChannel(ZIXUN_CHANNEL_MILITARY)
        self.zixun.clickZiXunChannel(ZIXUN_CHANNEL_VIDEO)
        self.base.assertTrue(ZIXUN_VIDEO_NO_INTERESTED)



    @allure.story('测试资讯流列表中的不感兴趣功能')
    def test005ZiXunChannelManage(self,zixun_init):
        """
        1、打开浏览器，上滑进入资讯流列表页面
        2、获取资讯流列表第一个标题
        3、点击“X”按钮，显示不感兴趣弹框
        4、点击“不感兴趣”，删除文章
        5、断言删除前和删除后的文章标题不相等
        """
        self.zixun.scrollUpZiXun(1)
        beforeArticleTitle = self.zixun.getZiXunArticleTitle()
        self.zixun.clickDeleteZiXunChannel(ZIXUN_ARTICLE_DELETE, 1)
        self.zixun.clickDeleteZiXunChannel(ZIXUN_DISLIKE, 1)
        afterArticleTitle = self.zixun.getZiXunArticleTitle()
        assert beforeArticleTitle != afterArticleTitle














