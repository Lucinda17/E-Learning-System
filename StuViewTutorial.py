
#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QDesktopWidget, QLineEdit, QMessageBox, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import sys

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import StuViewSubject
import Config

'''
cred = credentials.Certificate('ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
'''
cred = Config.cred
default_app = Config.default_app
db = Config.db

class StuViewTutorial(QWidget):
    def __init__(self, username, subject):
        super().__init__()

        self.title = "Student - View Tutorial"
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
        self.addSubjectBtn = QPushButton("Back", self)
        self.addSubjectBtn.resize(100, 40)
        self.addSubjectBtn.clicked.connect(self.addSubjectClicked)
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
        for user in users:
            if(user.to_dict()['subject']==self.subject):
                tutDetail = user.to_dict()['code']+": "+user.to_dict()['title']
                tutDetailLbl = QLabel(tutDetail,self)
                button = QPushButton("Attempt",self)
                gridd = QGridLayout(self)
                gridd.addWidget(tutDetailLbl,r,0,Qt.AlignRight)
                gridd.addWidget(button,r,1,Qt.AlignLeft)
                r += 1
                self.vbox.addLayout(gridd)
        
        self.vbox.addStretch(20)
        self.setLayout(self.vbox)

    def addSubjectClicked(self):
        self.hide()
        self.newWindow = StuViewSubject.StuViewSubject(self.username)
        self.newWindow.show()
        self.hide()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = StuViewTutorial(1161302962,"English")
    sys.exit(app.exec_())