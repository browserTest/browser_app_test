import logging
import os


"""获取相关文件目录"""

# 获取当前config配置文件的目录
dir_config = os.path.dirname(os.path.abspath(__file__))

# 通过config配置文件目录获取到上一级目录
dir_all = os.path.dirname(dir_config)

# 获取到logs的目录
dir_logs = os.path.join(dir_all, 'logs')

# 确定日志文件的目录及文件名
dir_log = os.path.join(dir_logs, 'output.log')

# 错误截图存放目录
dir_screenshot = os.path.join(dir_all, 'screenshot')

"""配置log相关信息"""
logging.basicConfig(level = logging.INFO,
                    format = '[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S',
                    filename = dir_log,
                    filemode = 'w')
