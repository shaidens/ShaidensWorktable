
import threading, os
import sys, ctypes

from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt

from qfluentwidgets import (setTheme,Theme)
from bases.ui_core import login_uiC

import sys, os
import PySide2
import faulthandler
faulthandler.enable() #debug
setTheme(Theme.DARK)
#Pyside 插件平台初始化
dir_name = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dir_name, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
print(plugin_path)

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("starter")

#High DPI适配
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)


# if not QApplication.instance():
class Main(object):
    _instance = None
    _instance_lock = threading.Lock()
    app: QApplication = None

    def __init__(self):
        # 只初始化一次
        if not hasattr(self, '_initialized'):
            self._initialized = True
            # 在这里添加其他初始化逻辑

    def __new__(cls, *args, **kwargs) -> object:
        if not cls._instance:
            with cls._instance_lock:
                if not cls._instance:
                    cls._instance = super(Main, cls).__new__(cls)

        return cls._instance

    @classmethod
    def get_instance(cls) -> 'Main':
        """获取单例实例的类方法"""
        return cls()


def run():
    global main
    main = Main()
    main.app = QApplication(sys.argv)
    print(main, 1)
    w = login_uiC.login_ui()
    w.show()
    w.createSubInterface()

    main.app.exec_()

def get_main_singleton():
    return Main.get_instance()

if __name__ == '__main__':
    run()
