import sys

from PyQt5.uic import loadUi
from Boundaries.GestioneUtente import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController
from Controller.GestioneInformazioniPersonale import GestorePersonale
from PyQt5.QtCore import QDate
from Model.GestioneUtente import UtenteModel


class PersonnelManagementView(QWidget):
    def __init__(self, accountController: accountController):
        super(PersonnelManagementView, self).__init__()
        self.accountController = accountController
        loadUi("../GestioneInformazioniPersonale/GestionePersonale.ui", self)
        self.displayTable.hide()
        self.instruction()
        self.currentTableDisplayed = ''
        self.currentSelectedUser = None

    def instruction(self):
        self.backButton.clicked.connect(self.toMainMenu)
        self.atletiButton.clicked.connect(self.atletiTab)
        self.istruttoriButton.clicked.connect(self.istruttoriTab)
        self.amministratoriButton.clicked.connect(self.amministratoriTab)
        self.creaUtenteButton.clicked.connect(self.toCreaUtenteView)
        self.modifyUtenteButton.clicked.connect(self.toModificaView)
        self.displayTable.cellClicked.connect(self.clickedCell)

    def showTab(self):
        if self.displayTable.isHidden() == True:
            self.displayTable.show()
        else:
            pass

    def genericPopulateTab(self, tab):
        self.currentSelectedUser = None
        self.showTab()
        utentiController = GestorePersonale.GestoreInformazioniPersonale()
        self.currentTableDisplayed = tab
        listaUtenti = utentiController.getUtentePerTipo(userType=tab)
        self.displayTable.setRowCount(len(listaUtenti))
        for row in range(len(listaUtenti)):
            self.displayTable.setItem(row, 0, QTableWidgetItem(str(listaUtenti[row].idUtente)))
            self.displayTable.setItem(row, 1, QTableWidgetItem(str(listaUtenti[row].nome)))
            self.displayTable.setItem(row, 2, QTableWidgetItem(str(listaUtenti[row].cognome)))
            self.displayTable.setItem(row, 3, QTableWidgetItem(str(listaUtenti[row].dataDiNascita)))
            self.displayTable.setItem(row, 4, QTableWidgetItem(str(listaUtenti[row].username)))
            self.displayTable.setItem(row, 5, QTableWidgetItem(str(listaUtenti[row].password)))
            self.displayTable.setItem(row, 6, QTableWidgetItem(str(listaUtenti[row].utenteTipo)))
            self.displayTable.setItem(row, 7, QTableWidgetItem(str(listaUtenti[row].email)))
            self.displayTable.setItem(row, 8, QTableWidgetItem(str(listaUtenti[row].telefono)))

    def clickedCell(self, row):
        currentUserId = self.displayTable.item(row,0).text()
        utentiController = GestorePersonale.GestoreInformazioniPersonale()
        self.currentSelectedUser = utentiController.getSingoloutente(userId=currentUserId)

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
        if self.currentSelectedUser is not None:
            self.insert_window = modificaUtente(accountController=self.accountController,
                                                displayedTable=self.currentTableDisplayed,
                                                user=self.currentSelectedUser)
            self.insert_window.show()
            self.hide()
        else:
            pass

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

        personaleController = GestorePersonale.GestoreInformazioniPersonale()
        listaInfo = [nome, cognome, dataNascita, username, password, tipoUtente, email, telefono]
        control = personaleController.controlloDati(*listaInfo)
        if control[0] is True:
            self.errorLabel.setText(control[1])
        else:
            personaleController.insertUser(*listaInfo)
            self.toGestionePersonale()

    def toGestionePersonale(self):
        self.screen = PersonnelManagementView(accountController=self.accountController)
        self.screen.show()
        self.screen.genericPopulateTab(tab=self.displayedTable)
        self.close()


class modificaUtente(QWidget):
    def __init__(self, accountController: accountController, displayedTable, user: UtenteModel):
        super(modificaUtente, self).__init__()
        self.user = user
        self.displayedTable = displayedTable
        self.accountController = accountController
        loadUi("../GestioneInformazioniPersonale/modificaUtente.ui", self)
        self.instruction()
        self.populateData()
    def instruction(self):
        self.backButton.clicked.connect(self.toGestionePersonale)
        self.modificaUtenteButton.clicked.connect(self.modificaUtente)
        self.dateInfo.dateChanged.connect(self.cambioData)

    def populateData(self):
        self.nameInfo.setText(self.user.nome)
        self.surnameInfo.setText(self.user.cognome)
        self.usernameInfo.setText(self.user.username)
        self.passwordInfo.setText(self.user.password)
        self.emailInfo.setText(self.user.email)
        self.phoneInfo.setText(self.user.telefono)
        self.dateInfo.setDate(QDate.fromString(self.user.dataDiNascita, "yyyy-MM-dd"))
        if self.user.utenteTipo == 'Atleta':
            self.tipoUtente.setCurrentIndex(0)
        elif self.user.utenteTipo == 'Istruttore':
            self.tipoUtente.setCurrentIndex(1)
        elif self.user.utenteTipo == 'Admin':
            self.tipoUtente.setCurrentIndex(2)
        else:
            pass

    def cambioData(self, date):
        dateString = date.toString("yyyy-MM-dd")
        self.user.setDataDiNascita(dateString)
    def modificaUtente(self):
        self.user.setNome(self.nameInfo.text())
        self.user.setCognome(self.surnameInfo.text())
        self.user.setPassword(self.passwordInfo.text())
        self.user.setUtenteTipo(self.tipoUtente.currentText())
        self.user.setEmail(self.emailInfo.text())
        self.user.setTelefono(self.phoneInfo.text())
        self.user.idUtente = str(self.user.idUtente)
        lista = []
        attributi = vars(self.user)
        for valore in attributi.values():
            lista.append(valore)
        personaleController = GestorePersonale.GestoreInformazioniPersonale()
        personaleController.userUpdater(*lista)
        self.toGestionePersonale()

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
