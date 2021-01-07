import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import *


class my_serial(QWidget):
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial()

    def serial_confirm(self, port, baud, databit, parity, stopbit):
        self.ser.port = port
        self.ser.baudrate = int(baud)
        self.ser.bytesize = int(databit)
        if parity == '无':
            self.ser.parity = 'N'
        elif parity == '奇校验':
            self.ser.parity = 'O'
        elif parity == '偶校验':
            self.ser.parity = 'E'
        self.ser.stopbits = int(stopbit)

        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, '错误', '该端口不能被打开！')
            return None

        if self.ser.isOpen():
            QMessageBox.information(self, '成功', '端口%s已连接！' % port)
