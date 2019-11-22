import pytest
from base_function.driver import Driver
from config.config import *
import re
from time import sleep
from browser.browser_element.WindowsTabElement import *
from aip import AipOcr

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
        elif type(element) == tuple:
            self.d.click(element[0], element[1])
        elif str(element).startswith("android"):
            self.d(resourceId=element).click()
        else:
            self.d(text=element).click()
        logging.info("点击元素: {}".format(logtext))


    # 根据元素id及text组合进行点击操作 —— LJX
    def clickByElementIdAndText(self, id, text, logtext):
        '''
        :param id: 元素id
        :param text: 元素text
        :param logtext：打印log的文案
        :return:
        '''
        self.d(resourceId=id, text= text).click()
        logging.info("点击元素： {}".format(logtext))


    # 根据元素className及text组合进行点击操作
    def clickByElementClassNameAndText(self, className, text, logtext, instance=1):
        '''
        :param className: 传入className元素
        :param text: 传入text元素
        :param logtext: 打印log的文案
        :param instance: 第几位
        :return:
        '''
        self.d(className=className, text= text, instance= instance).click()
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
        :param element: 元素名称，仅使用id或text识别
        :return:
        '''
        if str(element).startswith("com"):
            self.d(scrollable=True).scroll.to(resourceId=element)
        else:
            self.d(scrollable=True).scroll.to(text=element)
        logging.info('滑动查找元素： {}'.format(element))

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
        sleep(2)
        if mark:
            assert self.elementIsExit(element, timeout) == True, "断言元素存在失败，元素名称为： {}".format(element)
            logging.info("已找到元素，断言成功，元素名称为： {}".format(element))
        else:
            assert self.elementIsExit(element, timeout) == False, "断言元素不存在失败，元素名称为： {}".format(element)
            logging.info("元素已不存在，断言成功，元素名称为： {}".format(element))

    # 断言元素是否相等————LCM
    def assertEqual(self, element, element1,mark = True, timeout = 5):
        '''
        :param element: 元素名称
        :param element1: 元素名称1
        :param mark: 判断两个元素是否相等，如果为True（默认），则需要判断元素相等、包含的情况；若传False，则判断两个元素不相等
        :param timeout: 超时时间
        :return:
        '''
        if mark:
            if element == element1:
                assert True, "断言元素相等失败，元素名称为： {} {}".format(element,element1)
                logging.info("元素相等，断言成功，元素名称为： {} {}".format(element,element1))
            elif element in element1:
                assert True, "断言元素包含失败，元素名称为： {} {}".format(element, element1)
                logging.info("元素包含，断言成功，元素名称为： {} {}".format(element, element1))
            else:
                logging.info("断言元素失败，元素名称为： {} {}".format(element, element1))
        else:
            assert element != element1, "断言元素不相等，断言失败，元素名称为： {} {}".format(element,element1)
            logging.info("元素不相等，断言成功，元素名称为： {} {}".format(element,element1))

    # 提取元素文本    ---wmw
    def elementText(self,element,logtext, instance=0):
        '''
        :param element: 元素名称，可根据resource、xpath进行判断并提取元素文本
        :param logtext: 打印log的文案
        :return:
        '''
        if str(element).startswith("com"):
            text = self.d(resourceId=element, instance=instance).get_text()
            logging.info("提取第{}位的{}元素文本".format(instance, logtext))
            return text
        elif re.findall("//", str(element)):
            text = self.d.xpath(element, instance=instance).get_text()
            logging.info("提取第{}位的{}元素文本".format(instance, logtext))
            return text


    # 输入文本——LYX
    def elementSetText(self,element,text,logtext):
        '''
        :param element: 元素名称，可根据resource、xpath进行判断并设置文本
        :param text:所输入的文本
        :param logtext: 打印log的文案
        :return:
        '''
        if str(element).startswith("com"):
            text = self.d(resourceId=element).set_text(text)
        elif re.findall("//", str(element)):
            text = self.d.xpath(element).set_text(text)
        logging.info("输入文本: {}".format(logtext))


    # 根据元素名称进行长按操作——LYX
    def long_clickByElement(self, element, logtext,duration=5):
        '''
        :param element: 元素名称，可根据resource、坐标及Text进行判断并长按
        :param logtext: 打印log的文案
        :param duration：长按的时长，单位秒
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
        :param logtext: 打印log的文案
        :return:
        '''
        self.d(resourceId=id, text= text).long_click()
        logging.info("长按元素： {}".format(logtext))


    # 根据元素名称拖动控件——LYX
    def swipeByElement(self, element, logtext,direction="up",steps=20):
        '''
        :param element: 元素名称，可根据resource、坐标、元组（坐标）及Text进行判断并拖动
        :param direction: 拖动的方向
        :param logtext: 打印log的文案
        :param steps：1 steps大概 5ms
        :return:
        '''
        if str(element).startswith("com"):
            self.d(resourceId=element).swipe(direction,steps)
        elif re.findall("//", str(element)):
            self.d.xpath(element).swipe(direction,steps)
        elif type(element) == tuple:
            self.d.swipe(element[0], element[1], element[2], element[3])
        else:
            self.d(text=element).swipe(direction,steps)
        logging.info("拖动元素: {}".format(logtext))


    # 将元素从一个位置滑动至另一个位置————LCM
    def dragByElement(self, element, element1, num=1):
        '''
        :param element: 元素名称，可根据resource进行判断并拖动
        :param element1:元素坐标位置
        :param num:拖动的次数
        :return:
        '''
        for i in range(num):
            if str(element).startswith('com'):
                self.d(resourceId=element).drag_to(element1[0], element1[1], duration=0.05)
            else:
                pass
        logging.info("选择一个位置拖拽到另一个位置： {}次".format(num))



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

    # 根据元素id位于第几个进行长按操作 —— LJX
    def long_clickByElementIdAndInstance(self, element, logtext, instance=0, duration=1):
        '''
        :param element: 元素id
        :param logtext: 打印log的文案
        :param duration：长按的时长，单位秒
        :param instance：第几个
        :return:
        '''
        self.d(resourceId=element, instance=instance).long_click(duration)
        logging.info("长按元素: {}".format(logtext))

    # 增加公共监听
    def browserWatcher(self):
        self.d.watchers.run()
        self.d.watcher("始终允许").when(text='始终允许').click()
        self.d.watcher("允许").when(text='允许').click()
        self.d.watcher("确定").when(text='确定').click()

    # 二进制读取图片
    def readImage(self, imageFile):
        with open(imageFile, 'rb') as fp:
            return fp.read()


    # 图片识别返回文字
    def baiduOcr(self):
        text = []
        # 增加图片名称和地址
        pic = str(now_time) + "图片识别.jpg"
        pic_name = os.path.join(dir_screenshot, pic)

        # 拼接接口参数,接口api参数详解（https://cloud.baidu.com/doc/OCR/OCR-API/26.5C.E8.AF.B7.E6.B1.82.E8.AF.B4.E6.98.8E-3.html#.E8.AF.B7.E6.B1.82.E8.AF.B4.E6.98.8E）
        options = {}
        options["recognize_granularity"] = "big"
        options["detect_direction"] = "false"
        options["vertexes_location"] = "false"
        options["probability"] = "false"

        # 传对应的参数进行实例化
        self.client = AipOcr('17235264' , 'ejTp8Xd1ZTUGjnO1WkRoWFWE', 'MPapr5pwGlYBu5GHZXjYxnGmOekDd2QB')

        # 实时截图，截图存放在screenshot目录下
        screenshot = self.d.screenshot("{}".format(pic_name))
        logging.info('截图后进行图片识别:{}'.format(pic_name))
        image = self.readImage(screenshot)

        # 获取图片文字识别后的返回结果
        result = self.client.accurate(image, options)
        for word in result['words_result']:
            text.append(word['words'])
        return text

    # 获取元素坐标信息 —— LJX
    def getInfoBottom(self, elemnt, logtext):
        '''
        :param elemnt: 元素text
        :param logtext:打印log的文案
        :return:返回元素信息的坐标
        '''
        info = self.d(text=elemnt).info
        bottom = info[bounds][bottom]
        logging.info("获取元素坐标： {}".format(logtext))
        return bottom

    # 根据焦点位置,输入文本  ---wmw
    def elementInputFocalPositionText(self,text,logtext,clear=False):
        '''
        :param text: 输入文本
        :param logtext: 打印log的文案
        :param clear: 是否先清除文本内容
        :return:
        '''
        text = self.d.send_keys(text, clear=clear)
        logging.info("根据焦点位置，输入文本: {}".format(logtext))







