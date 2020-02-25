import socket
import multiprocessing
import re
from ch07.dynamic import mini_framework


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
            try:
                if path_info.__contains__("html"):
                    with open('./templates/' + path_info, "rb") as f:
                        file_data = f.read()
                else:
                    with open('./' + path_info, "rb") as f:
                        file_data = f.read()
            except:
                response_line = "HTTP/1.1 404 Not Found\r\n"
                response_header = "Server: PythonWebServer2.0\r\n"
                response_body = "ERROR!!!!!"
                response_data = response_line + response_header + "\r\n" + response_body
                client_socket.send(response_data.encode())
            else:
                response_header = "HTTP/1.1 200 OK\r\n"
                response_header += "Server: PythonWebServer1.0\r\n"
                response_header += "\r\n"
                response_body = file_data

                # 拼接报文
                response = response_header.encode("utf-8") + response_body
                # 发送
                client_socket.send(response)
            finally:
                client_socket.close()
        else:
            # 动态请求
            env = dict()
            env["PATH_INFO"] = path_info
            response_body = mini_framework.application(env, self.set_headers)
            # 拼接response
            response = self.response_header + response_body
            client_socket.send(response.encode("utf-8"))

    def set_headers(self, status, headers):
        print("-----web_server.py set_headers 被调用-----")
        response_header = "HTTP/1.1 %s\r\n" % status

        for temp in headers:
            response_header += "%s: %s\r\n" % (temp[0], temp[1])
        response_header += "\r\n"
        self.response_header = response_header

    def run(self):
        """
        等待客户连接，然后创建子进程为客户服务
        :return:
        """
        while True:
            # 从队列中取出一个客户套接字用以服务
            client_socker, client_addr = self.server_socket.accept()
            p = multiprocessing.Process(target=self.request_handler, args=(client_socker,))
            p.start()
            client_socker.close()


def main():
    # 创建一个server服务对象
    wsgi_server = WSGIServer()
    wsgi_server.run()


if __name__ == '__main__':
    main()
