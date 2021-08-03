import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.Qt import QIcon
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("myomock1.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.mystate = 0
        self.pb.clicked.connect(self.myclick)
        
#     def firstEvent(self):
#         self.pb.setIcon(QIcon('1.png'))
#         self.pb.clicked.connect(self.secondevent)
# 
#     def secondevent(self):    
#         self.pb.setIcon(QIcon('2.png'))
#         self.pb.clicked.connect(self.thirdevent)
#         
#     def thirdevent(self):    
#         self.pb.setIcon(QIcon('0.png'))
#         self.pb.clicked.connect(self.firstEvent)
        
    def myclick(self):
        if self.mystate == 0:
            self.mystate = 1
        elif self.mystate ==1:
            self.mystate = 2
        else :
            self. mystate = 0
             
        rMyIcon = QtGui.QPixmap(str(self.mystate)+".png");
        self.pb.setIcon(QtGui.QIcon(rMyIcon))
        
    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()