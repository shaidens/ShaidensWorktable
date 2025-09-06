# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_0828.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import ElevatedCardWidget, IconWidget, FluentIcon, CaptionLabel



class FastAppCard(ElevatedCardWidget):
    icon_size=(20,20)
    def __init__(self,Icon=None, subtitle="",parents=None):
        super().__init__(parent=parents)
        self.iconLabel = IconWidget(Icon) #使用flunticon的图标库
        self.iconLabel.setFixedSize(self.icon_size[0],self.icon_size[1]) #设置图标大小
        # self.iconLabel.setObjectName("_Center_icon_icon") #好像没啥用，但是不敢动
        self.label = CaptionLabel(subtitle, parent=self) #设置小标题

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setAlignment(Qt.AlignCenter)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.iconLabel, 0, Qt.AlignCenter)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.label, 0, Qt.AlignHCenter | Qt.AlignBottom)

class HELP_CARD(FastAppCard):
    def __init__(self, parents=None):
        super().__init__(Icon=FluentIcon.HELP,subtitle="help",parents=parents)

class SETTING_CARD(FastAppCard):
    def __init__(self, parents=None):
        super().__init__(Icon=FluentIcon.SETTING,subtitle="setting",parents=parents)


class ME_CARD(FastAppCard):
    def __init__(self, parents=None):
        super().__init__(Icon=FluentIcon.PEOPLE,subtitle="Me",parents=parents)

class HomePage(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"HomePage")
        Form.resize(656, 463)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.down = QFrame(Form)
        self.down.setObjectName(u"down")
        self.down.setMinimumSize(QSize(200, 200))
        self.down.setFrameShape(QFrame.StyledPanel)
        self.down.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.down)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fc1 = SETTING_CARD(self.down)
        self.fc1.setObjectName(u"fc1")
        self.fc1.setFrameShape(QFrame.StyledPanel)
        self.fc1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.fc1)

        self.fc2 = ME_CARD(self.down)
        self.fc2.setObjectName(u"fc2")
        self.fc2.setFrameShape(QFrame.StyledPanel)
        self.fc2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.fc2)

        self.fc3 = HELP_CARD(self.down)
        self.fc3.setObjectName(u"fc3")
        self.fc3.setFrameShape(QFrame.StyledPanel)
        self.fc3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.fc3)

        self.fc4 = QFrame(self.down)
        self.fc4.setObjectName(u"fc4")
        self.fc4.setFrameShape(QFrame.StyledPanel)
        self.fc4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.fc4)


        self.gridLayout.addWidget(self.down, 2, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 450, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 4)

        self.upleft = QWidget(Form)
        self.upleft.setObjectName(u"upleft")
        self.upleft.setMinimumSize(QSize(300,130))
        self.upleft.setStyleSheet(u"#upleft{\n"
"background-color:rgba(255, 255, 255,20);\n"
"border-radius:10px;\n"
"}")
        self.title = QLabel(self.upleft)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(30, 30, 151, 41))
        self.title.setMinimumSize(QSize(101, 41))
        self.title.setStyleSheet(u"font: 25pt \"Microsoft YaHei UI\";\n"
"color:white;")
        self.label = QLabel(self.upleft)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 150, 31))
        self.label.setMinimumSize(QSize(150, 30))
        self.label.setStyleSheet(u"font: 15pt \"Microsoft YaHei UI\";\n"
"color:white;")

        self.gridLayout.addWidget(self.upleft, 0, 0, 1, 1)

        self.down_H_spacer = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.down_H_spacer, 2, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.upright = QWidget(Form)
        self.upright.setObjectName(u"upright")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.upright.setMinimumSize(QSize(400, 130))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upright.sizePolicy().hasHeightForWidth())
        self.upright.setSizePolicy(sizePolicy)
        self.upright.setStyleSheet(u"#upright{\n"
"background-color:rgba(255, 255, 255,20);\n"
"border-radius:10px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.upright)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.upright)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"\n"
"font: 12pt \"Agency FB\";\n"
"color:rgb(88, 169, 255);")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.upright)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"\n"
"font: 12pt \"Agency FB\";\n"
"color:rgb(88, 169, 255);")

        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)

        self.server_status = QLabel(self.upright)
        self.server_status.setObjectName(u"server_status")
        sizePolicy.setHeightForWidth(self.server_status.sizePolicy().hasHeightForWidth())
        self.server_status.setSizePolicy(sizePolicy)
        self.server_status.setStyleSheet(u"\n"
"font: 12pt \"Agency FB\";\n"
"color:rgb(170, 255, 0);")

        self.gridLayout_2.addWidget(self.server_status, 2, 1, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 3)

        self.label_5 = QLabel(self.upright)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"font: 63 14pt \"Cascadia Code SemiBold\";")

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.server_status_icon = QLabel(self.upright)
        self.server_status_icon.setObjectName(u"server_status_icon")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.server_status_icon.sizePolicy().hasHeightForWidth())
        self.server_status_icon.setSizePolicy(sizePolicy2)
        self.server_status_icon.setMinimumSize(QSize(0, 20))
        # self.server_status_icon.setMaximumSize(QSize(16777215, 114514))
        self.server_status_icon.setBaseSize(QSize(0, 20))
        self.server_status_icon.setStyleSheet(u"font: 50pt \"Microsoft YaHei UI\";\n"
"color:green;")

        self.gridLayout_2.addWidget(self.server_status_icon, 1, 0, 2, 1)


        self.gridLayout.addWidget(self.upright, 0, 2, 1, 2)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self,Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"Greeting!", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6b22\u8fce\u8fdb\u5165\u5de5\u4f5c\u53f0", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Server", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"[127.0.0.1]   From Tencent Beijing ", None))
        """
        bug report:
        \ud83c\udde8\ud83c\uddf3本串字符是中国国旗的emoji unicode，在setText中使用会导致访问冲突崩溃。
        """
        self.server_status.setText(QCoreApplication.translate("Form", u"Online", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"|", None))
        self.server_status_icon.setText(QCoreApplication.translate("Form", u"\u00b7", None))
    # retranslateUi

