import sys

from PyQt5.QtCore import Qt

from views import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QTableWidget, QTableWidgetItem


class PersonnelManagementView(QWidget):

    def __init__(self):
        super().__init__()
        # Window settings
        self.title = 'Gestione Personale'
        self.width = 850
        self.height = 710
        # Item settings
        self.armi_button = None
        self.divise_button = None
        self.borsoni_button = None
        self.display_table = None
        self.create_button = None
        self.modify_button = None
        self.back_button = None
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

        self.upper_buttons_argument = ['Atleti', 'Istruttori', 'Amministratori']
        self.upper_buttons = []
        self.lower_buttons_argument = ['Crea', 'Visualizza', 'Indietro']
        self.lower_buttons = []

        for i in range(len(self.upper_buttons_argument)):
            button = QPushButton(self.upper_buttons_argument[i], self)
            button.setFixedHeight(self.button_fixed_height)
            button.setFixedWidth(self.button_fixed_width)
            button.setStyleSheet("background: rgb(200,200,200);")
            if i == 0 :
                button.move(100, self.button_vertical_distance)
            else:
                button.move(self.upper_buttons[i - 1].x() + self.button_horizontal_distance, self.button_vertical_distance)
            self.upper_buttons.append(button)

        self.back_button = QPushButton('Indietro', self)
        self.back_button.setFixedHeight(self.button_fixed_height)
        self.back_button.setFixedWidth(self.button_fixed_width)
        self.back_button.move(self.upper_buttons[1].x() + self.button_horizontal_distance, 580)
        self.back_button.setStyleSheet("background: rgb(255,70,70);")

        self.show()

        self.create_button = QPushButton('Crea', self)
        self.create_button.setFixedHeight(self.button_fixed_height)
        self.create_button.setFixedWidth(self.button_fixed_width)
        self.create_button.move(100, 580)
        self.create_button.setStyleSheet("background: rgb(140,255,70);")

        self.modify_button = QPushButton('Visualizza', self)
        self.modify_button.setFixedHeight(self.button_fixed_height)
        self.modify_button.setFixedWidth(self.button_fixed_width)
        self.modify_button.move(self.upper_buttons[0].x() + self.button_horizontal_distance, 580)
        self.modify_button.setStyleSheet("background: rgb(255,255,70);")

    def instruction(self):
        self.upper_buttons[0].clicked.connect(lambda: self.show_tab(self.upper_buttons_argument[0]))
        self.upper_buttons[1].clicked.connect(lambda: self.show_tab(self.upper_buttons_argument[1]))
        self.upper_buttons[2].clicked.connect(lambda: self.show_tab(self.upper_buttons_argument[2]))
        self.create_button.clicked.connect(lambda: self.insert())

    def show_tab(self, tab_type):
        print(f'Tab type: {tab_type}')
        self.table_column = ['Id', 'Nome', 'Cognome', 'Data di Nascita', 'Username', 'Password', 'Tipologia di Utente', 'Email', 'Telefono']

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

        for i in range(len(lista)):
            for j in range(len(self.table_column)):
                item = QTableWidgetItem(str(lista[i][j]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.display_table.setItem(i, j, item)

        self.create_button.show()
        self.modify_button.show()
        


    def insert(self):
        if self.tab_pointer == 'Atleti':
            self.insert_window = insertWindow('Inserisci atleta', self.table_column)
            self.insert_window.show()
            self.hide()

        if self.tab_pointer == 'Istruttori':
            self.insert_window = insertWindow('Inserisci istruttore', self.table_column)
            self.insert_window.show()
            self.hide()

        if self.tab_pointer == 'Amministratori':
            self.insert_window = insertWindow('Inserisci amministratore', self.table_column)
            self.insert_window.show()
            self.hide()



class insertWindow(QWidget):

    def __init__(self, window_title, table_column):
        super().__init__()
        # Window settings
        self.title = window_title
        self.width = 370
        self.height = 600
        # Item settings
        self.labels = []
        self.texts = []

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

            new_text = QLineEdit(self)
            new_text.move(self.horizontalTextDistance, self.verticalDistance)
            self.texts.append(new_text)

            self.verticalDistance += 50
            self.labels[i].show()
            self.texts[i].show()

        self.accept_button = QPushButton('Accetta', self)
        self.accept_button.setFixedHeight(self.button_fixed_height)
        self.accept_button.setFixedWidth(self.button_fixed_width)
        self.accept_button.move(self.horizontalLabelDistance, 475)
        self.accept_button.setStyleSheet("background: rgb(140,255,70);")

        self.back_button = self.accept_button = QPushButton('Indietro', self)
        self.back_button.setFixedHeight(self.button_fixed_height)
        self.back_button.setFixedWidth(self.button_fixed_width)
        self.back_button.move(self.horizontalTextDistance, 475)
        self.back_button.setStyleSheet("background: rgb(255,70,70);")

    def instruction(self):
        self.back_button.clicked.connect(lambda: self.close_this())

    def close_this(self):
        ex.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PersonnelManagementView()
    sys.exit(app.exec_())
