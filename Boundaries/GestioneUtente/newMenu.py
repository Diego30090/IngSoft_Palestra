import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem
from PyQt5.uic import loadUi
from Boundaries.GestioneUtente import loginView as lv, profileView as profile
from Boundaries.GestioneInformazioniPersonale import personnelManagementView as perman
from Boundaries.GestioneCalendario import VistaCalendario as cal
from Boundaries.GestioneInventario import InventarioView as inv
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as AccountController
from Boundaries.GestionePagamenti import elencoPagamenti as elepag
from Boundaries.GestioneNotifiche import elencoNotifiche as en
from Boundaries.GestioneUtente import mainMenu as menu
from Controller.GestioneUtente import GestoreMenu as gm

#Questo menù, assumendo una veste grafica non coerente nella relazione, non è da considerare una alpha.

class MainMenu(QWidget):

    def __init__(self, userController: AccountController):
        super().__init__()
        if userController.utente.getUsername() is None:
            self.userController = AccountController(None, None)
            self.flag = False
        else:
            self.userController = userController
            self.flag = True
        self.userController = userController
        loadUi("../GestioneUtente/newMenu.ui", self)
        self.show()
        self.instruction()

    def instruction(self):
        self.loadData()
        self.treeWidget.itemClicked.connect(self.changePage)
        self.LogoutButton.clicked.connect(self.logout)

    def loadData(self):
        self.UsernameText.setText(self.userController.utente.getUsername())
        self.TypeText.setText(self.userController.utente.getUtenteTipo())
        self.loadTable()



    # ----------------------------------------------
    '''
    Change Page section
    '''

    def changePage(self):
        name = self.treeWidget.currentItem().text(0)
        self.page(name)

    def page(self, name):
        if name == '1.1 - Visualizza Calendario Eventi':
            print(f'Pagina {name}')
        if name == '2.1 - Visualizza Personale':
            print(f'Pagina {name}')
        if name == '3.1 - Visualizza Inventario':
            print(f'Pagina {name}')
        if name == '4.1 - Visualizza Profilo':
            self.toProfile()
        if name == '4.2 - Modifica Profilo':
            print(f'Pagina {name}')
        if name == '5.1 - Visualizza Pagamenti':
            print(f'Pagina {name}')
        if name == '5.2 - Visualizza Multe':
            print(f'Pagina {name}')
        if name == '6.1 - Visualizza Notifiche':
            print(f'Pagina {name}')
        if name == '6.2 - Visualizza Log':
            print(f'Pagina {name}')

    # --------------------------------------------


    # Test inserimento dati su una QTreeView
    def loadTable(self):
        gestoreMenu = gm.GestoreMenu()
        data = gestoreMenu.menuDict
        items = []
        for key, values in data.items():
            item = QTreeWidgetItem([key])
            for value in values:
                child = QTreeWidgetItem([value])
                item.addChild(child)
            items.append(item)

        self.treeWidget.insertTopLevelItems(0, items)


    def logout(self):
        self.screen = lv.LoginView()
        self.screen.show()
        self.close()

    def toProfile(self):
        self.screen = profile.ProfileView(accountController=self.userController)
        self.screen.show()
        self.close()

    def toCalendar(self):
        self.screen = cal.VistaCalendario(accountController=self.userController)
        self.screen.show()
        self.close()

    def toPersonnelManagement(self):
        self.screen = perman.PersonnelManagementView(accountController=self.userController)
        self.screen.show()
        self.close()

    def toInventory(self):
        self.screen = inv.InventarioView(self.userController)
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
