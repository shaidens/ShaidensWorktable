# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import ImageLabel, BodyLabel
from qfluentwidgets import ElevatedCardWidget
from qfluentwidgets import CaptionLabel, IconWidget

from qfluentwidgets import FluentIcon, theme


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

class _Center_icon(FastAppCard):
    def __init__(self, parents=None):
        super().__init__(Icon=FluentIcon.HELP,subtitle="help",parents=parents)

class _Middle_left(FastAppCard):
    def __init__(self, parents=None):
        super().__init__(Icon=FluentIcon.SETTING,subtitle="setting",parents=parents)


class _Middle_right(FastAppCard):
    def __init__(self, parents=None):
        super().__init__(Icon=FluentIcon.PEOPLE,subtitle="Me",parents=parents)

class HomePage(QFrame):
    APP_BOX_SIZE_X=65
    APP_BOX_SIZE_Y=65
    def __init__(self, parents=None):
        super().__init__(parents)
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Form")
        # self.resize(705, 504)
        self.setObjectName("HomePage")
        self.MainLayout = QGridLayout(self)
        self.MainLayout.setObjectName(u"QG")
        self.up = QFrame(self)
        self.up.setObjectName(u"up")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up.sizePolicy().hasHeightForWidth())
        self.up.setSizePolicy(sizePolicy)
        self.up.setMinimumSize(QSize(0, 290))
        self.up.setFrameShape(QFrame.StyledPanel)
        self.up.setFrameShadow(QFrame.Raised)
        self.up.setStyleSheet("""
        border-image:url("./res/3-3.png");
        """)
        self.horizontalLayout = QHBoxLayout(self.up)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.image_title = ImageLabel(self.up)
        self.image_title.setObjectName(u"image_title")

        self.horizontalLayout.addWidget(self.image_title)

        self.MainLayout.addWidget(self.up, 0, 0, 1, 2)


        # self.space
        # self.MainLayout.addItem(self.spacer1, 1, 1, 1,2)
        self.down = QFrame(self)
        self.down.setObjectName(u"down")
        self.down.setFrameShape(QFrame.StyledPanel)
        self.down.setFrameShadow(QFrame.Raised)
        # self.spacer1 = QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred)
        # self.down.addWidget(self.spacer1)
        self.hboxLayout = QHBoxLayout(self.down)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.top_left = ElevatedCardWidget(self.down)
        self.top_left.setObjectName(u"top_left")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        # sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.top_left.sizePolicy().hasHeightForWidth())
        self.top_left.setSizePolicy(sizePolicy1)
        self.top_left.setMinimumSize(QSize(self.APP_BOX_SIZE_X, self.APP_BOX_SIZE_Y))
        self.top_left.setFrameShape(QFrame.StyledPanel)
        self.top_left.setFrameShadow(QFrame.Raised)

        self.hboxLayout.addWidget(self.top_left, 0)

        self.top_middle = ElevatedCardWidget(self.down)
        self.top_middle.setObjectName(u"top_middle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.top_middle.sizePolicy().hasHeightForWidth())
        self.top_middle.setSizePolicy(sizePolicy2)
        self.top_middle.setMinimumSize(QSize(self.APP_BOX_SIZE_X, self.APP_BOX_SIZE_Y))
        self.top_middle.setFrameShape(QFrame.StyledPanel)
        self.top_middle.setFrameShadow(QFrame.Raised)

        self.hboxLayout.addWidget(self.top_middle, 1)

        self.top_right = ElevatedCardWidget(self.down)
        self.top_right.setObjectName(u"top_right")
        sizePolicy2.setHeightForWidth(self.top_right.sizePolicy().hasHeightForWidth())
        self.top_right.setSizePolicy(sizePolicy2)
        self.top_right.setMinimumSize(QSize(self.APP_BOX_SIZE_X, self.APP_BOX_SIZE_Y))
        self.top_right.setFrameShape(QFrame.StyledPanel)
        self.top_right.setFrameShadow(QFrame.Raised)

        self.hboxLayout.addWidget(self.top_right, 2)

        self.middle_left = _Middle_left(self.down)
        self.middle_left.setObjectName(u"middle_left")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.middle_left.sizePolicy().hasHeightForWidth())
        self.middle_left.setSizePolicy(sizePolicy3)
        self.middle_left.setMinimumSize(QSize(self.APP_BOX_SIZE_X, self.APP_BOX_SIZE_Y))
        self.middle_left.setFrameShape(QFrame.StyledPanel)
        self.middle_left.setFrameShadow(QFrame.Raised)

        self.hboxLayout.addWidget(self.middle_left, 3)

        self.center = _Center_icon(self.down)
        self.center.setObjectName(u"center")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.center.sizePolicy().hasHeightForWidth())
        self.center.setSizePolicy(sizePolicy4)
        self.center.setMinimumSize(QSize(self.APP_BOX_SIZE_X, self.APP_BOX_SIZE_Y))
        self.center.setFrameShape(QFrame.StyledPanel)
        self.center.setFrameShadow(QFrame.Raised)

        self.hboxLayout.addWidget(self.center, 4)

        self.middle_right = _Middle_right(self.down)
        self.middle_right.setObjectName(u"middle_right")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.middle_right.sizePolicy().hasHeightForWidth())
        self.middle_right.setSizePolicy(sizePolicy5)
        self.middle_right.setMinimumSize(QSize(self.APP_BOX_SIZE_X, self.APP_BOX_SIZE_Y))
        self.middle_right.setFrameShape(QFrame.StyledPanel)
        self.middle_right.setFrameShadow(QFrame.Raised)

        self.hboxLayout.addWidget(self.middle_right, 5)

        self.bottom_left = ElevatedCardWidget(self.down)
        self.bottom_left.setObjectName(u"bottom_left")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.bottom_left.sizePolicy().hasHeightForWidth())
        self.bottom_left.setSizePolicy(sizePolicy6)
        self.bottom_left.setMinimumSize(QSize(self.APP_BOX_SIZE_X, self.APP_BOX_SIZE_Y))
        self.bottom_left.setFrameShape(QFrame.StyledPanel)
        self.bottom_left.setFrameShadow(QFrame.Raised)

        self.hboxLayout.addWidget(self.bottom_left, 6)

        self.bottom_middle = ElevatedCardWidget(self.down)
        self.bottom_middle.setObjectName(u"bottom_middle")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.bottom_middle.sizePolicy().hasHeightForWidth())
        self.bottom_middle.setSizePolicy(sizePolicy7)
        self.bottom_middle.setMinimumSize(QSize(self.APP_BOX_SIZE_X, self.APP_BOX_SIZE_Y))
        self.bottom_middle.setFrameShape(QFrame.StyledPanel)
        self.bottom_middle.setFrameShadow(QFrame.Raised)

        self.hboxLayout.addWidget(self.bottom_middle, 7)

        self.bottom_right = ElevatedCardWidget(self.down)
        self.bottom_right.setObjectName(u"bottom_right")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.bottom_right.sizePolicy().hasHeightForWidth())
        self.bottom_right.setSizePolicy(sizePolicy8)
        self.bottom_right.setMinimumSize(QSize(self.APP_BOX_SIZE_X, self.APP_BOX_SIZE_Y))
        self.bottom_right.setFrameShape(QFrame.StyledPanel)
        self.bottom_right.setFrameShadow(QFrame.Raised)

        self.hboxLayout.addWidget(self.bottom_right, 8)

        self.MainLayout.addWidget(self.down, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MainLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.retranslateUi()

        # QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.image_title.setText("")
    # retranslateUi
