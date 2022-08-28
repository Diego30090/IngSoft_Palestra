import sys
from views import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QGroupBox, QVBoxLayout


class ProfileView(QWidget):

    def __init__(self):
        super().__init__()
        # Window settings
        self.title = 'Profilo'
        self.width = 400
        self.height = 300
        # Starting Distance Layout
        self.starting_height_distance = 30
        self.fixed_left_distance = 75
        self.fixed_height_distance = 30
        self.left_line_distance = 190

        # Field Label
        self.name_label = None
        self.surname_label = None
        self.born_data_label = None
        self.username_label = None
        self.address_label = None
        self.email_label = None
        self.phone_label = None
        self.user_type_label = None

        # User info
        self.name_info = None
        self.surname_info = None
        self.born_data_info = None
        self.username_info = None
        self.address_info = None
        self.email_info = None
        self.phone_info = None
        self.user_type_info = None

        # Pulsanti Profilo
        self.edit_profile_button = None
        self.menu_button = None

        # Aggiunte per la modifica del Profilo
        self.confirm_button = None
        self.confirm_password_label = None
        self.confirm_password_info = None

        # item initializers and item commands
        self.login_ui()
        self.instruction()
        self.disabler()

    def login_ui(self):
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        # Sezione Nome
        self.name_label = QLabel('Nome: ', self)
        self.name_info = QLineEdit(self)

        # Sezione Cognome
        self.surname_label = QLabel('Cognome: ', self)
        self.surname_info = QLineEdit(self)

        # Sezione Data di Nascita
        self.born_data_label = QLabel('Data di nascita: ', self)
        self.born_data_info = QLineEdit(self)

        # Sezione Indirizzo
        self.address_label = QLabel('Indirizzo: ', self)
        self.address_info = QLineEdit(self)

        # Sezione Email
        self.email_label = QLabel('Email: ', self)
        self.email_info = QLineEdit(self)

        # Sezione user_type
        self.user_type_label = QLabel('Tipologia di Utente: ', self)
        self.user_type_info = QLineEdit(self)

        # Pulsanti
        self.edit_profile_button = QPushButton('Modifica Profilo', self)
        self.menu_button = QPushButton('Torna al Menu', self)

        self.init_distance()
        self.show()

    def init_distance(self):
        # Label User
        self.name_label.move(self.fixed_left_distance, self.starting_height_distance)
        self.surname_label.move(self.fixed_left_distance, self.name_label.y() + self.fixed_height_distance)
        self.born_data_label.move(self.fixed_left_distance, self.surname_label.y() + self.fixed_height_distance)
        self.address_label.move(self.fixed_left_distance, self.born_data_label.y() + self.fixed_height_distance)
        self.email_label.move(self.fixed_left_distance, self.address_label.y() + self.fixed_height_distance)
        self.user_type_label.move(self.fixed_left_distance, self.email_label.y() + self.fixed_height_distance)

        # Info User
        self.name_info.move(self.left_line_distance, self.starting_height_distance)
        self.surname_info.move(self.left_line_distance, self.surname_label.y())
        self.born_data_info.move(self.left_line_distance, self.born_data_label.y())
        self.address_info.move(self.left_line_distance, self.address_label.y())
        self.email_info.move(self.left_line_distance, self.email_label.y())
        self.user_type_info.move(self.left_line_distance, self.user_type_label.y())

        # Pulsanti
        self.edit_profile_button.move(self.user_type_label.x() + 20, self.user_type_label.y() + 50)
        self.menu_button.move(self.user_type_label.x()+145, self.user_type_label.y() + 50)


    def disabler(self):
        self.name_info.setDisabled(True)
        self.surname_info.setDisabled(True)
        self.born_data_info.setDisabled(True)
        #self.username_info.setDisabled(True)
        self.address_info.setDisabled(True)
        self.email_info.setDisabled(True)
        #self.phone_info.setDisabled(True)
        self.user_type_info.setDisabled(True)

    def enabler(self):
        # Disabilitazione dei vari pulsanti
        self.name_info.setDisabled(False)
        self.surname_info.setDisabled(False)
        self.born_data_info.setDisabled(False)
        # self.username_info.setDisabled(False)
        self.address_info.setDisabled(False)
        self.email_info.setDisabled(False)
        # self.phone_info.setDisabled(True)

        # Da abilitare solo se lo user_type è Admin
        self.user_type_info.setDisabled(True)

    def instruction(self):
        self.edit_profile_button.clicked.connect(self.edit_profile)

    def edit_profile(self):
        self.enabler()

        self.confirm_button = QPushButton('Salva', self)
        self.confirm_button.show()
        self.confirm_password_label = QLabel('Conferma la Password', self)
        self.confirm_password_label.show()
        self.confirm_password_info = QLineEdit(self)


        self.confirm_password_info.show()
        #self.confirm_password_info.move()
        #self.confirm_password_label.move()

        # Hide dei vari pulsanti
        self.edit_profile_button.hide()
        self.menu_button.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProfileView()
    sys.exit(app.exec_())