import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.uic import loadUi
from Boundaries.GestioneUtente import mainMenu as menu
from PyQt5.QtWidgets import QApplication, QWidget

from Controller.GestionePagamenti.GestorePagamenti import GestorePagamenti
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController
from Boundaries.GestionePagamenti import creaPagamentoView as creapag
from Boundaries.GestionePagamenti import elencoPagamenti as elepag


class modificaPagamento(QWidget):
    def __init__(self, accountController: accountController, idPagamento: str):
        self.userController = accountController
        self.username = accountController.utente.getUsername()
        self.idPagamento = idPagamento
        super(modificaPagamento, self).__init__()
        loadUi("../GestionePagamenti/ModificaPagamento.ui", self)
        self.instruction()
        self.populatePagamentiTable()
        self.populatePagamentoDetail()
        self.importoValidator()


    def instruction(self):
        self.backButton.clicked.connect(self.toElencoPagamenti)
        pass

    def importoValidator(self):
        regex = QRegExp("[0-9.]*")  # Only digits (0-9) and periods (.) allowed
        validator = QRegExpValidator(regex)
        self.lineEditImporto.setValidator(validator)

    def populatePagamentiTable(self):
        # funzione che mostra la lista dei pagamenti nella tabella principale
        pagamentiController = GestorePagamenti()
        listaPagamenti = pagamentiController.getListaPagamentiCompleta()
        self.tabellaPagamenti.setRowCount(len(listaPagamenti))
        for row in range(len(listaPagamenti)):
            self.tabellaPagamenti.setItem(row, 0, QTableWidgetItem(str(listaPagamenti[row].id)))
            self.tabellaPagamenti.setItem(row, 1, QTableWidgetItem(str(listaPagamenti[row].timestamp)))
            self.tabellaPagamenti.setItem(row, 2, QTableWidgetItem(f"{str(listaPagamenti[row].importo)} €"))
            if listaPagamenti[row].tipologia == 'pagamento effettuato' or listaPagamenti[row].tipologia == 'multa pagata':
                self.tabellaPagamenti.setItem(row, 3, QTableWidgetItem(str('Pagato')))
            else:
                self.tabellaPagamenti.setItem(row, 3, QTableWidgetItem(str('Non Pagato')))
            self.tabellaPagamenti.setItem(row, 4, QTableWidgetItem(str(listaPagamenti[row].dettaglio)))

    def populatePagamentoDetail(self):
        pagamentiController = GestorePagamenti()
        pagamentiController.getSingoloPagamento(self.idPagamento)

        self.lineEditImporto.setText(pagamentiController.getCurrentImporto())
        self.lineEditDettagli.setText(pagamentiController.getCurrentDettaglio())
        self.lineEditStato.setText(pagamentiController.getCurrentStatus())
        self.lineEditDescrizione.setText(pagamentiController.getCurrentDescrizione())
        pass

    def toModificaPagamento(self):
        # Va alla vista della visualizzazione dei pagamenti
        print(f"funzione che porta alla vista di modifica del pagamento")
        pass

    def toElencoPagamenti(self):
        self.screen = elepag.ElencoPagamenti(accountController=self.userController)
        self.screen.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = modificaPagamento(accountController=accountController('root1', 'pwd'), idPagamento='5')
    ex.show()
    sys.exit(app.exec_())
