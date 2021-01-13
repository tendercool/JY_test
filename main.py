from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import connect
import Ui_main
import Ui_con_dialog
import con_msg
import serial_my


class main_window(QMainWindow, Ui_main.Ui_MainWindow, Ui_con_dialog.Ui_dialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1250, 600)
        self.setupUi(self)
        self.dia = connect.Connect_Dialog()
        self.msg = con_msg.msg_config()
        with open("style.qss", 'r') as f:
            qApp.setStyleSheet(f.read())

        self.actionstart.triggered.connect(self.dia.show)
        self.actioninfor.triggered.connect(self.msg.show)

        self.btn_2KM_on.clicked.connect(self.btn_2KM_on_cb)
        self.btn_2KM_off.clicked.connect(self.btn_2KM_off_cb)
        self.btn_3KM_on.clicked.connect(self.btn_3KM_on_cb)
        self.btn_3KM_off.clicked.connect(self.btn_3KM_off_cb)
        self.btn_5KM_on.clicked.connect(self.btn_5KM_on_cb)
        self.btn_5KM_off.clicked.connect(self.btn_5KM_off_cb)
        self.btn_6KM_on.clicked.connect(self.btn_6KM_on_cb)
        self.btn_6KM_off.clicked.connect(self.btn_6KM_off_cb)
        self.btn_7KM_on.clicked.connect(self.btn_7KM_on_cb)
        self.btn_7KM_off.clicked.connect(self.btn_7KM_off_cb)
        self.btn_diesel_on.clicked.connect(self.btn_diesel_on_cb)
        self.btn_diesel_off.clicked.connect(self.btn_diesel_off_cb)
        self.btn_8QF_on.clicked.connect(self.btn_8QF_on_cb)
        self.btn_8QF_off.clicked.connect(self.btn_8QF_off_cb)
        self.btn_9QF_on.clicked.connect(self.btn_9QF_on_cb)
        self.btn_9QF_off.clicked.connect(self.btn_9QF_off_cb)
        self.btn_city_on.clicked.connect(self.btn_city_on_cb)
        self.btn_city_off.clicked.connect(self.btn_city_off_cb)

        self.actionclose_PV.triggered.connect(self.frame_PV_hide)
        self.actionshow_PV.triggered.connect(self.frame_PV_show)
        self.actionshow_diesel.triggered.connect(self.frame_diesel_show)
        self.actionclose_diesel.triggered.connect(self.frame_diesel_hide)
        self.actionshow_battery.triggered.connect(self.frame_battery_show)
        self.actionclose_battery.triggered.connect(self.frame_battery_hide)

        self.btn_2KM_on.setEnabled(True)
        self.btn_2KM_off.setEnabled(False)
        self.btn_3KM_on.setEnabled(True)
        self.btn_3KM_off.setEnabled(False)
        self.btn_5KM_on.setEnabled(True)
        self.btn_5KM_off.setEnabled(False)
        self.btn_6KM_on.setEnabled(True)
        self.btn_6KM_off.setEnabled(False)
        self.btn_7KM_on.setEnabled(True)
        self.btn_7KM_off.setEnabled(False)
        self.btn_8QF_on.setEnabled(True)
        self.btn_8QF_off.setEnabled(False)
        self.btn_9QF_on.setEnabled(True)
        self.btn_9QF_off.setEnabled(False)
        self.btn_diesel_on.setEnabled(True)
        self.btn_diesel_off.setEnabled(False)
        self.btn_city_on.setEnabled(True)
        self.btn_city_off.setEnabled(False)

    def frame_PV_hide(self):
        self.frame_main.show()
        self.frame_PV.hide()
        self.frame_diesel.hide()
        self.frame_battery.hide()

    def frame_PV_show(self):
        self.frame_main.hide()
        self.frame_PV.show()
        self.frame_PV.move(0, 0)
        self.frame_diesel.hide()
        self.frame_battery.hide()

    def frame_diesel_show(self):
        self.frame_main.hide()
        self.frame_diesel.show()
        self.frame_diesel.move(0, 0)
        self.frame_PV.hide()
        self.frame_battery.hide()

    def frame_diesel_hide(self):
        self.frame_main.show()
        self.frame_diesel.hide()
        self.frame_PV.hide()
        self.frame_battery.hide()

    def frame_battery_show(self):
        self.frame_main.hide()
        self.frame_battery.show()
        self.frame_battery.move(0, 0)
        self.frame_PV.hide()
        self.frame_diesel.hide()

    def frame_battery_hide(self):
        self.frame_main.show()
        self.frame_diesel.hide()
        self.frame_PV.hide()
        self.frame_battery.hide()

    def check_2KM_value(self):
        if self.btn_2KM_on.isEnabled():
            return 1
        else:
            return 0

    def btn_2KM_on_cb(self):
        reply = QMessageBox.question(self, '提示', '是否打开2KM接口',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_2KM_on.setEnabled(False)
            self.btn_2KM_off.setEnabled(True)
            self.PCS_signal_led.setPixmap(QPixmap('image/green_pic.png'))
        else:
            pass

    def btn_2KM_off_cb(self):
        reply = QMessageBox.question(self, '提示', '是否关闭2KM接口',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_2KM_on.setEnabled(True)
            self.btn_2KM_off.setEnabled(False)
            self.PCS_signal_led.setPixmap(QPixmap('image/red_pic.png'))
        else:
            pass

    def btn_3KM_on_cb(self):
        PCS_2KM_state = self.check_2KM_value()
        if PCS_2KM_state == 1:
            QMessageBox.warning(self, '警告', '请先打开2KM')
        else:
            reply = QMessageBox.question(self, '提示', '是否打开3KM光伏接口',
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.btn_3KM_on.setEnabled(False)
                self.btn_3KM_off.setEnabled(True)
                self.PV_signal_led.setPixmap(QPixmap('image/green_pic.png'))
                self.PV_current_val.setText('15')
                self.PV_P_val.setText('1000')
                self.PV_Q_val.setText('500')
            else:
                pass

    def btn_3KM_off_cb(self):
        reply = QMessageBox.question(self, '提示', '是否关闭3KM光伏接口',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_3KM_on.setEnabled(True)
            self.btn_3KM_off.setEnabled(False)
            self.PV_signal_led.setPixmap(QPixmap('image/red_pic.png'))
            self.PV_current_val.setText('0')
            self.PV_P_val.setText('0')
            self.PV_Q_val.setText('0')
        else:
            pass

    def btn_5KM_on_cb(self):
        reply = QMessageBox.question(self, '提示', '是否打开5KM负荷1接口',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_5KM_on.setEnabled(False)
            self.btn_5KM_off.setEnabled(True)
            self.load1_current_val.setText('15')
            self.load1_P_val.setText('1000')
            self.load1_Q_val.setText('500')
        else:
            pass

    def btn_5KM_off_cb(self):
        reply = QMessageBox.information(self, '提示', '是否关闭5KM负荷1接口',
                                        QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_5KM_on.setEnabled(True)
            self.btn_5KM_off.setEnabled(False)
            self.load1_current_val.setText('0')
            self.load1_P_val.setText('0')
            self.load1_Q_val.setText('0')
        else:
            pass

    def btn_6KM_on_cb(self):
        reply = QMessageBox.information(self, '提示', '是否打开6KM负荷1接口',
                                        QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_6KM_on.setEnabled(False)
            self.btn_6KM_off.setEnabled(True)
            self.load2_current_val.setText('15')
            self.load2_P_val.setText('1000')
            self.load2_Q_val.setText('500')
        else:
            pass

    def btn_6KM_off_cb(self):
        reply = QMessageBox.information(self, '提示', '是否关闭6KM负荷1接口',
                                        QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_6KM_on.setEnabled(True)
            self.btn_6KM_off.setEnabled(False)
            self.load2_current_val.setText('0')
            self.load2_P_val.setText('0')
            self.load2_Q_val.setText('0')
        else:
            pass

    def btn_7KM_on_cb(self):
        reply = QMessageBox.information(self, '提示', '是否打开7KM负荷1接口',
                                        QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_7KM_on.setEnabled(False)
            self.btn_7KM_off.setEnabled(True)
            self.load3_current_val.setText('15')
            self.load3_P_val.setText('1000')
            self.load3_Q_val.setText('500')
        else:
            pass

    def btn_7KM_off_cb(self):
        reply = QMessageBox.information(self, '提示', '是否关闭7KM负荷1接口',
                                        QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_7KM_on.setEnabled(True)
            self.btn_7KM_off.setEnabled(False)
            self.load3_current_val.setText('0')
            self.load3_P_val.setText('0')
            self.load3_Q_val.setText('0')
        else:
            pass

    def btn_diesel_on_cb(self):
        reply = QMessageBox.question(self, '提示', '是否打开柴油发动机',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.btn_diesel_on.setEnabled(False)
            self.btn_diesel_off.setEnabled(True)

        else:
            pass

    def btn_diesel_off_cb(self):
        reply = QMessageBox.question(self, '提示', '是否关闭柴油发动机',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_diesel_on.setEnabled(True)
            self.btn_diesel_off.setEnabled(False)

        else:
            pass

    def btn_8QF_on_cb(self):
        reply = QMessageBox.question(self, '提示', '是否打开8QF接口',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_8QF_on.setEnabled(False)
            self.btn_8QF_off.setEnabled(True)
            self.diesel_signal_led.setPixmap(QPixmap('image/green_pic.png'))
        else:
            pass

    def btn_8QF_off_cb(self):
        reply = QMessageBox.question(self, '提示', '是否关闭8QF接口',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_8QF_on.setEnabled(True)
            self.btn_8QF_off.setEnabled(False)
            self.diesel_signal_led.setPixmap(QPixmap('image/red_pic.png'))
        else:
            pass

    def btn_9QF_on_cb(self):
        reply = QMessageBox.question(self, '提示', '是否打开9QF接口',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_9QF_on.setEnabled(False)
            self.btn_9QF_off.setEnabled(True)
            self.BMS_signal_led.setPixmap(QPixmap('image/green_pic.png'))
        else:
            pass

    def btn_9QF_off_cb(self):
        reply = QMessageBox.question(self, '提示', '是否关闭9QF接口',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_9QF_on.setEnabled(True)
            self.btn_9QF_off.setEnabled(False)
            self.BMS_signal_led.setPixmap(QPixmap('image/red_pic.png'))
        else:
            pass

    def btn_city_on_cb(self):
        reply = QMessageBox.question(self, '提示', '是否打开市电接口',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_city_on.setEnabled(False)
            self.btn_city_off.setEnabled(True)
            self.city_voltage_val.setText('220')
            self.city_current_val.setText('15')
            self.city_P_val.setText('1000')
            self.city_Q_val.setText('500')
        else:
            pass

    def btn_city_off_cb(self):
        reply = QMessageBox.information(self, '提示', '是否关闭市电接口',
                                        QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.btn_city_on.setEnabled(True)
            self.btn_city_off.setEnabled(False)
            self.city_voltage_val.setText('0')
            self.city_current_val.setText('0')
            self.city_P_val.setText('0')
            self.city_Q_val.setText('0')
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = main_window()
    win.show()

    sys.exit(app.exec_())