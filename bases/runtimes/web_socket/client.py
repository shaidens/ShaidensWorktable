import socket as s
import sys
import threading as tg
import time
import os
import logging

import simplejson as json

from typing_extensions import Union
logging.basicConfig(level=logging.INFO, format='[%(asctime)s-%(name)s][web_socket] %(message)s')

WORK_ROOT_DIR = os.path.dirname(__file__)  # 获取工作目录(web_socket)
LIBS_DIR = os.path.dirname(WORK_ROOT_DIR)  # 获取libs目录
APPLICATION_ROOT_DIR = os.path.dirname(LIBS_DIR)  # 获取主程序根目录
CONFIGS_DIR = APPLICATION_ROOT_DIR + r"\configures"  # 获取配置文件目录
logging.info(
    "[client]\nCONFIGS_DIR -> {0}\n      APPLICATION_ROOT_DIR -> {1} \n      LIBS_DIR -> {2}\n       WORK_ROOT_DIR -> {3}".format(
        CONFIGS_DIR, APPLICATION_ROOT_DIR, LIBS_DIR, WORK_ROOT_DIR))
# 一些默认常量
SERVER_TIMEOUT = 5
SERVER_PORT = 14514
SERVER_HOST: str="127.0.0.1"


# 以下进行配置文件读取
def setup():
    global SERVER_HOST, SERVER_PORT, SERVER_TIMEOUT
    try:
        with open(CONFIGS_DIR + r"\\active\\web_socket.sd", "r", encoding="utf-8") as f:
            config = f.read()
            config = config.split("\n")
            for i in config:
                if i.startswith("#"):  # 跳过注释行
                    continue
                if i.startswith("SERVER_HOST"):
                    SERVER_HOST = i.split("=")[1]
                    logging.info("SERVER_HOST:%s", SERVER_HOST)
                if i.startswith("SERVER_PORT"):
                    SERVER_PORT = int(i.split("=")[1])
                    logging.info("SERVER_PORT:%s", SERVER_PORT)
                if i.startswith("SERVER_TIMEOUT"):
                    SERVER_TIMEOUT = i.split("=")[1]
                    logging.info("SERVER_TIMEOUT:%s", SERVER_TIMEOUT)
    except Exception as e:
        logging.error("[client]Config File Error! ->{0}".format(e))


logging.info("[client]Working Root Directory:%s", WORK_ROOT_DIR)
logging.info("[client]Application Root Directory:%s", APPLICATION_ROOT_DIR)


class Client(s.socket):
    postLogin = {
        "purpose": "login",
        "data": {
            "invitation_code": ""
        }
    }
    getdata={
        "purpose":"get",
        "data":""
    }
    def __init__(self):
        super().__init__(s.AF_INET, s.SOCK_STREAM)
        self.settimeout(int(SERVER_TIMEOUT))

        # self.software_lib_data=self.get_software_lib_static_data() #获取初始软件库信息
    def init(self) -> bool:
        setup()
        r=self.go()
        if r is True:
            self.software_lib_data = self.get_software_lib_static_data()
            logging.info("[client] get_softwareLib_data:{0}".format(self.software_lib_data))
        return r

    def go(self) -> Union[bool,str]:
        global SERVER_HOST, SERVER_PORT, SERVER_TIMEOUT
        try:
            # 解决socket.gaierror: [Errno 11001] getaddrinfo failed
            SERVER_HOST=SERVER_HOST.strip()
            logging.info("[client] Connecting to {0}:{1}".format(SERVER_HOST, SERVER_PORT))
            self.connect((SERVER_HOST, SERVER_PORT))
            logging.info("[client] Connected to {0}:{1}".format(SERVER_HOST, SERVER_PORT))
        except (TimeoutError,ConnectionRefusedError) as e:
            logging.error("[client] Connect Timeout! {0}".format(e))
            return "无法连接到服务器！请联系Shaiden或稍后再试 ☹️"
        return True
    def login(self, invitation_code):
        try:
            rei=invitation_code.strip()
            self.postLogin["data"]["invitation_code"] = rei
            self.sendall(json.dumps(self.postLogin).encode())
            data = self.recv(1024).decode()
            data = eval(data)
            if data[0] == "success":
                logging.info("[client] Login Success!:{0}".format(data[1]))
                return data[1]
            elif data[0] == "failed" or not data:
                logging.error("[client] Login Failed!:{0}".format(data))
                return data[1]
        except (TimeoutError, s.timeout) as e:
            logging.error("[client] Login Timeout! {0}".format(e))
            return "无法连接到服务器！请联系Shaiden或稍后再试"
    def get(self,data:str):
        try:
            self.getdata["data"]=data
            self.sendall(json.dumps(self.getdata).encode())
            recv=self.recv(1024).decode()
            # print(recv)

            recv=eval(recv) #简易地将str类型的json load
            if recv is None:
                return "数据获取失败!"
            else:
                return recv
        except (TimeoutError, s.timeout) as e:
            logging.error("[client] client.get Timeout! {0}".format(e))
            return "无法连接到服务器！请联系Shaiden或稍后再试"
    def get_software_lib_static_data(self):
        try:
            return self.get("data_software")
        except (TimeoutError, s.timeout) as e:
            logging.error("[client] Get Timeout! {0}".format())


if __name__ == '__main__':
    a = Client()
    a.go()
    a.login("Shaiden")
