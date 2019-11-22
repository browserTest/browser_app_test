"""
运行入口

"""

import subprocess,pytest
from config.config import *


def change_report():
    cmd = "allure generate --clean " + dir_report_xml + " -o " + dir_report_html
    subprocess.call(cmd, shell=True)

pytest.main(["-s","-q" , "--cmdopt=172.29.153.125","--alluredir={}".format(dir_report_xml), "browser/browser_test/test_DownLoadPage.py"])
pytest.main(["-s","-q" , "--cmdopt=172.29.153.125","--alluredir={}".format(dir_report_xml), "browser/browser_test/test_NewsPage.py"])
pytest.main(["-s","-q" , "--cmdopt=172.29.153.125","--alluredir={}".format(dir_report_xml), "browser/browser_test/test_PubMethod.py"])
pytest.main(["-s","-q" , "--cmdopt=172.29.153.125","--alluredir={}".format(dir_report_xml), "browser/browser_test/test_QuitPage.py"])
pytest.main(["-s","-q" , "--cmdopt=172.29.153.125","--alluredir={}".format(dir_report_xml), "browser/browser_test/test_SetUpPage.py"])
pytest.main(["-s","-q" , "--cmdopt=172.29.153.125","--alluredir={}".format(dir_report_xml), "browser/browser_test/test_SharePage.py"])
pytest.main(["-s","-q" , "--cmdopt=172.29.153.125","--alluredir={}".format(dir_report_xml), "browser/browser_test/test_WindowsTabPage.py"])

change_report()
