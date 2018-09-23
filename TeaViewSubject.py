#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QDesktopWidget, QLineEdit, QMessageBox, QButtonGroup 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import sys

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import TeacherProfile 
#import TeaViewTutorial

cred = credentials.Certificate('./ServiceAccountKey.json')
#default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

class TeaViewSubject(QWidget):
    def __init__(self, username):
        super().__init__()
        self.title = "Teacher - View Subject"
        self.width = 0
        self.height = 0
        self.top = 0
        self.left = 0

        self.username = username
        print("viewSubject")
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
        self.backBtn = QPushButton("Back", self)
        self.backBtn.resize(100, 40)
        self.backBtn.clicked.connect(self.backClicked)
        self.subjectList = []
        self.subjectBtnList = QButtonGroup(self)
        users_ref = db.collection(u'teachers')
        users = users_ref.get()
        
        z = self.screenSize.width()/6 - 100 
        x = z 
        y = 200

        for user in users:
            if(user.to_dict()['username']==self.username):
                
                self.subjectList = user.to_dict()['subjects']
                for subject in self.subjectList:
                    temp = QPushButton(subject,self)
                    temp.clicked.connect(self.subjectClicked)
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
        
        self.subjectBtnList.buttonClicked.connect(self.subjectClicked)
        '''
        #---- For testing ----
        self.subjectClicked()
        self.hide()
        #---------------------
        '''

        

    def backClicked(self):
        self.newWindow = TeacherProfile.TeacherProfile(self.username)
        self.newWindow.show()
        self.hide()

    def subjectClicked(self):
        sender = self.sender()
        #print("you pressed -> ",sender.text())
        #self.newWindow = TeaViewTutorial.TeaViewTutorial(self.username, sender.text())
        #wait :below
        self.newWindow = TeaViewTutorial.TeaViewTutorial(self.username,"English") 
        self.newWindow.show()
        self.hide()
