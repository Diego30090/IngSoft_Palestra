import sys
from views import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget


class LoginView(QWidget):

    def __init__(self):
        super().__init__()
        # Window settings
        self.title = 'Login'
        self.width = 300
        self.height = 150
        # Item settings
        self.login_button = None
        self.pass_text = None
        self.user_text = None
        self.pass_label = None
        self.user_label = None
        self.error_label = None
        # item initializers and item commands
        self.login_ui()
        self.instruction()

    def login_ui(self):
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        self.user_label = QLabel('Username', self)
        self.user_label.move(60, 30)

        self.pass_label = QLabel('Password', self)
        self.pass_label.move(60, 60)

        self.error_label = QLabel('', self)
        self.error_label.move(70, 80)
        self.error_label.setFixedWidth(300)
        self.error_label.setStyleSheet("color:red")

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

    def instruction(self):
        self.login_button.clicked.connect(self.login_butt_clicked)

    def login_butt_clicked(self):
        user = self.user_text.text()
        pwd = self.pass_text.text()
        if user != '' and pwd != '':
            flag = db.login(user, pwd)
            if flag:
                self.toMainMenu(user)

            else:
                err_text = "Errore: Credenziali non corrette!"
                self.error_label.setText(err_text)
        else:
            err_text = "Errore: inserisci i valori di login!"
            self.error_label.setText(err_text)

    def toMainMenu(self, user):
        self.screen = menu.MainMenu(username=user)
        self.screen.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginView()
    sys.exit(app.exec_())
