import sys
import os
from PyQt5.QtWidgets import QApplication
from Boundaries.GestioneUtente import loginView as login

if __name__ == '__main__':
    # Da inserire accountController e generalizzare il tutto
    os.chdir('Boundaries/GestioneUtente')
    app = QApplication(sys.argv)
    ex = login.LoginView()
    sys.exit(app.exec_())

# https://drive.google.com/drive/folders/10wTUP52GmpR36XTljvt4heKkZB6CpK5f?usp=sharing
