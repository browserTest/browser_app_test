import pytest
from base_function.driver import Driver
from config.config import *
import re
from time import sleep
from browser.browser_element.WindowsTabElement import *

class Base():

    def __init__(self, driver):
        self.d = driver


    # 根据app包名操作app
    def useApp(self, packagename, action):
        '''
        :param packagename: 应用包名
        :param action: 动作
        :return:
        '''
        if action == 'start':
            self.d.app_start(packagename)
        elif action == 'stop':
            self.d.app_stop(packagename)
        elif action == 'clear':
            self.d.app_clear(packagename)
        logging.info("{}： {}".format(action, packagename))


    # 对手机硬件进行home、back操作
    def usePhone(self, action):
        '''
        :param action: 操作动作
        :return:
        '''
        if action == 'home':
            self.d.press('home')
        elif action == 'back':
            self.d.press('back')
        logging.info("对设备进行操作，操作动作为： {}".format(action))


    # 根据当前屏幕显示结果确认手机是否需要先解锁
    def unlock(self):
        '''
        :param action: 操作动作
        :return:
        '''
        if not self.d.info.get('screenOn'):
            self.d.unlock()
            sleep(1)
            logging.info("解锁手机")


    # 根据元素名称进行点击操作
    def clickByElement(self, element, logtext):
        '''
        :param element: 元素名称，可根据resource、xpath及Text进行判断并点击
        :param logtext: 打印log的文案
        :return:
        '''
        if str(element).startswith("com"):
            self.d(resourceId=element).click()
        elif re.findall("//", str(element)):
            self.d.xpath(element).click()
        # 新增tuple判断————LCM
        elif type(element) == tuple:
            self.d.click(element[0], element[1])
        else:
            self.d(text=element).click()
        logging.info("点击元素: {}".format(logtext))


    # 根据元素id及text组合进行点击操作
    def clickByElementIdAndText(self, id, text, logtext):
        '''
        :param id: 元素id
        :param text: 元素text
        :return:
        '''
        self.d(resourceId=id, text= text).click()
        logging.info("点击元素： {}".format(logtext))

    # 根据元素id及text组合进行点击操作
    def clickByElementIdAndText(self, className, text, logtext):
        '''
        :param id: 元素id
        :param text: 元素text
        :return:
        '''
        self.d(className=className, text= text).click()
        logging.info("点击元素： {}".format(logtext))

    # 向下滑动页面
    def scroll(self, num = 1):
        '''
        :param num: 滑动次数，默认为1次
        :return:
        '''
        for i in range(num):
            self.d(scrollable=True).scroll(steps=100)
            sleep(1)
        logging.info("滑动页面： {}次".format(num))



    # 向下滑动页面到指定元素位置
    def scrollToElement(self, element):
        '''
        :param element: 元素名称，仅使用id或text识别，默认不查找元素，仅滑动页面
        :return:
        '''
        if str(element).startswith("com"):
            self.d(scrollable=True).scroll.to(resourceId=element)
        else:
            self.d(scrollable=True).scroll.to(text=element)
        logging.info('滑动查找元素： {}'.format(element))

    # 左右滑动页面
    def swipe(self, direction):
        """
        :param direction: 滑动方向
        :return:
        """
        self.d.swipe_ext(direction, scale=0.9)
        logging.info("向{}滑动页面".format(direction))

    # 查找元素，判断元素存在
    def elementIsExit(self, element, timeout = 5):
        '''
        :param element: 元素名称
        :param timeout: 超时时间
        :return: 返回查找结果True or False
        '''
        isExit = False
        while timeout > 0:
            # 获取到当前页面的hierarchy
            page_xml = self.d.dump_hierarchy()
            # 判断元素是否存在于hierarchy中
            if re.findall(element, page_xml):
                isExit = True
                logging.info('查询到元素： {}'.format(element))
                break
            else:
                timeout -= 1
                sleep(1)
        if isExit == False:
            logging.info('未找到元素，元素名称为: {}'.format(element))
        return isExit



    # 当元素未找到时，直接断言失败，跳过该用例
    def assertFalse(self, element):
        '''
        :param element: 元素名称
        :return:
        '''
        assert False , '未找到元素，断言失败，元素名称为： {}'.format(element)



    # 断言元素是否存在
    def assertTrue(self, element, mark = True, timeout = 5):
        '''
        :param element: 元素名称
        :param timeout: 超时时间
        :param mark: 判断元素是否存在，默认为True，如判断元素不存在，则必须传False
        :return:
        '''
        if mark:
            assert self.elementIsExit(element, timeout) == True, "断言元素存在失败，元素名称为： {}".format(element)
            logging.info("已找到元素，断言成功，元素名称为： {}".format(element))
        else:
            assert self.elementIsExit(element, timeout) == False, "断言元素不存在失败，元素名称为： {}".format(element)
            logging.info("元素已不存在，断言成功，元素名称为： {}".format(element))


    # 提取元素文本    ---wmw
    def elementText(self,element,logtext):
        '''
        :param element: 元素名称，可根据resource、xpath进行判断并提取元素文本
        :param logtext: 打印log的文案
        :return:
        '''
        if str(element).startswith("com"):
            text = self.d(resourceId=element).get_text()
            logging.info("提取元素文本: {}".format(logtext))
            return text
        elif re.findall("//", str(element)):
            text = self.d.xpath(element).get_text()
            logging.info("提取元素文本: {}".format(logtext))
            return text

    # 输入文本——LYX
    def elementSetText(self,element,text,logtext):
        '''
        :param element: 元素名称，可根据resource、xpath进行判断并设置文本
        :param logtext: 打印log的文案
        :return:
        '''
        if str(element).startswith("com"):
            text = self.d(resourceId=element).set_text(text)
        elif re.findall("//", str(element)):
            text = self.d.xpath(element).set_text(text)
            logging.info("提取元素文本: {}".format(logtext))


    # 根据元素名称进行长按操作——LYX
    def long_clickByElement(self, element, logtext,duration=5):
        '''
        :param element: 元素名称，可根据resource、坐标及Text进行判断并长按
        :param logtext: 打印log的文案
        :return:
        '''
        if str(element).startswith("com"):
            self.d(resourceId=element).long_click(duration)
        elif type(element) == tuple:
            self.d.long_click(element[0],element[1],duration)
        else:
            self.d(text=element).long_click(duration)
        logging.info("长按元素: {}".format(logtext))

    # 根据元素id及text组合进行长按操作——LYX
    def long_clickByElementIdAndText(self, id, text, logtext):
        '''
        :param id: 元素id
        :param text: 元素text
        :return:
        '''
        self.d(resourceId=id, text= text).long_click()
        logging.info("点击元素： {}".format(logtext))


    # 根据元素名称拖动控件——LYX
    def swipeByElement(self, element, direction,logtext,steps=20):
        '''
        :param element: 元素名称，可根据resource、坐标及Text进行判断并拖动
        :param logtext: 打印log的文案
        :return:
        '''
        if str(element).startswith("com"):
            self.d(resourceId=element).swipe(direction,steps)
        elif re.findall("//", str(element)):
            self.d.xpath(element).swipe(direction,steps)
        else:
            self.d(text=element).swipe(direction,steps)
        logging.info("长按元素: {}".format(logtext))


    # 多窗口页面滑动操作————LCM
    def scrollWindowsTabAction(self,element,num = 1):
        '''
        :param element:滑动多窗口及删除多窗口位置操作
        :param num:多窗口浏览页向上滑动的次数，默认为1次
        :return:
        '''
        if str(element).startswith('com'):
            for i in range(num):
                # 多窗口浏览上滑，删除窗口
                # self.d(resourceId=element).drag_to(element[0], duration=0.05)
                self.d(resourceId=element).drag_to(WINDOWS_POSITION_AFTER[0],WINDOWS_POSITION_AFTER[1], duration=0.05)
        elif type(element) == tuple:
            # 底部工具栏长按menu_more,点击X删除多窗口
            self.d.swipe(element[0],element[1],element[2],element[3])
        else:
            for j in range(num):
                # 水平向左滑动页面
                self.d(scrollable=True).scroll.horiz.backward(steps=150)
                sleep(3)
                # 水平向右滑动页面
                self.d(scrollable=True).scroll.horiz.forward(steps=100)
                sleep(3)
        logging.info("滑动操作多窗口页面： {}次".format(num))


    # 根据元素id位于第几个进行点击操作——wmw
    def clickByElementIdAndInstance(self, id, logtext,instance):
        '''

        :param id: 元素ID
        :param logtext: 打印log的文案
        :param instance: 位于第几个
        :return:
        '''
        self.d(resourceId=id,instance=instance).click()
        logging.info("点击元素： {}".format(logtext))



