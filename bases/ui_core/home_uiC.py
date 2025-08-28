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
from PySide2.QtWidgets import QApplication, QFrame
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import (InfoBar, InfoBarPosition)
# 子界面导入
from bases.ui.home import HomePage


class home_ui(QFrame,HomePage):
    def __init__(self, parents=None):
        super().__init__()

        self.setupUi(self)

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


