from PyQt5.QtWidgets import QLineEdit, QMainWindow, QFrame, QPushButton, QWidget, QApplication, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont, QColor
from PyQt5 import QtCore 
import sys
from backend import *

class codesColor(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.cWidget()
        self.UI_()
        self.buttons()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Colors')
        self.setStyleSheet("background-color:#F5F5DC;")
        self.show()
    
    def cWidget(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

    def UI_(self):
        self.frame_gen = QFrame(self.centralWidget)
        self.frame_gen.setFrameShape(QFrame.StyledPanel)
        self.frame_gen.setFrameShadow(QFrame.Raised)
        self.hlayout = QHBoxLayout(self.centralWidget)
        self.hlayout.addWidget(self.frame_gen)
        self.hlayout2 = QHBoxLayout(self.frame_gen)

    def buttons(self):
        self.show_ = QPushButton(self.frame_gen)
        self.show_.setText('Show')
        self.show_.setFont(QFont('Arial', 20))
        self.show_.setStyleSheet("background-color:#808080;")
        self.show_.clicked.connect(self.showed)
        self.hlayout2.addWidget(self.show_)
        self.lineedit = QLineEdit(self.frame_gen)
        self.lineedit.setFont(QFont('Arial', 20))
        self.lineedit.setStyleSheet("background-color:#808080;")
        self.hlayout2.addWidget(self.lineedit)
        self.closed = QPushButton(self.frame_gen)
        self.closed.setText('Close')
        self.closed.setFont(QFont('Arial', 20))
        self.closed.setStyleSheet("background-color:#808080;")
        self.hlayout2.addWidget(self.closed)

    def showed(self):
        text = value_resistance(self.lineedit.text())
        msgBox = QMessageBox()
        msgBox.setStyleSheet("QLabel{color: red; font-size: 20px; font-family: Arial; font-weight: bold;}")
        ans = msgBox.information(None, 'Result', text, QMessageBox.Ok)
        



def main():
    app = QApplication(sys.argv)
    ex = codesColor()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()