import sys
from views import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QGroupBox, QVBoxLayout, QGridLayout, \
    QSizePolicy, QDateEdit
from PyQt5.QtCore import *
from general import dateFormatter as dat


class ProfileView(QWidget):

    def __init__(self, profile_name):
        super().__init__()
        self.username = profile_name
        # Starting Distance Layout
        self.starting_height_distance = 60
        self.fixed_left_distance = 75
        self.fixed_height_distance = 30
        self.left_line_distance = 190

        self.standard_line_height = 20
        self.standard_line_width = 120

        self.starting_confirm_distance = 330
        self.show()

        self.profile_name_label = QLabel(f"Profilo di {self.username}", self)

        # Field Label
        self.name_label = QLabel(self)
        self.surname_label = QLabel(self)
        self.born_data_label = QLabel(self)
        self.username_label = QLabel(self)
        self.email_label = QLabel(self)
        self.phone_label = QLabel(self)
        self.user_type_label = QLabel(self)

        # User info
        # self.username_info = None
        self.name_info = QLineEdit(self)
        self.surname_info = QLineEdit(self)
        self.born_data_info = QDateEdit(self)
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
        self.new_born_data = QDateEdit(self)
        # self.new_username = QLineEdit(self)
        self.new_email = QLineEdit(self)
        self.new_phone = QLineEdit(self)
        self.new_user_type = QLineEdit(self)
        # Pulsanti
        self.confirm_button = QPushButton(self)
        self.confirm_password_label = None
        self.confirm_password_info = None
        self.confirm_password_info2 = QLineEdit(self)
        self.err_label = None

        # Element Serialization
        self.field_labels_obj = [self.name_label, self.surname_label, self.born_data_label,
                                 self.email_label, self.phone_label, self.user_type_label]
        self.field_labels_name = ['Nome: ', 'Cognome: ', 'Data di Nascita: ', 'Email: ', 'Telefono: ',
                                  'Tipologia di Utente: ']
        self.field_line_obj = [self.name_info, self.surname_info, self.born_data_info,
                               self.email_info, self.phone_info, self.user_type_info]
        self.new_line_obj = [self.new_name, self.new_surname, self.new_born_data, self.new_email,
                             self.new_phone, self.new_user_type]

        # item initializers and item commands
        self.profile_view_settings()
        self.profile_item_def()
        self.instruction()
        self.edit_profile_item_def()

    def profile_view_settings(self):
        self.setWindowTitle('Profilo')
        self.setFixedWidth(400)
        self.setFixedHeight(350)

    def profile_item_def(self):
        # Setting Nome della label
        for label in range(len(self.field_labels_obj)):
            self.field_labels_obj[label].setText(self.field_labels_name[label])

        # Label Nome Profilo
        self.profile_name_label.setStyleSheet('font: bold; font-size: 14px')

        # Pulsanti
        self.edit_profile_button = QPushButton('Modifica Profilo', self)
        self.menu_button = QPushButton('Torna al Menu', self)

        self.prof_item_geometry()
        self.profile_data_init(name=self.username)

    def prof_item_geometry(self):
        # set position of labels
        for label in range(len(self.field_labels_obj)):
            if label == 0:
                self.field_labels_obj[label].move(self.fixed_left_distance, self.starting_height_distance)
                self.field_labels_obj[label].show()
            else:
                self.field_labels_obj[label].move(self.fixed_left_distance,
                                                  self.field_labels_obj[label - 1].y() + self.fixed_height_distance)
                self.field_labels_obj[label].show()

        # set position of info elem
        for elem in range(len(self.field_line_obj)):
            self.field_line_obj[elem].setGeometry(self.left_line_distance, self.field_labels_obj[elem].y(),
                                                  self.standard_line_width, self.standard_line_height)
            self.field_line_obj[elem].setDisabled(True)
            self.field_line_obj[elem].show()

        self.profile_name_label.adjustSize()
        self.profile_name_label.move(int((self.width() - self.profile_name_label.width()) / 2), 20)

        # Pulsanti
        self.edit_profile_button.move(self.user_type_label.x() + 20, self.user_type_label.y() + 50)
        self.menu_button.move(self.user_type_label.x() + 145, self.user_type_label.y() + 50)

        self.profile_name_label.show()
        self.edit_profile_button.show()
        self.menu_button.show()

    def edit_profile_view_geometry(self):
        self.setWindowTitle('Modifica Profilo')
        self.setFixedWidth(510)
        self.setFixedHeight(360)

    def edit_profile_item_def(self):
        # Conferma password per salvare i dati
        self.confirm_password_label = QLabel('Conferma la Password', self)
        self.confirm_password_label.setStyleSheet("font: bold")
        # Campo inserimento password di conferma
        self.confirm_password_info = QLineEdit(self)
        self.confirm_password_info.setProperty("mandatoryField", True)
        self.confirm_password_info.setEchoMode(QLineEdit.Password)
        self.confirm_password_info2.setEchoMode(QLineEdit.Password)

        # Label di Errore
        self.err_label = QLabel('Errore: ', self)
        self.err_label.setStyleSheet("color: red")

        # Pulsante salvataggio dati
        self.confirm_button.setText("Salva")

    def edit_prof_item_geometry(self):
        for elem in range(len(self.new_line_obj)):
            self.new_line_obj[elem].setGeometry(self.starting_confirm_distance, self.field_line_obj[elem].y(),
                                                self.standard_line_width, self.standard_line_height)

        # Conferma della Password
        self.confirm_password_label.move(self.fixed_left_distance - 30,
                                         self.user_type_label.y() + self.fixed_height_distance)
        self.confirm_password_info.setGeometry(self.left_line_distance,
                                               self.user_type_label.y() + self.fixed_height_distance,
                                               self.standard_line_width, self.standard_line_height)
        self.confirm_password_info2.setGeometry(self.starting_confirm_distance, self.confirm_password_info.y(),
                                                self.standard_line_width, self.standard_line_height)
        # label di Errore
        self.err_label.move(int((self.width() - self.err_label.width()) / 2),
                            self.confirm_password_label.y() + self.fixed_height_distance)

        # Pulsante di Conferma
        self.confirm_button.move(self.left_line_distance, self.err_label.y() + self.fixed_height_distance)
        # Label Nome Profilo
        self.profile_name_label.move(int((self.width() - self.profile_name_label.width()) / 2), 20)

        if self.user_type_info.text() == 'Admin':
            self.new_user_type.setDisabled(False)
        else:
            self.new_user_type.setDisabled(True)

    def instruction(self):
        self.edit_profile_button.clicked.connect(self.edit_profile)
        self.confirm_button.clicked.connect(self.salva)
        self.menu_button.clicked.connect(self.toMainMenu)

    def edit_profile(self):
        self.edit_profile_view_geometry()
        self.edit_profile_item_def()
        self.edit_prof_item_geometry()
        elem_to_hide = [self.edit_profile_button, self.menu_button]
        for i in range(len(elem_to_hide)):
            elem_to_hide[i].hide()
        for elem in range(len(self.new_line_obj)):
            self.new_line_obj[elem].show()
        # elem_to_show
        self.elem_to_show = [self.confirm_password_label, self.confirm_password_info,
                             self.confirm_password_info2, self.confirm_button]
        for i in range(len(self.elem_to_show)):
            self.elem_to_show[i].show()
        self.edit_profile_data_init()

    def profile_data_init(self, name):
        val = db.user_info(name)
        to_substitute = [val[1], val[2], val[3], val[8], val[9], val[6]]
        for elem in range(len(to_substitute)):
            if elem != 2:
                self.field_line_obj[elem].setText(to_substitute[elem])
            else:
                if to_substitute[2] is None:
                    self.field_line_obj[elem].setDate(QDate(1000, 1, 1))
                else:
                    self.field_line_obj[elem].setDate(dat.str_to_date(to_substitute[2]))

    def edit_profile_data_init(self):
        print('init profile data')
        # get from db
        for i in range(len(self.field_line_obj)):
            if i != 2:
                self.new_line_obj[i].setText(self.field_line_obj[i].text())
            else:
                self.new_line_obj[i].setDate(self.field_line_obj[i].date())

    def error(self, err):
        self.err_label.setText(err)
        self.err_label.adjustSize()
        self.err_label.move(int((self.width() - self.err_label.width()) / 2),
                            self.confirm_password_label.y() + self.fixed_height_distance)
        self.err_label.show()

    def salva(self):
        if self.confirm_password_info.text() == '' and self.confirm_password_info2.text() == '':
            error = 'Errore: Password non inserita'
            self.error(err=error)
        elif self.confirm_password_info.text() != self.confirm_password_info2.text():
            error = 'Errore: Password non corrispondente'
            self.error(err=error)
        elif self.confirm_password_info.text() == self.confirm_password_info2.text():
            # get pass from db
            if self.confirm_password_info.text() != db.user_pass(self.username):
                error = 'Errore: Password sbagliata'
                self.error(err=error)
            else:
                self.err_label.hide()
                db.update_user(self.new_name.text(), self.new_surname.text(),
                               self.new_born_data.date().toString('yyyy-MM-dd'),
                               self.new_email.text(), self.new_phone.text(), self.new_user_type.text(), self.username)
                for elem in range(len(self.new_line_obj)):
                    self.new_line_obj[elem].hide()
                for elem in range(len(self.elem_to_show)):
                    self.elem_to_show[elem].hide()
                self.profile_view_settings()
                self.prof_item_geometry()

    def toMainMenu(self):
        self.screen = menu.MainMenu(username=self.username)
        self.screen.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProfileView(profile_name= 'root0')
    sys.exit(app.exec_())


