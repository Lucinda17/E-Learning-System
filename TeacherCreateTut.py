
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

import sys

class TeacherCreateTut(QWidget):
    def __init__(self):
        # set window title and sizes
        super().__init__()
        self.title = "Teacher: Create Tutorial"
        self.left = 100
        self.top = 100
        self.width = 503
        self.height = 316

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # create vBoxLayout
        self.vBoxLayout = QVBoxLayout()

        # create components in window
        self.caption1 = QLabel("Please enter the following details to create a tutorial: ")
        self.emptyline = QLabel("")
        
        self.info1 = QLabel("Subject Name")
        self.info2 = QLabel("Subject Code")
        self.info3 = QLabel("Tutorial Number")
        self.info4 = QLabel("Tutorial Type")
        
        self.inputBox1 = QLineEdit()
        self.inputBox2 = QLineEdit()
        self.inputBox3 = QLineEdit()
        self.comboBox1 = QComboBox()
        self.comboBox1.addItem("Fill in the Blank")
        self.comboBox1.addItem("Multiple Choice Question")
        
        self.createButton = QPushButton("Create", self)
        self.returnButton = QPushButton("Return", self)

        # add components into window
        self.vBoxLayout.addWidget(self.caption1)
        self.vBoxLayout.addWidget(self.emptyline)
        self.vBoxLayout.addWidget(self.info1)
        self.vBoxLayout.addWidget(self.inputBox1)
        self.vBoxLayout.addWidget(self.info2)
        self.vBoxLayout.addWidget(self.inputBox2)
        self.vBoxLayout.addWidget(self.info3)
        self.vBoxLayout.addWidget(self.inputBox3)
        self.vBoxLayout.addWidget(self.info4)
        self.vBoxLayout.addWidget(self.comboBox1)
        self.vBoxLayout.addWidget(self.emptyline)
        self.vBoxLayout.addWidget(self.createButton)
        self.vBoxLayout.addWidget(self.returnButton)
        self.createButton.clicked.connect(self.createTutorial)
        self.returnButton.clicked.connect(self.returnPreviousWindow)

        self.setLayout(self.vBoxLayout)
        self.show()

    def createTutorial(self):
        subjectName = self.inputBox1.text()
        subjectCode = self.inputBox2.text()
        tutorialNumber = self.inputBox3.text()
        tutorialType = self.comboBox1.currentText()

        if tutorialType == 'Fill in the Blank':
            print('Created FiB')
            #TeacherCreateFiB()
        else:
            print('Created MCQ')
            #TeacherCreateMCQ()
                
        # add code to move to next window once created
        # to-do

    def returnPreviousWindow(self):

        #FunctionNameofPreviousWindow()
        print('return')
        
        # add code to move to previous window once clicked
        # to-do

App = QApplication(sys.argv)
window = TeacherCreateTut()
sys.exit(App.exec())
