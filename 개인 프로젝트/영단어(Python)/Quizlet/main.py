import sys
from crawl import findWords
from output import quizletCrawl
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QVBoxLayout,QLabel, QLineEdit,QHBoxLayout
from PyQt5.QtGui import QIcon,QPixmap

class MyApp(QWidget):
    
    def submit(self):
        print(findWords(self.le.text()))

    def extract(self):
        print(quizletCrawl(self.le.text()))

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        self.btn1 = QPushButton(self)
        self.btn1.setText('만들기')
        self.btn1.clicked.connect(self.submit)
        self.btn2 = QPushButton(self)
        self.btn2.setText('추출하기')
        self.btn2.clicked.connect(self.extract)
        self.le = QLineEdit(self)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.le)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.le)
        vbox.addStretch(0.2)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.setLayout(hbox)
        
        self.setWindowTitle('Quizlet')
        self.setWindowIcon(QIcon('C:/Users/dahyun/Desktop/Quizlet/Images/logo.png'))
        self.move(300, 300)
        self.resize(400, 100)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
