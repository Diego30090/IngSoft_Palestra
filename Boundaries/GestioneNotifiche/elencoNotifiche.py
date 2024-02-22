import sys
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtGui

from Boundaries.GestioneUtente import mainMenu as menu
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController
from Controller.GestionePagamenti.GestorePagamenti import GestorePagamenti
from Boundaries.GestionePagamenti import creaPagamentoView as creapag
from Boundaries.GestionePagamenti import modificaPagamento as vispag

class ElencoNotifiche(QWidget):
    def __init__(self, accountController: accountController):
        self.userController = accountController
        self.username = accountController.utente.getUsername()
        super(ElencoNotifiche, self).__init__()
        loadUi("../GestioneNotifiche/VisualizzaNotifiche.ui", self)
        self.backButton.clicked.connect(self.toMainMenu)
    def toMainMenu(self):
        self.screen = menu.MainMenu(userController=self.userController)
        self.screen.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ElencoNotifiche(accountController=accountController('root1', 'pwd'))
    ex.show()
    sys.exit(app.exec_())
