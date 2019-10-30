import pytest
from base_function.driver import Driver
from config.config import *
import re
from time import sleep

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
    def elementText(self,element):
        '''
        :param element: 元素名称，可根据resource、xpath进行判断并提取元素文本
        :return: 返回元素文本
        '''
        #text = self.d(resourceId=element).get_text()
        #return text
        if str(element).startswith("com"):
            text = self.d(resourceId=element).get_text()
            return text
        elif re.findall("//", str(element)):
            text = self.d(resourceId=element).get_text()
            return text


    # 根据元素名称进行长按操作——LYX
    def long_clickByElement(self, element, logtext):
        '''
        :param element: 元素名称，可根据resource、坐标及Text进行判断并长按
        :param logtext: 打印log的文案
        :return:
        '''
        if str(element).startswith("com"):
            self.d(resourceId=element).long_click()
        elif type(element) == tuple:
            self.d.long_click(element[0],element[1])
        else:
            self.d(text=element).long_click()
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
