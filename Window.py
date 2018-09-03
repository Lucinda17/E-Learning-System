#!/usr/bin/python3
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Window():
    def __init__(self):
        super().__init__()

        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        self.title = "Login Page"
        self.top = 100
        self.left = 100
        self.width = 1800
        self.height = 500

        self.stylesheet = """
            QPushButton{
                background-color: #1e90ff;
                color: #000000;
            }

            QLabel{
                font-size: 23px;
            }
        """
        self.InitWindow()
        self.window.setStyleSheet(self.stylesheet)
        sys.exit(self.app.exec())

    def InitWindow(self):
        self.window.setWindowTitle(self.title)
        self.screenSize = QtWidgets.QDesktopWidget().screenGeometry(-1)
        #self.window.setGeometry(self.left, self.top, self.screenSize.width(), self.screenSize.height())
        self.window.setGeometry((self.screenSize.width()/2)-250, 100, 500, 800)
        self.window.setFixedSize(500, 800)
        self.addComponents()
        self.window.show()

    def addComponents(self):
        loginLbl = QtWidgets.QLabel("Login", self.window)
        #loginLbl.move((self.screenSize.width()/2)-20,90)
        f = 100
        loginLbl.move(230,90+f)
        userLE = QtWidgets.QLineEdit(self.window)
        userLE.setPlaceholderText("  username")
        userLE.resize(200, 26)
        userLE.move(150,150+f)
        #userLE.setStyleSheet("color: rgb(150,150,150);")
        passLE = QtWidgets.QLineEdit(self.window)
        passLE.setPlaceholderText("  password")
        #passLE.setStyleSheet("color: rgb(150,150,150);")
        passLE.resize(200, 26)
        passLE.move(150,190+f)
        passLE.setEchoMode(QLineEdit.Password)
        loginBtn = QtWidgets.QPushButton("Log in",self.window)
        loginBtn.move(150, 230+f)
        loginBtn.resize(200,26)
        #loginBtn.setStyleSheet("background-color: red") 
        #loginBtn.setStyleSheet("color: rgb(255,255,255);")

        

window = Window()