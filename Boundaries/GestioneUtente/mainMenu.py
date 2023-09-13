import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget

from Boundaries.GestioneUtente import loginView as lv, profileView as profile
from Boundaries.GestioneInformazioniPersonale import personnelManagementView as perman
from Boundaries.GestioneCalendario import VistaCalendario as cal
from Boundaries.GestioneInventario import InventarioView as inv
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as AccountController


class MainMenu(QWidget):

    def __init__(self, userController: AccountController):
        super().__init__()
        # login check
        if userController.utente.getUsername() is None:
            self.userController = AccountController(None, None)
            self.flag = False
        else:
            self.userController = userController
            self.flag = True
        self.starting_label = None
        self.title = 'Main Menu'
        self.width = 450
        self.height = 300
        self.starting_distance = 50

        # Manda alla view del calendario
        self.calendar_button = QPushButton(self)
        # Manda alla gestione personale
        self.personnelManagement_button = QPushButton(self)
        # Manda alla view del profilo
        self.profile_button = QPushButton(self)
        # Manda all'inventario
        self.inventory_button = QPushButton(self)
        # Manda al login
        self.logout_button = QPushButton(self)

        self.initUi()
        self.controlCheck()
        self.instruction()

    def initUi(self):
        self.setWindowTitle(self.title)

        local_buttons = [self.calendar_button, self.personnelManagement_button, self.profile_button,
                         self.inventory_button, self.logout_button]
        local_buttons_name = ['Calendario', 'Gestione Personale', 'Profilo', 'Inventario', 'Logout']
        btn_dim = [120, 90]
        for elem in range(len(local_buttons)):
            local_buttons[elem].setText(local_buttons_name[elem])
            local_buttons[elem].resize(*btn_dim)
        btn_row1 = [self.calendar_button, self.inventory_button, self.profile_button]
        btn_row1_rgb = ['200,200,200', '200,200,200', '200,200,200']
        btn_row2 = [self.personnelManagement_button, self.logout_button]
        btn_row2_rgb = ['200,200,200', '255,70,70']
        self.itemPositioning(btn_row1, self.starting_distance, btn_row1_rgb)

        self.itemPositioning(btn_row2, self.starting_distance + btn_dim[1] + 30, btn_row2_rgb)

        self.setFixedWidth(self.width)
        self.setFixedHeight(btn_row2[0].y() + btn_row2[0].height() + self.starting_distance)

        self.show()

    def itemPositioning(self, element, selected_height, rgb):
        lenght_sum = 0
        for elem in range(len(element)):
            if elem == 0:
                lenght_sum += 50
            element[elem].move(lenght_sum, selected_height)
            lenght_sum += element[elem].width() + 30
            element[elem].setStyleSheet(f"background: rgb({rgb[elem]});")
        if lenght_sum + 20 > self.width:
            self.width = lenght_sum + 20

    def controlCheck(self):
        self.buttons = [self.calendar_button, self.personnelManagement_button, self.profile_button,
                        self.inventory_button]
        atleta_opt = [False, True, False, False]
        istruttore_opt = [False, True, False, False]
        admin_opt = [False, False, False, False]
        disabled_opt = [True, True, True, True]
        # In caso di mancato login, disabilita tutti i pulsanti tranne quello del logout
        if self.flag is False:
            self.disabler(buttons=self.buttons, opt=disabled_opt)
        elif self.userController.utente.getUtenteTipo() == 'Atleta':
            self.disabler(buttons=self.buttons, opt=atleta_opt)
            self.personnelManagement_button.hide()
        elif self.userController.utente.getUtenteTipo() == "Istruttore":
            self.disabler(buttons=self.buttons, opt=istruttore_opt)
            self.personnelManagement_button.hide()
            # self.market_button.hide()
        elif self.userController.utente.getUtenteTipo() == "Admin":
            self.disabler(buttons=self.buttons, opt=admin_opt)
        else:
            self.disabler(buttons=self.buttons, opt=disabled_opt)
            self.calendar_button.hide()
            self.personnelManagement_button.hide()
            self.profile_button.hide()
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
        self.screen = cal.VistaCalendario(accountController =self.userController)
        self.screen.show()
        self.close()

    def toPersonnelManagement(self):
        self.screen = perman.PersonnelManagementView(accountController=self.userController)
        self.screen.show()
        self.close()

    def toProfile(self):
        self.screen = profile.ProfileView(accountController=self.userController)
        self.screen.show()
        self.close()

    def toInventory(self):
        self.screen = inv.InventarioView(self.userController)
        self.screen.show()
        self.close()

    def toLogout(self):
        self.screen = lv.LoginView()
        self.screen.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu(userController=AccountController('root1', 'pwd'))
    sys.exit(app.exec_())
