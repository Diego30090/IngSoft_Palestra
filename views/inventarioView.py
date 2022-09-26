import sys

from PyQt5.QtCore import Qt
import numpy as np
from views import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QTableWidget, QTableWidgetItem, \
                            QComboBox

class inventarioView(QWidget):

    def __init__(self, username):
        self.username = username
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
        self.tab_name = None
        self.insert_window = None
        self.table_on = False
        # item initializers and item commands
        self.inventario_UI()
        self.instruction()


    def inventario_UI(self):
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

        self.modify_button = QPushButton('Modifica', self)
        self.modify_button.setFixedHeight(self.button_fixed_height)
        self.modify_button.setFixedWidth(self.button_fixed_width)
        self.modify_button.move(self.armi_button.x() + self.button_horizontal_distance, 580)
        self.modify_button.setStyleSheet("background: rgb(255,255,70);")

    def instruction(self):
        self.armi_button.clicked.connect(lambda: self.show_tab('armi'))
        self.divise_button.clicked.connect(lambda: self.show_tab('divise'))
        self.borsoni_button.clicked.connect(lambda: self.show_tab('borsoni'))
        self.create_button.clicked.connect(lambda: self.insMod(False))
        if self.table_on is True:
            self.display_table.cellClicked.connect(lambda: self.selectRow)
        self.back_button.clicked.connect(self.toMainMenu)

    def show_tab(self, tab_type):
        self.table_on = True

        if tab_type == 'armi':
            self.table_column = ['Giacenza', 'Disponibilità', 'Arma', 'D/S', 'Materiale', 'Lunghezza', 'Produttore',
                                 'Impugnatura']
        elif tab_type == 'divise':
            self.table_column = ['Giacenza', 'Disponibilità', 'Elemento', 'D/S', 'Arma', 'Taglia', 'Sesso',
                                 'Produttore']
        elif tab_type == 'borsoni':
            self.table_column = ['Giacenza', 'Disponibilità', 'Attrezzatura', 'Produttore']
        self.tab_name = tab_type
        lista = db.select_inventario(tab_type)
        self.display_table = QTableWidget(len(lista), len(self.table_column), self)
        self.display_table.move(80, 150)
        self.display_table.setFixedWidth(self.table_fixed_width)
        self.display_table.setFixedHeight(self.table_fixed_height)
        self.display_table.setHorizontalHeaderLabels(self.table_column)

        self.id_list = []
        for i in range(len(lista)):
            id_number = lista[i][0]
            for j in range(len(self.table_column)):
                item = QTableWidgetItem(str(lista[i][j+1]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.display_table.setItem(i, j, item)
            self.id_list.append(id_number)

        self.create_button.show()
        self.modify_button.show()
        self.display_table.show()




    def selectRow(self):
        print('selectrow partita')
        self.modify_button.show()
        position = self.display_table.currentRow()
        item = db.select_inventario_by_id(self.id_list[position], self.tab_name)
        item.pop(0)
        print(item)
        return item

    def insMod(self, info):
        self.insert_window = insModWindow(f'Inserisci {self.tab_name}', self.table_column, self.tab_name, info)
        self.insert_window.show()
        self.hide()

    def toMainMenu(self):
        self.screen = menu.MainMenu(username=self.username)
        self.screen.show()
        self.close()


#INSertMODifyWINDOW
class insModWindow(QWidget):

    def __init__(self, window_title, table_column, tab_name, info):
        super().__init__()
        self.item = info
        print(self.item)
    # Window settings
        self.title = window_title
        self.width = 370
        self.height = 650
    # Item settings
        self.labels = []
        self.texts = []
        self.tab_name = tab_name

        self.button_fixed_height = 90
        self.button_fixed_width = 120

        self.accept_button = None
        self.back_button = None

        self.verticalDistance = 50
        self.horizontalLabelDistance = 50
        self.horizontalTextDistance = 200

        self.insModUI(table_column)
        self.instruction()
        self.show()

    def insModUI(self, table_column):
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        for i in range(len(table_column)):

            new_label = QLabel(table_column[i], self)
            new_label.move(self.horizontalLabelDistance, self.verticalDistance)
            self.labels.append(new_label)

            if table_column[i] == 'D/S':
                new_combo = QComboBox(self)
                new_combo.addItem('D')
                new_combo.addItem('S')
                new_combo.addItem('/')
                new_combo.setFixedWidth(133)
                new_combo.move(self.horizontalTextDistance, self.verticalDistance)
                self.texts.append(new_combo)
            elif table_column[i] == 'Sesso':
                new_combo = QComboBox(self)
                new_combo.addItem('M')
                new_combo.addItem('F')
                new_combo.addItem('/')
                new_combo.setFixedWidth(133)
                new_combo.move(self.horizontalTextDistance, self.verticalDistance)
                '''if self.item != None:
                    AllItems = [new_combo.itemText(i) for i in range(new_combo.count())]
                    for elem in range(len(AllItems)):
                        if AllItems[elem] == self.item[i]:
                            new_combo.selected.AllItems[elem]'''

                self.texts.append(new_combo)
            else:
                new_text = QLineEdit(self)
                new_text.move(self.horizontalTextDistance, self.verticalDistance)
                '''if self.item != None:
                    new_text.text(self.item[i])'''
                self.texts.append(new_text)

            self.verticalDistance += 50
            self.labels[i].show()
            self.texts[i].show()

        new_label = QLabel('Descrizione', self)
        new_label.move(self.horizontalLabelDistance, self.verticalDistance)
        self.labels.append(new_label)
        new_text = QLineEdit(self)
        new_text.move(self.horizontalTextDistance, self.verticalDistance)
        self.texts.append(new_text)

        self.accept_button = QPushButton('Accetta', self)
        self.accept_button.setFixedHeight(self.button_fixed_height)
        self.accept_button.setFixedWidth(self.button_fixed_width)
        self.accept_button.move(self.horizontalLabelDistance, 520)
        self.accept_button.setStyleSheet("background: rgb(140,255,70);")

        self.back_button = QPushButton('Indietro', self)
        self.back_button.setFixedHeight(self.button_fixed_height)
        self.back_button.setFixedWidth(self.button_fixed_width)
        self.back_button.move(self.horizontalTextDistance, 520)
        self.back_button.setStyleSheet("background: rgb(255,70,70);")

    def save_infos(self):
        info = []
        for i in range(len(self.texts)):
            if isinstance(self.texts[i], QLineEdit):
                info.append(self.texts[i].text())
            elif isinstance(self.texts[i], QComboBox):
                info.append(self.texts[i].currentText())
        db.insert_inventario(self.tab_name, info)
        self.close_this()

    def instruction(self):
        self.back_button.clicked.connect(lambda: self.close_this())
        self.accept_button.clicked.connect(lambda: self.save_infos())

    def close_this(self):
        ex.show()
        ex.show_tab(tab_type=ex.tab_name)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    '''item = db.select_inventario_by_id(1, 'armi')
    item = item[1:]
    item = np.asarray(item)
    item = item.flatten()
    print(item)'''
    ex = inventarioView(username='root0')
    '''ix = insModWindow('Inserisci arma', ['Giacenza', 'Disponibilità', 'Arma', 'D/S', 'Materiale', 'Lunghezza', 'Produttore',
                                 'Impugnatura'],'armi', item)'''
    sys.exit(app.exec_())

