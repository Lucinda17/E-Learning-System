
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

import sys
import StudentAttemptTut

class StudentAttemptMCQ(QWidget):
    def __init__(self):
        # set window title and sizes
        super().__init__()
        self.title = "Student: Attempt MCQ Question"

        self.subjectName = "English"
        self.subjectCode = "TCP2011"
        self.tutorialNumber = "Tutorial 1"
        self.numOfQuestion = 4
        self.emptyline = QLabel("")

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.screenSize = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.setGeometry(0, 0, self.screenSize.width(), self.screenSize.height())
        
        # create BoxLayouts
        widget = QWidget()
        layout = QVBoxLayout()

        # add components into window
        # to-do: import question and answer from tutorial database
        self.questionList = ["3+3=", "2+2=", "1+1=", "10+5"]
        self.answerList = [6, 4, 2, 15]
        self.inputBoxList = []
        self.submitButton = QPushButton("Submit", self)
        self.returnButton = QPushButton("Return", self)
        layout.addWidget(QLabel("Please enter answers for this tutorial:"))

        self.question1Option = [2, 4, 6 ,8]
        self.question2Option = [2, 4, 6 ,8]
        self.question3Option = [2, 4, 5 ,6]
        self.question4Option = [12, 13, 14 ,15]

        self.radioButtons1 = []
        self.radioButtons2 = []
        self.radioButtons3 = []
        self.radioButtons4 = []
        self.radioButtons = [self.radioButtons1, self.radioButtons2, self.radioButtons3, self.radioButtons4]

        for i in range(4):
            self.radioButtons1.append(QRadioButton(str(self.question1Option[i]), self))
            self.radioButtons2.append(QRadioButton(str(self.question2Option[i]), self))
            self.radioButtons3.append(QRadioButton(str(self.question3Option[i]), self))
            self.radioButtons4.append(QRadioButton(str(self.question4Option[i]), self))

        for i in range(self.numOfQuestion):
            # add question
            layout.addWidget(QLabel("Question " + str(i+1)))
            layout.addWidget(QLabel(self.questionList[i]))
            
            # add radio buttons
            layout.addWidget(self.createAnswerGroup(self.radioButtons, i))
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
                         
    def createAnswerGroup(self, radioButtons, questionNum):
        groupBox = QGroupBox()
        vBox = QVBoxLayout()

        for i in range(4):
            vBox.addWidget(radioButtons[questionNum][i])
        groupBox.setLayout(vBox)
        return groupBox
            
        
    def submitAnswer(self):
        userAnswerList = []

        for i in range(self.numOfQuestion):
            userAnswerList[i] = self.inputBoxList[i].text()

        # to-do
        # pass the answer by student to database
        # or pass the answer to this module first, then check answer?

    def returnPreviousWindow(self):
        self.newWindow = StudentAttemptTut.StudentAttemptTut()
        self.newWindow.show()
        self.close()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = StudentAttemptMCQ()
    sys.exit(App.exec())
