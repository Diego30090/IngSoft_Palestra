import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget

from Controller.GestionePagamenti.GestorePagamenti import GestorePagamenti
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController
from Boundaries.GestionePagamenti import elencoPagamenti as elepag

class CreaPagamento(QWidget):
    def __init__(self, accountController: accountController):
        self.userController = accountController
        self.username = accountController.utente.getUsername()
        super(CreaPagamento, self).__init__()
        loadUi("../GestionePagamenti/CreaPagamento.ui", self)
        self.instruction()
        self.importoValidator()
        self.populateDestinatarioList()

    def instruction(self):
        self.confermaCreazioneButton.clicked.connect(self.confermaPagamento)
        self.backButton.clicked.connect(self.toVisualizzaPagamento)
        pass

    def importoValidator(self):
        regex = QRegExp("[0-9.]*")  # Only digits (0-9) and periods (.) allowed
        validator = QRegExpValidator(regex)
        self.lineEditImporto.setValidator(validator)

    def populateDestinatarioList(self):
        lista = self.userController.returnEveryUsername()
        for username in lista:
            self.destinatarioList.addItem(username)
            pass

    def confermaPagamento(self):
        #funzione che conferma il pagamento
        dettagli = self.lineEditDettagli.text()
        importo = self.lineEditImporto.text()
        descrizione = self.lineEditDescrizione.text()
        gestorePagamento = GestorePagamenti()
        destinatario = self.destinatarioList.currentText()

        gestorePagamento.insertPagamento(dettagli, importo, descrizione, self.username, destinatario)

        self.toVisualizzaPagamento()
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