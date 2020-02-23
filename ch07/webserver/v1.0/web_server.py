import socket
import multiprocessing
import re
import time
from . import mini_framework


class WSGIServer:
    def __init__(self):
        """
        初始化功能，创建套接字/绑定等
        """
        # 创建一个服务器套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 套接字 地址重用选项 1设置0取消
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定
        self.server_socket.bind(('', 9999))
        # 监听，被动套接字，设置已完成三次握手队列长度
        self.server_socket.listen(128)

    def request_handler(self, client_socket):
        """
        处理客户请求
        :param client_socket:
        :return:
        """
        recv_data = client_socket.recv(4096)
        if not recv_data:
            print("连接断开")
            client_socket.close()
            return
        # 对接收的数据进行解码
        request_str_data = recv_data.decode()
        # 通过正则表达式提取数据
        ret = re.match(r"[^/]+([^ ]+)", request_str_data)
        if ret:
            path_info = ret.group(1)  # /index.html
            print(">" * 30, path_info)
        else:
            path_info = "/"
        print("用户请求路径是%s" % path_info)
        if path_info == '/':
            path_info = '/index.html'

        # 用if判断来区分动态请求/静态请求
        if not path_info.endswith(".py"):
            # 静态请求
            pass
        else:
            # 动态请求
            pass

    def set_headers(self, status, headers):
        pass

    def run(self):
        pass
