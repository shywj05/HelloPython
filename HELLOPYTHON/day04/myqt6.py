import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt6.ui")[0]

f
# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pb.clicked.connect(self.myclick)
# 첫수부터 n수 까지 더하기
    def myclick(self): 
        a = self.le1.text()
        int_a = int(a)
        b = self.le2.text()
        int_b = int(b)
        
        c = 0
        for i in range(int_a,int_b+1):
            c += i
        
        self.le3.setText(str(c))
        
if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()