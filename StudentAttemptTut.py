
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

import sys
import StudentAttemptFiB
import StudentAttemptMCQ

class StudentAttemptTut(QWidget):
    def __init__(self):
        # set window title and sizes
        super().__init__()
        self.title = "Student: View Tutorials"
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 200
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # create vBoxLayout
        self.vBoxLayout = QVBoxLayout()
        self.hBoxLayout1 = QHBoxLayout()
        self.hBoxLayout2 = QHBoxLayout()
        self.hBoxLayout3 = QHBoxLayout()
        self.hBoxLayout4 = QHBoxLayout()

        # create components in window

        # to-do: retrieve subject type from database
        # to-do: retrieve tutorials from database
        # to-do: retrieve tutorials type from database
        # self.subject = db.
        # for i in range(xxx): addWidget(QLabel(tutorialnumber))
        self.title = "Subject: "
        
        # stub
        self.subject = "English"
        self.caption1 = QLabel(self.title + self.subject)
        self.emptyline = QLabel("")

        self.tut1 = QLabel("Tutorial 1")
        self.tut2 = QLabel("Tutorial 2")
        self.tut3 = QLabel("Tutorial 3")
        self.tut4 = QLabel("Tutorial 4")

        self.tut1type = QLabel("Fill in the Blank")
        self.tut2type = QLabel("Multiple Choice Question")
        self.tut3type = QLabel("Fill in the Blank")
        self.tut4type = QLabel("Multiple Choice Question")

        self.attemptButton1 = QPushButton("Attempt", self)
        self.attemptButton2 = QPushButton("Attempt", self)
        self.attemptButton3 = QPushButton("Attempt", self)
        self.attemptButton4 = QPushButton("Attempt", self)
        self.viewButton1 = QPushButton("View Result", self)
        self.viewButton2 = QPushButton("View Result", self)
        self.viewButton3 = QPushButton("View Result", self)
        self.viewButton4 = QPushButton("View Result", self)

        # add components into window
        self.vBoxLayout.addWidget(self.caption1)
        self.vBoxLayout.addWidget(self.emptyline)
        
        self.hBoxLayout1.addWidget(self.tut1)
        self.hBoxLayout1.addWidget(self.tut1type)
        self.hBoxLayout1.addWidget(self.attemptButton1)
        self.hBoxLayout1.addWidget(self.viewButton1)
        self.attemptButton1.clicked.connect(lambda: self.attemptQuestion(self.tut1, self.tut1type))
        self.viewButton1.clicked.connect(lambda: self.viewResult(self.tut1))
        
        self.hBoxLayout2.addWidget(self.tut2)
        self.hBoxLayout2.addWidget(self.tut2type)
        self.hBoxLayout2.addWidget(self.attemptButton2)
        self.hBoxLayout2.addWidget(self.viewButton2)
        self.attemptButton2.clicked.connect(lambda: self.attemptQuestion(self.tut2, self.tut2type))
        self.viewButton2.clicked.connect(lambda: self.viewResult(self.tut2))
        
        self.hBoxLayout3.addWidget(self.tut3)
        self.hBoxLayout3.addWidget(self.tut3type)
        self.hBoxLayout3.addWidget(self.attemptButton3)
        self.hBoxLayout3.addWidget(self.viewButton3)
        self.attemptButton3.clicked.connect(lambda: self.attemptQuestion(self.tut3, self.tut3type))
        self.viewButton3.clicked.connect(lambda:self.viewResult(self.tut3))
        
        self.hBoxLayout4.addWidget(self.tut4)
        self.hBoxLayout4.addWidget(self.tut4type)
        self.hBoxLayout4.addWidget(self.attemptButton4)
        self.hBoxLayout4.addWidget(self.viewButton4)
        self.attemptButton4.clicked.connect(lambda: self.attemptQuestion(self.tut4, self.tut4type))
        self.viewButton4.clicked.connect(lambda: self.viewResult(self.tut4))

        self.vBoxLayout.addLayout(self.hBoxLayout1)
        self.vBoxLayout.addLayout(self.hBoxLayout2)
        self.vBoxLayout.addLayout(self.hBoxLayout3)
        self.vBoxLayout.addLayout(self.hBoxLayout4)
        self.setLayout(self.vBoxLayout)
        self.show()

    def attemptQuestion(self, tutNum, tutType):
        tutorialType = tutType.text()
        
        if tutorialType == 'Fill in the Blank':
            # stub only
            '''
            self.newWindow = StudentAttemptFiB.StudentAttemptFiB(self.subject)
            self.newWindow.show()
            self.close()
            '''
            self.newWindow = StudentAttemptFiB.StudentAttemptFiB()
            self.newWindow.show()
            self.close()

            # to implement this when added firebase
            # self.newWindow = StudentAttemptFiB.StudentAttemptFiB(self.subject, tutNum)
        else:
            # stub only
            '''
            self.newWindow = StudentAttemptMCQ.StudentAttemptMCQ(self.subject, tutNum)
            self.newWindow.show()
            self.close()
            '''
            self.newWindow = StudentAttemptMCQ.StudentAttemptMCQ()
            self.newWindow.show()
            self.close()
            
            # to implement this when added firebase
            # self.newWindow = StudentAttemptFiB.StudentAttemptFiB(self.subject, tutNum)

    def viewResult(self, tutNum):
        
            # stub only
            '''
            self.newWindow = StudentViewResult.StudentViewResult(self.subject, tutNum)
            self.newWindow.show()
            self.close()
            '''

            # to implement this when added firebase
            # self.newWindow = StudentAttemptFiB.StudentAttemptFiB(self.subject, tutNum)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = StudentAttemptTut()
    sys.exit(App.exec())
