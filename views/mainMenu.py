import sys

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget

from db import dbController as db
from views import loginView as lv, calendarioView as cal
from views import profileView as profile
from views import inventarioView as inv
from views import personnelManagementView as perman


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
        self.starting_label = None
        self.title = 'Main Menu'
        self.width = 450
        self.height = 300
        self.starting_distance = 50

        # Manda alla view del calendario
        self.calendar_button= QPushButton(self)
        # Manda alla gestione personale
        self.personnelManagement_button = QPushButton(self)
        # Manda alla view del profilo
        self.profile_button = QPushButton(self)
        # Manda all'inventario
        self.inventory_button = QPushButton(self)
        # Manda al login
        self.logout_button = QPushButton(self)

        self.init_ui()
        self.control_check()
        self.instruction()

    def init_ui(self):
        self.setWindowTitle(self.title)


        local_buttons = [self.calendar_button, self.personnelManagement_button, self.profile_button, self.inventory_button, self.logout_button]
        local_buttons_name = ['Calendario', 'Gestione Personale', 'Profilo', 'Inventario', 'Logout']
        btn_dim = [120, 90]
        for elem in range(len(local_buttons)):
            local_buttons[elem].setText(local_buttons_name[elem])
            local_buttons[elem].resize(*btn_dim)
        btn_row1 = [self.calendar_button, self.inventory_button, self.profile_button]
        btn_row2 = [self.personnelManagement_button, self.logout_button]

        self.positioning(btn_row1, self.starting_distance)

        self.positioning(btn_row2, self.starting_distance + btn_dim[1] + 30)

        self.setFixedWidth(self.width)
        self.setFixedHeight(btn_row2[0].y() + btn_row2[0].height() + self.starting_distance)

        self.show()

    def positioning(self, element, selected_height):
        lenght_sum = 0
        for elem in range(len(element)):
            if elem ==0:
                lenght_sum +=50
            element[elem].move(lenght_sum, selected_height)
            lenght_sum +=element[elem].width() + 30
        if lenght_sum +20 > self.width:
            self.width = lenght_sum +20

        print(lenght_sum)
    def control_check(self):
        self.buttons = [self.calendar_button, self.personnelManagement_button, self.profile_button, self.inventory_button]
        atleta_opt = [False, True, False, False]
        istruttore_opt = [False, True, False, False]
        admin_opt = [False, False, False, False]
        disabled_opt = [True, True, True, True]
        #In caso di mancato login, disabilita tutti i pulsanti tranne quello del logout
        if self.flag is False:
            self.disabler(buttons=self.buttons, opt= disabled_opt)
        elif self.user_type == 'Atleta':
            self.disabler(buttons=self.buttons, opt=atleta_opt)
            self.personnelManagement_button.hide()
        elif self.user_type == "Istruttore":
            self.disabler(buttons=self.buttons, opt=istruttore_opt)
            self.personnelManagement_button.hide()
            self.market_button.hide()
        elif self.user_type == "Admin":
            self.disabler(buttons=self.buttons, opt=admin_opt)
        else:
            self.disabler(buttons=self.buttons, opt=disabled_opt)
            self.calendar_button.hide()
            self.personnelManagement_button.hide()
            self.profile_button.hide()
            self.market_button.hide()
            self.inventory_button.hide()

    def disabler(self, buttons, opt):
        for elem in range(len(buttons)):
            buttons[elem].setDisabled(opt[elem])

    def instruction(self):
        self.calendar_button.clicked.connect(self.toCalendar)
        self.personnelManagement_button.clicked.connect(self.toPersonnelManagement)
        self.profile_button.clicked.connect(self.toProfile)
        self.inventory_button.clicked.connect(self.toInventory)
        self.logout_button.clicked.connect(self.toLogout)

    def toCalendar(self):
        self.screen = cal.mainWindow(username=self.username)
        self.screen.show()
        self.close()

    def toPersonnelManagement(self):
        self.screen = perman.PersonnelManagementView(username=self.username)
        self.screen.show()
        self.close()

    def toProfile(self):
        self.screen = profile.ProfileView(profile_name=self.username)
        self.screen.show()
        self.close()

    def toInventory(self):
        self.screen = inv.inventarioView(username=self.username)
        self.screen.show()
        self.close()

    def toLogout(self):
        self.screen = lv.LoginView()
        self.screen.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu(username= 'root1')
    sys.exit(app.exec_())