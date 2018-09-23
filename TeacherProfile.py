#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QDesktopWidget, QLineEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import sys

from TeaViewSubject import *
#from Teacher import *
#Connect to firebase library 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

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
        self.viewSubject = QPushButton("View Subject ",self)
        self.viewSubject.resize(200,60)
        self.viewSubject.move(100,100)
        self.viewSubject.clicked.connect(self.viewSubjectClicked)
        self.name="User Name:"+self.username
        self.nameLbl = QLabel(self.name, self)
        self.nameLbl.setFixedWidth(1000)
        self.nameLbl.setFixedHeight(100)
        print("teacher profile")
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
 
# create window(exit)  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow=TeacherProfile()
    sys.exit(app.exec_())

