import sys
from views import mainMenu as menu
from db import dbController as db
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget


class ProfileView(QWidget):

    def __init__(self):
        super().__init__()
        # Window settings
        self.title = 'Profilo'
        self.width = 500
        self.height = 450
        # Item settings
        self.name_label = None
        self.surname_label = None
        self.born_data_label = None
        self.username_label = None
        self.address_label = None
        self.email_label = None
        self.phone_label = None
        # item initializers and item commands
        self.login_ui()
        self.instruction()

    def login_ui(self):
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        self.show()

    def instruction(self):
        print('no instructions')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProfileView()
    sys.exit(app.exec_())