# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\PyQt\JY_test\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1311, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout1 = QtWidgets.QGridLayout()
        self.gridLayout1.setObjectName("gridLayout1")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout1.addWidget(self.label_20, 5, 19, 1, 2)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout1.addWidget(self.label_26, 11, 0, 1, 1)
        self.load1_P_val = QtWidgets.QLineEdit(self.centralwidget)
        self.load1_P_val.setObjectName("load1_P_val")
        self.gridLayout1.addWidget(self.load1_P_val, 8, 13, 1, 1)
        self.btn_5KM_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5KM_off.setObjectName("btn_5KM_off")
        self.gridLayout1.addWidget(self.btn_5KM_off, 7, 13, 1, 1)
        self.city_Q_val = QtWidgets.QLineEdit(self.centralwidget)
        self.city_Q_val.setObjectName("city_Q_val")
        self.gridLayout1.addWidget(self.city_Q_val, 1, 7, 1, 1)
        self.btn_6KM_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6KM_on.setObjectName("btn_6KM_on")
        self.gridLayout1.addWidget(self.btn_6KM_on, 7, 15, 1, 1)
        self.BMS_signal_led = QtWidgets.QLabel(self.centralwidget)
        self.BMS_signal_led.setText("")
        self.BMS_signal_led.setPixmap(QtGui.QPixmap("g:\\PyQt\\JY_test\\image/red_pic.png"))
        self.BMS_signal_led.setObjectName("BMS_signal_led")
        self.gridLayout1.addWidget(self.BMS_signal_led, 11, 13, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout1.addWidget(self.label_22, 6, 19, 1, 1)
        self.city_P_val = QtWidgets.QLineEdit(self.centralwidget)
        self.city_P_val.setObjectName("city_P_val")
        self.gridLayout1.addWidget(self.city_P_val, 0, 7, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout1.addWidget(self.line_2, 10, 0, 1, 21)
        self.btn_7KM_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7KM_off.setObjectName("btn_7KM_off")
        self.gridLayout1.addWidget(self.btn_7KM_off, 7, 20, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout1.addWidget(self.label_25, 9, 15, 1, 1)
        self.load2_P_val = QtWidgets.QLineEdit(self.centralwidget)
        self.load2_P_val.setObjectName("load2_P_val")
        self.gridLayout1.addWidget(self.load2_P_val, 8, 17, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout1.addWidget(self.label_4, 3, 5, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout1.addWidget(self.line_3, 4, 0, 1, 21)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout1.addWidget(self.label_9, 0, 13, 1, 1)
        self.btn_diesel_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_diesel_off.setObjectName("btn_diesel_off")
        self.gridLayout1.addWidget(self.btn_diesel_off, 13, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout1.addWidget(self.label_21, 6, 15, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout1.addWidget(self.label_10, 1, 13, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout1.addWidget(self.label_28, 11, 7, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout1.addWidget(self.label_24, 8, 19, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout1.addWidget(self.label_16, 5, 11, 1, 3)
        self.PCS_signal_led = QtWidgets.QLabel(self.centralwidget)
        self.PCS_signal_led.setText("")
        self.PCS_signal_led.setPixmap(QtGui.QPixmap("g:\\PyQt\\JY_test\\image/red_pic.png"))
        self.PCS_signal_led.setObjectName("PCS_signal_led")
        self.gridLayout1.addWidget(self.PCS_signal_led, 11, 5, 1, 1)
        self.btn_diesel_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_diesel_close.setObjectName("btn_diesel_close")
        self.gridLayout1.addWidget(self.btn_diesel_close, 13, 7, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout1.addWidget(self.label_15, 9, 19, 1, 1)
        self.btn_3KM_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3KM_off.setObjectName("btn_3KM_off")
        self.gridLayout1.addWidget(self.btn_3KM_off, 7, 9, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout1.addWidget(self.line_9, 12, 0, 1, 21)
        self.load1_Q_val = QtWidgets.QLineEdit(self.centralwidget)
        self.load1_Q_val.setObjectName("load1_Q_val")
        self.gridLayout1.addWidget(self.load1_Q_val, 9, 13, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout1.addWidget(self.label_12, 5, 0, 2, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout1.addWidget(self.label_7, 0, 5, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout1.addWidget(self.line, 2, 0, 1, 21)
        self.btn_2KM_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2KM_on.setObjectName("btn_2KM_on")
        self.gridLayout1.addWidget(self.btn_2KM_on, 3, 7, 1, 1)
        self.btn_9QF_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9QF_on.setObjectName("btn_9QF_on")
        self.gridLayout1.addWidget(self.btn_9QF_on, 7, 3, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout1.addWidget(self.line_10, 11, 4, 1, 1)
        self.btn_7KM_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7KM_on.setObjectName("btn_7KM_on")
        self.gridLayout1.addWidget(self.btn_7KM_on, 7, 19, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout1.addWidget(self.line_4, 5, 2, 5, 1)
        self.btn_2KM_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2KM_off.setObjectName("btn_2KM_off")
        self.gridLayout1.addWidget(self.btn_2KM_off, 3, 9, 1, 1)
        self.load1_current_val = QtWidgets.QLineEdit(self.centralwidget)
        self.load1_current_val.setObjectName("load1_current_val")
        self.gridLayout1.addWidget(self.load1_current_val, 6, 13, 1, 1)
        self.controller_signal_led = QtWidgets.QLabel(self.centralwidget)
        self.controller_signal_led.setText("")
        self.controller_signal_led.setPixmap(QtGui.QPixmap("g:\\PyQt\\JY_test\\image/red_pic.png"))
        self.controller_signal_led.setObjectName("controller_signal_led")
        self.gridLayout1.addWidget(self.controller_signal_led, 11, 17, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout1.addWidget(self.line_12, 11, 12, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout1.addWidget(self.label_14, 8, 7, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout1.addWidget(self.label, 8, 11, 1, 1)
        self.load3_P_val = QtWidgets.QLineEdit(self.centralwidget)
        self.load3_P_val.setObjectName("load3_P_val")
        self.gridLayout1.addWidget(self.load3_P_val, 8, 20, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout1.addWidget(self.label_6, 0, 0, 2, 2)
        self.load2_Q_val = QtWidgets.QLineEdit(self.centralwidget)
        self.load2_Q_val.setObjectName("load2_Q_val")
        self.gridLayout1.addWidget(self.load2_Q_val, 9, 17, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout1.addWidget(self.line_11, 11, 8, 1, 1)
        self.load3_Q_val = QtWidgets.QLineEdit(self.centralwidget)
        self.load3_Q_val.setObjectName("load3_Q_val")
        self.gridLayout1.addWidget(self.load3_Q_val, 9, 20, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout1.addWidget(self.line_6, 5, 10, 5, 1)
        self.btn_8QF_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8QF_off.setObjectName("btn_8QF_off")
        self.gridLayout1.addWidget(self.btn_8QF_off, 7, 1, 1, 1)
        self.btn_diesel_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_diesel_open.setObjectName("btn_diesel_open")
        self.gridLayout1.addWidget(self.btn_diesel_open, 13, 9, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout1.addWidget(self.label_5, 6, 7, 1, 1)
        self.PV_Q_val = QtWidgets.QLineEdit(self.centralwidget)
        self.PV_Q_val.setObjectName("PV_Q_val")
        self.gridLayout1.addWidget(self.PV_Q_val, 9, 9, 1, 1)
        self.PV_P_val = QtWidgets.QLineEdit(self.centralwidget)
        self.PV_P_val.setObjectName("PV_P_val")
        self.gridLayout1.addWidget(self.PV_P_val, 8, 9, 1, 1)
        self.btn_city_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_city_off.setObjectName("btn_city_off")
        self.gridLayout1.addWidget(self.btn_city_off, 1, 3, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout1.addWidget(self.label_27, 11, 3, 1, 1)
        self.btn_8QF_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8QF_on.setObjectName("btn_8QF_on")
        self.gridLayout1.addWidget(self.btn_8QF_on, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout1.addWidget(self.label_3, 9, 7, 1, 1)
        self.btn_city_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_city_on.setObjectName("btn_city_on")
        self.gridLayout1.addWidget(self.btn_city_on, 0, 3, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout1.addWidget(self.line_8, 5, 18, 5, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout1.addWidget(self.label_2, 9, 11, 1, 1)
        self.load2_current_val = QtWidgets.QLineEdit(self.centralwidget)
        self.load2_current_val.setObjectName("load2_current_val")
        self.gridLayout1.addWidget(self.load2_current_val, 6, 17, 1, 1)
        self.city_voltage_val = QtWidgets.QLineEdit(self.centralwidget)
        self.city_voltage_val.setObjectName("city_voltage_val")
        self.gridLayout1.addWidget(self.city_voltage_val, 0, 15, 1, 1)
        self.btn_5KM_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5KM_on.setObjectName("btn_5KM_on")
        self.gridLayout1.addWidget(self.btn_5KM_on, 7, 11, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout1.addWidget(self.label_11, 5, 7, 1, 3)
        self.PV_signal_led = QtWidgets.QLabel(self.centralwidget)
        self.PV_signal_led.setText("")
        self.PV_signal_led.setPixmap(QtGui.QPixmap("g:\\PyQt\\JY_test\\image/red_pic.png"))
        self.PV_signal_led.setObjectName("PV_signal_led")
        self.gridLayout1.addWidget(self.PV_signal_led, 11, 1, 1, 1)
        self.btn_6KM_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6KM_off.setObjectName("btn_6KM_off")
        self.gridLayout1.addWidget(self.btn_6KM_off, 7, 17, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout1.addWidget(self.label_18, 6, 11, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setObjectName("label_31")
        self.gridLayout1.addWidget(self.label_31, 11, 19, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setObjectName("label_30")
        self.gridLayout1.addWidget(self.label_30, 11, 15, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout1.addWidget(self.label_19, 5, 15, 1, 3)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout1.addWidget(self.label_23, 8, 15, 1, 1)
        self.diesel_signal_led = QtWidgets.QLabel(self.centralwidget)
        self.diesel_signal_led.setText("")
        self.diesel_signal_led.setPixmap(QtGui.QPixmap("g:\\PyQt\\JY_test\\image/red_pic.png"))
        self.diesel_signal_led.setObjectName("diesel_signal_led")
        self.gridLayout1.addWidget(self.diesel_signal_led, 11, 9, 1, 1)
        self.PV_current_val = QtWidgets.QLineEdit(self.centralwidget)
        self.PV_current_val.setObjectName("PV_current_val")
        self.gridLayout1.addWidget(self.PV_current_val, 6, 9, 1, 1)
        self.city_current_val = QtWidgets.QLineEdit(self.centralwidget)
        self.city_current_val.setObjectName("city_current_val")
        self.gridLayout1.addWidget(self.city_current_val, 1, 15, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout1.addWidget(self.label_8, 1, 5, 1, 1)
        self.btn_9QF_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9QF_off.setObjectName("btn_9QF_off")
        self.gridLayout1.addWidget(self.btn_9QF_off, 7, 5, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout1.addWidget(self.line_7, 5, 14, 5, 1)
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setObjectName("label_29")
        self.gridLayout1.addWidget(self.label_29, 11, 11, 1, 1)
        self.btn_diesel_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_diesel_on.setObjectName("btn_diesel_on")
        self.gridLayout1.addWidget(self.btn_diesel_on, 13, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout1.addWidget(self.label_13, 5, 3, 2, 3)
        self.btn_3KM_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3KM_on.setObjectName("btn_3KM_on")
        self.gridLayout1.addWidget(self.btn_3KM_on, 7, 7, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout1.addWidget(self.label_17, 13, 0, 1, 1)
        self.btn_diesel_manual = QtWidgets.QPushButton(self.centralwidget)
        self.btn_diesel_manual.setObjectName("btn_diesel_manual")
        self.gridLayout1.addWidget(self.btn_diesel_manual, 13, 5, 1, 1)
        self.load3_current_val = QtWidgets.QLineEdit(self.centralwidget)
        self.load3_current_val.setObjectName("load3_current_val")
        self.gridLayout1.addWidget(self.load3_current_val, 6, 20, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout1.addWidget(self.line_5, 5, 6, 5, 1)
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout1.addWidget(self.line_13, 11, 16, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout1, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1311, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_PV = QtWidgets.QMenu(self.menubar)
        self.menu_PV.setObjectName("menu_PV")
        self.menu_diesel = QtWidgets.QMenu(self.menubar)
        self.menu_diesel.setObjectName("menu_diesel")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionstart = QtWidgets.QAction(MainWindow)
        self.actionstart.setObjectName("actionstart")
        self.actioninfor = QtWidgets.QAction(MainWindow)
        self.actioninfor.setObjectName("actioninfor")
        self.actionshow_main = QtWidgets.QAction(MainWindow)
        self.actionshow_main.setObjectName("actionshow_main")
        self.actionclose_main = QtWidgets.QAction(MainWindow)
        self.actionclose_main.setObjectName("actionclose_main")
        self.actionshow_PV = QtWidgets.QAction(MainWindow)
        self.actionshow_PV.setObjectName("actionshow_PV")
        self.actionclose_PV = QtWidgets.QAction(MainWindow)
        self.actionclose_PV.setObjectName("actionclose_PV")
        self.actionshow_diesel = QtWidgets.QAction(MainWindow)
        self.actionshow_diesel.setObjectName("actionshow_diesel")
        self.actionclose_diesel = QtWidgets.QAction(MainWindow)
        self.actionclose_diesel.setObjectName("actionclose_diesel")
        self.actionshow_battery = QtWidgets.QAction(MainWindow)
        self.actionshow_battery.setObjectName("actionshow_battery")
        self.actionclose_battery = QtWidgets.QAction(MainWindow)
        self.actionclose_battery.setObjectName("actionclose_battery")
        self.menu.addAction(self.actionstart)
        self.menu.addAction(self.actioninfor)
        self.menu_PV.addAction(self.actionshow_PV)
        self.menu_PV.addAction(self.actionclose_PV)
        self.menu_diesel.addAction(self.actionshow_diesel)
        self.menu_diesel.addAction(self.actionclose_diesel)
        self.menu_4.addAction(self.actionshow_battery)
        self.menu_4.addAction(self.actionclose_battery)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_PV.menuAction())
        self.menubar.addAction(self.menu_diesel.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "  7KM负荷3接口"))
        self.label_26.setText(_translate("MainWindow", "通信状态"))
        self.btn_5KM_off.setText(_translate("MainWindow", "关"))
        self.btn_6KM_on.setText(_translate("MainWindow", "开"))
        self.label_22.setText(_translate("MainWindow", "负荷3电流"))
        self.btn_7KM_off.setText(_translate("MainWindow", "关"))
        self.label_25.setText(_translate("MainWindow", "负荷2Q"))
        self.label_4.setText(_translate("MainWindow", "  2KM"))
        self.label_9.setText(_translate("MainWindow", "电网电压"))
        self.btn_diesel_off.setText(_translate("MainWindow", "停机"))
        self.label_21.setText(_translate("MainWindow", "负荷2电流"))
        self.label_10.setText(_translate("MainWindow", "电网电流"))
        self.label_28.setText(_translate("MainWindow", "PCS"))
        self.label_24.setText(_translate("MainWindow", "负荷3P"))
        self.label_16.setText(_translate("MainWindow", "   5KM负荷1接口"))
        self.btn_diesel_close.setText(_translate("MainWindow", "柴充合闸"))
        self.label_15.setText(_translate("MainWindow", "负荷3Q"))
        self.btn_3KM_off.setText(_translate("MainWindow", "关"))
        self.label_12.setText(_translate("MainWindow", "   8QF柴发接口"))
        self.label_7.setText(_translate("MainWindow", "电网P"))
        self.btn_2KM_on.setText(_translate("MainWindow", "开"))
        self.btn_9QF_on.setText(_translate("MainWindow", "开"))
        self.btn_7KM_on.setText(_translate("MainWindow", "开"))
        self.btn_2KM_off.setText(_translate("MainWindow", "关"))
        self.label_14.setText(_translate("MainWindow", "光伏P"))
        self.label.setText(_translate("MainWindow", "负荷1P"))
        self.label_6.setText(_translate("MainWindow", "  市电接口"))
        self.btn_8QF_off.setText(_translate("MainWindow", "关"))
        self.btn_diesel_open.setText(_translate("MainWindow", "柴充分闸"))
        self.label_5.setText(_translate("MainWindow", "光伏电流"))
        self.btn_city_off.setText(_translate("MainWindow", "关"))
        self.label_27.setText(_translate("MainWindow", "光伏"))
        self.btn_8QF_on.setText(_translate("MainWindow", "开"))
        self.label_3.setText(_translate("MainWindow", "光伏Q"))
        self.btn_city_on.setText(_translate("MainWindow", "开"))
        self.label_2.setText(_translate("MainWindow", "负荷1Q"))
        self.btn_5KM_on.setText(_translate("MainWindow", "开"))
        self.label_11.setText(_translate("MainWindow", "   3KM光伏接口"))
        self.btn_6KM_off.setText(_translate("MainWindow", "关"))
        self.label_18.setText(_translate("MainWindow", "负荷1电流"))
        self.label_31.setText(_translate("MainWindow", "测控"))
        self.label_30.setText(_translate("MainWindow", "BMS"))
        self.label_19.setText(_translate("MainWindow", "  6KM负荷2接口"))
        self.label_23.setText(_translate("MainWindow", "负荷2P"))
        self.label_8.setText(_translate("MainWindow", "电网Q"))
        self.btn_9QF_off.setText(_translate("MainWindow", "关"))
        self.label_29.setText(_translate("MainWindow", "柴发"))
        self.btn_diesel_on.setText(_translate("MainWindow", "启动"))
        self.label_13.setText(_translate("MainWindow", "   9QF电池接口"))
        self.btn_3KM_on.setText(_translate("MainWindow", "开"))
        self.label_17.setText(_translate("MainWindow", "柴发控制"))
        self.btn_diesel_manual.setText(_translate("MainWindow", "手动"))
        self.menu.setTitle(_translate("MainWindow", "连接设置"))
        self.menu_PV.setTitle(_translate("MainWindow", "光伏参数"))
        self.menu_diesel.setTitle(_translate("MainWindow", "柴发参数"))
        self.menu_4.setTitle(_translate("MainWindow", "电池参数"))
        self.actionstart.setText(_translate("MainWindow", "连接配置"))
        self.actioninfor.setText(_translate("MainWindow", "详细报文"))
        self.actionshow_main.setText(_translate("MainWindow", "显示"))
        self.actionclose_main.setText(_translate("MainWindow", "关闭"))
        self.actionshow_PV.setText(_translate("MainWindow", "显示"))
        self.actionclose_PV.setText(_translate("MainWindow", "关闭"))
        self.actionshow_diesel.setText(_translate("MainWindow", "显示"))
        self.actionclose_diesel.setText(_translate("MainWindow", "关闭"))
        self.actionshow_battery.setText(_translate("MainWindow", "显示"))
        self.actionclose_battery.setText(_translate("MainWindow", "关闭"))
