import sys
from views import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QGroupBox, QVBoxLayout, QGridLayout, \
    QSizePolicy
from PyQt5.QtCore import *


class ProfileView(QWidget):

    def __init__(self):
        super().__init__()
        # Starting Distance Layout
        self.starting_height_distance = 30
        self.fixed_left_distance = 75
        self.fixed_height_distance = 30
        self.left_line_distance = 190

        self.standard_line_height = 20
        self.standard_line_width = 120

        self.starting_confirm_distance = 330
        self.show()

        self.label = QLabel("Test", self)
        self.label.show()

        # Field Label
        self.name_label = QLabel(self)
        self.surname_label = QLabel(self)
        self.born_data_label = QLabel(self)
        self.username_label = QLabel(self)
        self.address_label = QLabel(self)
        self.email_label = QLabel(self)
        self.phone_label = QLabel(self)
        self.user_type_label = QLabel(self)

        # User info
        #self.username_info = None
        self.name_info = QLineEdit(self)
        self.surname_info = QLineEdit(self)
        self.born_data_info = QLineEdit(self)
        self.address_info = QLineEdit(self)
        self.email_info = QLineEdit(self)
        self.phone_info = QLineEdit(self)
        self.user_type_info = QLineEdit(self)

        # Pulsanti Profilo
        self.edit_profile_button = None
        self.menu_button = None

        # Oggetti view Modifica profilo
            # Campi da compilare
        self.new_name = QLineEdit(self)
        self.new_surname = QLineEdit(self)
        self.new_born_data = QLineEdit(self)
        # self.new_username = QLineEdit(self)
        self.new_address = QLineEdit(self)
        self.new_email = QLineEdit(self)
        self.new_phone = QLineEdit(self)
        self.new_user_type = QLineEdit(self)
            # Pulsanti
        self.confirm_button = None
        self.confirm_password_label = None
        self.confirm_password_info = None
        self.err_label = None

        # Element Serialization
        self.field_labels_obj = [self.name_label, self.surname_label, self.born_data_label,
                                 self.address_label, self.email_label, self.phone_label, self.user_type_label]
        self.field_labels_name = ['Nome: ', 'Cognome: ', 'Data di Nascita: ', 'Indirizzo: ', 'Email: ', 'Telefono: ',
                                  'Tipologia di Utente: ']
        self.field_line_obj = [self.name_info, self.surname_info, self.born_data_info, self.address_info,
                               self.email_info, self.phone_info, self.user_type_info]
        self.new_line_obj = [self.new_name, self.new_surname, self.new_born_data, self.new_address, self.new_email,
                             self.new_phone, self.new_user_type]

        # item initializers and item commands
        self.profile_view_settings()
        self.profile_item_def()
        self.instruction()
        self.edit_profile_item_def()

    def profile_view_settings(self):
        self.setWindowTitle('Profilo')
        self.setFixedWidth(400)
        self.setFixedHeight(320)

    def edit_profile_view_geometry(self):
        self.setWindowTitle('Modifica Profilo')
        self.setFixedWidth(510)
        self.setFixedHeight(320)

    def profile_item_def(self):
        # Setting Nome della label
        for label in range(len(self.field_labels_obj)):
            self.field_labels_obj[label].setText(self.field_labels_name[label])

        # Pulsanti
        self.edit_profile_button = QPushButton('Modifica Profilo', self)
        self.menu_button = QPushButton('Torna al Menu', self)

        self.prof_item_geometry()

    def prof_item_geometry(self):
        # set position of labels
        for label in range(len(self.field_labels_obj)):
            if label == 0:
                self.field_labels_obj[label].move(self.fixed_left_distance, self.starting_height_distance)
                self.field_labels_obj[label].show()
            else:
                self.field_labels_obj[label].move(self.fixed_left_distance, self.field_labels_obj[label - 1].y() + self.fixed_height_distance)
                self.field_labels_obj[label].show()

        # set position of info elem
        for elem in range(len(self.field_line_obj)):
            self.field_line_obj[elem].setGeometry(self.left_line_distance, self.field_labels_obj[elem].y(), self.standard_line_width, self.standard_line_height)
            self.field_line_obj[elem].setDisabled(True)
            self.field_line_obj[elem].show()

        self.label.move(int((self.width() - self.label.width())/2),0)
        print(self.label.x())


        # Pulsanti
        self.edit_profile_button.move(self.user_type_label.x() + 20, self.user_type_label.y() + 50)
        self.menu_button.move(self.user_type_label.x()+145, self.user_type_label.y() + 50)

        self.edit_profile_button.show()
        self.menu_button.show()

    def edit_profile_item_def(self):
        # Conferma password per salvare i dati
        self.confirm_password_label = QLabel('Conferma la Password', self)
        self.confirm_password_label.setStyleSheet("font: bold")
        # Campo inserimento password di conferma
        self.confirm_password_info = QLineEdit(self)
        self.confirm_password_info.setProperty("mandatoryField", True)
        self.confirm_password_info.setEchoMode(QLineEdit.Password)

        # Label di Errore
        self.err_label = QLabel('Errore: ', self)
        self.err_label.setStyleSheet("color: red")

        # Pulsante salvataggio dati
        self.confirm_button = QPushButton('Salva', self)

    def edit_prof_item_geometry(self):
        for elem in range(len(self.new_line_obj)):
            self.new_line_obj[elem].setGeometry(self.starting_confirm_distance, self.field_line_obj[elem].y(), self.standard_line_width, self.standard_line_height)
            self.new_line_obj[elem].show()

        # Conferma della Password
        '''
        self.confirm_password_label.move(self.fixed_left_distance - 30,
                                         self.user_type_label.y() + self.fixed_height_distance)
        self.confirm_password_info.setGeometry(self.left_line_distance,
                                               self.user_type_label.y() + self.fixed_height_distance,
                                               self.standard_line_width, self.standard_line_height)
        # label di Errore
        self.err_label.move(self.left_line_distance - 40, self.confirm_password_label.y() + self.fixed_height_distance)
        # Pulsante di Conferma
        self.confirm_button.move(self.left_line_distance, self.err_label.y() + self.fixed_height_distance)
        '''

    def instruction(self):
        self.edit_profile_button.clicked.connect(self.edit_profile)
        #self.confirm_button.clicked.connect(self.salva)

    def edit_profile(self):
        print('change to edit_profile')
        self.edit_profile_view_geometry()
        self.edit_profile_item_def()
        self.edit_prof_item_geometry()

    def salva(self):
        self.profile_view_settings()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProfileView()
    sys.exit(app.exec_())