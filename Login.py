#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from StudentProfile import *

class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Login Page"
        self.width = 450
        self.height = 800
        self.top = 100
        self.left = self.width/2

        self.stylesheet = """
            QPushButton{
                background-color: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FBC2EB,stop: 1 #A6C1EE);
                border-radius: 115px;
                color: #FFFFFF;
            }

            QLabel{
                font-size: 23px;
            }
        """
        self.InitWindow()
        self.setStyleSheet(self.stylesheet)

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.screenSize = QtWidgets.QDesktopWidget().screenGeometry(-1)
        #self.window.setGeometry(self.left, self.top, self.screenSize.width(), self.screenSize.height())
        self.setGeometry((self.screenSize.width()/2)-self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        self.addComponents()
        self.show()

    def addComponents(self):
        loginLbl = QLabel("Login", self)
        loginLbl.setFixedWidth(90)
        loginLbl.setFixedHeight(100)
        #loginLbl.move((self.screenSize.width()/2)-20,90)
        f = 100
        loginLbl.move(self.left-30,70+f)
        userLE = QLineEdit(self)
        userLE.setPlaceholderText("  username")
        userLE.resize(200, 26)
        userLE.move(self.left-100,150+f)
        #userLE.setStyleSheet("color: rgb(150,150,150);")
        passLE = QLineEdit(self)
        passLE.setPlaceholderText("  password")
        #passLE.setStyleSheet("color: rgb(150,150,150);")
        passLE.resize(200, 26)
        passLE.move(self.left-100,190+f)
        passLE.setEchoMode(QLineEdit.Password)
        loginBtn = QPushButton("Log in",self)
        loginBtn.move(self.left-100, 230+f)
        loginBtn.resize(200,36)
        loginBtn.clicked.connect(self.LoginClicked)

    def LoginClicked(self):
        
        self.nd = StudentProfile()
        self.nd.show()
        self.hide()


        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Login()
    sys.exit(app.exec_())