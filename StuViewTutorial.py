
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
import StudentAttemptFiB
import StudentAttemptMCQ
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
        self.backBtn = QPushButton("Back", self)
        self.backBtn.resize(100, 40)
        self.backBtn.clicked.connect(self.backClicked)

        self.vbox = QVBoxLayout(self);
        hbox = QVBoxLayout(self);
        empty = QLabel("", self)
        vbox00 = QVBoxLayout(self)
        vbox00.addWidget(empty)

        space = " "*83
        self.title = space + "Subect: " + self.subject
        self.lbl = QLabel(self.title,self)
        self.vbox.addStretch(1)
        hbox.addLayout(vbox00)
        hbox.addWidget(self.lbl)
        self.vbox.addLayout(hbox)
        
        self.vbox.addLayout(vbox00)
        codeLbl1 = QLabel("Code", self)
        titleLbl1 = QLabel("Title", self)
        typeLbl1 = QLabel("Type", self)

        vbox11 = QVBoxLayout(self)
        vbox11.addWidget(empty)
        vbox21 = QVBoxLayout(self)
        vbox21.addWidget(empty)
        vbox31 = QVBoxLayout(self)
        vbox31.addWidget(empty)
        vbox41 = QVBoxLayout(self)
        vbox41.addWidget(empty)

        hbox11 = QHBoxLayout(self)
        hbox11.addLayout(vbox11)
        hbox11.addWidget(codeLbl1)
        hbox11.addWidget(titleLbl1)
        hbox11.addWidget(typeLbl1)
        hbox11.addLayout(vbox21)
        hbox11.addLayout(vbox31)
        hbox11.addLayout(vbox41)
        
        users_ref = db.collection(u'tutorials')
        users = users_ref.get()
        self.vbox.addLayout(hbox11)
        self.btnList = []
        self.codeList = []
        self.tTypeList = []
        for user in users:
            if(user.to_dict()['subject']==self.subject):
                hbox1 = QHBoxLayout(self)
                code = user.to_dict()['code']
                title = user.to_dict()['title']
                tType = user.to_dict()['type']
                if(tType == "FiB"):
                    tType = "Fill in the Blank"
                else:
                    tType = "Multiple Choice Quesiton"

                codeLbl = QLabel(code, self)
                titleLbl = QLabel(title, self)
                typeLbl = QLabel(tType, self)
                empty = QLabel("", self)

                attemptBtn= QPushButton("Attempt",self)
                attemptBtn.clicked.connect(self.attemptClicked)
                viewBtn= QPushButton("View Result",self)


                self.btnList.append(attemptBtn)
                self.codeList.append(code)
                self.tTypeList.append(tType)

                vbox1 = QVBoxLayout(self)
                vbox1.addWidget(empty)
                vbox2 = QVBoxLayout(self)
                vbox2.addWidget(empty)

                hbox1.addLayout(vbox1)
                hbox1.addWidget(codeLbl)
                hbox1.addWidget(titleLbl)
                hbox1.addWidget(typeLbl)
                hbox1.addWidget(attemptBtn)
                hbox1.addWidget(viewBtn)
                hbox1.addLayout(vbox2)
                
                self.vbox.addLayout(hbox1)
        
        self.vbox.addStretch(20)
        self.setLayout(self.vbox)


    def backClicked(self):
        self.hide()
        self.newWindow = StuViewSubject.StuViewSubject(self.username)
        self.newWindow.show()
        self.hide()

    def attemptClicked(self):
        sender = self.sender()
        index = 0
        for i in range(len(self.btnList)):
            if(self.btnList[i]==sender):
                index = i
        
        print("\ncode: ",self.codeList[index])
        print("Type: ",self.tTypeList[index])

        if self.tTypeList[index] == "Fill in the Blank":
            self.newWindow = StudentAttemptFiB.StudentAttemptFiB(self.username,self.subject,self.codeList[index])
            self.newWindow.show()

        else:
            self.newWindow = StudentAttemptMCQ.StudentAttemptMCQ(self.username,self.subject,self.codeList[index])
            self.newWindow.show()
            self.hide
        

        self.hide()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = StuViewTutorial(1161302962,"Mathematics")
    sys.exit(app.exec_())