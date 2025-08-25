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

# 子界面导入
from configures.bases.gui.default.Home_GUI import HomePage
from configures.bases.gui.default.SoftwareLib_GUIcore import softwareLib_ui


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


def execute():
    from main import Main
    main = Main()
    w = Ui_MainWindow()
    w.show()
    main.app.exec_()
