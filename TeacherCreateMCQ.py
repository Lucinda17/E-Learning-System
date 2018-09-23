# this module will be called by TeacherCreateTut.py
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

import sys
import TeacherCreateTut

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import TeacherCreateTut
#import TeacherCreateFiB
import Config
#db = Config.db
'''
cred = credentials.Certificate('ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
#default_app = firebase_admin.get_app()
db = firestore.client()
'''
db = Config.db

class TeacherCreateMCQ(QWidget):
    def __init__(self, username, subjectName, subjectCode, tutorialTitle, numOfQuestion):
        # set window title and sizes
        super().__init__()
        self.title = "Teacher: Create MCQ Question"

        self.username = username
        self.subjectName = subjectName
        self.subjectCode = subjectCode
        self.tutorialTitle= tutorialTitle
        self.numOfQuestion = numOfQuestion
        self.emptyline = QLabel("")

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        
        # create BoxLayouts
        widget = QWidget()
        layout = QVBoxLayout()

        # add components into window
        self.inputBoxList1 = []
        self.inputBoxList2 = []

        self.createButton = QPushButton("Create", self)
        self.returnButton = QPushButton("Return", self)
        layout.addWidget(QLabel("Please enter questions and answers for this tutorial:"))
        
        ans = 0
        for i in range(self.numOfQuestion):
            # add question
            layout.addWidget(QLabel("Question " + str(i+1)))
            self.inputBoxList1.append(QLineEdit())
            layout.addWidget(self.inputBoxList1[i])

            # add answer
            layout.addWidget(QLabel("Answers for 4 options"))
            for j in range(4):
                self.inputBoxList2.append(QLineEdit())
                layout.addWidget(self.inputBoxList2[ans])
                ans += 1

            layout.addWidget(self.emptyline)
                    
        layout.addWidget(self.createButton)
        layout.addWidget(self.returnButton)

        self.createButton.clicked.connect(self.enterQuestion)
        self.returnButton.clicked.connect(self.returnPreviousWindow)

        widget.setLayout(layout)

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
        for j in range(self.numOfQuestion * 4):
            answerList.append(self.inputBoxList2[j].text())
            
        # to-do
        # pass the question into database
        # important note:
        # example:
        # answerList[0] to answerList[3] is for Question 1
        # answerList[4] to answerList[7] is for Question 2
        # and so on....
        users_ref = db.collection(u'tutorials')
        users = users_ref.get()
        doc_ref = db.collection(u'tutorials').document().set({
            u'subject': self.subjectName,
            u'code': self.subjectCode,
            u'title': self.tutorialTitle,
            u'numOfQuestion': self.numOfQuestion,
            u'questionList': questionList,
            u'answerList': answerList,
            u'type': "MCQ"
        })
        confirm = QMessageBox.question(self, 'Successful', "Done!", QMessageBox.Ok)
        self.returnPreviousWindow()

    def returnPreviousWindow(self):
        self.newWindow = TeacherCreateTut.TeacherCreateTut()
        self.newWindow.show()
        self.close()
        
        # add code to move to previous window once clicked
        # to-do
        self.newWindow = TeacherCreateTut.TeacherCreateTut(self.username, self.subjectName)
        self.close()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = TeacherCreateMCQ()
    sys.exit(App.exec())
