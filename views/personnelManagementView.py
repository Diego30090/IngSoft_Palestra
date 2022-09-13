import sys

from PyQt5.QtCore import Qt, QDate

from views import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QTableWidget, QTableWidgetItem, \
    QDateEdit, QComboBox


class PersonnelManagementView(QWidget):

    def __init__(self):
        super().__init__()
        # Window settings
        self.title = 'Gestione Personale'
        self.width = 850
        self.height = 710
        # Upper Buttons
        self.upper_buttons_argument = ['Atleti', 'Istruttori', 'Amministratori']
        self.upper_buttons = []
        self.upper_buttons_rgb = ['200,200,200', '200,200,200', '200,200,200']
        # Lower Buttons
        self.lower_buttons_argument = ['Crea', 'Visualizza', 'Indietro']
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
        self.lower_buttons[0].clicked.connect(lambda: self.insert())

    def show_tab(self, tab_type):
        print(f'Tab type: {tab_type}')
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

    def insert(self):
        columns = self.table_column
        columns.pop(0)
        self.insert_window = insertWindow('Inserisci Utente', columns)
        self.insert_window.show()
        self.hide()
        tab = self.tab


class insertWindow(QWidget):

    def __init__(self, window_title, table_column):
        super().__init__()
        # Window settings
        self.title = window_title
        self.width = 370
        self.height = 610
        # Item settings
        self.labels = []
        self.texts = []
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
            self.labels.append(new_label)
            # print(table_column[i])
            if table_column[i] == 'Data di Nascita':
                new_text = QDateEdit(self)
                new_text.setDate(QDate(1900, 1, 1))
            elif self.labels[i].text() == 'Tipologia di Utente':
                new_text = QComboBox(self)
                new_text.addItem('Atleta')
                new_text.addItem('Istruttore')
                new_text.addItem('Admin')
            else:
                new_text = QLineEdit(self)
            new_text.move(self.horizontalTextDistance, self.verticalDistance)
            new_text.setFixedWidth(135)
            self.texts.append(new_text)

            self.verticalDistance += 50
            self.labels[i].show()
            self.texts[i].show()

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

    def err_handle(self, error):
        self.err_label.setText(f'Error: {error}')
        self.err_label.adjustSize()
        self.err_label.move(int((self.width - self.err_label.width()) / 2), self.verticalDistance - 10)

    def instruction(self):
        self.back_button.clicked.connect(lambda: self.close_this())
        self.accept_button.clicked.connect(self.record_create)

    def record_create(self):
        flag = True
        values = []
        for i in range(len(self.texts)):
            if isinstance(self.texts[i], QLineEdit) and self.texts[i].text() == '':
                error = 'Inserire tutti i campi'
                self.err_handle(error=error)
                flag = False
            if self.labels[i].text() == 'Username':
                user = self.texts[i].text()
                check_flag = db.check_username(user)
                if check_flag:
                    error = 'Username già esistente'
                    self.err_handle(error=error)
                    flag = False

        if flag:
            values.clear()
            for i in range(len(self.texts)):
                if isinstance(self.texts[i], QLineEdit):
                    values.append(str(self.texts[i].text()))
                elif isinstance(self.texts[i], QDateEdit):
                    values.append(str(self.texts[i].date().toString('yyyy-MM-dd')))
                elif isinstance(self.texts[i], QComboBox):
                    values.append(self.texts[i].currentText())
            db.insert_user(*values)
            self.close_this()

    def close_this(self):
        ex.show()
        ex.show_tab(tab_type=ex.tab)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PersonnelManagementView()
    sys.exit(app.exec_())
