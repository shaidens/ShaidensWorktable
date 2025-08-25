
import threading,os
import sys,ctypes

from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt

from qfluentwidgets import (setTheme,Theme)
from configures.bases.gui.default import Login_GUIcore
setTheme(Theme.DARK)
# 资源文件目录访问
def source_path(relative_path):
    # 是否Bundle Resource
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# 修改当前工作目录，使得资源文件可以被正确访问
cd = source_path('')
os.chdir(cd)



ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("starter")

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)




# if not QApplication.instance():
class Main(object):
    app: QApplication = None
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(Main, "_instance"):
            with Main._instance_lock:
                if not hasattr(Main, "_instance"):
                    Main._instance = object.__new__(cls)
        return Main._instance


def run():
    main:object = Main()
    main.app = QApplication(sys.argv)
    w = Login_GUIcore.login_ui()
    w.show()
    w.createSubInterface()
    # import msgWidget
    # a=msgWidget.MsgWidget_Page()
    # a.show()
    main.app.exec_()


if __name__ == '__main__':
    run()
