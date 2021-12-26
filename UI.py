from PyQt5.QtWidgets import QLineEdit, QMainWindow, QFrame, QPushButton, QWidget, QApplication, QHBoxLayout, QMessageBox, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont, QColor, QPixmap
from PyQt5 import QtCore 
import sys
from backend import *

class codesColor(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.cWidget()
        self.UI_()
        self.setpixmap()
        self.buttons()
        

    def initUI(self):
        self.resize(276, 192)
        self.setWindowTitle('Colors')
        #self.setStyleSheet("background-color:#F5F5DC;")
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
        self.vlayout1 = QVBoxLayout(self.frame_gen)
        

    def setpixmap(self):
        self.frame1 = QFrame(self.frame_gen)
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.vlayout1.addWidget(self.frame1)

        self.hlayout3 = QHBoxLayout(self.frame1)

        self.label = QLabel(self.frame1)
        self.label.setText("")
        self.label.setPixmap(QPixmap("../../Downloads/loR-2.png"))
        self.label.setObjectName("label")
        self.hlayout3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

    def buttons(self):
        self.frame2 = QFrame(self.frame_gen)
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.frame2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.vlayout1.addWidget(self.frame2)

        self.show_ = QPushButton(self.frame2)
        self.show_.setText('Show')
        self.show_.setFont(QFont('Arial', 20))
        self.show_.setStyleSheet("background-color:#808080;")
        self.show_.clicked.connect(self.showed)

        self.lineedit = QLineEdit(self.frame2)
        self.lineedit.setFont(QFont('Arial', 20))
        self.lineedit.setStyleSheet("background-color:#808080;")

        self.hlayout = QHBoxLayout(self.frame2)
        self.hlayout.addWidget(self.show_)
        self.hlayout.addWidget(self.lineedit)
        
        

    def showed(self):
        try:
            text = value_resistance(self.lineedit.text())
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{color: red; font-size: 20px; font-family: Arial; font-weight: bold;}")
            ans = msgBox.information(None, 'Result', text, QMessageBox.Ok)
        except:
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{color: red; font-size: 20px; font-family: Arial; font-weight: bold;}")
            ans = msgBox.information(None, 'Result', 'Error', QMessageBox.Ok)
        



def main():
    app = QApplication(sys.argv)
    ex = codesColor()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()