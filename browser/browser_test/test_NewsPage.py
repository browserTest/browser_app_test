import allure
import pytest
from browser.browser_element.PubElement import *
from browser.browser_page.HomePage import *
from browser.browser_page.MorePage import *
from browser.browser_page.PubMethod import *
from browser.browser_page.NewsPage import *


@allure.feature("魅族浏览器资讯流功能测试")
@pytest.mark.usefixtures("driver_setup")
class TestNewsPage():

    @pytest.fixture()
    def news_init(self,scope="function"):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.more = MorePage(self.driver)
        self.news = NewsPage(self.driver)
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
    def test001RefreshNews(self,news_init):
        '''
        1、打开浏览器，在首页点击“资讯”按钮进入资讯流列表
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
        self.home.clickInformation()
        beforeArticleTitle = self.news.getNewsArticleTitle()
        self.news.dropScrollNews()
        afterArticleTitle = self.news.getNewsArticleTitle()
        self.base.assertEqual(beforeArticleTitle,afterArticleTitle,False)
        self.news.scrollUpNewsToElement()
        self.news.clickNewsRefreshNotice()
        afterRefreshArticleTitle = self.news.getNewsArticleTitle()
        sleep(2)
        self.base.assertEqual(afterArticleTitle,afterRefreshArticleTitle,False)
        self.news.scrollUpNews(5)
        afterToArticleTitle = self.news.getNewsArticleTitle()
        self.base.assertEqual(afterRefreshArticleTitle,afterToArticleTitle,False)


    @allure.story('测试美女频道，打开标签列表、打开图片详情')
    def test002NewsBeautyGrilChannel(self,news_init):
        '''
        1、打开浏览器，在首页向上滑动进入资讯流列表
        2、点击资讯流列表的三角符号，进入频道管理页面
        3、点击“美女”，进入“美女”频道列表
        4、断言“美女图集”存在，则打开美女频道正常
        5、再点击打开“女神”标签，进入标签列表页中
        6、断言“女神”标签中“图集详情的内容ID”存在
        7、点击mback返回美女列表页
        8、滑动页面，选择美女图片打开进入美女图片详情
        9、断言图片详情页顶部返回按钮存在
        '''
        self.home.clickInformation()
        self.news.clickNewsTriangle()
        self.news.clickNewsChannel(NEWS_CHANNEL_BEAUTY_GIRL)
        self.base.assertTrue(NEWS_BEAUTY_GIRL_ATLAS)
        self.news.clickBeautyGirlLable(NEWS_BEAUTY_GIRL_LABEL)
        self.base.assertTrue(NEWS_BEAUTY_GIRL_GODDESS)
        self.pubmethod.clickBack()
        self.news.scrollUpNews(1)
        self.news.clickBeautyGirlList()
        self.base.assertTrue(NEWS_BEAUTY_GIRL_BACK)


    @allure.story('测试频道管理页面，新增、删除、长按、点击打开频道跳转正常等操作')
    def test003NewsChannelManage(self,news_init):
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
        sleep(4)
        self.home.clickInformation()
        self.news.clickNewsTriangle()
        self.news.longPressNewsChannel(NEWS_CHANNEL_TOUTIAO)
        self.news.clickDeleteNewsChannel(NEWS_CHANNEL_DELETE,2)
        self.news.clickFinishButton()
        self.news.addNewsChannel(NEWS_CHANNEL_VIDEO)
        self.news.addNewsChannel(NEWS_CHANNEL_MILITARY)
        self.news.clickNewsChannel(NEWS_CHANNEL_VIDEO)
        self.base.assertTrue(NEWS_VIDEO_NO_INTERESTED)


    @allure.story('测试资讯流列表中的不感兴趣功能')
    def test004NewsChannelManage(self,news_init):
        """
        1、打开浏览器，上滑进入资讯流列表页面
        2、获取资讯流列表第一个标题
        3、点击“X”按钮，显示不感兴趣弹框
        4、点击“不感兴趣”，删除文章
        5、断言删除前和删除后的文章标题不相等
        """
        self.home.clickInformation()
        beforeArticleTitle = self.news.getNewsArticleTitle()
        self.news.clickDeleteNewsChannel(NEWS_ARTICLE_DELETE, 1)
        self.news.clickDeleteNewsChannel(NEWS_DISLIKE, 1)
        afterArticleTitle = self.news.getNewsArticleTitle()
        self.base.assertEqual(beforeArticleTitle,afterArticleTitle,False)


    @allure.story('测试下拉刷新资讯流列表，更新资讯内容，打开任意文章，文章加载正常')
    def test005RefreshNewsOpenArticle(self,news_init):
        '''
        1、打开浏览器,在首页点击“资讯”按钮进入资讯流列表
        2、点击“倒三角”进入频道管理页面
        3、点击“健康”频道打开，进入资讯流列表
        4、下拉刷新资讯流列表内容
        4、获取列表中的文章标题文字信息
        5、点击打开资讯流列表的资讯文章详情
        6、根据百度文字识别 API 识别并获取图片中文字
        7、断言文章标题和文章详情页的文字的匹配度
        '''
        self.home.clickInformation()
        self.news.clickNewsTriangle()
        self.news.clickNewsChannel(NEWS_CHANNEL_HEALTH)
        self.news.dropScrollNews()
        beforetitle = self.news.getNewsArticleTitle()
        self.news.clickOpenNewsArticle()
        aftertitle = self.pubmethod.getBaiduApiText(NEWS_PAGE_MOREMENU)
        self.base.assertEqual(beforetitle,aftertitle,True)


    #  ---wmw
    @allure.story('测试资讯广告')
    def test006NewsAdvertisement(self, news_init):
        '''
        1、点击资讯按钮进入资讯流列表，并刷新资讯
        2、上滑页面，点击X按钮，删除广告，并断言是否存在
        '''
        self.pubmethod.clearApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.clickPrivacyAgree()
        self.pubmethod.clickPermissionAgree()
        sleep(4)
        # 点击资讯按钮进入资讯流列表
        self.home.clickInformation()
        # 点击“倒三角”进入频道管理页面
        self.news.clickNewsTriangle()
        # 点击“视频”频道打开，进入资讯流列表
        self.news.clickNewsChannel(NEWS_CHANNEL_VIDEO)
        # 上滑页面
        self.news.SlideUp()
        # 点击 X 按钮，删除广告
        self.news.clickNewsAdvertisementDelete()
        # 点击不感兴趣
        self.news.clickNewsAdvertisementUninterested()
        sleep(4)
        # 断言页面是否存在广告
        self.base.assertTrue(NEWS_ADVERTISEMENT, False)











