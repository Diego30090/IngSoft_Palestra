import sys
from PyQt5.uic import loadUi
from Boundaries.GestioneUtente import mainMenu as menu
from PyQt5.QtWidgets import QApplication, QWidget
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController
from Boundaries.GestionePagamenti import creaPagamentoView as creapag
from Boundaries.GestionePagamenti import elencoPagamenti as elepag

class visualizzaPagamento(QWidget):
    def __init__(self, accountController: accountController):
        self.userController = accountController
        self.username = accountController.utente.getUsername()
        super(visualizzaPagamento, self).__init__()
        loadUi("../GestionePagamenti/VisualizzaPagamento.ui", self)
        self.instruction()

    def instruction(self):
        self.backButton.clicked.connect(self.toElencoPagamenti)
        pass

    def toModificaPagamento(self):
        #Va alla vista della visualizzazione dei pagamenti
        print(f"funzione che porta alla vista di modifica del pagamento")
        pass

    def toElencoPagamenti(self):
        self.screen = elepag.ElencoPagamenti(accountController=self.userController)
        self.screen.show()
        self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = visualizzaPagamento(accountController=accountController('root1', 'pwd'))
    ex.show()
    sys.exit(app.exec_())
