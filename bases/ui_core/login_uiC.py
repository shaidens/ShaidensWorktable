

import re, os, sys
from PySide2.QtCore import Qt, QSize, QEventLoop, QTimer
from PySide2.QtGui import QIcon, QScreen
from PySide2.QtWidgets import QApplication
from qframelesswindow import FramelessMainWindow, FramelessWindow, StandardTitleBar
from qfluentwidgets import (InfoBarIcon,
                            Flyout,
                            FlyoutAnimationType,
                            SplashScreen,
                            InfoBar,
                            InfoBarPosition,
                            Theme, setTheme
                            )
sys.path.append('..')
from ..ui.login import LoginPage
from ..api import (core, web)

from bases.api.base import NoConnection, MissedConfigures
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("starter")
setTheme(Theme.DARK)


class login_ui(FramelessMainWindow, LoginPage): # class login_ui(FramelessMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setTitleBar(StandardTitleBar(self))
        self.titleBar.raise_()
        self.resize(768,489)

        # self.setWindowIcon(QIcon(r":..\..\res\icon\logo2.png"))
        self.setWindowTitle("Shaiden's工作台——登录 Sign in")
        self.titleBar.titleLabel.setStyleSheet(
            """
            QLabel{
                background:transparent;
                font:13px "Segoe UI";
                padding:0 2px;
                color:white;

            }
            """
        )
        self.more_UI_set()

        self.setWindowIcon(QIcon(':/image/res/icon/logo2.png'))
        self.set_window_center()
        # # 1. 创建启动页面
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(102, 102))



    def more_UI_set(self) -> None:
        self.pushButton.clicked.connect(self.complete_btn_pressed)
        self.if_memorize_invitation.stateChanged.connect(self.imi_checkbox_update)
    # @Slot(str)
    def imi_checkbox_update(self):
        self.imi_status=self.if_memorize_invitation.isChecked()
        if self.if_memorize_invitation.if_next_show_tips == True:
            if self.imi_status:
                self.core_api.configure_change("user","IMI_STATUS",True)
                self.core_api.configure_change("user","LATEST_INVITATION",self.invitation_edit.text())
                self.show_top_info("我的左眼用来记住你🙂~")
            else:
                self.core_api.configure_change("user","IMI_STATUS",False)
                self.show_top_info("我的右眼用来忘记你🙃~")
        else:
            if self.imi_status:
                self.core_api.configure_change("user","IMI_STATUS",True)
            else:
                self.core_api.configure_change("user","IMI_STATUS",False)
            self.if_memorize_invitation.if_next_show_tips = True

    def createSubInterface(self) -> None:
        loop = QEventLoop(self)
        QTimer.singleShot(500,loop.quit)
        loop.exec_()
        #此处进行初始化后端配置
        try:
            self.core_api = core.API()
            self.web_api = web.API()
            result = self.core_api.config_init()#r"C:/Users/shaid/Desktop/ShaidenWorkProject/Shaiden's(重定向)/Shaiden's(new)/bases/configures/groups/SST/") #此处设置配置组

            if self.core_api.IMI_STATUS:
                self.invitation_edit.setText(self.core_api.LATEST_INVITATION)
                self.if_memorize_invitation.if_next_show_tips = False
                self.if_memorize_invitation.setChecked(True)

            if isinstance(result, str):
                self.show_top_error(result)
            elif self.core_api.IMI_STATUS:
                self.complete_btn_pressed()
        except MissedConfigures as e:
            self.splashScreen.close()
            self.show_top_error("你的工作台缺少必要的配置文件！请联系Shaiden解决 [%s]" % str(e))
            return
        except NoConnection as e:
            self.splashScreen.close()
            self.show_top_error("无法连接到服务器😑 [%s]" % str(e))
            return
        self.splashScreen.close()

    def complete_btn_pressed(self) -> None:
        edit=self.invitation_edit.text()
        if edit and bool(re.match(r"^[A-Za-z0-9_-]*$",edit)):
            self.show_top_info("正在登陆中...")
            #伪延迟start
            # loop = QEventLoop(self)
            # QTimer.singleShot(250, loop.quit)
            # loop.exec_()

            result=self.web_api.login(edit)
            if isinstance(result, dict):
                if self.core_api.IMI_STATUS:
                    self.core_api.configure_change("user","LATEST_INVITATION",edit)
                self.show_top_success("登陆成功！让我们开始吧🥳🥳")
                self.infoBar.close()
                # #伪延迟end
                # loop = QEventLoop(self)
                # QTimer.singleShot(500, loop.quit)
                # loop.exec_()

                self.hide() #当界面无端消失地报错时，可以将此行注释以显示登陆界面
                self.core_api.root_ui_exec()
                # ...Function 登陆完成跳转界面
            elif result is None:
                self.show_edit_error("服务器不接受你的邀请函，因为它好像不存在😣")
            elif isinstance(result, str):
                self.show_edit_error("{0}".format(result))
            self.infoBar.close()
        elif edit:
            self.show_edit_error("你的邀请函代码格式出错啦 😣")
        else:
            self.show_edit_error("邀请函不能为空 😑")

    def show_edit_error(self,msg:str) -> None:
        Flyout.create(
            icon=InfoBarIcon.ERROR,
            title='Oops! :(',
            content=msg,
            target=self.invitation_edit,
            parent=self.frame_4,
            isClosable=True,
            aniType=FlyoutAnimationType.PULL_UP
        )
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
        self.infoBar=InfoBar.info(
            title='qwq',
            content=msg,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=time,
            parent=self
        )
    def show_top_error(self,msg:str,time=5000) -> None:
        self.infoBar=InfoBar.error(
            title='Error:(',
            content="😑"+msg,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=time,
            parent=self
        )
    def set_window_center(self) -> None:
        """使窗口居中显示"""
        # Get Screen geometry
        SrcSize = QScreen.availableGeometry(QApplication.primaryScreen())
        # Set X Position Center
        frmX = (SrcSize.width() - self.width()) / 2
        # Set Y Position Center
        frmY = (SrcSize.height() - self.height()) / 2
        # Set Form's Center Location
        self.move(frmX, frmY)

#         Flyout.create(
#             target=self.pushButton,
#             icon=InfoBarIcon.ERROR,
#             title='Lesson 4',
#             content="表达敬意吧，表达出敬意，然后迈向回旋的另一个全新阶段！",
#             isClosable=True,
#             tailPosition=TeachingTipTailPosition.BOTTOM,
#             duration=2000,
#             parent=self
#         )
