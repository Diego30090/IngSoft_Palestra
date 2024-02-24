import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi
from Boundaries.GestioneUtente import loginView as lv, profileView as profile
from Boundaries.GestioneInformazioniPersonale import personnelManagementView as perman
from Boundaries.GestioneCalendario import VistaCalendario as cal
from Boundaries.GestioneInventario import InventarioView as inv
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as AccountController
from Boundaries.GestionePagamenti import elencoPagamenti as elepag
from Boundaries.GestioneNotifiche import elencoNotifiche as en

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
        loadUi("../GestioneUtente/mainMenu.ui", self)
        self.show()
        # self.initUi()

        self.controlCheck()
        self.instruction()

    def controlCheck(self):
        self.buttons = [self.calendar_button, self.personnelManagement_button, self.profile_button,
                        self.inventory_button, self.gestionePagamenti_button, self.notifiche_button]
        atleta_opt = [False, True, False, False, False, False]
        istruttore_opt = [False, False, False, False, False, False]
        admin_opt = [False, False, False, False, False, False]
        disabled_opt = [True, True, True, True, True, True]
        # In caso di mancato login, disabilita tutti i pulsanti tranne quello del logout
        if self.flag is False:
            self.disabler(buttons=self.buttons, opt=disabled_opt)
        elif self.userController.utente.getUtenteTipo() == 'Atleta':
            self.disabler(buttons=self.buttons, opt=atleta_opt)
            self.personnelManagement_button.hide()
        elif self.userController.utente.getUtenteTipo() == "Istruttore":
            self.disabler(buttons=self.buttons, opt=istruttore_opt)
        elif self.userController.utente.getUtenteTipo() == "Admin":
            self.disabler(buttons=self.buttons, opt=admin_opt)
        else:
            self.disabler(buttons=self.buttons, opt=disabled_opt)

    def disabler(self, buttons, opt):
        for elem in range(len(buttons)):
            buttons[elem].setDisabled(opt[elem])

    def instruction(self):
        self.calendar_button.clicked.connect(self.toCalendar)
        self.personnelManagement_button.clicked.connect(self.toPersonnelManagement)
        self.profile_button.clicked.connect(self.toProfile)
        self.inventory_button.clicked.connect(self.toInventory)
        self.logout_button.clicked.connect(self.toLogout)
        self.gestionePagamenti_button.clicked.connect(self.toGestionePagamenti)
        self.notifiche_button.clicked.connect(self.toNotifiche)

    def toCalendar(self):
        self.screen = cal.VistaCalendario(accountController=self.userController)
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

    def toGestionePagamenti(self):
        self.screen = elepag.ElencoPagamenti(accountController=self.userController)
        self.screen.show()
        self.close()

    def toNotifiche(self):
        self.screen = en.ElencoNotifiche(accountController=self.userController)
        self.screen.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu(userController=AccountController('root0', '0000'))
    sys.exit(app.exec_())
