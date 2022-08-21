import sqlite3
import sys
import event

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from mainCalendario import Ui_Window
from mainCalendarioSelezionato import Ui_SecondWindow

class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("mainCalendarioSelezionato.ui", self)
        self.modifyButton.clicked.connect(self.updateWidget)
        self.backButton.clicked.connect(self.backWindow)

    def updateWidget(self, date):
        self.tasksListWidget.clear()

        db = sqlite3.connect("DatabaseCalendario.db") #il collegamento
        cursor = db.cursor() #fa il query (cosa gli chiedo del database)

        query = "SELECT name, time FROM tasks WHERE date = ?"
        row = (date,)
        results = cursor.execute(query, row).fetchall() #permette di eseguire i query sul database
        for result in results:
            item = QListWidgetItem(str(result[0])) #result [1] è quello completo, 0 è il task
            self.tasksListWidget.addItem(item)

    def backWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window()
        self.ui.setupUi(self.window)
        self.window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())