import sys
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtGui

from Boundaries.GestioneUtente import mainMenu as menu
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController
from Controller.GestionePagamenti.GestorePagamenti import GestorePagamenti
from Boundaries.GestionePagamenti import creaPagamentoView as creapag
from Boundaries.GestionePagamenti import visualizzaPagamento as vispag

class ElencoPagamenti(QWidget):
    def __init__(self, accountController: accountController):
        self.userController = accountController
        self.username = accountController.utente.getUsername()
        self.listaPagamenti = []
        super(ElencoPagamenti, self).__init__()
        loadUi("../GestionePagamenti/elencoPagamenti.ui", self)
        self.instruction()
        self.populatePagamentiTable()

    def instruction(self):
        self.backButton.clicked.connect(self.toMainView)
        self.creaPagamentoButton.clicked.connect(self.toCreaPagamento)
        #self.visualizzaPagamentoButton.clicked.connect(self.toVisualizzaPagamento)

    def populatePagamentiTable(self):
        #funzione che mostra la lista dei pagamenti nella tabella principale
        pagamentiController = GestorePagamenti()
        self.listaPagamenti = pagamentiController.getListaPagamentiCompleta()
        currentRow = 1
        self.tabellaPagamenti.setRowCount(len(self.listaPagamenti))
        for row in range(len(self.listaPagamenti)):
            self.tabellaPagamenti.setItem(row,0, QTableWidgetItem(str(self.listaPagamenti[row].id)))
            self.tabellaPagamenti.setItem(row, 1, QTableWidgetItem(str(self.listaPagamenti[row].timestamp)))
            self.tabellaPagamenti.setItem(row, 2, QTableWidgetItem(f"{str(self.listaPagamenti[row].importo)} €"))
            if self.listaPagamenti[row].tipologia == 'pagamento' or self.listaPagamenti[row].tipologia == 'multa':
                self.tabellaPagamenti.setItem(row, 3, QTableWidgetItem(str('Non Pagato')))
            else:
                self.tabellaPagamenti.setItem(row, 3, QTableWidgetItem(str('Pagato')))
            self.tabellaPagamenti.setItem(row, 4, QTableWidgetItem(str(self.listaPagamenti[row].dettaglio)))


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

