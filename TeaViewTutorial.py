
#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QDesktopWidget, QLineEdit, QMessageBox, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import sys

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import TeaViewSubject
import TeacherCreateTut
import Config

#cred = credentials.Certificate('ServiceAccountKey.json')
#default_app = firebase_admin.initialize_app(cred)
#db = firestore.client()
db = Config.db

class TeaViewTutorial(QWidget):
    def __init__(self, username, subject):
        super().__init__()

        self.title = "Teacher - View Tutorial"
        self.width = 0
        self.height = 0
        self.top = 0
        self.left = 0

        self.username = username
        self.subject = subject
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
        self.createTutBtn = QPushButton("Add", self)
        self.createTutBtn.resize(100, 40)
        self.createTutBtn.move(self.screenSize.width()-100,0)
        self.createTutBtn .clicked.connect(self.createTutClicked)
        self.lbl = QLabel(self.subject,self)
        self.vbox = QVBoxLayout(self)
        self.hbox = QHBoxLayout(self)
        self.vbox.addStretch(1)
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.lbl)
        self.hbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        users_ref = db.collection(u'tutorials')
        users = users_ref.get()
        
        self.vbox.addStretch(1)
        r = 0
        self.btn = []
        self.sub = []
        for user in users:
            if(user.to_dict()['subject']==self.subject):
                tutDetail = user.to_dict()['code']+": "+user.to_dict()['title']
                tutDetailLbl = QLabel(tutDetail,self)
                editBtn= QPushButton("Edit",self)
                removeBtn= QPushButton("Remove",self)
                removeBtn.clicked.connect(self.removeClicked)
                self.sub.append(user.to_dict()['code'])
                self.btn.append(removeBtn)
                hbox = QHBoxLayout(self)
                gridd = QGridLayout(self)
                gridd.addWidget(tutDetailLbl,r,0,Qt.AlignRight)
                hbox.addWidget(editBtn)
                hbox.addWidget(removeBtn)
                gridd.addLayout(hbox,r,1,Qt.AlignLeft)
                r += 1
                self.vbox.addLayout(gridd)
        
        self.vbox.addStretch(20)
        self.setLayout(self.vbox)

    def backClicked(self):
        self.hide()
        self.newWindow = TeaViewSubject.TeaViewSubject(self.username)
        self.newWindow.show()
        self.hide()

    def createTutClicked(self):
        self.hide()
        self.newWindow = TeacherCreateTut.TeacherCreateTut(self.username,self.subject)
        self.newWindow.show()
        self.hide()


    def removeClicked(self):
        sender = self.sender()
        index = 0
        for i in range(len(self.btn)):
            if(self.btn[i]==sender):
                index = i
        
        print(self.sub[index])
        users_ref = db.collection(u'tutorials')
        users = users_ref.get()
        for user in users:
            if(user.to_dict()['code']==self.sub[index]):
                db.collection(u'tutorials').document(user.id).delete()
                break

        #self.update()
        self.close()
        self.newWindow = TeaViewTutorial(self.username,self.subject)
        #a = QMessageBox.question(self,"Test", b,QMessageBox.Ok)
        #print("you pressed -> ",sender.text())
        #self.newWindow = TeaViewTutorial.TeaViewTutorial(self.username, sender.text())
        #wait :below
        #self.newWindow = TeaViewTutorial.TeaViewTutorial(self.username,sender.text())
        #self.newWindow.show()
        #self.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = TeaViewTutorial(1234567890,"Mathematics")
    sys.exit(app.exec_())
