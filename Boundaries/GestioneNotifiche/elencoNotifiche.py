import sys
from PyQt5.uic import loadUi

from Boundaries.GestioneUtente import mainMenu as menu
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController
from Controller.GestioneNotifiche.GestoreNotifiche import GestoreNotifiche


class ElencoNotifiche(QWidget):
    def __init__(self, accountController: accountController):
        self.userController = accountController
        self.username = accountController.utente.getUsername()
        super(ElencoNotifiche, self).__init__()
        loadUi("../GestioneNotifiche/VisualizzaNotifiche.ui", self)
        self.listaNotifiche = None
        self.selectedNotifica = None
        self.instruction()
        self.populateTabellaNotifiche()

    def instruction(self):
        self.backButton.clicked.connect(self.toMainMenu)
        self.eliminaNotificaButton.clicked.connect(self.eliiminaNotifica)
        self.tabellaNotifiche.cellClicked.connect(self.notificaSelezionata)


    def populateTabellaNotifiche(self):
        # la funzione popola la tabella notifiche
        gestoreNotifiche = GestoreNotifiche()
        listaNotifiche = []
        if self.userController.utente.getUtenteTipo()=="Admin":
           self.listaNotifiche = gestoreNotifiche.listaNotificheCompleta()
        else:
            self.listaNotifiche = gestoreNotifiche.listaNotificheUtente(self.userController.utente.getIdUtente())
        listaNotifiche = self.listaNotifiche
        self.tabellaNotifiche.setRowCount(len(listaNotifiche))
        for row in range(len(listaNotifiche)):
            self.tabellaNotifiche.setItem(row, 0, QTableWidgetItem(str(listaNotifiche[row].getData())))
            self.tabellaNotifiche.setItem(row, 1, QTableWidgetItem(str(listaNotifiche[row].getDettaglio())))

    def notificaSelezionata(self, row):
        self.selectedNotifica = self.listaNotifiche[row]

    def eliiminaNotifica(self):
        gestoreNotifiche = GestoreNotifiche()
        if self.selectedNotifica is not None:
            print(self.selectedNotifica)
            gestoreNotifiche.deleteNotifica(self.selectedNotifica.idNotifica)
            self.tabellaNotifiche.setRowCount(0)
            self.populateTabellaNotifiche()

    def toMainMenu(self):
        self.screen = menu.MainMenu(userController=self.userController)
        self.screen.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ElencoNotifiche(accountController=accountController('root1', 'pwd'))
    ex.show()
    sys.exit(app.exec_())
