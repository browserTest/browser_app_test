from config.config import *
import uiautomator2 as u2
import pytest
from time import sleep

class Driver():

    def driver_init(self, driver_ip):
        try:
            d = u2.connect_wifi(driver_ip)
            # logging.info("成功连接到设备：{}".format(driver_ip))
            sleep(1)
            return d
        except Exception as e:
            logging.info("初始化driver出现异常：{}".format(e))








