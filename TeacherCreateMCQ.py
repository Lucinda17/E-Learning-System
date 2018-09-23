# this module will be called by TeacherCreateTut.py
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

import sys
import TeacherCreateTut

class TeacherCreateMCQ(QWidget):
    def __init__(self, subjectName, subjectCode, tutorialNumber, numOfQuestion):
        # set window title and sizes
        super().__init__()
        self.title = "Teacher: Create MCQ Question"

        self.subjectName = subjectName
        self.subjectCode = subjectCode
        self.tutorialNumber = tutorialNumber
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
        
        for i in range(self.numOfQuestion):
            # add question
            layout.addWidget(QLabel("Question " + str(i+1)))
            self.inputBoxList1.append(QLineEdit())
            layout.addWidget(self.inputBoxList1[i])

            # add answer
            layout.addWidget(QLabel("Answers for 4 options"))
            for j in range(4):
                self.inputBoxList2.append(QLineEdit())
                layout.addWidget(QLineEdit())
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
            questionList[i] = self.inputBoxList1[i].text()
        for j in range(self.numOfQuestion * 4):
            answerList[i] = self.inputBoxList2[j].text()
            
        # to-do
        # pass the question into database
        # important note:
        # example:
        # answerList[0] to answerList[3] is for Question 1
        # answerList[4] to answerList[7] is for Question 2
        # and so on....

    def returnPreviousWindow(self):
        self.newWindow = TeacherCreateTut.TeacherCreateTut()
        self.newWindow.show()
        self.close()
        
        # add code to move to previous window once clicked
        # to-do

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = TeacherCreateMCQ()
    sys.exit(App.exec())
