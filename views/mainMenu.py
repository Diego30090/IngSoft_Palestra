import sys

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget
from db import dbController as db
from views import loginView as lv
from views import profileView as profile


class MainMenu(QWidget):

    def __init__(self, username):
        super().__init__()
        #login check
        if username is None:
            self.username = None
            self.flag = False
            self.user_type = None
        else:
            self.username = username
            self.flag = True
            self.user_type = db.user_type(self.username)
        print(self.user_type)
        self.starting_label = None
        self.title = 'Main Menu'
        self.width = 450
        self.height = 300

        # Manda alla view del calendario
        self.calendar_button= None
        # Manda alla gestione personale
        self.personnelManagement_button = None
        # Manda alla view del profilo
        self.profile_button = None
        # Manda al Mercato
        self.market_button = None
        # Manda all'inventario
        self.inventory_button = None
        # Manda al login
        self.logout_button = None

        #Label di prova
        self.trial_label = None
        self.init_ui()
        self.control_check()
        self.instruction()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        self.calendar_button = QPushButton('Calendario', self)
        self.calendar_button.move(0, 0)

        self.personnelManagement_button = QPushButton('Gestione Personale', self)
        self.personnelManagement_button.move(100, 0)

        self.profile_button = QPushButton('Profilo', self)
        self.profile_button.move(200, 0)

        self.market_button = QPushButton('Mercato', self)
        self.market_button.move(0, 50)

        self.inventory_button = QPushButton('Inventario', self)
        self.inventory_button.move(100, 50)

        self.logout_button = QPushButton('Logout', self)
        self.logout_button.move(200, 50)

        self.trial_label = QLabel('prova1', self)
        self.trial_label.setText(self.username)
        self.trial_label.move(300, 200)



        self.show()

    def control_check(self):
        #In caso di mancato login, disabilita tutti i pulsanti tranne quello del logout
        if self.flag is False:
            self.calendar_button.setDisabled(True)
            self.personnelManagement_button.setDisabled(True)
            self.profile_button.setDisabled(True)
            self.market_button.setDisabled(True)
            self.inventory_button.setDisabled(True)
        elif self.user_type == 'Atleta':
            self.calendar_button.setDisabled(False)
            self.personnelManagement_button.setDisabled(True)
            self.profile_button.setDisabled(False)
            self.market_button.setDisabled(False)
            self.inventory_button.setDisabled(False)
            self.personnelManagement_button.hide()
        elif self.user_type == "Istruttore":
            self.calendar_button.setDisabled(False)
            self.personnelManagement_button.setDisabled(True)
            self.profile_button.setDisabled(False)
            self.market_button.setDisabled(True)
            self.inventory_button.setDisabled(False)
            self.personnelManagement_button.hide()
            self.market_button.hide()
        elif self.user_type == "Admin":
            self.calendar_button.setDisabled(False)
            self.personnelManagement_button.setDisabled(False)
            self.profile_button.setDisabled(False)
            self.market_button.setDisabled(False)
            self.inventory_button.setDisabled(False)
        else:
            self.calendar_button.setDisabled(True)
            self.personnelManagement_button.setDisabled(True)
            self.profile_button.setDisabled(True)
            self.market_button.setDisabled(True)
            self.inventory_button.setDisabled(True)
            self.calendar_button.hide()
            self.personnelManagement_button.hide()
            self.profile_button.hide()
            self.market_button.hide()
            self.inventory_button.hide()
    def instruction(self):
        self.calendar_button.clicked.connect(self.toCalendar)
        self.personnelManagement_button.clicked.connect(self.toPersonnelManagement)
        self.profile_button.clicked.connect(self.toProfile)
        self.market_button.clicked.connect(self.toMarket)
        self.inventory_button.clicked.connect(self.toInventory)
        self.logout_button.clicked.connect(self.toLogout)
    def toCalendar(self):
        self.screen = QWidget()
        self.screen.trial_label = QLabel("View di prova del calendario", self.screen)
        self.screen.setFixedWidth(300)
        self.screen.setFixedHeight(200)
        self.screen.show()
        self.close()

    def toPersonnelManagement(self):
        self.screen = QWidget()
        self.screen.trial_label = QLabel("View di prova della Gestione del Personale", self.screen)
        self.screen.setFixedWidth(300)
        self.screen.setFixedHeight(200)
        self.screen.show()
        self.close()

    def toProfile(self):
        self.screen = profile.ProfileView(profile_name=self.username)
        self.screen.show()
        self.close()


    def toMarket(self):
        self.screen = QWidget()
        self.screen.trial_label = QLabel("View di prova del Mercato", self.screen)
        self.screen.setFixedWidth(300)
        self.screen.setFixedHeight(200)
        self.screen.show()
        self.close()
    def toInventory(self):
        self.screen = QWidget()
        self.screen.trial_label = QLabel("View di prova dell'inventario", self.screen)
        self.screen.setFixedWidth(300)
        self.screen.setFixedHeight(200)
        self.screen.show()
        self.close()

    def toLogout(self):
        self.screen = lv.MainView()
        self.screen.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu(username= 'root0')
    sys.exit(app.exec_())