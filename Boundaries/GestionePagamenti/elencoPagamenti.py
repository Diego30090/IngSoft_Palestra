import sys
from PyQt5.uic import loadUi
from Boundaries.GestioneUtente import mainMenu as menu
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController
from Controller.GestionePagamenti.GestorePagamenti import GestorePagamenti
from Boundaries.GestionePagamenti import creaPagamentoView as creapag
from Boundaries.GestionePagamenti import modificaPagamento as vispag


class ElencoPagamenti(QWidget):
    def __init__(self, accountController: accountController):
        self.userController = accountController
        self.username = accountController.utente.getUsername()
        super(ElencoPagamenti, self).__init__()
        loadUi("../GestionePagamenti/elencoPagamenti.ui", self)
        self.instruction()
        self.populatePagamentiTable()
        self.lockedOptions()

    def instruction(self):
        self.backButton.clicked.connect(self.toMainView)
        self.creaPagamentoButton.clicked.connect(self.toCreaPagamento)
        self.tabellaPagamenti.cellClicked.connect(self.clickedCell)
        self.modificaPagamentoButton.clicked.connect(self.toModificaPagamento)
        self.eliminaPagamentoButton.clicked.connect(self.eliminaPagamento)

    def populatePagamentiTable(self):
        # funzione che mostra la lista dei pagamenti nella tabella principale
        pagamentiController = GestorePagamenti()
        prova1 = pagamentiController.differenziazionePagamenti(utente = self.userController.utente)
        print(prova1)
        #Da completare con il differenziamento di utente
        listaPagamenti = pagamentiController.getListaPagamentiCompleta()
        self.tabellaPagamenti.setRowCount(len(listaPagamenti))

        for row in range(len(listaPagamenti)):
            self.tabellaPagamenti.setItem(row, 0, QTableWidgetItem(str(listaPagamenti[row].mittente)))
            self.tabellaPagamenti.setItem(row, 1, QTableWidgetItem(str(listaPagamenti[row].timestamp)))
            self.tabellaPagamenti.setItem(row, 2, QTableWidgetItem(f"{str(listaPagamenti[row].importo)} €"))
            if listaPagamenti[row].tipologia == 'pagamento effettuato' or listaPagamenti[
                row].tipologia == 'multa pagata':
                self.tabellaPagamenti.setItem(row, 3, QTableWidgetItem(str('Pagato')))
            else:
                self.tabellaPagamenti.setItem(row, 3, QTableWidgetItem(str('Non Pagato')))
            self.tabellaPagamenti.setItem(row, 4, QTableWidgetItem(str(listaPagamenti[row].dettaglio)))

    def lockedOptions(self):
        status = True
        if self.userController.utente.getUtenteTipo() == 'Admin':
            status = True
        else:
            status = False
        self.creaPagamentoButton.setEnabled(status)
        self.eliminaPagamentoButton.setEnabled(status)
        self.modificaPagamentoButton.setEnabled(status)
        pass

    def clickedCell(self, row):

        currentItemId = self.tabellaPagamenti.item(row, 0).text()
        currentPagamento = GestorePagamenti()
        currentPagamento.setSingoloPagamento(currentItemId)
        self.currentRow= row

        self.idInfo.setText(currentPagamento.getCurrentIdPagamento())
        self.dataInfo.setText(currentPagamento.getCurrentDataEmissione())
        self.importoInfo.setText(currentPagamento.getCurrentImporto())
        self.statusInfo.setText(currentPagamento.getCurrentStatus())
        self.tipologiaInfo.setText(currentPagamento.getCurrentTipologia())
        self.descrizioneInfo.setPlainText(currentPagamento.getCurrentDescrizione())

    def eliminaPagamento(self):
        pagamentoId = self.idInfo.text()
        if pagamentoId == '':
            print('Nessun pagamento da eliminare')
        else:
            currentPagamento = GestorePagamenti()
            id = self.idInfo.text()
            currentPagamento.eliminaPagamento(id=id)
            self.tabellaPagamenti.removeRow(self.currentRow)

        pass

    def toModificaPagamento(self):
        # Va alla vista della visualizzazione dei pagamenti se è stato selezionato un evento
        pagamentoId = self.idInfo.text()
        if pagamentoId == '':
            print('Nessun Id di pagamento')
        else:
            self.screen = vispag.modificaPagamento(accountController=self.userController, idPagamento=pagamentoId)
            self.screen.show()
            self.close()

    def toCreaPagamento(self):
        # Va alla vista di creazione del pagamento
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
    ex = ElencoPagamenti(accountController=accountController('root0', '0000'))
    ex.show()
    sys.exit(app.exec_())
