# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'root_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtGui import QScreen
from PySide2.QtWidgets import QApplication
from qfluentwidgets import FluentWindow
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import (InfoBar, InfoBarPosition)
# 子界面导入
from bases.ui_core.software_uiC import softwareLib_ui
from bases.ui.home import HomePage


class Ui_MainWindow(FluentWindow):
    def __init__(self, parents=None):
        super().__init__(parents)
        self.setupUi()
        self.set_window_center()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(800, 600)

        #实例化子界面
        self.home_page_sub_interface = HomePage(self)
        self.software_lib_page_sub_interface = softwareLib_ui(self)
        self.retranslateUi()

        self.initNavigation() #初始化导航栏
        self.initWindow() #初始化窗口
        QMetaObject.connectSlotsByName(self)

    # setupUi

    def initNavigation(self):
        self.addSubInterface(self.home_page_sub_interface, FIF.HOME, 'Home')
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.software_lib_page_sub_interface, FIF.APPLICATION, '软件库')

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon(':/image/res/icon/logo2.png'))
        self.setWindowTitle("Shaiden's 工作台")

    def set_window_center(self):
        """使窗口居中显示"""
        # Get Screen geometry
        SrcSize = QScreen.availableGeometry(QApplication.primaryScreen())
        # Set X Position Center
        frmX = (SrcSize.width() - self.width()) / 2
        # Set Y Position Center
        frmY = (SrcSize.height() - self.height()) / 2
        # Set Form's Center Location
        self.move(frmX, frmY)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Shaiden's \u5de5\u4f5c\u53f0", None))
    def show_top_success(self,msg:str,time=3000) -> None:
        InfoBar.success(
            title='欧耶~ 🥳',
            content=msg,
            parent=self,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=time,
            orient=Qt.Horizontal,
        )
    def show_top_info(self,msg:str,time=1000) -> None:
        InfoBar.info(
            title='qwq',
            content=msg,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=time,
            parent=self
        )
    def show_top_error(self,msg:str,time=5000) -> None:
        InfoBar.error(
            title='Error:(',
            content="😑"+msg,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=time,
            parent=self
        )

def execute():
    # from main import Main


    w = Ui_MainWindow()
    w.show()
    w.show_top_success("登陆成功！让我们开始吧🥳🥳")
    # print(main.app ,2)
    # main.app.exec_()
    # main.app.exec_()
