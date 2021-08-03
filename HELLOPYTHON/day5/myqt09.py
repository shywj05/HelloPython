import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("myqt09.ui")[0]


class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        a = self.le1.text()
        b = self.le2.text()
        c = self.le3.text()
        
        rnd = random.random()
        
        if rnd > 0.66:
            b = "가위"
        elif rnd > 0.33:
            b = "바위"
        else:
            b = "보"
        
        if a == b:
            c = "비김"
        elif a == "가위" and b == "보" or a == "바위" and b == "가위" or a == "보" and b == "바위":
            c = "이김"
        else:
            c = "짐"
        
        self.le2.setText(b)
        self.le3.setText(c)


if __name__ == "__main__":
    app = QApplication(sys.argv) 

    myWindow = WindowClass() 

    myWindow.show()

    app.exec_()
