# this module will be called by TeacherCreateTut.py
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

import sys

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import TeacherCreateTut

cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

class TeacherCreateFiB(QWidget):
    def __init__(self, subjectName, subjectCode, tutorialTitle, numOfQuestion):
        # set window title and sizes
        super().__init__()
        self.title = "Teacher: Create FiB Question"
        
        self.subjectName = subjectName
        self.subjectCode = subjectCode
        self.tutorialTitle= tutorialTitle
        self.numOfQuestion = numOfQuestion
        self.emptyline = QLabel("")

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        #self.screenSize = QtWidgets.QDesktopWidget().screenGeometry(-1)
        #self.setGeometry(0, 0, 800, 600)
        self.screenSize = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.setGeometry(0, 0, self.screenSize.width(), self.screenSize.height())
        
        # create vBoxLayout
        widget = QWidget()
        layout = QVBoxLayout(self)

        # add components into window
        self.inputBoxList1 = []
        self.inputBoxList2 = []
        self.createButton = QPushButton("Create", self)
        self.returnButton = QPushButton("Return", self)
        layout.addWidget(QLabel("Please enter questions and answers for this tutorial:"))
        
        for i in range(self.numOfQuestion):
            # add question
            layout.addWidget(QLabel("Question " + str(i+1)))
            self.inputBoxList1.append(QLineEdit())
            layout.addWidget(self.inputBoxList1[i])

            # add answer
            layout.addWidget(QLabel("Answer " + str(i+1)))
            self.inputBoxList2.append(QLineEdit())
            layout.addWidget(self.inputBoxList2[i])
            layout.addWidget(self.emptyline)
                    
        layout.addWidget(self.createButton)
        layout.addWidget(self.returnButton)

        self.createButton.clicked.connect(self.enterQuestion)
        self.returnButton.clicked.connect(self.returnPreviousWindow)

        widget.setLayout(layout)
        #self.setLayout(self.vBoxLayout)

        # scroll area
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(widget)
        self.vLayout = QVBoxLayout(self)
        self.vLayout.addWidget(self.scroll)
        self.setLayout(self.vLayout)
        self.showMaximized()

    def enterQuestion(self):
        questionList = []
        answerList = []
        
        for i in range(self.numOfQuestion):
            questionList.append(self.inputBoxList1[i].text())
            answerList.append(self.inputBoxList2[i].text())
            
        # to-do
        # pass the question into database
        users_ref = db.collection(u'tutorial')
        users = users_ref.get()
        doc_ref = db.collection(u'tutorial').document().set({
            u'subject': self.subjectName,
            u'code': self.subjectCode,
            u'title': self.tutorialTitle,
            u'numOfQuestion': self.numOfQuestion,
            u'questionList': questionList,
            u'answerList': answerList,
            u'type': "FiB"
        })
        confirm = QMessageBox.question(self, 'Successful', "Done!", QMessageBox.Ok)
        self.returnPreviousWindow()

    def returnPreviousWindow(self):
        #FunctionNameofPreviousWindow()
        print('return')
        
        # add code to move to previous window once clicked
        # to-do
        self.newWindow = TeacherCreateTut.TeacherCreateTut()
        self.close()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = TeacherCreateFiB()
    sys.exit(App.exec())
