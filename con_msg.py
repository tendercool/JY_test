from PyQt5.QtWidgets import QDialog,QHBoxLayout,QTextBrowser,QApplication,QGridLayout,QLabel
import sys
import serial_my
import tcp_my



class msg_config(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('通讯报文')
        self.resize(800,400)
        layout = QGridLayout()
        self.tcp_text = QTextBrowser()
        self.tcp_name = QLabel('TCP报文')
        self.serial_text = QTextBrowser()
        self.serial_name = QLabel('串口报文')
        layout.addWidget(self.tcp_name,0,0)
        layout.addWidget(self.tcp_text,0,1)
        layout.addWidget(self.serial_name,1,0)
        layout.addWidget(self.serial_text,1,1)

        self.setLayout(layout)

        self.serial_this = serial_my.my_serial()
        self.tcp_this = tcp_my.tcp_config()

    def serial_msg(self):
        msg = self.serial_this.serial_get_msg()
        self.serial_text.append(msg)

        textCursor = self.serial_text.textCursor()
        textCursor.movePosition(textCursor.End)
        self.serial_text.setTextCursor(textCursor)
    
    def tcp_msg(self):
        msg = self.tcp_this.tcp_get_msg()
        self.tcp_text.append(msg)

        textCursor = self.tcp_text.textCursor()
        textCursor.movePosition(textCursor.End)
        self.tcp_text.setTextCursor(textCursor)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dia = msg_config()
    dia.show()

    sys.exit(app.exec())
    



