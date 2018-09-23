
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

import sys
import StuViewTutorial
import Config

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

db = Config.db

class StudentAttemptFiB(QWidget):
    def __init__(self,username,subject,code):
        # set window title and sizes
        super().__init__()
        self.title = "Student: Attempt FiB Question"

        self.username = username
        self.subject = subject
        self.code = code 
        self.emptyline = QLabel("")

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.screenSize = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.setGeometry(0, 0, self.screenSize.width(), self.screenSize.height())

        # create vBoxLayout
        widget = QWidget()
        layout = QVBoxLayout(self)

        # add components into window
        # to-do: import question and answer from tutorial database
        self.questionList = []
        self.answerList = []
        self.inputBoxList = []
        self.submitButton = QPushButton("Submit", self)
        self.returnButton = QPushButton("Return", self)
        layout.addWidget(QLabel("Please enter answers for this tutorial:"))

        users_ref = db.collection(u'tutorials')
        users = users_ref.get()
        for user in users:
            if(user.to_dict()['subject']==self.subject):
                self.questionList = user.to_dict()['questionList']
                self.answerList = user.to_dict()['answerList']
                break


        for i in range(len(self.questionList)):
            # add question
            layout.addWidget(QLabel("Question " + str(i+1)))
            layout.addWidget(QLabel(self.questionList[i]))

            # add answer input box
            layout.addWidget(QLabel("Answer " + str(i+1)))
            self.inputBoxList.append(QLineEdit())
            layout.addWidget(self.inputBoxList[i])
            layout.addWidget(self.emptyline)

        layout.addWidget(self.submitButton)
        layout.addWidget(self.returnButton)

        self.submitButton.clicked.connect(self.submitAnswer)
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

    def submitAnswer(self):
        userAnswerList = []
        for i in range(len(self.questionList)):
            userAnswerList.append(self.inputBoxList[i].text())

        # to-do
        # pass the answer by student to database
        # or pass the answer to this module first, then check answer?
        message = ""
        marks = 0
        for userAns,correctAns in zip(userAnswerList, self.answerList):
            message += "Your answer: "+userAns+" Correct answer: "+correctAns
            if(userAns == correctAns):
                marks += 1
                message += "  Correct!"
            else:
                message += "  Wrong"

            message += "\n"
        
        message += "\nTotal mark >> "+str(marks)+"/"+str(len(self.questionList))
        result = QMessageBox.question(self, "Result", message, QMessageBox.Ok)
        self.returnPreviousWindow()

    def returnPreviousWindow(self):
        self.newWindow = StuViewTutorial.StuViewTutorial(self.username,self.subject)
        self.newWindow.show()
        self.close()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = StudentAttemptFiB()
    sys.exit(App.exec())
