import sys

from PyQt5.uic import loadUi
from Boundaries.GestioneUtente import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as accountController
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
        utentiController = self.accountController
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
        self.currentSelectedUser = self.accountController.getSingoloutente(userId=currentUserId)

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

        control = accountController.controlloDati(accountController, nome=nome, cognome=cognome, password=password,
                                                  email=email, telefono=telefono, username=username,
                                                  dataNascita=dataNascita)
        if control[0] is True:
            self.errorLabel.setText(control[1])
        else:
            db.insert_user(nome=nome, cognome=cognome, data_nascita=dataNascita,
                           username=username, password=password,
                           utente_tipo=tipoUtente, email=email, telefono=telefono)
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
        self.accountController.userUpdater(*lista)
        self.toGestionePersonale()

    def toGestionePersonale(self):
        self.screen = PersonnelManagementView(accountController=self.accountController)
        self.screen.show()
        self.screen.genericPopulateTab(tab=self.displayedTable)
        self.close()


'''
class PersonnelManagementView(QWidget):

    def __init__(self, accountController: accountController):
        super().__init__()
        self.accountController = accountController
        # Window settings
        self.title = 'Gestione Personale'
        self.width = 850
        self.height = 710
        # Upper Buttons
        self.upper_buttons_argument = ['Atleti', 'Istruttori', 'Amministratori']
        self.upper_buttons = []
        self.upper_buttons_rgb = ['200,200,200', '200,200,200', '200,200,200']
        # Lower Buttons
        self.lower_buttons_argument = ['Crea', 'Modifica', 'Indietro']
        self.lower_buttons = []
        self.lower_buttons_rgb = ['140,255,70', '255,255,70', '255,70,70']
        # Button distances
        self.button_fixed_height = 90
        self.button_fixed_width = 120
        self.button_horizontal_distance = 265
        self.button_vertical_distance = 40
        # Table columns settings
        self.table_column = None
        self.table_fixed_width = 690
        self.table_fixed_height = 400
        # settings for new windows
        self.tab_pointer = None
        self.insert_window = None
        # item initializers and item commands
        self.inventario_ui()
        self.instruction()

    def inventario_ui(self):
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        self.button_create(button_name=self.upper_buttons_argument, button_array=self.upper_buttons,
                           rgb=self.upper_buttons_rgb, start_pos_x=100, x_dist=self.button_horizontal_distance,
                           start_pos_y=self.button_vertical_distance)
        self.button_create(button_name=self.lower_buttons_argument, button_array=self.lower_buttons,
                           rgb=self.lower_buttons_rgb, start_pos_x=100, x_dist=self.button_horizontal_distance,
                           start_pos_y=580)
        self.show()
        self.lower_buttons[0].hide()
        self.lower_buttons[1].hide()

    # La seguente funzione, prende un array di pulsanti da creare, a cui assegna tutto.
    # Si parte dalla tipologia di oggetto con il nome, per poi passare alla geometria del pulsante,
    # fino al colore dello stesso
    def button_create(self, button_name, button_array: QPushButton, rgb, start_pos_x, x_dist, start_pos_y):
        for i in range(len(button_name)):
            button = QPushButton(button_name[i], self)
            if i == 0:
                button.setGeometry(start_pos_x, start_pos_y, self.button_fixed_width, self.button_fixed_height)
            else:
                button.setGeometry(button_array[i - 1].x() + x_dist, start_pos_y, self.button_fixed_width,
                                   self.button_fixed_height)
            button.setStyleSheet(f"background: rgb({rgb[i]});")
            button_array.append(button)

    def instruction(self):

        self.upper_buttons[0].clicked.connect(lambda: self.show_tab(self.upper_buttons_argument[0]))
        self.upper_buttons[1].clicked.connect(lambda: self.show_tab(self.upper_buttons_argument[1]))
        self.upper_buttons[2].clicked.connect(lambda: self.show_tab(self.upper_buttons_argument[2]))
        self.lower_buttons[0].clicked.connect(lambda: self.toCrudView())
        #self.lower_buttons[1].clicked.connect(lambda: )
        self.lower_buttons[2].clicked.connect(self.toMainMenu)

    def show_tab(self, tab_type):
        self.table_column = ['Id', 'Nome', 'Cognome', 'Data di Nascita', 'Username', 'Password', 'Tipologia di Utente',
                             'Email', 'Telefono']

        if tab_type == self.upper_buttons_argument[0]:
            lista = db.select_utente('Atleta')
        elif tab_type == self.upper_buttons_argument[1]:
            lista = db.select_utente('Istruttore')
        else:
            lista = db.select_utente('Admin')
        self.display_table = QTableWidget(len(lista), len(self.table_column), self)

        self.display_table.setFixedWidth(self.table_fixed_width)
        self.display_table.setFixedHeight(self.table_fixed_height)
        self.display_table.setHorizontalHeaderLabels(self.table_column)
        self.display_table.move(80, 150)
        self.display_table.show()
        self.tab_pointer = tab_type
        self.tab = tab_type

        for i in range(len(lista)):
            for j in range(len(self.table_column)):
                item = QTableWidgetItem(str(lista[i][j]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.display_table.setItem(i, j, item)

        self.lower_buttons[0].show()
        self.lower_buttons[1].show()

    def toCrudView(self):
        columns = self.table_column
        columns.pop(0)
        self.insert_window = PersonnelManagementCrudView('Inserisci Utente', columns, self.tab, self.accountController)
        self.insert_window.show()
        self.hide()

    def toMainMenu(self):
        self.screen = menu.MainMenu(self.accountController)
        self.screen.show()
        self.close()


class PersonnelManagementCrudView(QWidget):

    def __init__(self, window_title, table_column, tab_type, accountController):
        super().__init__()
        self.accountController = accountController
        self.tab_type = tab_type
        # Window settings
        self.title = window_title
        self.width = 370
        self.height = 610
        # Item settings
        self.info_labels = []
        self.info_texts = []
        self.err_label = QLabel(self)

        self.button_fixed_height = 90
        self.button_fixed_width = 120

        self.accept_button = None
        self.back_button = None

        self.verticalDistance = 50
        self.horizontalLabelDistance = 50
        self.horizontalTextDistance = 200

        self.insertUI(table_column)
        self.instruction()
        self.show()

    def insertUI(self, table_column):
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        for i in range(len(table_column)):
            new_label = QLabel(table_column[i], self)
            new_label.move(self.horizontalLabelDistance, self.verticalDistance)
            self.info_labels.append(new_label)
            if table_column[i] == 'Data di Nascita':
                new_text = QDateEdit(self)
                new_text.setDate(QDate(1900, 1, 1))
            elif self.info_labels[i].text() == 'Tipologia di Utente':
                new_text = QComboBox(self)
                new_text.addItem('Atleta')
                new_text.addItem('Istruttore')
                new_text.addItem('Admin')
            else:
                new_text = QLineEdit(self)
            new_text.move(self.horizontalTextDistance, self.verticalDistance)
            new_text.setFixedWidth(135)
            self.info_texts.append(new_text)

            self.verticalDistance += 50
            self.info_labels[i].show()
            self.info_texts[i].show()

        self.accept_button = QPushButton('Accetta', self)
        self.accept_button.setFixedHeight(self.button_fixed_height)
        self.accept_button.setFixedWidth(self.button_fixed_width)
        self.accept_button.move(self.horizontalLabelDistance, self.height - self.accept_button.width() - 10)
        self.accept_button.setStyleSheet("background: rgb(140,255,70);")

        self.back_button = QPushButton('Indietro', self)
        self.back_button.setFixedHeight(self.button_fixed_height)
        self.back_button.setFixedWidth(self.button_fixed_width)
        self.back_button.move(self.horizontalTextDistance, self.height - self.back_button.width() - 10)
        self.back_button.setStyleSheet("background: rgb(255,70,70);")

        self.err_label.setStyleSheet('color: red')

    def errorHandle(self, error):
        self.err_label.setText(f'Error: {error}')
        self.err_label.adjustSize()
        self.err_label.move(int((self.width - self.err_label.width()) / 2), self.verticalDistance - 10)

    def instruction(self):
        self.back_button.clicked.connect(lambda: self.closeThis())
        self.accept_button.clicked.connect(self.recordCreate)

    def recordCreate(self):
        flag = True
        values = []
        for i in range(len(self.info_texts)):
            if isinstance(self.info_texts[i], QLineEdit) and self.info_texts[i].text() == '':
                error = 'Inserire tutti i campi'
                self.errorHandle(error=error)
                flag = False
            if self.info_labels[i].text() == 'Username':
                user = self.info_texts[i].text()
                check_flag = db.check_username(user)
                if check_flag:
                    error = 'Username già esistente'
                    self.errorHandle(error=error)
                    flag = False

        if flag:
            values.clear()
            for i in range(len(self.info_texts)):
                if isinstance(self.info_texts[i], QLineEdit):
                    values.append(str(self.info_texts[i].text()))
                elif isinstance(self.info_texts[i], QDateEdit):
                    values.append(str(self.info_texts[i].date().toString('yyyy-MM-dd')))
                elif isinstance(self.info_texts[i], QComboBox):
                    values.append(self.info_texts[i].currentText())
            db.insert_user(*values)
            self.closeThis()

    def closeThis(self):
        self.screen = PersonnelManagementView( accountController=self.accountController)
        self.screen.show()
        self.screen.show_tab(tab_type=self.tab_type)
        self.close()
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PersonnelManagementView(accountController=accountController('root1', 'pwd'))
    ex.show()
    sys.exit(app.exec_())
