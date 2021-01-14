import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


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

    def serial_get_msg(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.ser.close()
            return None
        if num > 0:
            data = self.ser.read(num)
            num = len(data)
            # if self.radioButton_2.checkState():
            out_s = ''
            for i in range(0,num):
                out_s = out_s + '{:02X}'.format(data[i])
            return out_s
        else:
            pass
    
    def serial_send(self,input_s):
        if self.ser.isOpen():
            if input_s != '':
                input_s = input_s.strip()
                send_list = []
                while input_s != '':
                    num = int(input_s[0:2],16)
                    input_s = input_s[2:].strip()
                    send_list.append(num)
                input_s = bytes(send_list)
            else:
                input_s = (input_s +'\r\n').encode('utf-8')

            self.ser.write(input_s)
        else:
            pass 