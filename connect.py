from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import serial_my
import serial.tools.list_ports
import Ui_con_dialog
import config
import tcp_my
import socket


class Connect_Dialog(QDialog, Ui_con_dialog.Ui_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.serial_con = serial_my.my_serial()
        # self.tcp_con = tcp_my.tcp_config()
        

        con = config.MyForm()
        self.comboBox_baudrate.setCurrentText(con.baud)
        self.comboBox_databit.setCurrentText(con.databit)

  
        self.IP_reget.clicked.connect(self.get_home_ip)

        self.pushButton_check.clicked.connect(self.check_port)
        self.pushButton_connect.clicked.connect(self.connect_port)
        self.pushButton_disconnect.clicked.connect(self.disconnect_port)

        self.btn_connect_IP.clicked.connect(self.ip_connect)

    def ip_connect(self):
        ip = self.aim_IP.text()
        port = self.aim_port.text()
        tcp_my.tcp_config.tcp_confirm(self,ip,port)

    def get_home_ip(self):
        # self.tcp_con = tcp_my.tcp_config()
        # self.addrs = socket.getaddrinfo(socket.gethostname(),None)
        # self.home_IP.setText(str(self.addrs))
        add_string = tcp_my.tcp_config.tcp_host(self)
        self.home_IP.setText(str(add_string))


    def disconnect_port(self):
        self.serial_con.ser.close()
        QMessageBox.information(self, '提示',
                                '端口%s连接已关闭！' % self.serial_con.ser.port)

    def connect_port(self):
        if self.serial_con.ser.isOpen():
            QMessageBox.information(self, '提示', '已连接,请勿重复提交！')
        else:
            self.serial_con.serial_confirm(
                self.comboBox_port.currentText(),
                self.comboBox_baudrate.currentText(),
                self.comboBox_databit.currentText(),
                self.comboBox_parity.currentText(),
                self.comboBox_stopbit.currentText())

    def check_port(self):
        self.com_dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox_port.clear()
        for port in port_list:
            self.com_dict['%s' % port[0]] = '%s' % port[1]
            self.comboBox_port.addItem(port[0])

        if len(self.com_dict) == 0:
            QMessageBox.information(self, '提示', '无可用串口')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dia = Connect_Dialog()
    dia.show()

    sys.exit(app.exec_())
