
from base import *


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
        if configGroupPath:
            self.set_configures_groups(configGroupPath)
        else:
            self.set_configures_groups()
        self.deal_default_configures()
        logging.info("[core.py] loaded configures:{0}".format(self.loaded_configures))

    def set_configures_groups(self, group_path=APPLICATION_ROOT_DIR + r"\bases\configures\groups\SST"):
        if os.path.exists(group_path):
            for __file__ in os.listdir(group_path):
                if __file__.endswith(".sd"):
                    if os.path.exists(APPLICATION_ROOT_DIR + r"/bases/configures/active" + __file__):
                        os.remove(APPLICATION_ROOT_DIR + r"/bases/configures/active" + __file__)
                    shutil.copy(group_path + r"/" + __file__, APPLICATION_ROOT_DIR + r"/bases/configures/active")
                    self.loaded_configures[__file__.split(".")[0]] = APPLICATION_ROOT_DIR + r"/configures/configs/" + __file__
            logging.info("[core.py] configure groups were set up.")
        else:
            raise FileNotFoundError(f"{group_path} does not exist.")
    def deal_default_configures(self):
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
