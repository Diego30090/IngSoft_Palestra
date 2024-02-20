import sys
from PyQt5.uic import loadUi
from Boundaries.GestioneUtente import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController


class ElencoPagamenti(QWidget):
    def __init__(self, accountController: accountController):
        self.userController = accountController
        self.username = accountController.utente.getUsername()
        super(ElencoPagamenti, self).__init__()
        loadUi("visualizzaPagamenti.ui", self)
        pass

    def insertUi(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ElencoPagamenti(accountController=accountController('root1', 'pwd'))
    ex.show()
    sys.exit(app.exec_())

