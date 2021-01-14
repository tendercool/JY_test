import Ui_con_dialog
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import socket

class tcp_config(QWidget):
    def __init__(self):
        super().__init__()
        
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # self.signal_write_msg = QtCore.pyqtSignal(str)

    def tcp_stop(self):
        try:
            self.tcp_socket.close()
        except Exception as ret:
            pass

    def tcp_host(self):
        # addrs = socket.getaddrinfo(socket.gethostname(),None)
        # addr = [item[4][0] for item in addrs if ':' not in item[4][0]][0]
        # return addr
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 80))
            my_addr = s.getsockname()[0]
        except Exception as ret:
            # 若无法连接互联网使用，会调用以下方法
            try:
                my_addr = socket.gethostbyname(socket.gethostname())
                
            except Exception as ret_e:
                QMessageBox.warning(self,'错误',"无法获取ip，请连接网络！")
        finally:
            s.close()
        return my_addr


    def tcp_confirm(self,ip,port):
        
        self.ports = int(port)
        self.host = str(ip)
        try:
            address = (self.host, self.ports)
        except Exception as ret:
            QMessageBox.warning(self,'错误','请输入端口及IP！')
        else:
            try:
                # msg = '正在连接目标服务器\n'
                # self.signal_write_msg.emit(msg)
                self.tcp_socket.connect(address)
                QMessageBox.information(self,'提示','正在连接目标服务器！')
                
            except Exception as ret:
                # msg = '无法连接目标服务器\n'
                # self.signal_write_msg.emit(msg)
                QMessageBox.warning(self,'错误','无法连接目标服务器!')
                
            else:
                # msg = 'TCP客户端已连接IP:%s端口:%s\n' % address
                # self.signal_write_msg.emit(msg)
                QMessageBox.information(self,'提示','TCP客户端已连接IP:%s端口:%s' % address)
    
    def tcp_get_msg(self):
        receive_data = self.tcp_socket.accept(1024)
        receive_data.decode(encoding = 'utf-8')
        return receive_data

    def tcp_send_msg(self,data):
        send_data = data.encode(encoding='utf-8')
        self.tcp_socket.send(send_data)