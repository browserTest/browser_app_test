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


    # 滑动页面,默认滑动一次
    def scrollPage(self, num = 1):
        self.base.scroll(num)


    # 滑动页面到指定元素
    def scrollPageToElement(self, element):
        self.base.scrollToElement(element)
