import pytest
from base_function.base import Base
from browser.browser_element.PubElement import *
from time import sleep


class PubMethod(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 启动应用
    def startApp(self, packagename):
        self.base.useApp(packagename, 'start')
        sleep(1)

    # 退出应用
    def stopApp(self, packagename):
        self.base.useApp(packagename, 'stop')
        sleep(1)

    # 清除应用数据
    def clearApp(self, packagename):
        self.base.useApp(packagename, 'clear')
        sleep(1)
