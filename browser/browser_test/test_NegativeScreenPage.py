import allure
from browser.browser_page.AddToHomePage import *
from browser.browser_page.NegativeScreenPage import *
from browser.browser_page.PubMethod import *
from browser.browser_element.AddToHome import *
from browser.browser_page.SearchPanelPage import *
from browser.browser_page.ToolBarPanelPage import *
from browser.browser_page.WindowsTabPage import *

@allure.feature("测试负一屏页面")
@pytest.mark.usefixtures("driver_setup")
class TestNegativePage():

    @pytest.fixture(scope="function")
    def negative_init(self):
        self.base = Base(self.driver)
        self.home = HomePage(self.driver)
        self.negativescreen = NegativeScreenPage(self.driver)
        self.addtohome = AddToHomePage(self.driver)
        self.pubmethod = PubMethod(self.driver)
        self.searchpanel = SearchPanelPage(self.driver)
        self.toolbarpanel = ToolBarPanelPage(self.driver)
        self.windowstab = WindowsTabPage(self.driver)
        logging.info("")
        logging.info("****开始执行用例****")
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        yield
        logging.info("****用例执行结束****")
        logging.info("")

    @allure.story('测试负一屏-》精选页添加书签、打开网站 —— LJX')
    @pytest.mark.P1
    def test001ExcellentChoiceAddBookmark(self, negative_init):
        '''
        1、进入负一屏，删除“hao123”书签
        2、进入精选页，添加“hao123”书签，点击进入“hao123”网站，断言页面是否存在'hao123导航-上网从这里开始'元素
        3、返回上一层到负一屏，上滑页面1次，断言是否存在“hao123”书签
        '''
        self.pubmethod.mbackToHomeOrNegative()
        # 进入负一屏，删除"hao123"书签
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteBookmark(HAO123)
        # 再进入精选页，添加"hao123"书签
        self.negativescreen.clickNegativeScrollUP(NEGATIVE_ADD_TEXT)
        self.addtohome.addBookmark(HAO123)
        # 点击"hao123"进入网页，断言是否存在'hao123导航-上网从这里开始'元素
        self.addtohome.clickAddToHomeWebsite(HAO123)
        self.base.assertTrue(HAO123WEB, timeout=3)
        # 返回上一层到负一屏，上滑页面1次，断言是否存在"hao123"书签
        sleep(3)
        self.base.clickByElement(WEBSITE_BACKWARD, '工底部具栏返回上一层')
        self.base.scroll()
        self.base.assertTrue(HAO123, timeout=3)

    @allure.story('测试负一屏-》分类页添加书签、打开网站 —— LJX')
    @pytest.mark.P1
    def test002ClassifyAddBookmark(self, negative_init):
        '''
        1、进入负一屏，删除“凤凰网”书签
        2、进入添加到主页-》分类-》资讯头条，添加“凤凰网”书签，点击进入“凤凰网”网站，断言页面是否存在'手机鳳凰網'元素
        3、返回上一层到负一屏，上滑页面1次，断言负一屏是否存在“凤凰网”书签
        '''
        # 进入负一屏，删除"凤凰网"书签，进入分类-》资讯头条
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteBookmark(IFENG_SIMPLIFIED)
        # 进入添加到主页-》分类-》资讯头条，添加“凤凰网”书签
        self.negativescreen.clickNegativeScrollUP(NEGATIVE_ADD_TEXT)
        self.addtohome.clickAddToHomeTab(CLASSFICATION_TEXT)
        self.addtohome.clickAddToHomeTab(INFORMATION_TEXT)
        self.addtohome.addBookmark(IFENG_SIMPLIFIED)
        # 点击"凤凰网"进入网页，断言是否进入"凤凰网"网页
        self.addtohome.clickAddToHomeWebsite(IFENG_SIMPLIFIED)
        self.base.assertTrue(IFENG_TRADITIONAL, timeout=3)
        # 返回上一层到负一屏，上滑页面1次，断言是否存在"凤凰网"书签
        sleep(2)
        self.base.clickByElement(WEBSITE_BACKWARD, '工底部具栏返回上一层')
        self.base.scroll()
        self.base.assertTrue(IFENG_SIMPLIFIED, timeout=3)

    @allure.story('测试负一屏-》历史页添加书签、打开网站 —— LJX')
    @pytest.mark.P1
    def test003HistoryAddBookmark(self, negative_init):
        '''
        1、进入负一屏，删除“百度一下”书签
        2、访问"m.baidu.com"
        3、进入添加到主页-》历史，断言是否存在"百度一下"元素
        4、添加“百度一下”书签，点击进入“百度一下”网站，断言页面是否存在'百度一下，你就知道'元素
        5、返回上一层到负一屏，上滑页面1次，断言负一屏是否存在“百度一下”书签
        '''
        # 调方法保证无痕模式已关闭
        # 进入负一屏，删除“百度一下”书签
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteBookmark(BAIDU_TEXT)
        # 点击搜索框，搜索'm.baidu.com'
        self.home.clickHomeSearch()
        self.searchpanel.inputBaidu()
        self.searchpanel.clickSearchInto()
        # 监听地理位置弹框，点击“始终允许”
        self.base.browserWatcher()
        sleep(2)
        # 返回上一层到负一屏，点击"添加"，进入历史，断言是否存在"百度一下"网页，并添加书签
        self.base.clickByElement(WEBSITE_BACKWARD, '工底部具栏返回上一层')
        self.negativescreen.clickNegativeScrollUP(NEGATIVE_ADD_TEXT)
        self.addtohome.clickAddToHomeTab(HISTORY_TEXT)
        self.base.assertTrue(BAIDU_TEXT, timeout=3)
        self.addtohome.addBookmark(BAIDU_TEXT)
        # 点击"百度一下"进入网页，断言是否存在"百度一下，你就知道"元素
        self.addtohome.clickAddToHomeWebsite(BAIDU_TEXT)
        self.base.assertTrue(BAIDU_LOGO, timeout=3)
        # 返回上一层到负一屏，上滑页面1次，断言是否存在"百度一下"书签
        sleep(2)
        self.base.clickByElement(WEBSITE_BACKWARD, '工底部具栏返回上一层')
        self.base.scroll()
        self.base.assertTrue(BAIDU_TEXT, timeout=3)

    @allure.story('测试负一屏-》自定义页添加书签 —— LJX')
    @pytest.mark.P1
    def test004DIYAddBookmark(self, negative_init):
        '''
        1、进入负一屏，删除“百度搜索”书签
        2、进入负一屏-》自定义，网址输入框输入'baidu'关键字,点击联想词“百度搜索”，再点击“添加”
        3、停留2秒，toast消失后，上滑页面1次，断言负一屏是否存在“百度搜索”书签
        '''
        # 进入负一屏，删除“百度一下”书签
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteBookmark(BAIDU_SEARCH)
        # 在负一屏点击"添加"，进入自定义
        self.negativescreen.clickNegativeScrollUP(NEGATIVE_ADD_TEXT)
        self.addtohome.clickAddToHomeTab(DIY_TEXT)
        # 点击网址输入框，输入'baidu'关键字,点击联想词“百度搜索”，再点击“添加”
        self.addtohome.clickAddToHomeTab(DIY_URL_ID)
        self.base.elementSetText(DIY_URL_ID, 'baidu', '网址输入框输入"baidu"')
        self.addtohome.clickAddToHomeTab(BAIDU_THINK)
        self.addtohome.clickAddToHomeTab(DIY_ADD_ID)
        sleep(2)
        # 上滑页面1次，断言页面是否存在"百度搜索"书签
        self.base.scroll()
        self.base.assertTrue(BAIDU_SEARCH, timeout=3)

    @allure.story('添加书签后，在负一屏点击默认图标和任一手动添加图标，正常跳转 —— LJX')
    @pytest.mark.P1
    def test005AddBookmark(self, negative_init):
        '''
        1、进入负一屏，删除"魅族社区"书签
        2、进入精选页，添加“魅族社区”书签，返回上一层到负一屏，断言负一屏是否存在“魅族社区”书签，点击进入“魅族社区”网站，断言页面是否存在'魅族社区'元素
        3、点击进入“网址导航”网站，断言页面是否存在'网址导航'元素
        '''
        # 进入负一屏，删除"魅族社区"书签
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteBookmark(MEIZU_COMMUNITY)
        # 再进入精选页，添加"魅族社区"书签
        self.negativescreen.clickNegativeScrollUP(NEGATIVE_ADD_TEXT)
        self.addtohome.addBookmark(MEIZU_COMMUNITY)
        # 返回上一层到负一屏，上滑页面1次，断言是否存在"魅族社区"书签
        self.pubmethod.clickBack()
        sleep(1)
        self.base.scroll()
        self.base.assertTrue(MEIZU_COMMUNITY, timeout=3)
        # 负一屏点击“魅族社区”书签，断言是否正常跳转
        self.negativescreen.clickNegativeScrollUP(MEIZU_COMMUNITY)
        self.base.assertTrue(MEIZU_COMMUNITY_HOME, timeout=3)
        sleep(2)
        self.base.clickByElement(WEBSITE_BACKWARD, '工底部具栏返回上一层')
        # 负一屏点击“网址导航”书签，断言是否正常跳转
        # todo:缺少下滑
        self.negativescreen.clickNegativeScrollUP(WEBSITE_GUIDE)
        self.base.assertTrue(WEBSITE_GUIDE_HOME, timeout=3)

    @allure.story('长按负一屏图标：新窗口打开功能正常 —— LJX')
    @pytest.mark.P1
    def test006NegativeNewWindowOpen(self, negative_init):
        '''
        1、当负一屏不存在“魅族社区”书签，则进入精选页添加“魅族社区”
        2、进入负一屏，获取当前窗口数量，长按“魅族社区”书签，选择新窗口打开，断言正常打开
        3、获取当前窗口数量，断言窗口数量+1
        '''
        # 进入负一屏，添加"魅族社区"书签
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.addBookmarkToNegative(MEIZU_COMMUNITY)
        # 多窗口打开前，获取窗口数量
        winNumBefore = self.windowstab.getWindowsNum()
        # 长按"魅族社区"，多窗口打开
        self.negativescreen.longClickNegative(MEIZU_COMMUNITY)
        self.negativescreen.clickNegative(NEW_WINDOW_OPEN)
        # 多窗口打开后，获取窗口数量
        winNumAfter = self.windowstab.getWindowsNum()
        # 断言当前页面存在"热帖"元素，且窗口数量+1
        self.base.assertTrue(MEIZU_COMMUNITY_HOME, timeout=3)
        self.base.assertEqual(int(winNumBefore)+1, int(winNumAfter), True, timeout=3)

    @allure.story('长按负一屏图标：删除功能正常 —— LJX')
    @pytest.mark.P1
    def test007NegativeDelete(self, negative_init):
        '''
        1、当负一屏不存在“魅族社区”书签，则进入精选页添加“魅族社区”
        2、在负一屏，长按“魅族社区”书签，选择删除后，断言不存在“魅族社区”元素
        '''
        # 进入负一屏，添加"魅族社区"书签
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.addBookmarkToNegative(MEIZU_COMMUNITY)
        # 长按删除"魅族社区"书签，断言当前页面不存在"魅族社区"
        self.negativescreen.longClickNegative(MEIZU_COMMUNITY)
        self.negativescreen.clickNegative(DELETE_TEXT)
        self.base.assertTrue(MEIZU_COMMUNITY, False, timeout=3)

    @allure.story('长按负一屏图标：编辑功能正常 —— LJX')
    @pytest.mark.P1
    def test008NegativeEdit(self, negative_init):
        '''
        1、如果负一屏存在“豆瓣”，删除“豆瓣”书签
        2、添加“魅族社区”书签
        3、长按“魅族社区”书签，选择编辑，编辑成豆瓣网站
        4、返回负一屏，断言负一屏存在“豆瓣”书签
        5、点击打开"豆瓣"，断言是否存在"豆瓣App 记录你的书影音生活"元素
        '''
        # 进入负一屏，删除"豆瓣"书签
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteBookmark(DOUBAN_NAME)
        # 如果负一屏不存在"魅族社区"书签，则添加该书签
        self.negativescreen.addBookmarkToNegative(MEIZU_COMMUNITY)
        # 长按编辑"魅族社区"，修改网址名称和URL为"豆瓣"
        self.negativescreen.longClickNegative(MEIZU_COMMUNITY)
        self.negativescreen.clickNegative(EDIT)
        self.negativescreen.clickNegative(WEBSITE_NAME)
        self.negativescreen.setText(WEBSITE_NAME, DOUBAN_NAME)
        self.negativescreen.clickNegative(WEBSITE_URL)
        self.negativescreen.setText(WEBSITE_URL, DOUBAN_URL)
        self.negativescreen.clickNegative(EDIT_CONFIRM)
        # 等1秒后，上滑1次页面，断言负一屏存在"豆瓣"元素，打开
        sleep(1)
        self.base.scroll()
        self.base.assertTrue(DOUBAN_NAME, True, timeout=3)
        self.negativescreen.clickNegative(DOUBAN_NAME)
        self.base.assertTrue(DOUBAN_HOME, timeout=3)

    @allure.story('长按负一屏图标：发送至桌面功能正常 —— LJX')
    @pytest.mark.P1
    def test009NegativeSendToDesk(self, negative_init):
        '''
        1、当桌面存在“魅族社区”，则删除“魅族社区”
        1、进入浏览器，当负一屏不存在“魅族社区”书签，则进入精选页添加“魅族社区”
        2、进入负一屏，长按“魅族社区”书签，选择发送至桌面，断言桌面存在“魅族社区”书签
        '''
        # 桌面删除书签存在问题：没有左右滑动桌面找书签
        # 退出浏览器，在桌面删除"魅族社区"
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.deleteBookmark(MEIZU_COMMUNITY, TOP_OF_LAUNCHER)
        # 打开浏览器，进入负一屏，添加"魅族社区"书签
        self.pubmethod.startApp(BROWSER_PACKAGE_NAME)
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.addBookmarkToNegative(MEIZU_COMMUNITY)
        # 3次长按"魅族社区"书签，选择发送至桌面
        self.negativescreen.sendToDeskNegative(MEIZU_COMMUNITY)
        # 等2秒后，退出浏览器，断言是否存在"魅族社区"元素、断言是否存在桌面包名元素
        sleep(2)
        self.pubmethod.stopApp(BROWSER_PACKAGE_NAME)
        self.base.assertTrue(MEIZU_COMMUNITY, True, timeout=3)
        self.base.assertTrue(LAUNCHER_PACKAGE_NAME, True, timeout=3)

    @allure.story('长按负一屏图标：多选功能正常 —— LJX')
    @pytest.mark.P1
    def test010NegativeMultiSelect(self, negative_init):
        '''
        1、进入负一屏，添加"网易"书签
        2、长按“网易”书签，进入"多选"状态，获取屏幕顶部标题
        3、点击"全选"后，再获取屏幕顶部标题，断言"全选"前后，顶部标题不一样
        4、点击"取消"后，断言当前页面不存在"取消"元素
        '''
        # 进入负一屏，添加"网易"书签
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.addBookmarkToNegative(NETEASE)
        # 长按"网易"书签
        self.negativescreen.longClickNegative(NETEASE)
        self.negativescreen.clickNegative(SELECT_MORE)
        # 点击"全选"前，获取顶部标题，点击"全选"后，再获取顶部标题
        actionBarBefore =self.negativescreen.getNegativeActionBar()
        self.negativescreen.clickNegative(SELECT)
        actionBarAfter = self.negativescreen.getNegativeActionBar()
        # 断言"全选"前后，顶部标题不一样
        self.base.assertEqual(actionBarBefore, actionBarAfter, False, timeout=3)
        # 点击"取消"退出多选状态后，断言当前页面不存在"取消"元素
        self.negativescreen.clickNegative(SELECT_CANCEL)
        self.base.assertTrue(SELECT_CANCEL, False, timeout=3)

    @allure.story('长按拖拽负一屏图标，可正常合并文件夹、重命名文件夹 —— LJX')
    @pytest.mark.P1
    def test011NegativeMergeFile(self, negative_init):
        '''
        1、当负一屏不存在“魅族社区”书签，则进入精选页添加“魅族社区”
        2、进入负一屏，长按“魅族社区”书签，选择删除，断言负一屏不存在“魅族社区”书签
        '''
        # 进入负一屏，添加"途牛旅游"、"百度新闻"书签
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHomeOnPage(MYCOLLECTION)
        # todo:最好能删除所有文件夹
        self.negativescreen.deleteFolder(AUTOMATION_FILE)
        self.negativescreen.addBookmarkToNegative(TUNIU)
        # todo:缺少下滑
        self.negativescreen.addBookmarkToNegative(BAIDU_NEWS)
        # 合并书签后，断言当前页面存在"文件夹"元素
        self.base.dragElementToElement(TUNIU, BAIDU_NEWS)
        self.base.assertTrue(FILE, timeout=3)
        # 长按"文件夹"，重命名为"自动化测试"后，断言当前页面存在"自动化测试"元素
        self.negativescreen.longClickNegative(FILE)
        self.negativescreen.clickNegative(RERAME_FILE)
        self.negativescreen.setText(RERAME_FILE_ID, AUTOMATION_FILE)
        self.negativescreen.clickNegative(CONFIRM_TEXT)
        self.base.assertTrue(AUTOMATION_FILE, timeout=3)

    @allure.story('长按文件夹，删除文件夹功能正常 —— LJX')
    @pytest.mark.P1
    def test012NegativeDeleteFile(self, negative_init):
        '''
        1、进入负一屏，长按删除"自动化测试"文件
        2、断言当前页面不存在"自动化测试"元素
        '''
        # todo:最好先保证"自动化测试"文件夹存在，不然没有删除"自动化测试"文件夹，该用例也能跑通过
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHomeOnPage(MYCOLLECTION)
        self.negativescreen.deleteFolder(AUTOMATION_FILE)
        self.base.assertTrue(AUTOMATION_FILE, False, timeout=3)

    @allure.story('长按文件夹，移动文件夹功能正常 —— LJX')
    @pytest.mark.P1
    def test013NegativeMoveFile(self, negative_init):
        '''
        1、当负一屏不存在“新浪微博”、“手机腾讯”书签，则添加书签，并合并文件夹
        2、获取"文件夹"坐标，拖拽"文件夹"到指定坐标，再获取"文件夹"坐标，断言坐标有变化
        '''
        # 进入负一屏，添加"新浪微博"、"手机腾讯"书签
        self.pubmethod.mbackToHomeOrNegative()
        self.home.clickHomeOnPage(MYCOLLECTION)
        # todo:最好能删除所有文件夹
        self.negativescreen.addBookmarkToNegative(SINA_WEIBO)
        # todo:缺少下滑
        self.negativescreen.addBookmarkToNegative(MOBILE_TENCENT)
        self.base.dragElementToElement(SINA_WEIBO, MOBILE_TENCENT)
        # 移动文件夹前，获取"自动化测试"文件夹坐标信息
        bottomBefore = self.negativescreen.folderBottom(FILE)
        self.negativescreen.dragFolder(FILE, DRAG_FILE_POSITION)
        # 移动文件夹后，获取"自动化测试"文件夹坐标信息
        bottomAfter = self.negativescreen.folderBottom(FILE)
        # 断言文件夹移动后坐标不一样
        self.base.assertEqual(bottomBefore, bottomAfter, False, timeout=3)









