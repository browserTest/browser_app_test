"""
运行入口

"""

import subprocess,pytest
from config.config import *


def change_report():
    cmd = "allure generate --clean " + dir_report_xml + " -o " + dir_report_html
    subprocess.call(cmd, shell=True)

pytest.main(["-s","-q" , "--cmdopt=172.18.8.148","--alluredir={}".format(dir_report_xml), "browser/browser_test/test_PersonalCenterPage.py::TestPersonalCenterPage::test001PersonalCenterPage"])
#pytest.main(["-s","-q" , "--cmdopt=172.18.8.148","--alluredir={}".format(dir_report_xml), "browser/browser_test/test_PubMethod.py"])
change_report()
