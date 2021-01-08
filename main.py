from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import connect
import Ui_main
import Ui_con_dialog
import con_msg

class main_window(QMainWindow,Ui_main.Ui_MainWindow,Ui_con_dialog.Ui_dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.dia = connect.Connect_Dialog()
        self.msg = con_msg.msg_config()

        self.actionstart.triggered.connect(self.dia.show)
        self.actioninfor.triggered.connect(self.msg.show)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = main_window()
    win.show()

    sys.exit(app.exec_())