import sys
from PyQt5.uic import loadUi
from Boundaries.GestioneUtente import mainMenu as menu
from PyQt5.QtWidgets import QApplication, QWidget
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController
from Boundaries.GestionePagamenti import elencoPagamenti as elepag

class CreaPagamento(QWidget):
    def __init__(self, accountController: accountController):
        self.userController = accountController
        self.username = accountController.utente.getUsername()
        super(CreaPagamento, self).__init__()
        loadUi("../GestionePagamenti/CreaPagamento.ui", self)
        self.instruction()

    def instruction(self):
        self.confermaCreazioneButton.clicked.connect(self.confermaPagamento)
        self.backButton.clicked.connect(self.toVisualizzaPagamento)
        pass

    def confermaPagamento(self):
        #funzione che conferma il pagamento
        pass

    def toVisualizzaPagamento(self):
        #funzione che riporta alla visualizzazione completa dei pagamenti
        self.screen = elepag.ElencoPagamenti(accountController=self.userController)
        self.screen.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CreaPagamento(accountController=accountController(username='root1',password='pwd'))
    ex.show()
    sys.exit(app.exec_())