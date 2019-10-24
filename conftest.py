
import pytest,time,allure,subprocess,uiautomator2
from config.config import *
from base_function.driver import Driver
from allure_commons.types import AttachmentType



# 命令传参方法
def pytest_addoption(parser):
    """
    :param parser:
    :return:
    """
    parser.addoption("--cmdopt",  default="172.18.8.52", help="手机的IP地址")

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


# 将dirver对象获取到并作为装饰器供其余方法调用
@pytest.fixture()
def driver_setup(request, cmdopt):
    logging.info('————————————开始执行自动化测试——————————————————')
    # 获取到driver对象
    global driver1
    driver1 = Driver().driver_init(cmdopt)
    request.instance.driver = Driver().driver_init(cmdopt)
    # 启动监听器
    # driver1.watchers.watched = True
    # browser_watcher()


# 定义监听器
def browser_watcher():
    driver1.watcher("始终允许").when(text='始终允许').click()
    driver1.watcher("允许").when(text='允许').click()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    '''
    hook pytest断言失败时截图
    :return:
    '''

    outcome = yield
    res = outcome.get_result()
    if res.when == "call" and res.failed:
        try:
            pic_info = screen()
            allure.attach(pic_info, '失败截图', AttachmentType.JPG)
        except Exception as e:
            logging.info("断言失败后截图报错：" + e)


def screen():
    '''
    截图操作
    pic_name:截图名称
    :return:
    '''
    try:
        fail_pic = str(now_time) + "_error.jpg"
        pic_name = os.path.join(dir_screenshot, fail_pic)
        driver1.screenshot("{}".format(pic_name))
        logging.info('截图:{}'.format(pic_name))
        with open(pic_name, 'rb') as r:
            file_info = r.read()
        return file_info
    except Exception as e:
        logging.info("截图失败!:{}".format(e))








