#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QDesktopWidget, QLineEdit, QMessageBox 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import sys

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import StudentProfile 

cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

class StuViewSubject(QWidget):
    def __init__(self, username):
        super().__init__()

        self.title = "Student - View Subject"
        self.width = 0
        self.height = 0
        self.top = 0
        self.left = 0

        self.username = username
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.screenSize = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.setGeometry(0, 0, self.screenSize.width(), self.screenSize.height())
        #self.setFixedSize(self.screenSize.width(), self.screenSize.height())
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        self.addComponents()
        self.show()

    def addComponents(self):
        self.addSubjectBtn = QPushButton("Back", self)
        self.addSubjectBtn.resize(100, 40)
        self.addSubjectBtn.clicked.connect(self.addSubjectClicked)
        self.subjectList = []
        users_ref = db.collection(u'students')
        users = users_ref.get()
        
        z = self.screenSize.width()/6 - 100 
        x = z 
        y = 200
        for user in users:
            if(user.to_dict()['username']==self.username):
                
                self.subjectList = user.to_dict()['subjects']
                for subject in self.subjectList:
                    temp = QPushButton(subject,self)
                    temp.setStyleSheet("QPushButton{background-color: #3498db}"
                                       "QPushButton{border-radius: 115px}"
                                       "QPushButton{color: #FFFFFF}"
                                       "QPushButton{font-size: 20px}")
                    temp.resize(200,100)
                    temp.move(x,y)
                    x += z + 100
                    if(x>self.screenSize.width()):
                        x = z
                        y += 200
        

    def addSubjectClicked(self):
        self.hide()
        self.newWindow = StudentProfile.StudentProfile(self.username)
        self.newWindow.show()
        self.hide()

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = StuViewSubject()
    sys.exit(app.exec_())