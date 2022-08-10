import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget


class LoginUi(QWidget):
    # class LoginUi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.login_button = None
        self.pass_text = None
        self.user_text = None
        self.pass_label = None
        self.user_label = None
        self.title = 'Login'
        self.width = 300
        self.height = 150
        self.init_ui()
        self.login_button.clicked.connect(self.login_clicked)

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        self.user_label = QLabel('Username', self)
        self.user_label.move(60, 30)

        self.pass_label = QLabel('Password', self)
        self.pass_label.move(60, 60)

        self.user_text = QLineEdit(self)
        self.user_text.move(130, 30)
        self.user_text.setFixedHeight(20)

        self.pass_text = QLineEdit(self)
        self.pass_text.move(130, 60)
        self.pass_text.setEchoMode(QLineEdit.Password)
        self.pass_text.setFixedHeight(20)

        self.login_button = QPushButton("Login", self)
        self.login_button.setFixedHeight(25)
        self.login_button.move(100, 100)
        self.show()

    def login_clicked(self):
        print(self.user_text.text())
        print(self.pass_text.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginUi()
    sys.exit(app.exec_())
