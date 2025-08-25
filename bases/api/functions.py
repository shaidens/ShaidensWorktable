import os, sys, shutil, logging, requests
import threading
import gc
import zipfile

import urllib3.exceptions
from PySide2.QtCore import QThread, Signal
from queue import Queue


from libs.web_socket.client import Client, setup



# logger=logging.info("functions.py -> APPLICATION_ROOT_DIR:{0}".format(APPLICATION_ROOT_DIR))



class DownloadThread(QThread):
    def __init__(self, bytes_queue: Queue, url, temp_dir):
        super().__init__()
        self.bytes_queue = bytes_queue
        self.url = url
        self.temp_dir = temp_dir

    def run(self):
        while not self.bytes_queue.empty():
            bytes_range = self.bytes_queue.get()
            headers = {
                "User-Agent": "Mozilla/5.0",
                "Range": "bytes={}".format(bytes_range[1])
            }
            response = requests.get(self.url, headers=headers)
            with open(self.temp_dir + r"\{0}.tmp".format(bytes_range[0]), "wb") as f:
                f.write(response.content)
                logging.info("[functions] [*DownloadThread.run] in temp file {}.tmp".format(bytes_range[0]))
            response.close()
        else:
            logging.info("[functions] [*DownloadThread.run] quited.")
            self.quit()


class DownloadCoreThread(QThread):
    trigger = Signal(str)

    def __init__(self, **kwargs):
        super().__init__()

        self.url=kwargs["url"]
        self.copies_count=kwargs["copies_count"]
        self.filepath = kwargs["filepath"]
        self.filename = kwargs["filename"]
        self.temp_Dir = kwargs["temp_Dir"]
        self.copies_count = kwargs["copies_count"]
        self.thread_count = kwargs["thread_count"]

        logging.info("[functions] [DownloadCoreThread.__init__] CoreThread init over.")
    def run(self):
        self.url_init()
        # 创建线程并下载
        logging.info("[functions] [DownloadCoreThread.run] Gotten into CoreThread.")
        thread_list = []

        for i in range(self.thread_count):
            print(5141)
            thread = DownloadThread(self.bytes_queue, self.url, self.temp_Dir)
            thread.start()
            thread_list.append(thread)

        while thread_list:
            for __thread__ in thread_list:
                if not __thread__.isRunning() or __thread__.isFinished():
                    thread_list.remove(__thread__)
        else:
            self.trigger.emit("下载完成")
    def url_init(self):
        # 获取文件的大小
        try:
            response = requests.head(self.url)
            file_length = int(response.headers['Content-Length'])
            # 计算三个部分下载大小
            self.bytes_queue = Queue()
            start_bytes = -1
            for i in range(self.copies_count):
                bytes_size = int(file_length / self.copies_count) * i
                if i == self.copies_count - 1:
                    bytes_size = file_length
                bytes_length = "{}-{}".format(start_bytes + 1, bytes_size)
                self.bytes_queue.put([i, bytes_length])
                start_bytes = bytes_size
        except urllib3.exceptions.MaxRetryError or requests.exceptions.ConnectionError as e:
            logging.error("[functions] [DownloadCoreThread.url_init] Failed to get file size.\n    :------:------:------:    \n {0}".format(e))
            self.trigger.emit("Opps,下载出错了:( :{}".format(e))
            return False

class API(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        self.loaded_configures = {}

    def Set_up_init(self, configGroupPath=None):
        logging.info("Start to init.")

        setup()
        # print(SERVER_HOST)
        self.web_socket = Client()
        res = self.web_socket.init()
        if res is not True:
            logging.error("WebSocket init failed.")
        logging.info("Init finished.")
        return res

    def set_basic_directory(self):

        if not os.path.exists(APPLICATION_ROOT_DIR + r"/data"):
            os.mkdir(APPLICATION_ROOT_DIR + r"/data")
            logging.info("data directory was set up.")
        if not os.path.exists(APPLICATION_ROOT_DIR + r"/data/temp"):
            os.mkdir(APPLICATION_ROOT_DIR + r"/data/temp")
            logging.info("data_temp directory was set up.")
        # if not os.path.exists(APPLICATION_ROOT_DIR+r"/res"):
        #     os.mkdir(APPLICATION_ROOT_DIR+r"/res")
        # if not os.path.exists(APPLICATION_ROOT_DIR+r"/res/icon"):
        #     os.mkdir(APPLICATION_ROOT_DIR+r"/res/icon")
        # if not os.path.exists(APPLICATION_ROOT_DIR+r"/res/icon/software"):
        #     os.mkdir(APPLICATION_ROOT_DIR+r"/res/icon/software")
        # if not os.path.exists(APPLICATION_ROOT_DIR+r"/config"):
        #     os.mkdir(APPLICATION_ROOT_DIR+r"/config")

    def set_configures_groups(self, group_path=APPLICATION_ROOT_DIR + r"/configures/group/SST"):
        if os.path.exists(group_path):
            for __file__ in os.listdir(group_path):
                if __file__.endswith(".sd"):
                    if os.path.exists(APPLICATION_ROOT_DIR + r"/configures/configs/" + __file__):
                        os.remove(APPLICATION_ROOT_DIR + r"/configures/configs/" + __file__)
                    shutil.copy(group_path + r"/" + __file__, APPLICATION_ROOT_DIR + r"/configures/configs")
                    self.loaded_configures[
                        __file__.split(".")[0]] = APPLICATION_ROOT_DIR + r"/configures/configs/" + __file__
            logging.info("configure groups were set up.")
        else:
            raise FileNotFoundError(f"{group_path} does not exist.")

    def deal_default_configures(self):
        if os.path.exists(APPLICATION_ROOT_DIR + r"/configures/configs/user.sd"):
            logging.info("user.sd exists.")
            with open(APPLICATION_ROOT_DIR + r"/configures/configs/user.sd", "r", encoding="utf-8") as f:
                config = f.read()
                config = config.strip()
                if not config:
                    logging.info("user.sd is empty.")
                    f.__exit__()
                    with open(APPLICATION_ROOT_DIR + r"/configures/configs/user.sd", "w", encoding="utf-8") as f:
                        f.write("IMI_STATUS=False\nLATEST_INVITATION=None")
                    self.IMI_STATUS = False
                    self.LATEST_INVITATION = None
                else:
                    logging.info("user.sd is not empty.")
                    config = config.split("\n")
                    for i in config:
                        if i.startswith("#"):  # 跳过注释行
                            continue
                        if i.startswith("IMI_STATUS"):  # if_memorize_invitation是否记住邀请码
                            self.IMI_STATUS = eval(i.split("=")[1])
                            logging.info("IMI_status:%s", self.IMI_STATUS)
                        if i.startswith("LATEST_INVITATION") and self.IMI_STATUS:  # if_memorize_invitation
                            self.LATEST_INVITATION = i.split("=")[1]
                            logging.info("LATEST_INVITATION:%s", self.LATEST_INVITATION)

        else:
            logging.info("user.sd does not exist.")
            with open(APPLICATION_ROOT_DIR + r"/configures/configs/user.sd", "w", encoding="utf-8") as f:
                f.write("IMI_STATUS=False\nLATEST_INVITATION=None")
            self.IMI_STATUS = False
            self.LATEST_INVITATION = None

        self.loaded_configures["user"] = APPLICATION_ROOT_DIR + r"/configures/configs/user.sd"

        logging.info("default configure was set up.")

    def configure_add(self, config_name, key, value):
        """
        依据open(model="a").write()
        :param config_name:
        :param key:
        :param value:
        :return:
        """
        if os.path.exists(self.loaded_configures[config_name]):
            with open(self.loaded_configures[config_name], "a", encoding="utf-8") as f:
                f.write("\n" + key + "=" + value)
                logging.info("configure_add:{0}".format(key + "=" + value + "\n"))

    def configure_write(self, config_name, key, value):
        """
            依据open(model="w").write

        :param config_name:
        :param key:
        :param value:
        :return:
        """
        if os.path.exists(self.loaded_configures[config_name]):
            with open(self.loaded_configures[config_name], "w", encoding="utf-8") as f:
                f.write("\n" + key + "=" + value)
                logging.info("configure_add:{0}".format(key + "=" + value + "\n"))

    # def configure_add(self, config_name, key, value):
    def configure_change(self, config_name: str, key: str, value: bool):
        """

        :param config_name:
        :param key:
        :param value:
        :return:
        """
        if os.path.exists(self.loaded_configures[config_name]):
            with open(self.loaded_configures[config_name], "r", encoding="utf-8") as f:
                content = f.read()
                content = content.strip().split('\n')
                # print(content)
                logging.info("configure_{0}_content:{1}".format(config_name, str(content)))
            with open(self.loaded_configures[config_name], "w", encoding="utf-8") as f:
                for __key__ in content:
                    if __key__.startswith(key):
                        rekey = key + "=" + str(value)
                        content[content.index(__key__)] = rekey
                        logging.info("configure_change:{0} -> {1}".format(__key__, rekey))
                        break
                    else:
                        continue
                for __rewrite__ in content:
                    f.write("\n" + __rewrite__)
            self.deal_default_configures()

    def login(self, invitation_code: str, loading_ui=None):
        result = self.web_socket.login(invitation_code)
        return result

    def get_softwareLib_data(self):
        """回应获取软件库软件信息data的api接口"""
        result = self.web_socket.get("data_software")
        logging.info("get_softwareLib_data:{0}".format(result))
        self.web_socket.software_lib_data = result  # 顺便更新websocket的data到最新
        return result

    def root_ui_exec(self) -> None:
        from configures.bases.gui.default.Root_GUIcore import execute
        # 将execute的导入放在此处，旨在进行延迟导入，防止循环导入导致importerror
        execute()

    def get_static_software_lib_data(self):
        """
        获取客户端初始从服务端获取的软件库信息，不会再次调用client.get()
        :return:
        """
        return self.web_socket.software_lib_data

    def Software_if_exist(self, title: str) -> bool:
        """
        判断是否已经下载了该软件
        :param title: 软件名称
        :return: bool
        """
        with os.scandir(APPLICATION_ROOT_DIR + r"\data\software") as entries:  # 遍历出来的目录名称符合软件名称，可通过是否存在同名目录来判断是否存在该软件。
            for entry in entries:
                if entry.is_dir() and entry.name == title:
                    return True
        return False
    def open_software(self, title: str):
        """
        打开软件
        默认在软件存在时被调用
        :param title: 软件名称
        :return:
        """
        
        os.startfile(APPLICATION_ROOT_DIR + r"\data\software\{0}".format(title))
        
    def download_software(self, title: str, type_: str, address: str, thread_count: int = 5, copies_count: int = 20):
        temp_Dir = APPLICATION_ROOT_DIR + r"\data\temp\{0}".format(title)
        filepath = APPLICATION_ROOT_DIR + "\data\software\{0}".format(title)  # 下载后保存的文件路径

        try:
            for __dir__ in [temp_Dir, filepath]:
                if os.path.exists(__dir__):
                    shutil.rmtree(__dir__)
                    # print(__dir__)
                    os.mkdir(__dir__)
                else:
                    os.mkdir(__dir__)
            # os.mkdir(temp_Dir)  # 在临时文件夹中建立起一个单独的文件夹区域避免多软件下载时的冲突
            # os.mkdir(filepath)
        except FileExistsError:
            # breakpoint()
            raise "114514"

        url: str = address
        filename = "{0}.{1}".format(title, type_)  # 下载后保存的文件名

        thread_count = thread_count  # 启用线程数
        copies_count = 20  # 将文件分为多少个部分作为单个下载任务

        #副主线程
        self.DMT = DownloadCoreThread( url=url, filename=filename, filepath=filepath,
                                 temp_Dir=temp_Dir, thread_count=thread_count, copies_count=copies_count)
        self.DMT.start()
        self.DMT.trigger.connect(lambda :self.__localize_file__(filetype=type_,filename=filename, filepath=filepath, copies_count=copies_count, temp_Dir=temp_Dir), )
        """
        致命BUG（已修复）
        经过部分线程代码逻辑改动后，运行时出现
            finished with exit code -1073740791 (0xC0000409)
        崩溃，发现是由于QThread: Destroyed while thread is still running造成的。后将
            DMT=DownloadCoreThread(...) 改为->  self.DMT=DownloadCoreThread(...)
        bug修理完成.
        """
    def __localize_file__(self, **kwargs):
        """
        用于本地化下载后的琐碎区块文件。
        功能包括
        合成
        识别是否为zip，若是则解压
        :param kwargs:
        :return:
        """
        output_path = os.path.join(kwargs["filepath"], kwargs["filename"])

        # 删除目标文件（确保权限）
        try:
            if os.path.exists(output_path):
                os.remove(output_path)
        except PermissionError:
            logging.error(f"无法删除文件 {output_path}，权限不足")
            return False

        # 分块合并（更安全的内存管理）
        chunk_size = 4 * 1024 * 1024  # 4MB 块（更保守）
        try:
            with open(output_path, 'wb') as f_out:
                for i in range(kwargs["copies_count"]):
                    temp_path = os.path.join(kwargs["temp_Dir"], f"{i}.tmp")
                    if not os.path.exists(temp_path):
                        continue  # 跳过未完成的块

                    # 逐块验证并写入
                    with open(temp_path, 'rb') as f_in:
                        while True:
                            chunk = f_in.read(chunk_size)
                            if not chunk:
                                break
                            f_out.write(chunk)
                            f_out.flush()  # 强制写入磁盘
                            gc.collect()  # 主动触发垃圾回收
        except Exception as e:
            logging.error(f"合并文件时出错: {str(e)}")
            return False

        # 清理临时文件（确保完成后再删除）
        for i in range(kwargs["copies_count"]):
            temp_path = os.path.join(kwargs["temp_Dir"], f"{i}.tmp")
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except:
                    pass

        """
        考虑到软件库大多为.exe格式，遂决定 软件包解压功能后续添加
        """
        # 解压功能
        # if zipfile.is_zipfile(output_path) or kwargs["filetype"] == "zip":
        #     try:
        #         with zipfile.ZipFile(output_path, 'r') as zip_ref:
        #             zip_ref.extractall(kwargs["filepath"])
        #     except Exception as e:
        #         logging.error(f"解压文件时出错: {str(e)}")
        #         return False
        # return True


