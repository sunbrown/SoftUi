# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 903)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-radius:10px;\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.QWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.QWidget1.setStyleSheet("")
        self.QWidget1.setObjectName("QWidget1")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.QWidget1)
        self.verticalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_title_4 = QtWidgets.QLabel(self.QWidget1)
        self.label_title_4.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title_4.setFont(font)
        self.label_title_4.setStyleSheet("")
        self.label_title_4.setObjectName("label_title_4")
        self.verticalLayout_12.addWidget(self.label_title_4, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.QWidget1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_23.addWidget(self.label_10)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem2)
        self.QWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.QWidget2.setStyleSheet("color: rgb(0, 0, 127);\n"
"background-color: rgb(203, 203, 203);\n"
"border-radius:20px;")
        self.QWidget2.setObjectName("QWidget2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.QWidget2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_imNum_10 = QtWidgets.QLabel(self.QWidget2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_imNum_10.setFont(font)
        self.label_imNum_10.setStyleSheet("font: 24pt \"楷体\";")
        self.label_imNum_10.setObjectName("label_imNum_10")
        self.verticalLayout_15.addWidget(self.label_imNum_10)
        self.label_i_10 = QtWidgets.QLabel(self.QWidget2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_i_10.setFont(font)
        self.label_i_10.setStyleSheet("font: 24pt \"楷体\";")
        self.label_i_10.setObjectName("label_i_10")
        self.verticalLayout_15.addWidget(self.label_i_10)
        self.label_res_10 = QtWidgets.QLabel(self.QWidget2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_res_10.setFont(font)
        self.label_res_10.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 24pt \"楷体\";")
        self.label_res_10.setObjectName("label_res_10")
        self.verticalLayout_15.addWidget(self.label_res_10)
        self.horizontalLayout_23.addWidget(self.QWidget2)
        self.horizontalLayout_23.setStretch(0, 1)
        self.horizontalLayout_23.setStretch(1, 20)
        self.horizontalLayout_23.setStretch(2, 1)
        self.horizontalLayout_23.setStretch(3, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_23)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.pushBt_up_10 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushBt_up_10.setFont(font)
        self.pushBt_up_10.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"height:100px;\n"
"font: 35pt \"楷体\";\n"
"color: rgb(0, 0, 127);\n"
"")
        self.pushBt_up_10.setObjectName("pushBt_up_10")
        self.horizontalLayout_24.addWidget(self.pushBt_up_10)
        self.pushBt_dwn_10 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushBt_dwn_10.setFont(font)
        self.pushBt_dwn_10.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"height:100px;\n"
"font: 35pt \"楷体\";\n"
"color: rgb(0, 0, 127);")
        self.pushBt_dwn_10.setObjectName("pushBt_dwn_10")
        self.horizontalLayout_24.addWidget(self.pushBt_dwn_10)
        self.pushBt_reset_10 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushBt_reset_10.setFont(font)
        self.pushBt_reset_10.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"height:100px;\n"
"font: 35pt \"楷体\";\n"
"color: rgb(0, 0, 127);\n"
"")
        self.pushBt_reset_10.setObjectName("pushBt_reset_10")
        self.horizontalLayout_24.addWidget(self.pushBt_reset_10)
        self.pushBt_cntinu_10 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushBt_cntinu_10.setFont(font)
        self.pushBt_cntinu_10.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"height:100px;\n"
"font: 35pt \"楷体\";\n"
"color: rgb(0, 0, 127);")
        self.pushBt_cntinu_10.setObjectName("pushBt_cntinu_10")
        self.horizontalLayout_24.addWidget(self.pushBt_cntinu_10)
        self.verticalLayout.addLayout(self.horizontalLayout_24)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 20)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushBt_reset_10.clicked.connect(self.label_10.update)
        self.pushBt_up_10.clicked.connect(self.label_10.show)
        self.pushBt_dwn_10.clicked.connect(self.label_10.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_4.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:30pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">甲状腺超声图像智能识别与分类系统</span></p></body></html>"))
        self.label_imNum_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">图像总数：</span></p></body></html>"))
        self.label_i_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">处理第 张：</span></p></body></html>"))
        self.label_res_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">预测结果：</span></p></body></html>"))
        self.pushBt_up_10.setText(_translate("MainWindow", "上一张"))
        self.pushBt_dwn_10.setText(_translate("MainWindow", "下一张"))
        self.pushBt_reset_10.setText(_translate("MainWindow", "开始"))
        self.pushBt_cntinu_10.setText(_translate("MainWindow", "切换"))

