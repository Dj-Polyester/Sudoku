# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from clickable import clickable

class Ui_MainWindow(object):
    
    def __init__(self,diff):
        self.diff_keyword=diff
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") 
        MainWindow.resize(472, 422)
        self.MainWindow=MainWindow
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(150, 70, 181, 16))
        self.horizontalSlider.setMaximum(3)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 120, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 200, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setText(self.diff_keyword)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 350, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 350, 31, 31))
        self.label_3.setPixmap(QtGui.QPixmap("../pictures/q_mark.png"))
        self.label_3.setScaledContents(True)
        

        self.label_3.setObjectName("label_3")
        clickable(self.label_3).connect(self.get_help)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 14))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.horizontalSlider.valueChanged.connect(self.chng_diff)
        self.pushButton_2.clicked.connect(self.start_sudoku)
        self.pushButton_3.clicked.connect(self.quit_main_menu)
        self.pushButton_4.clicked.connect(self.collect_data)
    
    

    def get_help(self):
        print("clicked")

    def chng_diff(self):
        diff=self.horizontalSlider.value()
        
        if diff==0: self.diff_keyword="easy" 
        elif diff==1: self.diff_keyword="medium"
        elif diff==2: self.diff_keyword="hard"
        else: self.diff_keyword="evil"

        self.label_2.setText(self.diff_keyword)
    
    def start_sudoku(self):
        self.MainWindow.close()
        os.system("python3 ../sudoku_menu/sudoku_start.py "+self.diff_keyword)



    def quit_main_menu(self):
        QtCore.QCoreApplication.instance().quit()

    def collect_data(self):
        os.system("python3 ../collect/collect_website.py")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sudoku"))
        MainWindow.setWindowIcon(QtGui.QIcon("../pictures/sudoku.png"))

        self.pushButton_2.setText(_translate("MainWindow", "Play"))
        self.label.setText(_translate("MainWindow", "Set Difficulty:"))
        self.pushButton_3.setText(_translate("MainWindow", "Quit"))
        self.label_2.setText(_translate("MainWindow", "Easy"))
        self.pushButton_4.setText(_translate("MainWindow", "Collect data"))
