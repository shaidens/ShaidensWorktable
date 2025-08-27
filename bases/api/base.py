import os
import sys
import shutil
import gc
import threading
import logging

import requests
import simplejson
import urllib3.exceptions

from PySide2.QtCore import QThread, Signal
from queue import Queue

path_pieces=sys.path[0].split('\\')
disk_head=path_pieces[0]
path_pieces.pop(0)
print(path_pieces)
APPLICATION_ROOT_DIR = disk_head+"\\"+str(os.path.join(*path_pieces))  # 获取项目根目录("../Shaiden's/")


threading.stack_size(5 * 1024 * 1024)#设置线程栈大小（5MB）

gc.enable()  # 强制开启垃圾回收
gc.set_threshold(100, 10, 10)  # 调整回收频率

logging.basicConfig(level=logging.INFO, format='[%(asctime)s-%(name)s] %(message)s')


class NoConnection(Exception):
    """
    这是为了方便无法连接服务器时GUI直接捕捉错误以判断结果并直接对GUI反应，不需要API介入。
    """
    def __init__(self, e):
        self.e = e

    def __str__(self):
        return "Failed to connect to the server, because:{}".format(self.e)

class MissedConfigures(Exception):
    """
    缺少配置文件
    """
    def __init__(self, e):
        self.e = e

    def __str__(self):
        return "Missed configures:{}".format(self.e)