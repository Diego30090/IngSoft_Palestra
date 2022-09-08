import sys

from PyQt5.QtCore import Qt

from views import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QTableWidget, QTableWidgetItem

class inventarioView(QWidget):

    def __init__(self):
        super().__init__()
        # Window settings
        self.title = 'Inventario'
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

        self.armi_button = QPushButton('Armi', self)
        self.armi_button.setFixedHeight(self.button_fixed_height)
        self.armi_button.setFixedWidth(self.button_fixed_width)
        self.armi_button.move(100, self.button_vertical_distance)
        self.armi_button.setStyleSheet("background: rgb(200,200,200);")

        self.divise_button = QPushButton('Divise', self)
        self.divise_button.setFixedHeight(self.button_fixed_height)
        self.divise_button.setFixedWidth(self.button_fixed_width)
        self.divise_button.move(self.armi_button.x() + self.button_horizontal_distance, self.button_vertical_distance)
        self.divise_button.setStyleSheet("background: rgb(200,200,200);")

        self.borsoni_button = QPushButton('Borsoni', self)
        self.borsoni_button.setFixedHeight(self.button_fixed_height)
        self.borsoni_button.setFixedWidth(self.button_fixed_width)
        self.borsoni_button.move(self.divise_button.x() + self.button_horizontal_distance, self.button_vertical_distance)
        self.borsoni_button.setStyleSheet("background: rgb(200,200,200);")

        self.back_button = QPushButton('Indietro', self)
        self.back_button.setFixedHeight(self.button_fixed_height)
        self.back_button.setFixedWidth(self.button_fixed_width)
        self.back_button.move(self.divise_button.x() + self.button_horizontal_distance, 580)
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
        self.modify_button.move(self.armi_button.x() + self.button_horizontal_distance, 580)
        self.modify_button.setStyleSheet("background: rgb(255,255,70);")

    def instruction(self):
        self.armi_button.clicked.connect(lambda: self.show_tab('armi'))
        self.divise_button.clicked.connect(lambda: self.show_tab('divise'))
        self.borsoni_button.clicked.connect(lambda: self.show_tab('borsoni'))
        self.create_button.clicked.connect(lambda: self.insert())

    def show_tab(self, tab_type):

        if tab_type == 'armi':
            self.table_column = ['Giacenza', 'Disponibilità', 'Arma', 'D/S', 'Materiale', 'Lunghezza', 'Produttore',
                                 'Impugnatura']
        elif tab_type == 'divise':
            self.table_column = ['Giacenza', 'Disponibilità', 'Elemento', 'D/S', 'Arma', 'Taglia', 'Sesso',
                                 'Produttore']
        elif tab_type == 'borsoni':
            self.table_column = ['Giacenza', 'Disponibilità', 'Attrezzatura', 'Produttore']
        self.tab_pointer = tab_type
        lista = db.select_inventario(tab_type)
        self.display_table = QTableWidget(len(lista), len(self.table_column), self)
        self.display_table.move(80, 150)
        self.display_table.setFixedWidth(self.table_fixed_width)
        self.display_table.setFixedHeight(self.table_fixed_height)
        self.display_table.setHorizontalHeaderLabels(self.table_column)

        for i in range(len(lista)):
            for j in range(len(self.table_column)):
                item = QTableWidgetItem(str(lista[i][j+1]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.display_table.setItem(i, j, item)

        self.create_button.show()
        self.modify_button.show()
        self.display_table.show()

    def insert(self):
        if self.tab_pointer == 'armi':
            self.insert_window = insertWindow('Inserisci arma', self.table_column)
            self.insert_window.show()
            self.hide()

        if self.tab_pointer == 'divise':
            self.insert_window = insertWindow('Inserisci divisa', self.table_column)
            self.insert_window.show()
            self.hide()

        if self.tab_pointer == 'borsoni':
            self.insert_window = insertWindow('Inserisci borsone', self.table_column)
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
    ex = inventarioView()
    sys.exit(app.exec_())

