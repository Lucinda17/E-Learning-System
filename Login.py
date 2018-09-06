#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from StudentProfile import *

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Login Page"
        self.width = 450
        self.height = 800
        self.top = 100
        self.left = self.width/2
        
        # Global variables
        self.i = 1
        self.usersDict = {}

        #*****************************************************
        """self.stylesheet = 
            .self.loginTab{
                background-color: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FBC2EB,stop: 1 #A6C1EE);
                border-radius: 115px;
                color: #FFFFFF;
            }

            QLabel{
                font-size: 23px;
            }
        """
        self.InitWindow()
        #self.setStyleSheet(self.stylesheet)

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
        loginLbl = QLabel("E-Learning System", self)
        loginLbl.setFixedHeight(100)
        loginLbl.setStyleSheet("QLabel{font-size: 23px}")
        self.top = 100
        loginLbl.move(self.left-90,70+self.top)
        self.userLE = QLineEdit(self)
        self.userLE.setPlaceholderText("  username")
        self.userLE.resize(200, 26)
        self.userLE.move(self.left-100,200+self.top)
        self.passLE = QLineEdit(self)
        self.passLE.setPlaceholderText("  password")
        self.passLE.resize(200, 26)
        self.passLE.move(self.left-100,240+self.top)
        self.passLE.setEchoMode(QLineEdit.Password)
        
        self.testLbl = QLabel("password invalid", self)
        self.testLbl.move(9999,9999)

        self.LoginTab = QPushButton("Login", self)
        self.LoginTab.move(self.left-100, 150+self.top)
        self.LoginTab.resize(100,36)
        self.LoginTab.setStyleSheet("QPushButton{background-color: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FBC2EB,stop: 1 #A6C1EE)}"
                                    "QPushButton{border-radius: 115px}"
                                    "QPushButton{color: #FFFFFF}")
        self.LoginTab.clicked.connect(self.LoginTabClicked)

        self.SignUpTab = QPushButton("Sign up", self)
        self.SignUpTab.move(self.left, 150+self.top)
        self.SignUpTab.resize(100,36)
        self.SignUpTab.setStyleSheet("QPushButton{background-color: white}"
                                     "QPushButton{border-radius: 115px}"
                                     "QPushButton{color: #8e838e}")
        self.SignUpTab.clicked.connect(self.SignUpTabClicked)

        self.loginBtn = QPushButton("Log in",self)
        self.loginBtn.move(self.left-100, 280+self.top)
        self.loginBtn.resize(200,36)
        self.loginBtn.clicked.connect(self.LoginClicked)
        self.loginBtn.setStyleSheet("QPushButton{background-color: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FBC2EB,stop: 1 #A6C1EE)}"
                                    "QPushButton{border-radius: 115px}"
                                    "QPushButton{color: #FFFFFF}")

        self.readBtn = QPushButton("Read", self)
        self.readBtn.move(self.left-100, 320+self.top)
        self.readBtn.resize(200,36)
        self.readBtn.clicked.connect(self.ReadClicked)

        self.signupBtn = QPushButton("Sign up",self)
        self.signupBtn.move(9999,9999)
        self.signupBtn.resize(200,36)
        self.signupBtn.clicked.connect(self.SignUpClicked)
        self.signupBtn.setStyleSheet("QPushButton{background-color: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FBC2EB,stop: 1 #A6C1EE)}"
                                     "QPushButton{border-radius: 115px}"
                                     "QPushButton{color: #FFFFFF}")
        
    def LoginClicked(self):
        '''
        self.nd = StudentProfile()
        self.nd.show()
        self.hide()
        
        '''

        print(len(self.userLE.text())==10)
        print(len(self.passLE.text())>4 and len(self.passLE.text())<15)
        checkU = len(self.userLE.text())==10
        checkP = len(self.passLE.text())>4 and len(self.passLE.text())<15
        '''
        users_ref = db.collection(u'users')
        users = users_ref.get()

        found = False
        userNF = False
        passNF = False
        for user in users:
            if self.userLE.text()==user.to_dict()['username']:
                userNF = True
                if self.passLE.text()== user.to_dict()['password']:
                    passNF = True
                    found = True
                    break

        if found:
            print("Login successful")
        else:
            print("Login fail")
            if userNF == False:
                 self.userErrorLbl = QLabel("username not found")
                 self.userErrorLbl.move(self.left+110,200+self.top)
            if passNF == False:
                 self.passErrorLbl = QLabel("password not found")
                 self.passErrorLbl.move(self.left+110,240+self.top)
        '''
        if checkU and checkP:
            print("Login successful")
        else:
            print("Login fail")
            if not checkU:
                 self.testLbl.move(self.left+105,240+self.top)
                 print("in not checkU")
            if not checkP:
                 passErrorLbl = QLabel("password not found")
                 passErrorLbl.move(self.left+110,240+self.top)

    def SignUpClicked(self):
        users_ref = db.collection(u'users')
        users = users_ref.get()

        found = False
        for user in users:
            if self.userLE.text()==user.to_dict()['username']:
                found = True
                break

        if found:
            print("ID already exist")
        else:
            doc_ref = db.collection(u'users').document().set({
                u'username': self.userLE.text(),
                u'password': self.passLE.text()
            })
            print("Sign up successful")
        

    def ReadClicked(self):
        users_ref = db.collection(u'users')
        users = users_ref.get()

        for user in users:
            self.usersDict[user.to_dict()['username']] = user.to_dict()['password']
            #print(u'{} => {} : {}'.format(user.id, user.to_dict()['username'], user.to_dict()['password']))

        print()
        for key, value in self.usersDict.items():
            print(key, "\t:\t",value)

    def SignUpTabClicked(self):
        self.SignUpTab.setStyleSheet("QPushButton{background-color: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FBC2EB,stop: 1 #A6C1EE)}"
                                    "QPushButton{border-radius: 115px;}"
                                    "QPushButton{color: #FFFFFF}")
        self.LoginTab.setStyleSheet("QPushButton{background-color: white}"
                                    "QPushButton{border-radius: 115px}"
                                    "QPushButton{color: #8e838e}")
        self.loginBtn.move(9999,9999)
        self.signupBtn.move(self.left-100, 280+self.top)

    def LoginTabClicked(self):
        self.LoginTab.setStyleSheet("QPushButton{background-color: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FBC2EB,stop: 1 #A6C1EE)}"
                                    "QPushButton{border-radius: 115px}"
                                    "QPushButton{color: #FFFFFF}")
        self.SignUpTab.setStyleSheet("QPushButton{background-color: white}"
                                    "QPushButton{border-radius: 115px}"
                                    "QPushButton{color: #8e838e}")
        self.signupBtn.move(9999,9999)
        self.loginBtn.move(self.left-100, 280+self.top)
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Login()
    sys.exit(app.exec_())
