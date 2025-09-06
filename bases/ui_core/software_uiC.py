import os.path, sys

from bases.ui.software import *

from PySide2.QtGui import QIcon
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QFrame
from json import dumps

from bases.api import (core, web)
from bases.api.base import APPLICATION_ROOT_DIR


class AppCard(CardWidget):
    def __init__(self, icon, title, content, address:list, func, type_:str,parent=None,btn_tips="下载"):
        """

        :param icon: 一个str链接 被用于获取图标
        :param title: 一个str 软件名称（标题）
        :param content: str 软件描述
        :param address: list 对应SoftwareLibData.json里的"download"内容
        :param func: 传入的一个方法
        :param parent: ...
        """
        super().__init__(parent)

        self.iconWidget = IconWidget(icon)
        self.titleLabel = BodyLabel(title, self)
        self.contentLabel = CaptionLabel(content, self)
        self.downloadButton = PushButton(f'{btn_tips}', self)
        self.moreButton = TransparentToolButton(FluentIcon.MORE, self)

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.setFixedHeight(73)
        self.iconWidget.setFixedSize(48, 48)
        self.contentLabel.setTextColor("#606060", "#d2d2d2")
        self.downloadButton.setFixedWidth(120)

        self.hBoxLayout.setContentsMargins(20, 11, 11, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.downloadButton, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.moreButton, 0, Qt.AlignRight)

        self.moreButton.setFixedSize(32, 32)

        self.downloadButton.clicked.connect(lambda :func(title,type_,address))


class softwareLib_ui(SoftwareLibPage,QFrame):
    def __init__(self, parents=None):
        super().__init__(parents)
        self.setupUi(self)

        self.data = {}
        self.core_api = core.API()
        self.web_api = web.API()
        self._contents_init()
        self.signal_connect()
    def _contents_init(self):
        """
        用于初始化内容
        :return:
        """
        if not os.path.exists(APPLICATION_ROOT_DIR+"\\data\\software"):
            os.mkdir(APPLICATION_ROOT_DIR+"\\data\\software")
        """初始化软件库内容"""
        result=self.web_api.get_static_software_lib_data()
        # print(1)
        print(result)
        if type(result) is str:
            self.show_edit_error(result)
        else:
            self.data=result
            with open(APPLICATION_ROOT_DIR+"\\data\\software\\SoftwareLibData.json", "w", encoding="utf-8") as file:
                file.write(dumps(result))
            self.load_data_contents()

    def _contents_reload(self):

        """
        用于刷新内容
        :return:
        """
        result=self.web_api.get_softwareLib_data() #新获取来自服务端的软件信息
        self.data=result
        with open(APPLICATION_ROOT_DIR+"\\data\\software\\SoftwareLibData.json", "w", encoding="utf-8") as file:
            file.write(dumps(result))
        self.load_data_contents()
        self.show_top_success("刷新over~",time=1000)

    def load_data_contents(self):
        """
        用于加载来自服务端数据的软件库软件信息到ui,不与服务端沟通，只负责load本地
        :return:
        """
        # logging.info("开始加载软件库数据")
        try:
            self.clear_scroll_area_with_layout()

            global data_labels
            data_labels={}
            for __labels__ in self.data.keys():
                temp=self.data[__labels__] #获取到名为 __labels__ 的软件信息(dict)详情格式见相关文件
                is_exist=self.core_api.software_if_exist(title=__labels__,type_=temp["info"]["type"])
                """ $$$TIPS!!!&&&
                在此文件中使用qfluentwidgets的图标库需通过 FluentIcon(FluentIcon.APPLICATION)使用
                而不能使用 FluentIcon.xxx !会导致堵塞/GUI不显示/隐藏式报错，不知原因！  FluentIcon(FluentIcon.APPLICATION)
                """
                icon=QIcon(self.web_api.get_icons_from_url(temp["icon"],__labels__+".png"))
                data_labels[__labels__]=AppCard(
                    icon=icon if not temp["icon"].isspace() else FluentIcon(FluentIcon.APPLICATION) ,
                    title=__labels__,
                    content=temp["description"],
                    address=temp["download"],
                    func=self.download_signal if not is_exist else self.core_api.open_software,
                    type_=temp["info"]["type"],
                    parent=self.scrollAreaWidgetContents,
                    btn_tips="下载" if not is_exist else "打开"
                )
                # data_labels[__labels__].setAlignment(Qt.AlignCenter)
                self.verticalLayout_5.addWidget(data_labels[__labels__]) #将完成的AppCard添加到scrollAreaWidgetContents中
                # data_labels[__labels__].openButton.clicked.connect(lambda: self.download_singles(__labels__,temp["info"]["type"],temp["download"])) #绑定对应Appcard中下载按钮的信号与槽

            self.end_tip = QLabel(self.scrollAreaWidgetContents)
            self.end_tip.setObjectName(u"end_tip")
            self.end_tip.setMinimumSize(QSize(100, 30))
            self.end_tip.setStyleSheet(u"#end_tip{\n"
                                       "	font: 25 10pt \"Microsoft YaHei\";\n"
                                       "	color:#dddddd;\n"
                                       "	\n"
                                       "}")
            self.end_tip.setAlignment(Qt.AlignCenter)
            self.verticalLayout_5.addWidget(self.end_tip)
            self.end_tip.setText(QCoreApplication.translate("Form", u"\u5df2\u7ecf\u5230\u5e95\u5566 QAQ", None))

        except Exception as e:
            print(e)
            self.show_top_error(f"刷新失败:{e}")
            return
    def signal_connect(self):
        """
        用于UI所有信号与槽的连接
        Special: AppCard控件的相关信号槽在设置组件时已经配置完成并几乎不再改变
        :return:
        """
        self.reload_btn.clicked.connect(self._contents_reload)

    def download_signal(self, title:str, type_:str, address:list):
        """
        用于进行每个AppCard downloadButton信号与下载功能的捆绑
        type_:文件尾缀（类型）
        :return:
        """

        try:
            for __address__ in address:#取出一个下载地址
                if not self.core_api.software_if_exist(title,type_): #判断是否已经下载了这个软件
                    if int(self.threads_spinBox.value())>0:
                        self.show_top_info(f"正在下载 {title}")
                        self.web_api.download_software(title,
                                                       type_,
                                                       __address__,
                                                       thread_count=int(self.threads_spinBox.value()),
                                                       callback=self.show_top_info_slot
                                                       )#int(self.theads_spinBox.value())) #下载
                    else:
                        self.show_top_error(f"0个下载线程啥也干不了......")
                else:
                    # self.show_edit_error("已经下载了该软件了喔 QAQ")
                    self.show_top_error("已经下载了该软件了喔 QAQ")
        except Exception as e:
            self.show_top_error(f"下载失败:{e}")
    def open_signal(self, title:str):
        """
        调用function中的功能以打开软件。
        此方法默认在软件存在时运行
        :param title:
        :return:
        """
        self.core_api.open_software(title)

    def clear_scroll_area_with_layout(self):
        layout = self.scrollAreaWidgetContents.layout()
        if layout:
            #移除并删除所有布局项
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
        else:
            # 如果没有布局，直接删除所有子控件
            for child in self.scrollAreaWidgetContents.children():
                if isinstance(child, QWidget):
                    child.deleteLater()

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

    def show_top_info(self, msg: str) -> None:
        InfoBar.info(
            title='qwq',
            content=msg,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=3000,
            parent=self
        )

    @Slot(str)
    def show_top_info_slot(self, msg: str) -> None:
        InfoBar.info(
            title='qwq',
            content=msg,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=3000,
            parent=self
        )