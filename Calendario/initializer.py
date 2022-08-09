import sqlite3
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from mainCalendario import Ui_Window
from mainCalendarioSelezionato import Ui_SecondWindow


class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("mainCalendario.ui", self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged) #quando la data che selezione cambia mi connetto alla funzione calendarDateChanged
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)
        self.infoButton.clicked.connect(self.openWindow)
        #self.tasksListWidget.clicked.connect(self.openWindow)
        #self.tasksListWidget.clicked.connect(self.tagImportListClicked)
        self.tasksListWidget.clicked.connect(self.moveData)


    def calendarDateChanged(self):
        dateSelected = self.calendarWidget.selectedDate().toPyDate() #funzione di QCalendarWidget che indica la data selezionata, in forma di stringa PyDate e strftime che lo mette in giorno mese anno
        print("Data selezionata: ", dateSelected)
        self.updateTaskList(dateSelected)

    def updateTaskList(self, date):
        self.tasksListWidget.clear()

        db = sqlite3.connect("DatabaseCalendario.db") #il collegamento
        cursor = db.cursor() #fa il query (cosa gli chiedo del database)

        query = "SELECT task, completed FROM tasks WHERE date = ?"
        row = (date,)
        results = cursor.execute(query, row).fetchall()
        for result in results:
            item = QListWidgetItem(str(result[0])) #result [1] è quello completo, 0 è il task
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            elif result[1] == "NO":
                item.setCheckState(QtCore.Qt.Unchecked)
            self.tasksListWidget.addItem(item)

    def saveChanges(self):
        db = sqlite3.connect("DatabaseCalendario.db")
        cursor = db.cursor()
        date = self.calendarWidget.selectedDate().toPyDate()

        for i in range(self.tasksListWidget.count()):
            item = self.tasksListWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE task = ? AND date = ?"
            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND date = ?"
            row = (task, date,)
            cursor.execute(query, row)
        db.commit()

        messageBox = QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def addNewTask(self):
        db = sqlite3.connect("DatabaseCalendario.db")
        cursor = db.cursor()

        newTask = str(self.taskLineEdit.text())
        date = self.calendarWidget.selectedDate().toPyDate()

        query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)"
        row = (newTask, "NO", date,)

        cursor.execute(query, row)
        db.commit()
        self.updateTaskList(date)
        self.taskLineEdit.clear()

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def moveData(self):
        side = self.tasksListWidget.currentRow() #questo è il problema, non riesco in alcun modo a selezionare solamente
        # la riga e il suo interno allo stesso tempo devo trovare un modo per popolare quella riga in particolare con
        # oggetti invece che con solo un nome e un quadrato di controllo
        print(side)
        #assegna cosa a seconda finestra
        #self.ui.labelReceiver.setText(row)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    '''def tagImportListClicked(self):
        print("You clicked the widget")
        row = self.tasksListWidget.currentRow()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        #assegna cosa a seconda finestra
        self.ui.labelReceiver.setText(row)'''



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())