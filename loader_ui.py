# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\FER\py2\loader.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 528)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color: rgba(106, 124, 101, 200);\n"
"}\n"
"\n"
"QLabel{\n"
"    color: white;\n"
"    font: 12pt \"Century Gothic\";\n"
"}\n"
"\n"
"QRadioButton{\n"
"    font: 12pt \"Century Gothic\";\n"
"}\n"
"Line{\n"
"    height: 1px;\n"
"    border: 0;\n"
"    border-top: 1px solid white;\n"
"    padding: 0; \n"
"    margin-top: 5px;\n"
"}\n"
"\n"
"QMenu{\n"
"background-color: black;\n"
"font: 12pt \"Century Gothic\";\n"
"    font-weight: bold;\n"
"    color:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"backgroud-color: white\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(390, 100, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 12pt \"Century Gothic\";\n"
"    font-weight: bold;\n"
"    color:white;\n"
"    background-color:rgba(72, 99, 63,200);\n"
"    border: 1px solid rgb(72, 99, 63);\n"
"    \n"
"}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 190, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 12pt \"Century Gothic\";\n"
"    font-weight: bold;\n"
"    color:white;\n"
"background-color:rgba(43, 61, 37, 200);\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    font: 13pt \"Century Gothic\";\n"
"    font-weight: bold;\n"
"    color:white;\n"
"    background-color:rgb(67, 96, 57);\n"
"    border: 2px solid white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 421, 641))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgba(21, 33, 20);\n"
"}\n"
"Line{\n"
"    height: 1px;\n"
"    border: 0;\n"
"    border-top: 1px solid white;\n"
"    padding: 0; \n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 230, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: Transparent;\n"
"border-radius: 25px;\n"
"border: 1px solid white;\n"
"color: white;\n"
"font: 12pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(35, 56, 33);\n"
"border: 2px solid white;\n"
"font: 13pt \"Century Gothic\";\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(80, 300, 261, 16))
        self.line_2.setStyleSheet("Line{\n"
"    height: 1px;\n"
"    border: 0;\n"
"    border-top: 1px solid white;\n"
"    padding: 0; \n"
"}")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(80, 190, 261, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setStyleSheet("Line{\n"
"    height: 1px;\n"
"    border: 0;\n"
"    border-top: 1px solid white;\n"
"    padding: 0; \n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 340, 141, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 380, 141, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 420, 141, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 771, 61))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color:rgba(0,0,0,100);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 71, 61))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background-color:Transparent;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(38, 39, 40);\n"
"}")
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 0, 71, 61))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"background-color:Transparent;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(38, 39, 40);\n"
"}")
        self.pushButton_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 420, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 380, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 340, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 140, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("QRadioButton{\n"
"    color: white;\n"
"    font: 12pt \"Century Gothic\";\n"
"}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(110, 100, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("QRadioButton{\n"
"    color: white;\n"
"    font: 12pt \"Century Gothic\";\n"
"}")
        self.radioButton.setObjectName("radioButton")
        self.pushButton_2.raise_()
        self.line_2.raise_()
        self.line.raise_()
        self.frame_2.raise_()
        self.label_3.raise_()
        self.lineEdit_4.raise_()
        self.label_2.raise_()
        self.lineEdit_3.raise_()
        self.label.raise_()
        self.lineEdit_2.raise_()
        self.radioButton_2.raise_()
        self.radioButton.raise_()
        self.frame.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionEncoded_encrypted = QtWidgets.QAction(MainWindow)
        self.actionEncoded_encrypted.setObjectName("actionEncoded_encrypted")
        self.actionNormal_image = QtWidgets.QAction(MainWindow)
        self.actionNormal_image.setObjectName("actionNormal_image")
        self.line.setStyleSheet(""
                                "height: 1px;"
                                "border: 0;"
                                "border-top: 1px solid white;"
                                "padding: 0;}")
        self.line_2.setStyleSheet(""
                                  "height: 1px;"
                                  "border: 0;"
                                  "border-top: 1px solid white;"
                                  "padding: 0;}")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "URL"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.pushButton_2.setText(_translate("MainWindow", "Gallery"))
        self.pushButton_5.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.pushButton_6.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.label_3.setText(_translate("MainWindow", "Size:"))
        self.label_2.setText(_translate("MainWindow", "Date:"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.radioButton_2.setText(_translate("MainWindow", "Normal image"))
        self.radioButton.setText(_translate("MainWindow", "Encoded and encrypted "))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionEncoded_encrypted.setText(_translate("MainWindow", "Encoded and encrypted"))
        self.actionNormal_image.setText(_translate("MainWindow", "Normal image"))

import load_icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

