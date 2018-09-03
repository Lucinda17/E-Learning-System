#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QDesktopWidget, QLineEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import sys

class StudentProfile(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Student Profile Page"
        self.width = 0
        self.height = 0
        self.top = 0
        self.left = 0

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

    def addComponents(self):
        pass


    '''
    # To open new window
    def Clicked(self):
        
        self.nd = StudentProfile()
        self.nd.show()
        self.hide()
    '''

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = StudentProfile()
    sys.exit(app.exec_())