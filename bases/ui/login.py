# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import LineEdit
from qfluentwidgets import PrimaryPushButton,CheckBox

import configures.qrc.LoginQRC_rc


class CheckBox_(CheckBox):
    def __init__(self,txt:str):
        super().__init__(txt)
        self.if_next_show_tips=True

class LoginPage(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(768, 489)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(768, 489))
        MainWindow.setMaximumSize(QSize(1286, 489))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_widget = QWidget(self.centralwidget)
        self.left_widget.setObjectName(u"left_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_widget.sizePolicy().hasHeightForWidth())
        self.left_widget.setSizePolicy(sizePolicy1)
        self.left_widget.setMinimumSize(QSize(518, 489))
        self.left_widget.setMaximumSize(QSize(518, 489))
        self.left_widget.setStyleSheet(u"#left_widget{\n"
"	border-image:url(:/image/res/3-2.jpg);\n"
"}")
        self.title = QLabel(self.left_widget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 420, 132, 27))
        font = QFont()
        font.setFamily(u"Microsoft JhengHei")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(56)
        self.title.setFont(font)
        self.title.setStyleSheet(u"#title{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 15pt \"Microsoft JhengHei\";\n"
"qproperty-alignment:AlignCenter;\n"
"font-weight:450;\n"
"letter-spacing:2px;\n"
"}")
        self.subtitle = QLabel(self.left_widget)
        self.subtitle.setObjectName(u"subtitle")
        self.subtitle.setGeometry(QRect(10, 450, 132, 20))
        self.subtitle.setStyleSheet(u"#subtitle{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 11pt \"Microsoft JhengHei\";\n"
"qproperty-alignment:AlignCenter;\n"
"font-weight:440;\n"
"letter-spacing:1px;\n"
"}")

        self.horizontalLayout.addWidget(self.left_widget)

        self.right_widget = QWidget(self.centralwidget)
        self.right_widget.setObjectName(u"right_widget")
        sizePolicy1.setHeightForWidth(self.right_widget.sizePolicy().hasHeightForWidth())
        self.right_widget.setSizePolicy(sizePolicy1)
        self.right_widget.setMinimumSize(QSize(250, 489))
        self.right_widget.setMaximumSize(QSize(114514, 489))
        self.right_widget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.right_widget.setLayoutDirection(Qt.LeftToRight)
        self.right_widget.setStyleSheet(u"#right_widget{\n"
"	text-align:center;\n"
"   background-color:white;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.right_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame_2 = QFrame(self.right_widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.login_title = QLabel(self.frame_2)
        self.login_title.setObjectName(u"login_title")
        self.login_title.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.login_title.sizePolicy().hasHeightForWidth())
        self.login_title.setSizePolicy(sizePolicy2)
        self.login_title.setMinimumSize(QSize(187, 30))
        self.login_title.setMaximumSize(QSize(16777215, 30))
        self.login_title.setStyleSheet(u"#login_title{\n"
"	font: 25 18pt \"Microsoft YaHei UI Light\";\n"
"	color:#262d4a;\n"
"	qproperty-alignment:AlignCenter;\n"
"}")

        self.verticalLayout_2.addWidget(self.login_title)


        self.verticalLayout.addWidget(self.frame_2)

        self.user_icon_frame = QFrame(self.right_widget)
        self.user_icon_frame.setObjectName(u"user_icon_frame")
        sizePolicy2.setHeightForWidth(self.user_icon_frame.sizePolicy().hasHeightForWidth())
        self.user_icon_frame.setSizePolicy(sizePolicy2)
        self.user_icon_frame.setMinimumSize(QSize(80, 85))
        self.user_icon_frame.setMaximumSize(QSize(114515, 85))
        self.user_icon_frame.setLayoutDirection(Qt.LeftToRight)
        self.user_icon_frame.setStyleSheet(u"#user_icon{\n"
"	background-color:rgb(255,255,255);\n"
"	\n"
"}")
        self.user_icon_frame.setFrameShape(QFrame.StyledPanel)
        self.user_icon_frame.setFrameShadow(QFrame.Raised)
        self.user_icon_frame.setLineWidth(1)
        self.horizontalLayout_2 = QHBoxLayout(self.user_icon_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.user_icon = QLabel(self.user_icon_frame)
        self.user_icon.setObjectName(u"user_icon")
        sizePolicy1.setHeightForWidth(self.user_icon.sizePolicy().hasHeightForWidth())
        self.user_icon.setSizePolicy(sizePolicy1)
        self.user_icon.setMinimumSize(QSize(65, 65))
        self.user_icon.setMaximumSize(QSize(65, 65))
        self.user_icon.setStyleSheet(u"#user_icon{\n"
"	border-image:url(:/image/res/icon/unkown_user.png);\n"
"	border-radius:40px;\n"
"	background-color:rgba(0,0,0,0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.user_icon)


        self.verticalLayout.addWidget(self.user_icon_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame = QFrame(self.right_widget)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(0, 190))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.edit_tips = QLabel(self.frame_3)
        self.edit_tips.setObjectName(u"edit_tips")
        self.edit_tips.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.edit_tips.sizePolicy().hasHeightForWidth())
        self.edit_tips.setSizePolicy(sizePolicy2)
        self.edit_tips.setMinimumSize(QSize(50, 33))
        self.edit_tips.setMaximumSize(QSize(16777215, 30))
        self.edit_tips.setStyleSheet(u"#edit_tips{\n"
"	font: 25 12pt \"Microsoft YaHei UI Light\";\n"
"	color:#262d4a;\n"
"	qproperty-alignment:AlignCenter;\n"
"}")

        self.gridLayout_2.addWidget(self.edit_tips, 0, 0, 1, 1)

        self.invitation_edit = LineEdit(self.frame_3)
        self.invitation_edit.setObjectName(u"invitation_edit")
        sizePolicy1.setHeightForWidth(self.invitation_edit.sizePolicy().hasHeightForWidth())
        self.invitation_edit.setSizePolicy(sizePolicy1)
        self.invitation_edit.setMinimumSize(QSize(242, 0))
        self.invitation_edit.setMaximumSize(QSize(16777215, 25))
        self.invitation_edit.setStyleSheet(u"\n"
"QLineEdit{\n"
"	font-size:14px;\n"
"	\n"
"	font-family:\"Agency FB\";\n"
"}")
        self.invitation_edit.setReadOnly(False)

        self.gridLayout_2.addWidget(self.invitation_edit, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(46, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)
        pushButton_icon=QIcon()
        pushButton_icon.addFile("./res/icon/complete.png")
        self.pushButton = PrimaryPushButton(pushButton_icon,' ',parent=self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_3.addWidget(self.pushButton)

        # imi_btn_group=QButtonGroup(self.frame)
        self.if_memorize_invitation=CheckBox_('记住我的邀请函')
        self.if_memorize_invitation.setObjectName("imi_radio_btn")
        self.if_memorize_invitation.setStyleSheet("""
            #imi_radio_btn{
                font-size:15px;
                
                }
            #imi_radio_btn::indicator { 
            width: 13px; height: 13px; 
            }
        """)
        # self.if_memorize_invitation.setSizeIncrement()
        # imi_btn_group.addButton(self.if_memorize_invitation)
        # self.if_memorize_invitation.setChecked(True)
        self.gridLayout_2.addWidget(self.if_memorize_invitation, 1, 1, 1, 1)


        self.horizontalSpacer_2 = QSpacerItem(46, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.frame_4, 4, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.right_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Shaiden's \u767b\u5f55 Sign in", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"SHAIDEN'S", None))
        self.subtitle.setText(QCoreApplication.translate("MainWindow", u"\u884c\u6b62\u7531\u5fc3 \u751f\u6d3b\u7531\u5df1", None))
        self.login_title.setText(QCoreApplication.translate("MainWindow", u"  \u73b0\u5728\u767b\u5f55\uff01", None))
        self.user_icon.setText("")
        self.edit_tips.setText(QCoreApplication.translate("MainWindow", u"\u9080\u8bf7\u51fd:", None))
        self.invitation_edit.setText("")
        self.invitation_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4efb\u4f55\u7684\u9080\u8bf7\u51fd\u4ee3\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Complete!", None))
    # retranslateUi

