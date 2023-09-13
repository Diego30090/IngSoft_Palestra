import sys
import os
from PyQt5.QtWidgets import QApplication
from Boundaries.GestioneUtente import loginView as login

if __name__ == '__main__':
    os.chdir('Boundaries/GestioneUtente')
    app = QApplication(sys.argv)
    ex = login.LoginView()
    sys.exit(app.exec_())
