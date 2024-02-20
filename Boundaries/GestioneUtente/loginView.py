import sys

from PyQt5.uic import loadUi

from Boundaries.GestioneUtente import mainMenu as menu
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as controller


class LoginView(QWidget):
    def __init__(self, ):
        super(LoginView, self).__init__()
        loadUi("../GestioneUtente/Login.ui", self)
        self.instruction()
        self.show()

    def instruction(self):
        self.login_button.clicked.connect(self.loginButtonClicked)

    def loginButtonClicked(self):
        userController = controller(self.user_text.text(), self.pass_text.text())
        if userController.utente.getUsername() != '' and userController.utente.getPassword() != '':
            flag = userController.login()
            if flag:
                self.toMainMenu(userController)
            else:
                err_text = "Errore: Credenziali non corrette!"
                self.error_label.setText(err_text)
        else:
            err_text = "Errore: inserisci i valori di login!"
            self.error_label.setText(err_text)

    def toMainMenu(self, userController):
        self.screen = menu.MainMenu(userController)
        self.screen.show()
        self.close()


class LoginViewOld(QWidget):

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
        self.loginUi()
        self.instruction()

    def loginUi(self):
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
        self.login_button.clicked.connect(self.loginButtonClicked)

    def loginButtonClicked(self):
        userController = controller(self.user_text.text(), self.pass_text.text())

        if userController.utente.getUsername() != '' and userController.utente.getPassword() != '':
            flag = userController.login()
            if flag:
                self.toMainMenu(userController)


            else:
                err_text = "Errore: Credenziali non corrette!"
                self.error_label.setText(err_text)
        else:
            err_text = "Errore: inserisci i valori di login!"
            self.error_label.setText(err_text)

    def toMainMenu(self, userController):
        self.screen = menu.MainMenu(userController)
        self.screen.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginView()
    sys.exit(app.exec_())
