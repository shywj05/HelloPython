import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.Qt import QIcon
from PyQt5.QtCore import *
from notebook.services.contents.handlers import _checkpoint_id_regex

import cx_Oracle


def getMax():
    conn=cx_Oracle.connect("python/python@localhost:1521/xe")
    cs = conn.cursor()
    rs = cs.execute( "select nvl(max(pan)+1,1) as maxpan from omok")
    max_pan = 0
    for record in rs:
        max_pan = int(record[0])
    cs.close()
    conn.close()
    return max_pan

def writeHistroy(pan, history, win):
    conn=cx_Oracle.connect("python/python@localhost:1521/xe")
    cs = conn.cursor()
    
    sql = "insert into omok(pan, pseq, history, win) values (:1,:2,:3,:4)"
    
    for i,h in enumerate(history):
        cs.execute(sql,(pan, i, h, win))
    
    conn.commit()    
    cs.close()
    conn.close()



form_class = uic.loadUiType("myomock2.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.mystate = 0
        self.pb.clicked.connect(self.myclick)
        self.flag_wb = True
        self.flag_ing = True
        self.history = []
        self.pb2d = []
        self.arr2d = [
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0]
            ]
        
        for i in range(10):
            line = []
            for j in range(10):
                temp = QPushButton("", self)
                temp.clicked.connect(self.myclick)
                temp.setIcon(QIcon("0.png"))
                temp.setIconSize(QSize(50,50))
                temp.setGeometry(j*40, i*40, 40, 40)
                temp.setToolTip(str(i)+","+str(j))
                line.append(temp)
            self.pb2d.append(line)
        
        self.pb.clicked.connect(self.myreset)    
        self.myrender()
            
    
    def myreset(self):
        print("클릭")
        self.flag_wb = True
        self.flag_ing = True
        for i in range(10):
            for j in range(10):
                self.arr2d[i][j] = 0
        
        self.history.clear()
        self.myrender()
        
        
        
        
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QIcon("0.png")) 
                if self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QIcon("1.png"))
                if self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QIcon("2.png"))
            
         
#         self.button = QtGui.QPushButton('', self)
#         self.button.clicked.connect(self.handleButton)
#         self.button.setIcon(QtGui.QIcon('myImage.jpg'))
        
    def myclick(self):
#         print(self.sender().toolTip()) #sender는 보내는거?
        if self.flag_ing == False :
            return 
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        int_i = int(arr_ij[0])
        int_j = int(arr_ij[1])
        
        if self.arr2d[int_i][int_j] > 0:
            return
        
        int_stone = 0
        
        if self.flag_wb :
            self.arr2d[int_i][int_j] = 1
            int_stone = 1
        else :
            self.arr2d[int_i][int_j] = 2
            int_stone = 2
            
        up = self.getUP(int_i, int_j, int_stone)
        dw = self.getDW(int_i, int_j, int_stone)
        
        le = self.getLE(int_i, int_j, int_stone)
        ri = self.getRI(int_i, int_j, int_stone)
        
        ul = self.getUL(int_i, int_j, int_stone)
        ur = self.getUR(int_i, int_j, int_stone)
        
        dl = self.getDL(int_i, int_j, int_stone)
        dr = self.getDR(int_i, int_j, int_stone)
        print(up)
        print(dw)
        print(le)
        print(ri)
        print(ul)
        print(ur)
        print(dl)
        print(dr)
        
        d1 = up + dw + 1
        d2 = dl + ur + 1
        d3 = le + ri + 1
        d4 = ul + dr + 1
        
        self.myrender()
        
        self.history()
        
        str100 = "";
        for i in range(10):
            for j in range(10):
                str100 += str(self.arr2d[i][j])
        self.history.append(str100)
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            self.flag_ing = False
            win = 0
            if self.flag_wb :
                QMessageBox.about(self, "오목게임", "백돌이 이겼습니다.")
                win = 1
            else :
                QMessageBox.about(self, "오목게임", "흑돌이 이겼습니다.")
                win = 2
            
            max_pan = getMax()
            writeHistroy(max_pan,self.history,win)
                
           
        self.flag_wb = not self.flag_wb
        
    def getUP(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_i += -1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else :
                    return count
        except:
            return count
        
    def getDW(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_i += 1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else :
                    return count
        except:
            return count
        
    def getLE(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_j += -1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else :
                    return count
        except:
            return count
        
    def getRI(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_j += 1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else :
                    return count
        except:
            return count
        
    def getUL(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_i += -1
                int_j += -1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else :
                    return count
        except:
            return count
        
    def getUR(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_i += -1
                int_j += 1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else :
                    return count
        except:
            return count
        
    def getDL(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_i += 1
                int_j += -1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else :
                    return count
        except:
            return count
        
    def getDR(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_i += 1
                int_j += 1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else :
                    return count
        except:
            return count
        
        
    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()