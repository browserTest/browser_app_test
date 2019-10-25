from base_function.base import Base
from browser.browser_element.AddToHome import *


class AddToHomePage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击负一屏精选页面添加按钮
    def clickChoiceAddTo(self):
        if self.base.elementIsExit(CHOICE_ADD_TO_XPATH):
            self.base.clickByElementIdAndText(CHOICE_ADD_TO_XPATH, '负一屏精选页面添加按钮')
        else:
            self.assertFalse(CHOICE_ADD_TO_XPATH)
