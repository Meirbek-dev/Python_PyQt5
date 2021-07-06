import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('solve.ui', self)
        self.setWindowIcon(QtGui.QIcon('logo.jpg'))
        self.label_primer.setPixmap(QPixmap('1variant.png'))
        self.label_primer.setScaledContents(True)
        self.pushButton_solve.clicked.connect(self.solve)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_exit.clicked.connect(self.close)

    def solve(self):
        try:
            x = float(self.lineEdit_X.text())
            if x <= 5:
                a = float(self.lineEdit_A.text())
                b = float(self.lineEdit_B.text())
                c = float(self.lineEdit_C.text())
                d = float(self.lineEdit_D.text())
                y = (a ** 2 * c + b ** 2 - d) / x
            else:
                y = x ** 2 + 5
            self.label_answer.setText('Ответ: ' + str(format(y, '.2f')))
        except:
            self.label_answer.setStyleSheet("color: red;")
            self.label_answer.setText('Ошибка!')

    def clear(self):
        self.lineEdit_X.setText('')
        self.lineEdit_A.setText('')
        self.lineEdit_B.setText('')
        self.lineEdit_C.setText('')
        self.lineEdit_D.setText('')
        self.label_answer.setStyleSheet("color: black;")
        self.label_answer.setText('Ответ: ')


app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec_())
