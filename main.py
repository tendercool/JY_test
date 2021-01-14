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
        with open("style.qss", 'r') as f:
            qApp.setStyleSheet(f.read())

        self.PV_VAL = [
            'PV_VAL_1', 'PV_VAL_2', 'PV_VAL_3', 'PV_VAL_4', 'PV_VAL_5',
            'PV_VAL_6', 'PV_VAL_7', 'PV_VAL_8', 'PV_VAL_9'
        ]
        self.DIESEL_VAL = [
            'DIESEL_VAL_1',
            'DIESEL_VAL_2',
            'DIESEL_VAL_3',
            'DIESEL_VAL_4',
            'DIESEL_VAL_5',
            'DIESEL_VAL_6',
            'DIESEL_VAL_7',
            'DIESEL_VAL_8',
            'DIESEL_VAL_9',
            'DIESEL_VAL_10',
            'DIESEL_VAL_11',
            'DIESEL_VAL_12',
            'DIESEL_VAL_13',
            'DIESEL_VAL_14',
            'DIESEL_VAL_15',
            'DIESEL_VAL_16',
            'DIESEL_VAL_17',
            'DIESEL_VAL_18',
            'DIESEL_VAL_19',
            'DIESEL_VAL_20',
            'DIESEL_VAL_21',
            'DIESEL_VAL_22',
        ]
        self.BMS_VAL = [
            'BMS_VAL_1',
            'BMS_VAL_2',
            'BMS_VAL_3',
            'BMS_VAL_4',
            'BMS_VAL_5',
            'BMS_VAL_6',
            'BMS_VAL_7',
            'BMS_VAL_8',
            'BMS_VAL_9',
            'BMS_VAL_10',
            'BMS_VAL_11',
            'BMS_VAL_12',
            'BMS_VAL_13',
            'BMS_VAL_14',
            'BMS_VAL_15',
            'BMS_VAL_16',
            'BMS_VAL_17',
            'BMS_VAL_18',
            'BMS_VAL_19',
            'BMS_VAL_20',
            'BMS_VAL_21',
            'BMS_VAL_22',
            'BMS_VAL_23',
            'BMS_VAL_24',
            'BMS_VAL_25',
            'BMS_VAL_26',
            'BMS_VAL_27',
            'BMS_VAL_28',
        ]

        self.dia = connect.Connect_Dialog()
        self.msg = con_msg.msg_config()
        # self.timer = QTimer()
        # self.timer.start(1000)
        # self.timer.timeout.connect(self.set_btn)
        

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

    # def set_btn(self):
    #     if self.dia.serial_con.ser.isOpen():
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
        # else:
        #     self.btn_2KM_on.setEnabled(False)
        #     self.btn_2KM_off.setEnabled(False)
        #     self.btn_3KM_on.setEnabled(False)
        #     self.btn_3KM_off.setEnabled(False)
        #     self.btn_5KM_on.setEnabled(False)
        #     self.btn_5KM_off.setEnabled(False)
        #     self.btn_6KM_on.setEnabled(False)
        #     self.btn_6KM_off.setEnabled(False)
        #     self.btn_7KM_on.setEnabled(False)
        #     self.btn_7KM_off.setEnabled(False)
        #     self.btn_8QF_on.setEnabled(False)
        #     self.btn_8QF_off.setEnabled(False)
        #     self.btn_9QF_on.setEnabled(False)
        #     self.btn_9QF_off.setEnabled(False)
        #     self.btn_diesel_on.setEnabled(False)
        #     self.btn_diesel_off.setEnabled(False)
        #     self.btn_city_on.setEnabled(False)
        #     self.btn_city_off.setEnabled(False)

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

                self.PV_VAL_UPDATE()
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
  #-------------------------------简单队列测试----------------------
  #----暂无问题，根据接收报文生成队列，切片，与参数值队列组成字典，顺序赋值。后续考虑以exec函数处理，eval计算字符串
    def PV_VAL_UPDATE(self):
        if self.dia.serial_con.ser.isOpen():
            rec_msg = ['11','EF','CC','AF','AD','12','24','25','99']
            if rec_msg != '':
                PV_dict = dict(zip(self.PV_VAL,rec_msg))
                
                for key in PV_dict:
                    print(PV_dict[key])
                    exec('self.%s.setText("%s")' % (key, PV_dict[key]))
    #             # self.PV_VAL_1.setText(PV_dict['PV_VAL_1'])
                # self.PV_VAL_2.setText(PV_dict['PV_VAL_2'])
                # self.PV_VAL_3.setText(PV_dict['PV_VAL_3'])
                # self.PV_VAL_4.setText(PV_dict['PV_VAL_4'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = main_window()
    win.show()

    sys.exit(app.exec_())