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

    def show_tab(self, tab_type):

        if tab_type == 'armi':
            self.table_column = ['Giacenza', 'Disponibilità', 'Arma', 'D/S', 'Materiale', 'Lunghezza', 'Produttore',
                                 'Impugnatura']
        elif tab_type == 'divise':
            self.table_column = ['Giacenza', 'Disponibilità', 'Elemento', 'D/S', 'Arma', 'Taglia', 'Sesso',
                                 'Produttore']
        elif tab_type == 'borsoni':
            self.table_column = ['Giacenza', 'Disponibilità', 'Attrezzatura', 'Produttore']
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = inventarioView()
    sys.exit(app.exec_())


class insertArmaWindow (QWidget):

    def __init__(self):
    # Window settings
        self.title = 'Inserisci Arma'
        self.width = 400
        self.height = 500
    # Item settings
        self.giacenza_label = None
        self.disponibilita_label = None
        self.arma_label = None
        self.ds_label = None
        self.materiale_label = None
        self.lunghezza_label = None
        self.produttore_label = None
        self.impugnatura_label = None

        self.giacenza_text = None
        self.disponibilita_text = None
        self.arma_text = None
        self.ds_text = None
        self.materiale_text = None
        self.lunghezza_text = None
        self.produttore_text = None
        self.impugnatura_text = None

        self.button_fixed_height = 90
        self.button_fixed_width = 120

        self.accept_button = None
        self.back_button = None
    #Button distances
        self.verticalDistance = 50
        self.horizontalLabelDistance = 50
        self.horizontalTextDistance = 200

    def insertArmaUI (self):

        self.giacenza_label = QLabel('Giacenza', self)
        self.giacenza_label.move(self.horizontalLabelDistance, self.verticalDistance)

        self.disponibilita_label = QLabel('Disponibilità', self)
        self.disponibilita_label.move(self.horizontalLabelDistance, self.giacenza_label.y() + self.verticalDistance)

        self.arma_label = QLabel('Arma', self)
        self.arma_label.move(self.horizontalLabelDistance, self.disponibilita_label.y() + self.verticalDistance)

        self.ds_label = QLabel('D/S', self)
        self.ds_label.move(self.horizontalLabelDistance, self.arma_label.y() + self.verticalDistance)

        self.materiale_label = QLabel('Materiale', self)
        self.materiale_label.move(self.horizontalLabelDistance, self.ds_label.y() + self.verticalDistance)

        self.lunghezza_label = QLabel('Lunghezza', self)
        self.lunghezza_label.move(self.horizontalLabelDistance, self.materiale_label.y() + self.verticalDistance)

        self.produttore_label = QLabel('Produttore', self)
        self.produttore_label.move(self.horizontalLabelDistance, self.lunghezza_label.y() + self.verticalDistance)

        self.impugnatura_label = QLabel('Impugnatura', self)
        self.impugnatura_label.move(self.horizontalLabelDistance, self.produttore_label.y() + self.verticalDistance)

        self.giacenza_text = QLineEdit(self)
        self.giacenza_text.move(self.horizontalTextDistance, self.verticalDistance)
        self.giacenza_text.setFixedHeight(20)

        self.disponibilita_text = QLineEdit(self)
        self.disponibilita_text.move(self.horizontalTextDistance, self.giacenza_text.y() + self.verticalDistance)
        self.disponibilita_text.setFixedHeight(20)

        self.arma_text = QLineEdit(self)
        self.arma_text.move(self.horizontalTextDistance, self.disponibilita_text.y() + self.verticalDistance)
        self.arma_text.setFixedHeight(20)

        self.ds_text = QLineEdit(self)
        self.ds_text.move(self.horizontalTextDistance, self.arma_text.y() + self.verticalDistance)
        self.ds_text.setFixedHeight(20)

        self.materiale_text = QLineEdit(self)
        self.materiale_text.move(self.horizontalTextDistance, self.ds_text.y() + self.verticalDistance)
        self.materiale_text.setFixedHeight(20)

        self.lunghezza_text = QLineEdit(self)
        self.lunghezza_text.move(self.horizontalTextDistance, self.materiale_text.y() + self.verticalDistance)
        self.lunghezza_text.setFixedHeight(20)

        self.produttore_text = QLineEdit(self)
        self.produttore_text.move(self.horizontalTextDistance, self.lunghezza_text.y() + self.verticalDistance)
        self.produttore_text.setFixedHeight(20)

        self.impugnatura_text = QLineEdit(self)
        self.impugnatura_text.move(self.horizontalTextDistance, self.produttore_text.y() + self.verticalDistance)
        self.impugnatura_text.setFixedHeight(20)

        self.accept_button = QPushButton('Accetta', self)
        self.accept_button.setFixedHeight(self.button_fixed_height)
        self.accept_button.setFixedWidth(self.button_fixed_width)
        self.accept_button.move(self.horizontalLabelDistance, self.impugnatura_label.y() + self.verticalDistance)
        self.accept_button.setStyleSheet("background: rgb(140,255,70);")

        self.back_button = self.accept_button = QPushButton('Indietro', self)
        self.back_button.setFixedHeight(self.button_fixed_height)
        self.back_button.setFixedWidth(self.button_fixed_width)
        self.back_button.move(self.horizontalTextDistance, self.impugnatura_label.y() + self.verticalDistance)
        self.back_button.setStyleSheet("background: rgb(140,255,70);")

        self.show()




