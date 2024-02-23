import datetime
import sys

from PyQt5.QtCore import Qt, QDate
from PyQt5.uic import loadUi
from Boundaries.GestioneUtente import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QTableWidget, QTableWidgetItem, \
    QDateEdit, QComboBox
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController


class PersonnelManagementView(QWidget):
    def __init__(self, accountController: accountController):
        super(PersonnelManagementView, self).__init__()
        self.accountController = accountController
        loadUi("../GestioneInformazioniPersonale/GestionePersonale.ui", self)
        self.displayTable.hide()
        self.instruction()
        self.currentTableDisplayed = ''

    def instruction(self):
        self.backButton.clicked.connect(self.toMainMenu)
        self.atletiButton.clicked.connect(self.atletiTab)
        self.istruttoriButton.clicked.connect(self.istruttoriTab)
        self.amministratoriButton.clicked.connect(self.amministratoriTab)
        self.creaUtenteButton.clicked.connect(self.toCreaUtenteView)
        self.modifyUtenteButton.clicked.connect(self.toModificaView)

    def showTab(self):
        if self.displayTable.isHidden() == True:
            self.displayTable.show()
        else:
            pass

    def genericPopulateTab(self, tab):
        self.showTab()
        self.currentTableDisplayed = tab
        if tab is None:
            lista = []
        else:
            lista = db.select_utente(tab)
        self.displayTable.setRowCount(len(lista))
        for i in range(len(lista)):

            for j in range(7):
                item = QTableWidgetItem(str(lista[i][j]))
                self.displayTable.setItem(i, j, item)

    def atletiTab(self):
        self.genericPopulateTab('Atleta')

    def istruttoriTab(self):
        self.genericPopulateTab('Istruttore')

    def amministratoriTab(self):
        self.genericPopulateTab('Admin')

    def toCreaUtenteView(self):
        self.insert_window = creaUtenteView(accountController=self.accountController,
                                            displayedTable=self.currentTableDisplayed)
        self.insert_window.show()
        self.hide()

    def toModificaView(self):
        self.insert_window = modificaUtente(accountController=self.accountController,
                                            displayedTable=self.currentTableDisplayed,
                                            daModificare = '')
        self.insert_window.show()
        self.hide()

    def toMainMenu(self):
        self.screen = menu.MainMenu(self.accountController)
        self.screen.show()
        self.close()


class creaUtenteView(QWidget):
    def __init__(self, accountController: accountController, displayedTable):
        super(creaUtenteView, self).__init__()
        self.displayedTable = displayedTable
        self.accountController = accountController
        loadUi("../GestioneInformazioniPersonale/creaUtente.ui", self)
        self.instruction()

    def instruction(self):
        self.backButton.clicked.connect(self.toGestionePersonale)
        self.creaUtenteButton.clicked.connect(self.creaUtente)


    def creaUtente(self):
        self.errorLabel.setText('')
        nome = self.nameInfo.text()
        cognome = self.surnameInfo.text()
        dataNascita = self.dateInfo.date().toString('yyyy-MM-dd')
        username = self.usernameInfo.text()
        password = self.passwordInfo.text()
        tipoUtente = self.tipoUtente.currentText()
        email = self.emailInfo.text()
        telefono = self.phoneInfo.text()

        control = accountController.controlloDati(accountController, nome=nome, cognome=cognome, password=password,
                                                  email=email, telefono=telefono, username=username, dataNascita=dataNascita)
        if control[0] is True:
            self.errorLabel.setText(control[1])
        else:
            db.insert_user(nome=nome, cognome=cognome, data_nascita=dataNascita,
                           username=username,password=password,
                           utente_tipo=tipoUtente,email=email, telefono=telefono)
            self.toGestionePersonale()

    def toGestionePersonale(self):
        self.screen = PersonnelManagementView(accountController=self.accountController)
        self.screen.show()
        self.screen.genericPopulateTab(tab=self.displayedTable)
        self.close()

class modificaUtente(QWidget):
    def __init__(self, accountController: accountController, displayedTable, daModificare):
        super(modificaUtente, self).__init__()
        self.daModificare = daModificare
        self.displayedTable = displayedTable
        self.accountController = accountController
        loadUi("../GestioneInformazioniPersonale/creaUtente.ui", self)
        self.instruction()

    def instruction(self):
        self.backButton.clicked.connect(self.toGestionePersonale)
        self.creaUtenteButton.clicked.connect(self.modificaUtente)


    def modificaUtente(self):
        pass

    def toGestionePersonale(self):
        self.screen = PersonnelManagementView(accountController=self.accountController)
        self.screen.show()
        self.screen.genericPopulateTab(tab=self.displayedTable)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PersonnelManagementView(accountController=accountController('root1', 'pwd'))
    ex.show()
    sys.exit(app.exec_())
