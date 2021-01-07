import Ui_con_dialog
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import socket

class tcp_config(QWidget):
    def __init__():
        super().__init__()
        self.setupUi(self)
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.signal_write_msg = QtCore.pyqtSignal(str)

    def tcp_host(self):
        addrs = socket.getaddrinfo(socket.gethostname(),None)
        addr = [item[4][0] for item in addrs if ':' not in item[4][0]][0]
        return addr


    def tcp_confirm(self,ip,port):
        
        self.ports = int(port)
        self.host = ip
        try:
            address = (str(self.host), int(self.ports))
        except Exception as ret:
            msg = '请检查目标IP，目标端口\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                msg = '正在连接目标服务器\n'
                self.signal_write_msg.emit(msg)
                self.tcp_socket.connect(address)
            except Exception as ret:
                msg = '无法连接目标服务器\n'
                self.signal_write_msg.emit(msg)
            else:
                msg = 'TCP客户端已连接IP:%s端口:%s\n' % address
                self.signal_write_msg.emit(msg)