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
        self.height = 600
        # Item settings
        self.armi_button = None
        self.divise_button = None
        self.borsoni_button = None
        self.display_table = None
        # Button settings
        self.button_fixed_height = 90
        self.button_fixed_width = 120
        self.button_horizontal_distance = 265
        self.button_vertical_distance = 40
        # Table columns settings
        self.table_column_arma = ['Giacenza', 'Disponibilità', 'Arma', 'D/S', 'Materiale', 'Lunghezza', 'Produttore', 'Impugnatura']
        self.table_column_divise = ['Giacenza', 'Disponibilità', 'Elemento', 'D/S', 'Arma', 'Taglia', 'Sesso', 'Produttore']
        self.table_column_borsoni = ['Attrezzatura', 'Produttore']
        self.table_fixed_width = 690
        self.table_fixed_height = 400
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

        self.show()


    def instruction(self):
        self.armi_button.clicked.connect(lambda: self.select_tab('armi'))
        self.divise_button.clicked.connect(lambda: self.show_tab('divise'))
        self.borsoni_button.clicked.connect(lambda: self.show_tab('borsoni'))


    def select_tab(self, tab_type):
        if tab_type == 'armi':
            self.show_armi()
        if tab_type == 'divise':
            print('tabella divise')
        if tab_type == 'borsoni':
            print('tabella borsoni')


    def show_armi(self):
        self.display_table = QTableWidget(10, len(self.table_column_arma), self)
        self.display_table.move(80, 150)
        self.display_table.setFixedWidth(self.table_fixed_width)
        self.display_table.setFixedHeight(self.table_fixed_height)

        self.display_table.setHorizontalHeaderLabels(self.table_column_arma)

        for i in range(10):
            for j in range(len(self.table_column_arma)):
                #Nella linea sotto viene scritto qualcosa nelle varie celle
                item = QTableWidgetItem(str(i * j))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.display_table.setItem(i, j, item)

        self.display_table.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = inventarioView()
    sys.exit(app.exec_())
