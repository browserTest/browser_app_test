import pytest
from base_function.base import Base
from browser.browser_element.PubElement import *
from time import sleep
from config.config import *


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