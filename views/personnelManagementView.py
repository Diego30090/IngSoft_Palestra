import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class PersonnelManagementView(QWidget):
    def __init__(self):
        super().__init__()
        # Definizione dei vari elementi
        self.lista_atleta_button = QPushButton(self)
        self.lista_istruttori_button = QPushButton(self)
        self.lista_amministratori_button = QPushButton(self)
        self.button_list= [self.lista_atleta_button, self.lista_istruttori_button, self.lista_amministratori_button]
        self.button_list_name = ['Lista Atleti', 'Lista Istruttori', 'Lista Amministratori']

        # Initializer proprietà e istruzioni della view
        self.view_geom_init()
        self.init_ui()

    def init_ui(self):
        for i in range(len(self.button_list)):
            self.button_list[i].setText(self.button_list_name[i])
            self.button_list[i].adjustSize()
        self.show()
        self.item_geom_init()

    def view_geom_init(self):
        self.setWindowTitle('Gestione Personale')
        self.setFixedHeight(400)
        self.setFixedWidth(500)

    def item_geom_init(self):
        self.dimension = 120
        self.starting_height = 50
        self.starting_width = 50
        for i in range(len(self.button_list)):
            if i==0:
                self.button_list[i].setGeometry(self.starting_width, self.starting_height, self.dimension, self.dimension)
            else:
                self.button_list[i].setGeometry(self.button_list[i-1].width() + self.button_list[i-1].x()+30, self.starting_height, self.dimension, self.dimension)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PersonnelManagementView()
    sys.exit(app.exec_())