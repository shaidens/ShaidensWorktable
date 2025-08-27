
from .base import *


class API(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        self.loaded_configures = {}
        # self.set_basic_directory()
        #设置初始路径的内容编写到了DIR_INIT.py中，此处暂时不考虑初始路径的设置

    def config_init(self, configGroupPath=None):
        if configGroupPath is None:
            self.set_configures_groups()
        else:
            self.set_configures_groups(configGroupPath)
        self.deal_default_configures()

    def set_configures_groups(self, group_path=APPLICATION_ROOT_DIR + r"\bases\configures\groups\SST"):
        if os.path.exists(group_path):
            for __file__ in os.listdir(group_path):
                if __file__.endswith(".sd"):
                    if os.path.exists(APPLICATION_ROOT_DIR + r"\bases\configures\active" + __file__):
                        os.remove(APPLICATION_ROOT_DIR + r"\bases\configures\active" + __file__)
                    shutil.copy(group_path + r"/" + __file__, APPLICATION_ROOT_DIR + r"\bases\configures\active")
                    self.loaded_configures[__file__.split(".")[0]] = APPLICATION_ROOT_DIR + r"/configures/configs/" + __file__
            logging.info("[core.py] configure groups were set up.")
        else:
            raise MissedConfigures(f"{group_path} does not exist.")
    def deal_default_configures(self):
        try:
            if os.path.exists(APPLICATION_ROOT_DIR + r"/bases/configures/active/user.sd"):
                logging.info("[core.py] user.sd exists.")
                with open(APPLICATION_ROOT_DIR + r"/bases/configures/active/user.sd", "r", encoding="utf-8") as f:
                    config = f.read()
                    config = config.strip()
                    if not config:
                        logging.info("[core.py] But user.sd is empty. awa")
                        f.__exit__(None, None, None)
                        with open(APPLICATION_ROOT_DIR + r"/bases/configures/active/user.sd", "w", encoding="utf-8") as f:
                            f.write(
                                """
                                IMI_STATUS=False\n
                                LATEST_INVITATION=None
                                """
                            )

                        self.IMI_STATUS = False
                        self.LATEST_INVITATION = None
                    else:
                        logging.info("[core.py]user.sd is not empty! That's awesome!! \\(AWA)/")
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
                logging.info("[core.py]user.sd does not exist. qwq")
                with open(APPLICATION_ROOT_DIR + r"/bases/configures/active/user.sd", "w", encoding="utf-8") as f:
                    f.write(
                        """
                        IMI_STATUS=False\n
                        LATEST_INVITATION=None
                        """
                    )

                    self.IMI_STATUS = False
                    self.LATEST_INVITATION = None

            self.loaded_configures["user"] = APPLICATION_ROOT_DIR + r"/bases/configures/active/user.sd"

            logging.info("[core.py] default configure was already set up.")
        except AttributeError as e:
            raise MissedConfigures(str(e))
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

    # @staticmethod
    def root_ui_exec(self) -> None:
        from bases.ui_core.home_uiC import execute
        # 将execute的导入放在此处，旨在进行延迟导入，防止循环导入导致importerror
        execute()

    @staticmethod
    def software_if_exist(title: str) -> bool:
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

    @staticmethod
    def open_software(title: str):
        """
        打开软件
        默认在软件存在时被调用
        :param title: 软件名称
        :return:
        """

        os.startfile(APPLICATION_ROOT_DIR + r"\data\software\{0}".format(title))