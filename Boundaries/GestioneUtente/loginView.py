import sys

from PyQt5.uic import loadUi

from Boundaries.GestioneUtente import mainMenu as menu
from PyQt5.QtWidgets import QApplication, QWidget
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginView()
    sys.exit(app.exec_())
