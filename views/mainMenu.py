import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget


class MainMenu(QWidget):

    def __init__(self):
        super().__init__()

        self.starting_label = None
        self.title = 'Main Menu'
        self.width = 300
        self.height = 150
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        self.starting_label = QLabel('Label di prova del menu iniziale', self)
        self.starting_label.move(60, 30)

        self.show()

    def login_clicked(self):
        print('prova1')