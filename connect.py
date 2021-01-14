from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
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
        self.tcp_con = tcp_my.tcp_config()
        self.con_state = 0
        self.tcp_state = 0
        con = config.MyForm()
        self.comboBox_baudrate.setCurrentText(con.baud)
        self.comboBox_databit.setCurrentText(con.databit)

  
        self.IP_reget.clicked.connect(self.get_home_ip)

        self.pushButton_check.clicked.connect(self.check_port)
        self.pushButton_connect.clicked.connect(self.connect_port)
        self.pushButton_disconnect.clicked.connect(self.disconnect_port)

        self.btn_connect_IP.clicked.connect(self.ip_connect)
        self.btn_disconnect_IP.clicked.connect(self.ip_close)

    def ip_close(self):
        self.tcp_con.tcp_stop()
        self.tcp_state = 0
        QMessageBox.information(self,'提示','已断开网络！')

    def ip_connect(self):
        if self.aim_port.text() != '' or self.aim_IP.text() != '':
            ip = self.aim_IP.text()
            port = self.aim_port.text()
            self.tcp_con.tcp_confirm(ip,port)
            self.tcp_state = 1
        else:
            QMessageBox.warning(self,'错误','IP及端口不能为空！')
            self.tcp_state = 0


    def get_home_ip(self):
        self.home_IP.clear()
        self.home_IP.setText(str(self.tcp_con.tcp_host()))
    


    def disconnect_port(self):
        self.serial_con.ser.close()
        QMessageBox.information(self, '提示',
                                '端口%s连接已关闭！' % self.serial_con.ser.port)
        self.con_state = 0

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
            self.con_state = 1
        

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
