
import re,os

from PySide2.QtCore import Qt,QSize,QEventLoop,QTimer
from PySide2.QtGui import QIcon,QScreen
from PySide2.QtWidgets import QApplication
from qframelesswindow import FramelessMainWindow,FramelessWindow,StandardTitleBar
from qfluentwidgets import (InfoBarIcon,
                            Flyout,
                            FlyoutAnimationType,
                            SplashScreen,
                            InfoBar,
                            InfoBarPosition,
                            Theme,setTheme
                            )
setTheme(Theme.DARK)

from configures.bases.gui.default.Login_GUI import LoginPage
#由于本文件的运行由main.py发起，所以默认的工作路径就是工程根目录.../Shaiden's,所以导入时需要如上。

from functions import API
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("starter")
# class login_ui(FramelessMainWindow, Ui_MainWindow):
class login_ui(FramelessMainWindow, LoginPage):

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
                self.func.configure_change("user","IMI_STATUS",True)
                self.func.configure_change("user","LATEST_INVITATION",self.invitation_edit.text())
                self.show_top_info("我的左眼用来记住你🙂~")
            else:
                self.func.configure_change("user","IMI_STATUS",False)
                self.show_top_info("我的右眼用来忘记你🙃~")
        else:
            if self.imi_status:
                self.func.configure_change("user","IMI_STATUS",True)
            else:
                self.func.configure_change("user","IMI_STATUS",False)
            self.if_memorize_invitation.if_next_show_tips = True
    def createSubInterface(self) -> None:
        loop = QEventLoop(self)
        QTimer.singleShot(500,loop.quit)
        loop.exec_()
        #此处进行初始化后端配置
        try:
            self.func = API()
            result = self.func.Set_up_init(r"C:/Users/shaid/Desktop/ShaidenWorkProject/Shaiden's/configures/group/test/") #此处设置配置组

            if self.func.IMI_STATUS:
                self.invitation_edit.setText(self.func.LATEST_INVITATION)
                self.if_memorize_invitation.if_next_show_tips = False
                self.if_memorize_invitation.setChecked(True)

            if type(result) is str:
                self.show_top_error(result)
            elif self.func.IMI_STATUS:
                self.complete_btn_pressed()
        except AttributeError as e:
            self.show_top_error("你的工作台缺少必要的配置文件！请联系Shaiden解决 [%s]" % str(e))


        self.splashScreen.close()

    def complete_btn_pressed(self) -> None:
        edit=self.invitation_edit.text()
        if edit and bool(re.match(r"^[A-Za-z0-9_-]*$",edit)):
            self.show_top_info("正在登陆中...")
            #伪延迟start
            loop = QEventLoop(self)
            QTimer.singleShot(250, loop.quit)
            loop.exec_()

            result=self.func.login(edit)
            if type(result) is dict:
                if self.func.IMI_STATUS:
                    self.func.configure_change("user","LATEST_INVITATION",edit)
                self.show_top_success("登陆成功！让我们开始吧🥳🥳")
                self.infoBar.close()
                #伪延迟end
                loop = QEventLoop(self)
                QTimer.singleShot(500, loop.quit)
                loop.exec_()

                self.hide()
                self.func.root_ui_exec()
                # ...Function 登陆完成跳转界面
            elif result is None:
                self.show_edit_error("服务器不接受你的邀请函，因为它好像不存在😣")
            elif type(result) is str:
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
