import sys
from PyQt5.uic import loadUi
from Boundaries.GestioneUtente import mainMenu as menu
from PyQt5.QtWidgets import QApplication, QWidget
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController
from Boundaries.GestionePagamenti import creaPagamentoView as creapag
from Boundaries.GestionePagamenti import visualizzaPagamento as vispag

class ElencoPagamenti(QWidget):
    def __init__(self, accountController: accountController):
        self.userController = accountController
        self.username = accountController.utente.getUsername()
        super(ElencoPagamenti, self).__init__()
        loadUi("../GestionePagamenti/elencoPagamenti.ui", self)
        self.instruction()

    def instruction(self):
        self.backButton.clicked.connect(self.toMainView)
        self.creaPagamentoButton.clicked.connect(self.toCreaPagamento)
        #self.visualizzaPagamentoButton.clicked.connect(self.toVisualizzaPagamento)

    def listaPagamenti(self):
        #funzione che mostra la lista dei pagamenti nella tabella principale
        pass

    def toVisualizzaPagamento(self):
        #Va alla vista della visualizzazione dei pagamenti se è stato selezionato un evento
        self.screen = vispag.visualizzaPagamento(accountController=self.userController)
        self.screen.show()
        self.close()
        pass

    def toCreaPagamento(self):
        #Va alla vista di creazione del pagamento
        self.screen = creapag.CreaPagamento(accountController=self.userController)
        self.screen.show()
        self.close()
        pass

    def toMainView(self):
        self.screen = menu.MainMenu(userController=self.userController)
        self.screen.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ElencoPagamenti(accountController=accountController('root1', 'pwd'))
    ex.show()
    sys.exit(app.exec_())

