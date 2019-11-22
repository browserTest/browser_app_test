from time import sleep

import pytest
from base_function.base import Base
from browser.browser_element.ToolbarPanel import *
from base_function.driver import Driver
from browser.browser_element.PubElement import *
from browser.browser_element.CollectionAndHistory import *
from browser.browser_element.PersonalCenter import *
from browser.browser_element.SearchPanel import *

class PersonalCenterPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)


    # 点击个人中心页--我的账号图标 ---wmw
    def clickFlymemeB(self):
        # 判断页面是否存在未登录
        if self.base.elementIsExit(PERSONAL_CENTER_NOT_LOGGED_IN):
            self.base.clickByElement(PERSONAL_CENTER_FLYME_ME_A, '我的账号图标')
        else:
            self.assertFalse(PERSONAL_CENTER_NOT_LOGGED_IN)

    # 点击我的消息 ---wmw
    def clickMyMessages(self):
        # 判断页面是否存在我的账号图标
        if self.base.elementIsExit(PERSONAL_CENTER_FLYME_ME_A):
            self.base.clickByElement(PERSONAL_CENTER_MY_MESSAGES, '我的消息')
        else:
            self.assertFalse(PERSONAL_CENTER_FLYME_ME_A)

    # 点击我的评论 ---wmw
    def clickMyComment(self):
        # 判断页面是否存在我的账号图标
        if self.base.elementIsExit(PERSONAL_CENTER_FLYME_ME_A):
            self.base.clickByElement(PERSONAL_CENTER_MY_COMMENT, '我的评论')
        else:
            self.assertFalse(PERSONAL_CENTER_FLYME_ME_A)

    # 判断账号是否登陆，未登录则登录账号 ---wmw
    def elementIsLandFlymeme(self):
        # 判断页面是否存在未登录
        if self.base.elementIsExit(PERSONAL_CENTER_NOT_LOGGED_IN):
            self.base.clickByElement(PERSONAL_CENTER_FLYME_ME_A, '我的账号图标')
            # 输入密码
            self.inputPassWord()
            # 点击登录
            self.clickLoggenIn()
            sleep(4)
            # 此处有bug，为了确保当前页面账号更新已登陆成功，故多点几次我的消息
            self.clickMyMessages()
            self.clickMyMessages()
        else:
            return

    # 点击赞了我的消息 ---wmw
    def clickPraisedMyMessages(self):
        if self.base.elementIsExit(PERSONAL_CENTER_MY_MESSAGES_A):
            self.base.clickByElement(PERSONAL_CENTER_MY_MESSAGES_A, '赞了我的消息')
        else:
            self.assertFalse(PERSONAL_CENTER_MY_MESSAGES_A)

    # 点击我的评论页，第一条评论 ---wmw
    def clickPraisedMyComment(self):
        if self.base.elementIsExit(PERSONAL_CENTER_MY_COMMENT_A):
            self.base.clickByElement(PERSONAL_CENTER_COMMENT_ONE, '点击我的评论页，第一条评论')
        else:
            self.assertFalse(PERSONAL_CENTER_MY_COMMENT_A)

    # 输入密码 ---wmw
    def inputPassWord(self):
        if self.base.elementIsExit(PERSONAL_CENTER_PASSWORD):
            self.base.elementSetText(PERSONAL_CENTER_PASSWORD, "app123456789" ,"输入密码")
        else:
            self.assertFalse(PERSONAL_CENTER_PASSWORD)

    # 登录 ---wmw
    def clickLoggenIn(self):
        if self.base.elementIsExit(PERSONAL_CENTER_REGISTER):
            self.base.clickByElement(PERSONAL_CENTER_LOGGED_IN, "登录")
        else:
            self.assertFalse(PERSONAL_CENTER_REGISTER)

    # 点击评论文章  ---wmw
    def clickCommentary(self):
        if self.base.elementIsExit(PERSONAL_CENTER_COMMENT_DETAILS):
            self.base.clickByElement(PERSONAL_CENTER_COMMENTARY, "点击评论文章")
        else:
            self.assertFalse(PERSONAL_CENTER_COMMENT_DETAILS)

    # 点击小游戏——LYX
    def clickMiniGame(self):
        if self.base.elementIsExit(MINI_GAME):
            self.base.clickByElement(MINI_GAME, "小游戏")
        else:
            self.assertFalse(MINI_GAME)
