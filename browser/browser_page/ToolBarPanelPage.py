from base_function.base import Base


class ToolBarPanelPage(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    # 点击底部工具栏的位置
    def clickToolsPanel(self ,element):
        '''
        :param element: 元素名称
        :return:
        '''
        if self.base.elementIsExit(element):
            self.base.clickByElement(element, "工具面板-》{}".format(element))
        else:
            self.base.assertFalse(element)
            
