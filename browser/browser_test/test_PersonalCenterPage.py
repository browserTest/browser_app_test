from base_function.driver import *
import pytest
from config.config import *
from browser.browser_page.HomePage import HomePage
from browser.browser_page.PubMethod import PubMethod
from browser.browser_element.PubElement import *
from base_function.base import Base
from browser.browser_element.Home import *
from browser.browser_element.ToolbarPanel import *
from browser.browser_page.HomePage import *
from browser.browser_page.ToolbarPanelPage import *
from browser.browser_page.PersonalCenterPage import *
import allure
from browser.browser_element.MyCollection import *





@allure.feature("���Ը�������ҳ��")
@pytest.mark.usefixtures("driver_setup")
class TestPersonalCenterPage():

    @pytest.fixture(scope="function")
    def PersonalCenter_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.pubmethod= PubMethod(self.driver)
        self.toolbarpanel = ToolbarPanelPage(self.driver)
        self.personalcenter = PersonalCenterPage(self.driver)
        logging.info("")
        logging.info("****��ʼִ������****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****����ִ�н���****")
        logging.info("")



    @allure.story('���Ը��������˺ŵ�¼ҳ')
    def test001PersonalCenterPage(self, PersonalCenter_init):

        self.home.clickMore()
        self.toolbarpanel.clickFlymeme()
        # ����δ��¼�Ƿ����
        self.base.assertTrue333('δ��¼')


