
from .base import *
import sys
sys.path.append("..")
from ..runtimes.web_socket.client import Client,setup





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
                logging.info("[web.py] [*DownloadThread.run] in temp file {}.tmp".format(bytes_range[0]))
            response.close()
        else:
            logging.info("[web.py] [*DownloadThread.run] quited.")
            self.quit()


class DownloadCoreThread(QThread):
    trigger = Signal(str)
    over = Signal(str) #发射后用于唤醒__localiser__
    def __init__(self, **kwargs):
        super().__init__()

        self.url=kwargs["url"]
        self.copies_count=kwargs["copies_count"]
        self.filepath = kwargs["filepath"]
        self.filename = kwargs["filename"]
        self.temp_Dir = kwargs["temp_Dir"]
        self.copies_count = kwargs["copies_count"]
        self.thread_count = kwargs["thread_count"]

        logging.info("[web.py] [DownloadCoreThread.__init__] CoreThread init over.")
    def run(self):
        try:
            self.url_init()
            # 创建线程并下载
            logging.info("[web.py] [DownloadCoreThread.run] Gotten into CoreThread.")
            thread_list = []
            if self.thread_count > 0:
                for i in range(self.thread_count):
                    thread = DownloadThread(self.bytes_queue, self.url, self.temp_Dir)
                    thread.start()
                    thread_list.append(thread)
            else:
                self.trigger.emit("你的线程下载数设置为0！Nothing happened.")
            while thread_list:
                for __thread__ in thread_list:
                    if not __thread__.isRunning() or __thread__.isFinished():
                        thread_list.remove(__thread__)
            else:
                self.over.emit("下载完成")
        except Exception as e:
            logging.error("[web.py] [DownloadCoreThread.url_init] Failed to get file size.\n          :------:------:------:          \n {0} \n".format(e))
            self.trigger.emit("Opps,下载出错了:( :{}".format(e))
            return False

    def url_init(self):
        """通过计算文件大小分配线程任务"""

        response = requests.head(self.url)
        file_length = int(response.headers['Content-Length'])
        self.bytes_queue = Queue()
        start_bytes = -1
        for i in range(self.copies_count):
            bytes_size = int(file_length / self.copies_count) * i
            if i == self.copies_count - 1:
                bytes_size = file_length
            bytes_length = "{}-{}".format(start_bytes + 1, bytes_size)
            self.bytes_queue.put([i, bytes_length])
            start_bytes = bytes_size
        #except urllib3.exceptions.MaxRetryError or requests.exceptions.ConnectionError or ConnectionRefusedError or urllib3.exceptions.NewConnectionError as e:


class API( object):
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance
    def __init__(self):
        # setup() #网络配置文件读取初始化
        self.web_socket = Client()
        result = self.web_socket.init()
        if result is not True:
            logging.error("[web.py]WebSocket init failed.")
            # 这意味着调用端需作出捕捉
            raise NoConnection("WebSocket init failed.")
        logging.info("[web.py]Init finished.")

    def login(self, invitation_code: str, loading_ui=None):
        result = self.web_socket.login(invitation_code)
        return result

    def get_softwareLib_data(self):
        """回应获取软件库软件信息data的api接口"""
        result = self.web_socket.get("data_software")
        logging.info("[web.py]get_softwareLib_data:{0}".format(result))
        self.web_socket.software_lib_data = result  # 顺便更新websocket的data到最新
        return result

    def get_static_software_lib_data(self):
        """
        获取客户端初始从服务端获取的软件库信息，不会再次调用client.get()
        :return:
        """
        return self.web_socket.software_lib_data

    def download_software(self, title: str, type_: str, address: str, thread_count: int = 5, copies_count: int = 20,callback=None):
        temp_Dir = APPLICATION_ROOT_DIR + r"\data\temp\{0}".format(title)
        filepath = APPLICATION_ROOT_DIR + r"\data\software\{0}".format(title)  # 下载后保存的文件路径

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
        self.DMT = DownloadCoreThread(
            url=url,
            filename=filename, filepath=filepath,
            temp_Dir=temp_Dir,
            thread_count=thread_count,
            copies_count=copies_count
        )

        self.DMT.start()
        self.DMT.over.connect(
            lambda :self.__localize_file__(
                filetype=type_,filename=filename, filepath=filepath,
                copies_count=copies_count,
                temp_Dir=temp_Dir
            ),
        )

        if callback is not None:
            self.DMT.trigger.connect(callback)

        """
        致命BUG（已修复）
        经过部分线程代码逻辑改动后，运行时出现
            finished with exit code -1073740791 (0xC0000409)
        崩溃，发现是由于QThread: Destroyed while thread is still running造成的。后将
            DMT=DownloadCoreThread(...) 改为->  self.DMT=DownloadCoreThread(...)
        bug修理完成.
        """
    @staticmethod
    def __localize_file__(**kwargs):
        """
        用于本地化下载后的琐碎区块文件。
        功能包括
        合成
        识别是否为zip，#(若是则解压)
        :param kwargs:
        :return:
        """
        print(1123141312)
        output_path = os.path.join(kwargs["filepath"], kwargs["filename"])

        #清理路径
        try:
            if os.path.exists(output_path):
                os.remove(output_path)
        except PermissionError:
            logging.error(f"无法删除文件 {output_path}，权限不足")
            return False

        #分块合并
        chunk_size = 4 * 1024 * 1024  # 4MB 块(稍微保守些 可稍微提升)
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
    @staticmethod
    def get_icons_from_url(url, SaveFileName: str):
        """
        用于通过request模块获取icon图片的函数
        :param url:
        :param SaveFileName:
        :return:
        """
        try:
            response = requests.get(url)
            image_data = response.content
            file_path = APPLICATION_ROOT_DIR + r"\bases\res\icon\software\{0}".format(SaveFileName)
            with open(file_path, 'wb') as f:
                f.write(image_data)
                return os.path.abspath(file_path)
        except Exception:
            return False
