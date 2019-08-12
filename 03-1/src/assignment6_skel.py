import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'test3_4_1.dat'
        self.scoredb = []
        self.readScoreDB()
        #self.showScoreDB()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.lb1 = QLabel("Name:", self)
        self.lb1.move(15,10)
        self.ed1 = QLineEdit(self) #
        self.ed1.move(60,10)
        self.lb2 = QLabel("Age:", self)
        self.lb2.move(190,10)
        self.ed2 = QLineEdit(self) #
        self.ed2.move(220,10)
        self.lb3 = QLabel("Score:", self)
        self.lb3.move(350,10)
        self.ed3 = QLineEdit(self) #
        self.ed3.move(400,10)
        self.lb4 = QLabel("Amount:", self)
        self.lb4.move(170,35)
        self.ed4 = QLineEdit(self) #
        self.ed4.move(220,35)
        self.lb5 = QLabel("Key:", self)
        self.lb5.move(350,35)
        self.cb1 = QComboBox(self) #
        self.cb1.addItems(["Name", "Age", "Score"])
        self.cb1.move(400,35)
        self.pb1=QPushButton("Add", self)
        self.pb1.move(20,60)
        self.pb1.clicked.connect(self.buttonClicked) # 수정
        self.pb2=QPushButton("Del", self)
        self.pb2.move(80,60)
        self.pb2.clicked.connect(self.buttonClicked)
        self.pb3=QPushButton("Find", self)
        self.pb3.move(140,60)
        self.pb3.clicked.connect(self.buttonClicked)
        self.pb4=QPushButton("Inc", self)
        self.pb4.move(200,60)
        self.pb4.clicked.connect(self.buttonClicked)
        self.pb5=QPushButton("show", self)
        self.pb5.move(260,60)
        self.pb5.clicked.connect(self.buttonClicked)
        self.te = QTextEdit(" ",self)
        self.te.move(20, 100)
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        for p in sorted(self.scoredb, key=lambda person: person[self.cb1.currentText()]): #여기서 int로 들어올때 문제 발생 --> 하나가 인트로 저장 되어 있음..
            #print(type(p['Age'])) - debug
            for attr in sorted(p):
                self.te.append(attr + "=" + str(p[attr])) # 수정 int를 str로 캐스팅
            self.te.append("\n")

        # button의 value를 읽어와 케이스 판단, qlineedit의 값들을 읽어오고 입력된 명령을 수행
    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == "Add":
            record = {'Name':str(self.ed1.text()), 'Age':int(self.ed2.text()), 'Score':int(self.ed3.text())}
            self.scoredb += [record]
        elif key == "Del":
            for p in self.scoredb[:]: # 수정
                #print(type(p)) --> 계속 TypeError: string indices must be integers 가 남: 디버깅 용도, 데이터에서 dict이 아닌 str이 있었음
                if p['Name'] == self.ed1.text():
                    self.scoredb.remove(p)
        elif key == "Find":
            for p in self.scoredb:
                if p['Name'] == self.ed1.text():
                    for attr in p:
                        self.te.append(attr + "=" + str(p[attr])) #QTextEdit에 출력 할 수 있게 수정 해야함
                    self.te.append("\n")

        elif key == "Inc":
            for p in self.scoredb:
                if p['Name'] == self.ed1.text():
                    p['Score'] = int(p['Score']) + int(self.ed4.text()) # 수정, Score를 int로 받음

        elif key == "show":
            #sortKey ='Name' if len(parse) == 1 else parse[1]
            self.showScoreDB()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
