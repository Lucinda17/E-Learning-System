#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QDesktopWidget, QLineEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import sys

from TeaViewSubject import *
import Login
import Config

#Connect to firebase library 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

db = Config.db

class TeacherProfile(QWidget):
    # create window(Headline)
    def __init__(self,username):
        super().__init__()
        
        self.title = 'Teacher Profile Page'
        self.left = 0
        self.top = 0
        self.width = 0
        self.height = 0

        self.username=username

        self.stylesheet = """
            QPushButton{
                background-color: #3498db;
                border-radius: 115px;
                color: #FFFFFF;
                font-size: 20px;
            }

            QLabel{
                font-size: 23px;
            }
        """
        self.InitWindow()
        self.setStyleSheet(self.stylesheet)
        
    # create window(setting)
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.screenSize = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.setGeometry(0, 0, self.screenSize.width(), self.screenSize.height())
        self.setFixedSize(self.screenSize.width(), self.screenSize.height())
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        self.addComponents()
        self.show()

    #add component function
    def addComponents(self):
#Add Teacher Profile
        self.name = ""
        users_ref = db.collection(u'teachers')
        users = users_ref.get()
        
        for user in users:
            if(user.to_dict()['username']==self.username):
                self.name = user.to_dict()['name']


        profileLbl = QLabel("Teacher Profile", self)
        profileLbl.setFixedHeight(100)
        profileLbl.setStyleSheet("QLabel{font-size: 70px}")
        profileLbl.move(700,100)
        #
        #View Subject Button
        self.viewSubject = QPushButton("View Subject ",self)
        self.viewSubject.resize(300,100)
        self.viewSubject.move(1200,800)
        self.viewSubject.clicked.connect(self.viewSubjectClicked)

        #discussionBoard Button(stub)
        self.discussionBoard = QPushButton("Access to Discussion Board",self)
        self.discussionBoard.resize(300,100)
        self.discussionBoard.move(800,800)

        #Student Performance Button(stub)
        self.stuPerform = QPushButton("Access to Student Performance",self)
        self.stuPerform.resize(300,100)
        self.stuPerform.move(400,800)

        #Name Label
        self.nameLabel="Name:                           "+self.name
        nameLbl = QLabel(self.nameLabel, self)
        nameLbl.setStyleSheet("QLabel{font-size: 40px}")
        nameLbl.move(400,300)

        self.idLabel=  "ID:                                      "+self.username
        idLbl = QLabel(self.idLabel, self)
        idLbl.setStyleSheet("QLabel{font-size: 40px}")
        idLbl.move(400,400)
                                
        self.subLabel="Subject Teaching:                  Mathematics,Physics"
        subLbl = QLabel(self.subLabel, self)
        subLbl.setStyleSheet("QLabel{font-size: 40px}")
        subLbl.move(400,500)

        self.createTutBtn = QPushButton("Back", self)
        self.createTutBtn .resize(100, 40)
        self.createTutBtn .clicked.connect(self.backClicked)

        '''
        #---- For testing ----
        self.viewSubjectClicked()
        self.hide()
        #---------------------
        '''

    def viewSubjectClicked(self):
        self.newWindow = TeaViewSubject(self.username)
        self.newWindow.show()
        self.close()
    
    def backClicked(self):
        self.newWindow = Login.Login()
        self.newWindow.show()
        self.hide()
 
# create window(exit)  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow=TeacherProfile()
    sys.exit(app.exec_())

