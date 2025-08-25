import os
import socket as s
import threading as t
import sys
import logging

from typing_extensions import Union
import simplejson as json

from bases import *

logging.basicConfig(level=logging.INFO, format='[%(asctime)s-%(name)s][web_socket] %(message)s')
DEFAULT_INVITATION = {
    "Shaiden": {"power": ShaidenPower_UserPower().__str__()}
}

DEFAULT_SOFTWARES={
    "微信Wechat":{
        "description":"市面上主流的社交软件。不只是社交平台，更是一种生活方式",
        "link":"https://dldir1v6.qq.com/weixin/Windows/WeChatSetup.exe",
        # "icon": "https://www.baidu.com/img/bd_logo1.png",
    }
}
#软件单元的数据格式应为： {"AppName":{"description":"...","link":["www.abc.net/abx.txt",...],"icon":,"一个网址或一个服务端文件地址"}}


class ServerAPI():
    def __init__(self):
        # self.invitations: dict
        self.invitations:dict=self._jsonFileSetup(r".\profile\invitations.json", DEFAULT_INVITATION)
        self.data_software:dict=self._jsonFileSetup(r".\data\SoftwareLibData.json", DEFAULT_SOFTWARES)
        logging.info("ServerAPI.jsonFileSetup{0}".format(self.data_software))

        self.allowAccessVars={
            "data_software":self.data_software,
        }
    def _jsonFileSetup(self,filename_path:str,default_value=None,logging=True) -> Union[dict,None]:

        if not os.path.exists(filename_path):
            with open(filename_path, "w") as f:
                f.write(json.dumps({}))
            logging.info(f"{filename_path} has been created with {default_value}.") if logging else None
            return default_value
        else:
            with open(filename_path, "r") as f:
               return json.loads(f.read())

    def login(self, invitation: str) -> Union[dict,str]:
        logging.info("ServerAPI.login with {0}".format(invitation))
        try:
            if invitation in self.invitations.keys():
                power = get_user_power(self.invitations[invitation]["power"])
                logging.info("ServerAPI.login UserPower:{0}".format(str(self.invitations[invitation])))
                if power.powers["LOGIN"]:
                    logging.info("ServerAPI.login success to login:{0}".format(str(self.invitations[invitation])))
                    return self.invitations[invitation]  # 返回该用户的配置文件
            else:
                logging.info("ServerAPI.login failed to login:{0}".format("no such invitation."))
                return {"failed": "no such invitation."}
        except Exception as e:
            logging.error("ServerAPI.login failed to login:{0}".format(e))
            return {"failed": str(e)}


    def get_data(self,key:str):
        if key not in self.allowAccessVars.keys():#若无指定值
            return None #交给客户端处理
        return self.allowAccessVars[key]

class Server(s.socket):
    def __init__(self):
        super().__init__(s.AF_INET, s.SOCK_STREAM)
        self.bind(("", 14514))
        self.listen(5)
        self.ifStop = False  # True时可以运行
        self.api = ServerAPI()
        self.lock = t.Lock()
        self.connections = {}
        self.threading_pool = {}

    def go(self):
        while not self.ifStop:
            conn, addr = self.accept()
            logging.info("{0} has connected to the server".format(addr))
            td = t.Thread(target=self.NewConnection, args=(conn,),daemon=True)
            self.threading_pool[conn.getpeername()[0]]=td
            td.start()
            logging.info("Threading pool:{0}".format(self.threading_pool))
            logging.info("Connections pool:{0}".format(self.connections))
        else:
            for __t__ in self.threading_pool:
                __t__.join()

    def NewConnection(self, connection: s.socket):
        while not self.ifStop:
            try:
                self.connections[connection.getpeername()[0]]=connection

                recv = connection.recv(1024).decode()
                if not recv:
                    continue
                logging.info("Connection:{0} -> received:{1}".format(connection.getpeername(), recv))

                data = json.loads(recv)
                with self.lock:
                    if data["purpose"] == "login":
                        logging.info("Connection:{0} -> login (1)".format(connection.getpeername(), recv))
                        self._acceptLogin(connection, str(data["data"]["invitation_code"]))
                    elif data["purpose"].lower() == "get":
                        logging.info("Connection:{0} -> GET {1}".format(connection.getpeername(), recv))
                        ret=json.dumps(self.api.get_data(data["data"]))
                        logging.info("Connection:{0} -> return msg :{1}".format(connection.getpeername(), ret))
                        connection.sendall(ret.encode(encoding="utf-8"))
                    else:
                        logging.error("Connection:{0} -> no such command:{1}".format(connection.getpeername(), recv))
                        connection.sendall(json.dumps(
                            ["error", ["failed","no such command."]]
                        ).encode())
            except json.JSONDecodeError as e:
                logging.error("Connection:{0} -> json decode error:{1}".format(connection.getpeername(), e))
                connection.sendall(json.dumps(
                    ["error", ["failed","json decode error."]]
                ).encode())
        else:
            connection.sendall(json.dumps(
                ["disconnect", ["disconnect", "server is closed."]]
            ).encode())
            connection.close()
            del self.connections[connection.getpeername()[0]]
            self.threading_pool[connection.getpeername()[0]].join()
            del self.threading_pool[connection.getpeername()[0]]
    def _acceptLogin(self, connection: s.socket, value: str):
        result = self.api.login(value)
        if result and "failed" not in result.keys():
            logging.info("Connection:{0} -> login result:{1}".format(connection.getpeername(), result))
            connection.sendall(json.dumps(
                ["success", result]  # 此处对应客户端接受登陆结果的解析代码
            ).encode())
            return True
        else:
            logging.error(
                "Connection:{0} -> Failed to login. login result:{1}".format(connection.getpeername(), result))
            connection.sendall(json.dumps(
                ["error", result]
            ).encode())
            return False


if __name__ == '__main__':
    # a=ServerAPI()
    # a.login("Shaiden")
    b = Server()
    b.go()
