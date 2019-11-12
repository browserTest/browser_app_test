from base_function.base import *
from browser.browser_element.ZiXunInformationElement import *


class ZiXunInformationPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 从浏览器首页上滑进入资讯流列表————LCM
    def scrollUpZiXun(self,num):
        if self.base.elementIsExit(ZIXUN_TEXT):
            self.base.scroll(num)
        else:
            self.assertFalse(ZIXUN_TEXT)

    # 资讯流列表滑动到指定位置————LCM
    def scrollUpZiXunToElement(self):
        if self.base.elementIsExit(ZIXUN_CHANNEL_TOUTIAO):
            self.base.scrollToElement(ZIXUN_REFRESH_NOTICE_TEXT)
        else:
            self.assertFalse(ZIXUN_CHANNEL_TOUTIAO)

    # 下拉刷新资讯流列表内容————LCM
    def dropScrollZiXun(self):
        if self.base.elementIsExit(ZIXUN_CHANNEL_TOUTIAO):
            self.base.dragByElement(ZIXUN_ARTICLE_TITLE,ZIXUN_REFRESH_POSITION,2)
        else:
            self.assertFalse(ZIXUN_CHANNEL_TOUTIAO)

    # 资讯流列表点击刷新提示语刷新资讯内容————LCM
    def clickZiXunRefreshNotice(self):
        if self.base.elementIsExit(ZIXUN_REFRESH_NOTICE_TEXT):
            self.base.clickByElement(ZIXUN_REFRESH_NOTICE_TEXT,'点击刷新提示语“上次看到这里，点击刷新”，刷新资讯流内容')
        else:
            self.assertFalse(ZIXUN_REFRESH_NOTICE_TEXT)

    # 获取资讯流列表的文章标题内容————LCM
    def getZiXunArticleTitle(self):
        if self.base.elementIsExit(ZIXUN_ARTICLE_TITLE):
            return self.base.elementText(ZIXUN_ARTICLE_TITLE,'获取资讯流列表的文章标题内容')
        else:
            self.assertFalse(ZIXUN_ARTICLE_TITLE)

    # 点击资讯文章进入资讯文章详情页————LCM
    def clickOpenZiXunArticle(self):
        if self.base.elementIsExit(ZIXUN_ARTICLE_TITLE):
            self.base.clickByElement(ZIXUN_ARTICLE_TITLE,'在资讯流列表点击资讯文章、视频连播页进入详情页')
            if self.base.elementIsExit(ZIXUN_PAGE_MOREMENU):
                self.base.assertTrue(ZIXUN_PAGE_BACK)
            else:
                self.base.assertTrue(ZIXUN_PAGE_VIDEO)
        else:
            self.assertFalse(ZIXUN_ARTICLE_TITLE)


    # 在资讯列表点击倒三角，进入频道管理页面
    def clickZiXunTriangle(self):
        if self.base.elementIsExit(ZIUN_TRIANGLE):
            self.base.clickByElement(ZIUN_TRIANGLE,'资讯流列表点击“倒三角”符号，进入频道管理页面')
        else:
            self.assertFalse(ZIUN_TRIANGLE)


    # 频道管理页面，点击频道打开资讯流列表
    def clickZiXunChannel(self,element):
        # 判断我的频道频道是否存在
        if self.base.elementIsExit(ZIXUN_MY_CHANNEL_ADDED):
            self.base.clickByElement(element,'我的频道管理页面，选择点击“频道”，进入资讯流列表')
        else:
            self.assertFalse(ZIXUN_MY_CHANNEL_ADDED)


    # 在美女频道列表中，点击标签，详情页正常显示
    def clickMeiNvLable(self, element):
        # 判断是否在美女频道列表中
        if self.base.elementIsExit(ZIXUN_CHANNEL_MEINV):
            self.base.clickByElement(element, '在美女频道列表中，点击标签，进入标签详情页')
        else:
            self.assertFalse(ZIXUN_CHANNEL_MEINV)


    # 在美女频道列表中，点击图片，进入图片详情页
    def clickMeiNvList(self):
        # 判断是否在美女频道列表中
        if self.base.elementIsExit(ZIXUN_CHANNEL_MEINV):
            self.base.clickByElement(ZIXUN_MEINV_PICTURE, '在美女频道列表中，点击图片，进入图片详情页')
        else:
            self.assertFalse(ZIXUN_CHANNEL_MEINV)


    # 频道管理页面，点击添加频道
    def addZiXunChannel(self,element):
        # 判断我的频道ID是否存在
        if self.base.elementIsExit(ZIXUN_MY_CHANNEL_NEW_ADD):
            self.base.clickByElement(element, '我的频道管理页面，进行"添加"频道')
        else:
            self.assertFalse(ZIXUN_MY_CHANNEL_NEW_ADD)


    # 频道管理页面，长按“我的频道”内容
    def longPressZiXunChannel(self,element):
        # 判断我的频道ID是否存在
        if self.base.elementIsExit(ZIXUN_MY_CHANNEL_ADDED):
            self.base.long_clickByElement(element, '我的频道管理页面，长按“头条”频道内容，显示“X”按钮')
        else:
            self.assertFalse(ZIXUN_MY_CHANNEL_ADDED)


    # 频道管理页面，点击“编辑”按钮
    # def clickEditorButton(self):
    #     # 判断我的频道ID是否存在
    #     if self.base.elementIsExit(ZIXUN_MY_CHANNEL_ADDED):
    #         self.base.clickByElement(ZIXUN_CHANNEL_EDITOR, '我的频道管理页面，点击我的频道的“编辑”按钮')
    #     else:
    #         self.assertFalse(ZIXUN_MY_CHANNEL_ADDED)


    # 删除频道或者删除资讯文章
    def clickDeleteZiXunChannel(self,element,num):
        # 判断“头条”频道是否存在
        if self.base.elementIsExit(ZIXUN_CHANNEL_TOUTIAO):
            for i in range(num):
                self.base.clickByElement(element, '点击"X"按钮，进行"删除"文章/频道')
        else:
            self.assertFalse(ZIXUN_CHANNEL_TOUTIAO)


    # 频道管理页面，点击“完成”按钮
    def clickFinishButton(self):
        # 判断我的频道ID是否存在
        if self.base.elementIsExit(ZIXUN_MY_CHANNEL_ADDED):
            self.base.clickByElement(ZIXUN_CHANNEL_FINISH, '我的频道管理页面，点击我的频道的"完成"按钮')
        else:
            self.assertFalse(ZIXUN_MY_CHANNEL_ADDED)



