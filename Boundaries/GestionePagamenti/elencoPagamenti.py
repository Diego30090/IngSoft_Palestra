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
        super(ElencoPagamenti, self).__init__()
        loadUi("../GestionePagamenti/elencoPagamenti.ui", self)
        self.instruction()
        self.populatePagamentiTable()

    def instruction(self):
        self.backButton.clicked.connect(self.toMainView)
        self.creaPagamentoButton.clicked.connect(self.toCreaPagamento)
        self.tabellaPagamenti.cellClicked.connect(self.clickedCell)

    def populatePagamentiTable(self):
        #funzione che mostra la lista dei pagamenti nella tabella principale
        pagamentiController = GestorePagamenti()
        listaPagamenti = pagamentiController.getListaPagamentiCompleta()
        self.tabellaPagamenti.setRowCount(len(listaPagamenti))
        for row in range(len(listaPagamenti)):
            self.tabellaPagamenti.setItem(row,0, QTableWidgetItem(str(listaPagamenti[row].id)))
            self.tabellaPagamenti.setItem(row, 1, QTableWidgetItem(str(listaPagamenti[row].timestamp)))
            self.tabellaPagamenti.setItem(row, 2, QTableWidgetItem(f"{str(listaPagamenti[row].importo)} €"))
            if listaPagamenti[row].tipologia == 'pagamento effettuato' or listaPagamenti[row].tipologia == 'multa pagata':
                self.tabellaPagamenti.setItem(row, 3, QTableWidgetItem(str('Pagato')))
            else:
                self.tabellaPagamenti.setItem(row, 3, QTableWidgetItem(str('Non Pagato')))
            self.tabellaPagamenti.setItem(row, 4, QTableWidgetItem(str(listaPagamenti[row].dettaglio)))

    def clickedCell(self,row, column):

        currentItemId = self.tabellaPagamenti.item(row,0).text()
        currentPagamento = GestorePagamenti()
        currentPagamento.getSingoloPagamento(currentItemId)

        self.idInfo.setText(currentPagamento.getCurrentIdPagamento())
        self.dataInfo.setText(currentPagamento.getCurrentDataEmissione())
        self.importoInfo.setText(currentPagamento.getCurrentImporto())
        self.statusInfo.setText(currentPagamento.getCurrentStatus())
        self.tipologiaInfo.setText(currentPagamento.getCurrentTipologia())
        self.descrizioneInfo.setPlainText(currentPagamento.getCurrentDescrizione())

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

