import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Login'
        self.width = 300
        self.height = 150
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        user_label = QLabel('Username', self)
        user_label.move(60, 30)

        pass_label = QLabel('Password', self)
        pass_label.move(60, 60)

        user_text = QLineEdit(self)
        user_text.move(130, 35)
        user_text.setFixedHeight(20)

        pass_text = QLineEdit(self)
        pass_text.move(130, 65)
        pass_text.setEchoMode(QLineEdit.Password)
        pass_text.setFixedHeight(20)

        login_button =QPushButton("Login",self)
        login_button.setFixedHeight(25)
        login_button.move(100, 100)
        login_button.setObjectName('asd')

        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())