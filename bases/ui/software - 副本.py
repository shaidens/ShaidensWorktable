# -*- coding: utf-8 -*-
import os

################################################################################
## Form generated from reading UI file 'SoftwareLib_GUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QSize, QRect, QMetaObject, QCoreApplication, Qt)
from PySide2.QtWidgets import *
from qfluentwidgets import (PushButton, SpinBox, LineEdit, SingleDirectionScrollArea, Flyout, InfoBarIcon,
                            FlyoutAnimationType,InfoBar,InfoBarPosition, FluentIcon, CardWidget, IconWidget, BodyLabel, CaptionLabel,
                            TransparentToolButton)


# from qfluentwidgets import LineEdit
# from qfluentwidgets import PushButton,IconWidget
# from qfluentwidgets import SingleDirectionScrollArea
# from qfluentwidgets import SpinBox,Flyout,InfoBarIcon,FlyoutAnimationType,CardWidget


class SoftwareLibPage(QFrame):
    def __init__(self, parents=None):
        super().__init__(parents)
        self.data = {}
        # self.setupUi()

    def setupUi(self,Form):
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(704, 500)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        # self.verticalLayout.setSpacing(50)
        # self.a_spacer_v=QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.up = QFrame(self)
        self.up.setObjectName(u"up")

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up.sizePolicy().hasHeightForWidth())
        self.up.setSizePolicy(sizePolicy)
        self.up.setMaximumSize(QSize(16777215, 100))
        self.up.setFrameShape(QFrame.StyledPanel)
        self.up.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.up)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.up_left = QFrame(self.up)
        self.up_left.setObjectName(u"up_left")
        self.up_left.setMinimumSize(QSize(200, 0))
        self.up_left.setMaximumSize(QSize(250, 16777215))
        self.up_left.setFrameShape(QFrame.StyledPanel)
        self.up_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.up_left)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(self.up_left)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"#title{\n"
                                 "	\n"
                                 "color:white;\n"
                                 "	font: 20pt \"Microsoft YaHei UI\";\n"
                                 "}")

        self.verticalLayout_2.addWidget(self.title)

        self.subtitle = QLabel(self.up_left)
        self.subtitle.setObjectName(u"subtitle")
        self.subtitle.setStyleSheet(u"#subtitle{\n"
                                    "	font: 25 10pt \"Microsoft JhengHei\";\n"
                                    "color:white;\n"
                                    "}")

        self.verticalLayout_2.addWidget(self.subtitle)

        self.horizontalLayout.addWidget(self.up_left)

        self.up_right = QFrame(self.up)
        self.up_right.setObjectName(u"up_right")
        self.up_right.setFrameShape(QFrame.StyledPanel)
        self.up_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.up_right)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.up_right_up = QFrame(self.up_right)
        self.up_right_up.setObjectName(u"up_right_up")
        self.up_right_up.setFrameShape(QFrame.StyledPanel)
        self.up_right_up.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.up_right_up)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.reload_btn = PushButton(self.up_right_up)
        self.reload_btn.setObjectName(u"reload_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.reload_btn.sizePolicy().hasHeightForWidth())
        self.reload_btn.setSizePolicy(sizePolicy1)
        self.reload_btn.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_3.addWidget(self.reload_btn)

        self.tasks_btn = PushButton(self.up_right_up)
        self.tasks_btn.setObjectName(u"tasks_btn")
        self.tasks_btn.setMinimumSize(QSize(85, 0))
        self.tasks_btn.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_3.addWidget(self.tasks_btn)

        self.treads_spinBox_tip = QLabel(self.up_right_up)
        self.treads_spinBox_tip.setObjectName(u"treads_spinBox_tip")

        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.treads_spinBox_tip.sizePolicy().hasHeightForWidth())
        self.treads_spinBox_tip.setSizePolicy(sizePolicy2)
        self.treads_spinBox_tip.setStyleSheet("""
        #treads_spinBox_tip{
        color:white;
        }
        """)
        self.horizontalLayout_3.addWidget(self.treads_spinBox_tip)

        self.threads_spinBox = SpinBox(self.up_right_up)
        self.threads_spinBox.setObjectName(u"threads_spinBox")
        self.horizontalLayout_3.addWidget(self.threads_spinBox)

        self.verticalLayout_3.addWidget(self.up_right_up)

        self.up_right_down = QFrame(self.up_right)
        self.up_right_down.setObjectName(u"up_right_down")
        self.up_right_down.setFrameShape(QFrame.StyledPanel)
        self.up_right_down.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.up_right_down)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.search_eidt = LineEdit(self.up_right_down)
        self.search_eidt.setObjectName(u"search_eidt")

        self.horizontalLayout_2.addWidget(self.search_eidt)

        self.search_btn = PushButton(self.up_right_down)
        self.search_btn.setObjectName(u"search_btn")

        self.horizontalLayout_2.addWidget(self.search_btn)

        self.verticalLayout_3.addWidget(self.up_right_down)

        self.horizontalLayout.addWidget(self.up_right)

        self.verticalLayout.addWidget(self.up)

        self.down = QFrame(self)
        self.down.setObjectName(u"down")
        self.down.setMinimumSize(QSize(0, 350))
        self.down.setFrameShape(QFrame.StyledPanel)
        self.down.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.down)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = SingleDirectionScrollArea(self.down)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 682, 360))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.down)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def show_edit_error(self, msg: str) -> None:
        Flyout.create(
            icon=InfoBarIcon.ERROR,
            title='Oops! :(',
            content=msg,
            target=self.invitation_edit,
            parent=self.frame_4,
            isClosable=True,
            aniType=FlyoutAnimationType.PULL_UP
        )

    def show_top_error(self, msg: str, time=5000) -> None:
        self.infoBar = InfoBar.error(
            title='Error:(',
            content="😑" + msg,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=time,
            parent=self
        )

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u5e93", None))
        self.subtitle.setText(QCoreApplication.translate("Form",
                                                         u"\u8fd9\u70e7\u5f55\u4e86\u4e00\u4e9b\u53ef\u80fd\u5e38\u7528\u7684\u8f6f\u4ef6",
                                                         None))
        self.reload_btn.setText(QCoreApplication.translate("Form", u"\u5237\u65b0", None))
        self.tasks_btn.setText(QCoreApplication.translate("Form", u"\u4efb\u52a1\u5217\u8868", None))
        self.treads_spinBox_tip.setText(
            QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u7ebf\u7a0b\u6570\uff1a", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))

    # retranslateUi
