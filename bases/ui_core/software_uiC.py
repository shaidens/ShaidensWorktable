import os.path

import functions
from configures.bases.gui.default.SoftwareLib_GUI import *
from functions import API

from PySide2.QtGui import QIcon
from json import dumps
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

class softwareLib_ui(SoftwareLibPage):
    def __init__(self, parents=None):
        super().__init__(parents)

        self.api=API()
        # print(1)
        self.setupUi()
        # self.retranslateUi()
        self._contents_init()
        # self.load_data_contents()

        # self.more_UI_set()
    def _contents_init(self):

        if not os.path.exists(functions.APPLICATION_ROOT_DIR+"\\data\\software"):
            os.mkdir(functions.APPLICATION_ROOT_DIR+"\\data\\software")
        """初始化软件库内容"""
        result=self.api.get_static_software_lib_data()
        # print(1)
        print(result)
        if type(result) is str:
            self.show_edit_error(result)
        else:
            self.data=result
            with open(functions.APPLICATION_ROOT_DIR+"\\data\\software\\SoftwareLibData.json", "w", encoding="utf-8") as file:
                file.write(dumps(result))
            self.load_data_contents()

    def _contents_reload(self):

        """
        用于刷新内容
        :return:
        """
        result=self.api.get_softwareLib_data()
        self.data=result
        with open(functions.APPLICATION_ROOT_DIR+"\\data\\software\\SoftwareLibData.json", "w", encoding="utf-8") as file:
            file.write(dumps(result))
        self.load_data_contents()
    def load_data_contents(self):
        """
        用于加载来自服务端数据的软件库软件信息到ui
        :return:
        """
        # logging.info("开始加载软件库数据")
        global data_labels
        data_labels={}
        for __labels__ in self.data.keys():
            temp=self.data[__labels__] #获取到名为 __labels__ 的软件信息(dict)详情格式见相关文件
            is_exist=self.api.Software_if_exist(__labels__)
            """ $$$TIPS!!!&&&
            在此文件中使用qfluentwidgets的图标库需通过 FluentIcon(FluentIcon.APPLICATION)使用
            而不能使用 FluentIcon.xxx !会导致堵塞/GUI不显示/隐藏式报错，不知原因！  FluentIcon(FluentIcon.APPLICATION)
            """
            icon=QIcon(functions.get_icons_from_url(temp["icon"],__labels__+".png"))
            data_labels[__labels__]=AppCard(
                icon=icon if not temp["icon"].isspace() else FluentIcon(FluentIcon.APPLICATION) ,
                title=__labels__,
                content=temp["description"],
                address=temp["download"],
                func=self.download_signal if not is_exist else self.api.open_software,
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

    def download_signal(self, title:str, type_:str, address:list):
        """
        用于进行每个AppCard downloadButton信号与下载功能的捆绑
        type_:文件尾缀（类型）
        :return:
        """

        for __address__ in address:#取出一个下载地址
            if not self.api.Software_if_exist(title): #判断是否已经下载了这个软件
                self.api.download_software(title,type_,__address__,thread_count=int(self.threads_spinBox.value()))#int(self.theads_spinBox.value())) #下载
            else:
                # self.show_edit_error("已经下载了该软件了喔 QAQ")
                self.show_top_error("已经下载了该软件了喔 QAQ")

    def open_signal(self, title:str):
        """
        调用function中的功能以打开软件。
        此方法默认在软件存在时运行
        :param title:
        :return:
        """
        self.api.open_software(title)