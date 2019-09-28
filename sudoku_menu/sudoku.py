# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sudoku.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import collect_log as clog
from textEdit import textEdit


class Ui_SudokuWindow(object):
    def __init__(self,diff):
        self.diff_keyword=diff
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.textEdits=self.read_write_sudoku()

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 510, 175, 60))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 510, 60, 60))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(275, 510, 151, 60))
        # palette = QtGui.QPalette()
        # brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        # brush = QtGui.QBrush(QtGui.QColor(138, 226, 52, 128))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        # brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        # brush = QtGui.QBrush(QtGui.QColor(138, 226, 52, 128))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        # brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        # self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 519, 14))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def read_write_sudoku(self):
        textEdits=[]
        su=clog.getSudokuLog("../logs/{}.log".format(self.diff_keyword))
        i=0
        j=0
        tmp=[]
        while j!=9:
            WIDTH=50
            Text=textEdit(centralwidget=self.centralwidget,start=120,width=WIDTH,i=i,j=j)

            tmp_num=su[j][i]  

            if tmp_num==" ":
                pass
            else:
                Text.edit.setText(tmp_num)
                Text.edit.setReadOnly(True)

            tmp.append(Text)
            i+=1
            if i%9==0:
                i=0
                j+=1
                textEdits.append(tmp)
                tmp=[]
        return textEdits
    
    # def txtInputChanged():
    # if txtInput.toPlainText().length() > maxInputLen:
    #     text = txtInput.toPlainText()
    #     text = text[:maxInputLen]
    #     txtInput.setPlainText(text)

    #     cursor = txtInput.textCursor()
    # cursor.setPosition(maxInputLen)
    # txtInput.setTextCursor(cursor)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Main menu"))
        self.label.setText(_translate("MainWindow", "0"))


