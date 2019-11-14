import pytest
from base_function.base import Base
from browser.browser_element.PubElement import *
from time import sleep
from config.config import *
from fuzzywuzzy import fuzz, process


class PubMethod(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 启动应用
    def startApp(self, packagename):
        self.base.useApp(packagename, 'start')
        sleep(2)

    # 退出应用
    def stopApp(self, packagename):
        self.base.useApp(packagename, 'stop')
        sleep(2)

    # 清除应用数据
    def clearApp(self, packagename):
        self.base.useApp(packagename, 'clear')
        sleep(2)

    # 点击手机home键
    def clickHome(self):
        sleep(1)
        self.base.usePhone('home')


    # 点击手机back
    def clickBack(self):
        sleep(1)
        self.base.usePhone('back')

    # 点击隐私弹窗同意按钮——LYX
    def clickPrivacyAgree(self):
        if self.base.elementIsExit(PRIVACY_AGREE_BUTTUN):
            self.base.clickByElement(PRIVACY_AGREE_BUTTUN, '隐私弹窗同意按钮')
        else:
            self.assertFalse(PRIVACY_AGREE_BUTTUN)

    # 点击隐私弹窗不同意按钮——LYX
    def clickPrivacyDisagree(self):
        if self.base.elementIsExit(PRIVACY_DISAGREE_BUTTUN):
            self.base.clickByElement(PRIVACY_DISAGREE_BUTTUN, '隐私弹窗不同意按钮')
        else:
            self.assertFalse(PRIVACY_DISAGREE_BUTTUN)

    # 点击权限弹窗拒绝按钮——LYX
    def clickPermissionDisagree(self):
        if self.base.elementIsExit(PERMISSION_DISAGREE_BUTTUN):
            self.base.clickByElement(PERMISSION_DISAGREE_BUTTUN, '权限弹窗拒绝按钮')
        else:
            self.assertFalse(PERMISSION_DISAGREE_BUTTUN)

    # 点击权限弹窗允许按钮——LYX
    def clickPermissionAgree(self):
        if self.base.elementIsExit(PERMISSION_AGREE_BUTTON):
            self.base.clickByElement(PERMISSION_AGREE_BUTTON, '权限弹窗允许按钮')
        else:
            self.assertFalse(PERMISSION_AGREE_BUTTON)

    # 获取百度文字识别 API 识别并提取图片中文字————LCM
    def getBaiduApiText(self,element,conditions):
        '''
        :param element: 判断页面存在的元素
        :param conditions: 提取文字的条件
        :return: 返回提取的文字信息
        '''
        if self.base.elementIsExit(element):
            sleep(2)
            text = self.base.baiduOcr()
            textTitle = ""
            for i in range(len(text)):
                if i == conditions :
                    var = ''.join(text[i])
                    var1 = ''.join(text[i+1])
                    var2 = ''.join(text[i+2])
                    textTitle = textTitle.join(var + var1 + var2)
                    return textTitle