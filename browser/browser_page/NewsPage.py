from base_function.base import *
from browser.browser_element.NewsElement import *


class NewsPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 从浏览器首页上滑进入资讯流列表————LCM
    def scrollUpNews(self,num):
        if self.base.elementIsExit(NEWS_TEXT):
            self.base.scroll(num)
        else:
            self.assertFalse(NEWS_TEXT)

    # 资讯流列表滑动到指定位置————LCM
    def scrollUpNewsToElement(self):
        if self.base.elementIsExit(NEWS_CHANNEL_TOUTIAO):
            self.base.scrollToElement(NEWS_REFRESH_NOTICE_TEXT)
        else:
            self.assertFalse(NEWS_CHANNEL_TOUTIAO)

    # 下拉刷新资讯流列表内容————LCM
    def dropScrollNews(self):
        if self.base.elementIsExit(NEWS_TEXT):
            self.base.dragByElement(NEWS_ARTICLE_TITLE,NEWS_REFRESH_POSITION,2)
        else:
            self.assertFalse(NEWS_TEXT)

    # 资讯流列表点击刷新提示语刷新资讯内容————LCM
    def clickNewsRefreshNotice(self):
        if self.base.elementIsExit(NEWS_REFRESH_NOTICE_TEXT):
            self.base.clickByElement(NEWS_REFRESH_NOTICE_TEXT,'点击刷新提示语“上次看到这里，点击刷新”，刷新资讯流内容')
            sleep(2)
        else:
            self.assertFalse(NEWS_REFRESH_NOTICE_TEXT)

    # 获取资讯流列表的文章标题内容————LCM
    def getNewsArticleTitle(self):
        if self.base.elementIsExit(NEWS_ARTICLE_TITLE):
            strText = self.base.elementText(NEWS_ARTICLE_TITLE, '获取资讯流列表的文章标题内容')
            strTitle = re.sub('\W+', '', strText)
            return strTitle
        else:
            self.assertFalse(NEWS_ARTICLE_TITLE)


    # 点击资讯文章进入资讯文章详情页————LCM
    def clickOpenNewsArticle(self):
        if self.base.elementIsExit(NEWS_ARTICLE_TITLE):
            self.base.clickByElement(NEWS_ARTICLE_TITLE,'在资讯流列表点击资讯文章进入详情页')

        else:
            self.assertFalse(NEWS_ARTICLE_TITLE)



    # 向上滑动页面  ---wmw
    def SlideUp(self):
        if self.base.elementIsExit(NEWS_VIDEO_NO_INTERESTED):
            self.base.swipeByElement(NEWS_ADVERTISEMENT_POSITION_X,"向上滑动页面")
        else:
            self.assertFalse(NEWS_VIDEO_NO_INTERESTED)


    # 点击广告X按钮---wmw
    def clickNewsAdvertisementDelete(self):
        if self.base.elementIsExit(NEWS_ADVERTISEMENT):
            self.base.clickByElement(NEWS_ADVERTISEMENT_DELETE,"点击广告X按钮")
        else:
            self.assertFalse(NEWS_ADVERTISEMENT)


    # 点击广告--不感兴趣   ---wmw
    def clickNewsAdvertisementUninterested(self):
         self.base.clickByElement(NEWS_ADVERTISEMENT_UNINTERESTED,"点击不感兴趣")


    # 点击打开或安装按钮---wmw
    def clickNewsAdvertisementOpenOrInstall(self):
        # 判断页面是否存在广告
        if self.base.elementIsExit(NEWS_ADVERTISEMENT):
            # 判断页面是否存在打开
            if self.base.elementIsExit(NEWS_ADVERTISEMENT_OPEN):
                self.base.clickByElement(NEWS_ADVERTISEMENT_OPEN, '点击打开')
            else:
                # 向下滑动找到安装,并点击安装
                self.base.scrollToElement(NEWS_ADVERTISEMENT)
                self.base.clickByElement(NEWS_ADVERTISEMENT_INSTALL, '点击安装')
                sleep(40)
                self.base.clickByElement(NEWS_ADVERTISEMENT_OPEN, '点击打开')
        else:
            self.assertFalse(NEWS_ADVERTISEMENT)


    # 在资讯列表点击倒三角，进入频道管理页面
    def clickNewsTriangle(self):
        if self.base.elementIsExit(NEWS_TRIANGLE):
            self.base.clickByElement(NEWS_TRIANGLE,'资讯流列表点击“倒三角”符号，进入频道管理页面')
        else:
            self.assertFalse(NEWS_TRIANGLE)


    # 频道管理页面，点击频道打开资讯流列表
    def clickNewsChannel(self,element):
        # 判断我的频道频道是否存在
        if self.base.elementIsExit(NEWS_MY_CHANNEL_ADDED):
            self.base.clickByElement(element,'我的频道管理页面，选择点击“频道”，进入资讯流列表')
        else:
            self.assertFalse(NEWS_MY_CHANNEL_ADDED)


    # 在美女频道列表中，点击标签，详情页正常显示
    def clickBeautyGirlLable(self, element):
        # 判断是否在美女频道列表中
        if self.base.elementIsExit(NEWS_CHANNEL_BEAUTY_GIRL):
            self.base.clickByElement(element, '在美女频道列表中，点击标签，进入标签详情页')
        else:
            self.assertFalse(NEWS_CHANNEL_BEAUTY_GIRL)


    # 在美女频道列表中，点击图片，进入图片详情页
    def clickBeautyGirlList(self):
        # 判断是否在美女频道列表中
        if self.base.elementIsExit(NEWS_CHANNEL_BEAUTY_GIRL):
            self.base.clickByElement(NEWS_BEAUTY_GIRL_PICTURE, '在美女频道列表中，点击图片，进入图片详情页')
        else:
            self.assertFalse(NEWS_CHANNEL_BEAUTY_GIRL)


    # 频道管理页面，点击添加频道
    def addNewsChannel(self,element):
        # 判断我的频道ID是否存在
        if self.base.elementIsExit(NEWS_MY_CHANNEL_NEW_ADD):
            self.base.clickByElement(element, '我的频道管理页面，进行"添加"频道')
        else:
            self.assertFalse(NEWS_MY_CHANNEL_NEW_ADD)


    # 频道管理页面，长按“我的频道”内容
    def longPressNewsChannel(self,element):
        # 判断我的频道ID是否存在
        if self.base.elementIsExit(NEWS_MY_CHANNEL_ADDED):
            self.base.long_clickByElement(element, '我的频道管理页面，长按“头条”频道内容，显示“X”按钮')
        else:
            self.assertFalse(NEWS_MY_CHANNEL_ADDED)


    # 删除频道或者删除资讯文章
    def clickDeleteNewsChannel(self,element,num):
        # 判断“头条”频道是否存在
        if self.base.elementIsExit(NEWS_CHANNEL_TOUTIAO):
            for i in range(num):
                self.base.clickByElement(element, '点击"X"按钮，进行"删除"文章/频道')
        else:
            self.assertFalse(NEWS_CHANNEL_TOUTIAO)


    # 频道管理页面，点击“完成”按钮
    def clickFinishButton(self):
        # 判断我的频道ID是否存在
        if self.base.elementIsExit(NEWS_MY_CHANNEL_ADDED):
            self.base.clickByElement(NEWS_CHANNEL_FINISH, '我的频道管理页面，点击我的频道的"完成"按钮')
        else:
            self.assertFalse(NEWS_MY_CHANNEL_ADDED)



