#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
from StudentProfile import *
import StudentProfile
from Student import *
#from TeacherProfile import *
import TeacherProfile
from Teacher import *
import Config

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time

#cred = credentials.Certificate('ServiceAccountKey.json')
#default_app = firebase_admin.initialize_app(cred)
#db = firestore.client()
db = Config.db

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
        self.tab = "login"

        self.InitWindow()

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
        #*******************************************************************************
        # Coordinates
        # ====
        self.top = 100
        self.loginLbl_X = self.left-95
        self.loginLbl_Y = 70+self.top
        self.userLE_X = self.left-100
        self.userLE_Y =200+self.top
        self.passLE_X =self.left-100
        self.passLE_Y =240+self.top
        '''self.ULELbl_X =
        self.ULELbl_Y = 
        self.PLELbl_X =
        self.PLELbl_Y =
        self.LoginTab_X =
        self.LoginTab_Y = 
        self.SignUpTab_X =
        self.SignUpTab_Y =
        '''
        self.loginBtn_X = self.left-100 
        self.loginBtn_Y = 280+self.top
        '''
        self.siginBtn_X =
        self.siginBtn_Y =
        self.readBtn_X =
        self.readBtn_Y ='''
        #*******************************************************************************
        loginLbl.move(self.loginLbl_X,self.loginLbl_Y)
        self.userLE = QLineEdit(self)
        self.userLE.setPlaceholderText("  username(id)")
        self.userLE.resize(200, 26)
        self.userLE.move(self.userLE_X,self.userLE_Y)
        self.passLE = QLineEdit(self)
        self.passLE.setPlaceholderText("  password")
        self.passLE.resize(200, 26)
        self.passLE.move(self.passLE_X,self.passLE_Y)
        self.passLE.setEchoMode(QLineEdit.Password)

        self.nameLE = QLineEdit(self)
        self.nameLE.setPlaceholderText("  full name")
        self.nameLE.resize(200,26)
        self.nameLE.move(9999,9999)
        
        # ULELbl = User Login Error Label
        self.ULELbl = QLabel("not found!", self)
        self.ULELbl.setStyleSheet("QLabel{color: #FF0000}")
        self.ULELbl.move(9999,9999)

        # PLELbl = Password Login Error Label
        self.PLELbl = QLabel("incorrect!", self)
        self.PLELbl.setStyleSheet("QLabel{color: #FF0000}")
        self.PLELbl.move(9999,9999)

        self.LoginTab = QPushButton("Login", self)
        self.LoginTab.move(self.left-100,150+self.top)
        self.LoginTab.resize(100,36)
        self.LoginTab.setStyleSheet("QPushButton{background-color: #3498db}"
                                    "QPushButton{border-radius: 115px}"
                                    "QPushButton{color: #FFFFFF}"
                                    "QPushButton{font-size:17px}")
                                    
        self.LoginTab.clicked.connect(self.LoginTabClicked)

        self.SignUpTab = QPushButton("Sign up", self)
        self.SignUpTab.move(self.left, 150+self.top)
        self.SignUpTab.resize(100,36)
        self.SignUpTab.setStyleSheet("QPushButton{background-color: white}"
                                     "QPushButton{border-radius: 115px}"
                                     "QPushButton{color: #8e838e}"
                                     "QPushButton{font-size:17px}")
        self.SignUpTab.clicked.connect(self.SignUpTabClicked)

        self.loginBtn = QPushButton("Log in",self)
        self.loginBtn.move(self.left-100, 280+self.top)
        self.loginBtn.resize(200,36)
        self.loginBtn.clicked.connect(self.LoginClicked)
        self.loginBtn.setStyleSheet("QPushButton{background-color: #3498db}"
                                    "QPushButton{border-radius: 115px}"
                                    "QPushButton{color: #FFFFFF}"
                                    "QPushButton{font-size:17px}")

        self.readBtn = QPushButton("Read", self)
        self.readBtn.move(self.left-100, 320+self.top)
        self.readBtn.resize(200,36)
        self.readBtn.clicked.connect(self.ReadClicked)
        self.readBtn.setVisible(False)

        self.signupBtn = QPushButton("Sign up",self)
        self.signupBtn.move(9999,9999)
        self.signupBtn.resize(200,36)
        self.signupBtn.clicked.connect(self.SignUpClicked)
        self.signupBtn.setStyleSheet("QPushButton{background-color:#3498db}"
                                     "QPushButton{border-radius: 115px}"
                                     "QPushButton{color: #FFFFFF}"
                                     "QPushButton{font-size:17px}")
        
        
        '''
        #---- For testing ----
        self.userLE.setText("1161302962")
        self.passLE.setText("Aa1111")

        #---------------------
        '''
        
        
    def LoginClicked(self):
        self.ULELbl.move(9999,9999)
        self.PLELbl.move(9999,9999)
        found = False
        # Search in "teachers"
        users_ref = db.collection(u'teachers')
        users = users_ref.get()
        for user in users:
            if self.userLE.text()==user.to_dict()['username']:
                found = True
                # Check password
                if self.passLE.text()== user.to_dict()['password']:
                    
                    print("login - teacher")
                    self.nd = TeacherProfile.TeacherProfile(user.to_dict()['username'])
                    self.nd.show()
                    self.hide()
                    break
                else:
                    self.ULELbl.move(9999,9999)
                    self.PLELbl.move(self.left+110,240+self.top)
                    self.passLE.setText("")

        # Serach in "students"
        if not found:
            users_ref = db.collection(u'students')
            users = users_ref.get()
            for user in users:
                if self.userLE.text()==user.to_dict()['username']:
                    found = True
                    # Check password
                    if self.passLE.text()== user.to_dict()['password']:
                        a = self.userLE.text()

                        self.nd = StudentProfile.StudentProfile(user.to_dict()['username'])

                        self.nd.show()
                        self.hide()
                        break
                    else:
                        self.ULELbl.move(9999,9999)
                        self.PLELbl.move(self.left+110,240+self.top)
                        self.passLE.setText("")
                        

        # Not found in either "teachers" or "students"
        if not found:
            self.ULELbl.move(self.left+110,200+self.top)
            self.PLELbl.move(9999,9999)
            self.userLE.setText("")
            self.passLE.setText("")

    def SignUpClicked(self):
        print("-----SignupClicked-----")
        if self.CheckUsername(self.userLE.text()) and self.CheckPassword(self.passLE.text()):
            users_ref = db.collection(u'teachers')
            users = users_ref.get()
            userID = ""

            found = False
            print("\n-----teachers-----")
            # Search in "teachers"
            for user in users:
                if self.userLE.text()==user.to_dict()['username']:
                    found = True
                    userID = user.id
                    break
            # if found in teachers
            if found:
                print("-----found in teachers-----")
                doc_ref = db.collection(u'teachers').document(userID).set({
                    u'username': self.userLE.text(),
                    u'password': self.passLE.text(),
                    u'name': self.nameLE.text()
                })
                
                confirmMB = QMessageBox.question(self, 'Successful', "Sign up successful", QMessageBox.Ok)
               
                self.nd = TeacherProfile.TeacherProfile(user.to_dict()['username'])
                self.nd.show()
                self.hide()
            # not found in teachers
            else:
                print("\n-----Students-----")
                users_ref = db.collection(u'students')
                users = users_ref.get()
                
                # Search in "students"
                for user in users:
                    print(user.to_dict()['username'])
                    if self.userLE.text()==user.to_dict()['username']:
                        found = True
                        userID = user.id
                        break
                # if found in student
                if found:        
                    print("\n-----found in students-----")
                    try:
                        if self.userLE.text()==user.to_dict()['name']:
                            print("\n***** Name is already exist *****")
                    except:
                        doc_ref = db.collection(u'students').document(userID).set({
                            u'username': self.userLE.text(),
                            u'password': self.passLE.text(),
                            u'name': self.nameLE.text()
                        })
                        confirmMB = QMessageBox.question(self, 'Successful', "Sign up successful", QMessageBox.Ok)
                        self.nd = StudentProfile.StudentProfile(self.userLE.text())
                        self.nd.show()
                        self.hide()
                # not found in students
                else:
                    errorMB = QMessageBox.question(self, 'Invalid', "Your ID is not in the database", QMessageBox.Ok)
                    self.userLE.setText("")
                    self.passLE.setText("")

        else:
            if not self.CheckUsername(self.userLE.text()):
                errorMessageU = "1. Username must be your student ID(10 digits)\n"
                errorMB = QMessageBox.question(self, 'Invalid', errorMessageU, QMessageBox.Ok)
                self.userLE.setText("")
            else:
                errorMessageP1 = "1. Password length must be at least 6\n"
                errorMessageP2 = "2. Password must contain both numbers and alphabets\n"
                errorMessageP3 = "3. Password must contain both UPPERCASE and lowercase"
                errorMessage = errorMessageP1+errorMessageP2+errorMessageP3
                errorMB = QMessageBox.question(self, 'Invalid', errorMessage, QMessageBox.Ok)
                self.passLE.setText("")

    def ReadClicked(self):
        users_ref = db.collection(u'students')
        users = users_ref.get()
        print("----- Students -----")
        for user in users:
            self.usersDict[user.to_dict()['username']] = user.to_dict()['password']
            print(f"{user.to_dict()['username']} : {user.to_dict()['name']} : {user.to_dict()['password']}")
            #print(u'{} => {} : {}'.format(user.id, user.to_dict()['username'], user.to_dict()['password']))
        print("----- end of Students -----\n")


 
        users_ref = db.collection(u'teachers')
        users = users_ref.get()
        print("----- Teachers -----")
        for user in users:
            self.usersDict[user.to_dict()['username']] = user.to_dict()['password']
            print(f"{user.to_dict()['username']} : {user.to_dict()['name']} : {user.to_dict()['password']}")
            #print(u'{} => {} : {}'.format(user.id, user.to_dict()['username'], user.to_dict()['password']))
        print("----- end of Teachers -----\n")
        
    def SignUpTabClicked(self):
        self.SignUpTab.setStyleSheet("QPushButton{background-color: #3498db}"
                                    "QPushButton{border-radius: 115px;}"
                                    "QPushButton{color: #FFFFFF}"
                                    "QPushButton{font-size:17px}")
        self.LoginTab.setStyleSheet("QPushButton{background-color: white}"
                                    "QPushButton{border-radius: 115px}"
                                    "QPushButton{color: #8e838e}"
                                    "QPushButton{font-size:17px}")
        self.loginBtn.move(9999,9999)
        self.signupBtn.move(self.loginBtn_X, self.loginBtn_Y+40)
        self.userLE.move(self.userLE_X, self.userLE_Y+40)
        self.nameLE.move(self.userLE_X, self.userLE_Y)
        self.passLE.move(self.passLE_X, self.passLE_Y+40)
        self.tab = "signup"

    def LoginTabClicked(self):
        self.LoginTab.setStyleSheet("QPushButton{background-color:#3498db}"
                                    "QPushButton{border-radius: 115px}"
                                    "QPushButton{color: #FFFFFF}"
                                    "QPushButton{font-size:17px}")
        self.SignUpTab.setStyleSheet("QPushButton{background-color: white}"
                                    "QPushButton{border-radius: 115px}"
                                    "QPushButton{color: #8e838e}"
                                    "QPushButton{font-size:17px}")
        self.signupBtn.move(9999,9999)
        self.loginBtn.move(self.loginBtn_X, self.loginBtn_Y)
        self.userLE.move(self.userLE_X, self.userLE_Y)
        self.passLE.move(self.passLE_X, self.passLE_Y)
        self.nameLE.move(9999,9999)
        self.tab = "login"
    
    def CheckUsername(self, user):
        valid = True
        if not len(user)==10:
            valid = False
            print("Username length not equal to 10")
        if any(c.isalpha() for c in user):
            valid = False
            print("Found character")
        return valid

    def CheckPassword(self, passw):
        valid = True
        if len(passw) < 6:
            valid = False
            print("Password length is less than 6")
        if not (any(c.isalpha() for  c in passw) and any(c.isdigit() for c in passw)):
            valid = False
            print("Password must contain both alphabets and numbers")
        if not any(c.isupper() for c in passw):
            valid = False
            print("Password must contains at least one uppercase alphabet")
        if not any(c.islower() for c in passw):
            valid = False
        print(f"valid: {valid}")
        return valid

    def keyPressEvent(self, event):
        if event.key()==QtCore.Qt.Key_Return:
            if(self.tab == "signup"):
                print("Signup is clicked")
                self.SignUpClicked()
            else:
                print("Login is clicked")
                self.LoginClicked()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Login()
    sys.exit(app.exec_())
