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
        loadUi("mainCalendario.ui", self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged) #quando la data che selezione cambia mi connetto alla funzione calendarDateChanged
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)
        self.infoButton.clicked.connect(self.openWindow)
        self.tasksListWidget.clicked.connect(self.openWindow)
        #self.tasksListWidget.clicked.connect(self.tagImportListClicked)
        #self.tasksListWidget.clicked.connect(self.moveData)


    def calendarDateChanged(self):
        dateSelected = self.calendarWidget.selectedDate().toPyDate() #funzione di QCalendarWidget che indica la data selezionata, in forma di stringa PyDate e strftime che lo mette in giorno mese anno
        print("Data selezionata: ", dateSelected)
        self.updateTaskList(dateSelected)

    def updateTaskList(self, date):
        self.tasksListWidget.clear()

        db = sqlite3.connect("DatabaseCalendario.db") #il collegamento
        cursor = db.cursor() #fa il query (cosa gli chiedo del database)

        query = "SELECT name, time FROM tasks WHERE date = ?"
        row = (date,)
        results = cursor.execute(query, row).fetchall() #permette di eseguire i query sul database
        for result in results:
            item = QListWidgetItem(str(result[0])) #result [1] è quello completo, 0 è il task
            self.tasksListWidget.addItem(item)

    def saveChanges(self):
        db = sqlite3.connect("DatabaseCalendario.db")
        cursor = db.cursor()
        date = self.calendarWidget.selectedDate().toPyDate()

        for i in range(self.tasksListWidget.count()):
            item = self.tasksListWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE name = ? AND date = ?"
            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE name = ? AND date = ?"
            row = (name, date,)
            cursor.execute(query, row)
        db.commit()

        messageBox = QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def addNewTask(self):
        db = sqlite3.connect("DatabaseCalendario.db")
        cursor = db.cursor()

        newName = str(self.taskLineEdit.text())
        date = self.calendarWidget.selectedDate().toPyDate()
        newLocation = str(self.taskLineEdit1.text())
        newTime = str(self.taskLineEdit2.text())
        newOrganizer = str(self.taskLineEdit3.text())
        newDescription = str(self.taskLineEdit4.text())

        query = "INSERT INTO tasks(name, date, location, time, organizer, description) VALUES (?,?,?,?,?,?)"
        row = (newName, date, newLocation, newTime, newOrganizer, newDescription,)

        cursor.execute(query, row)
        db.commit()
        self.updateTaskList(date)
        self.taskLineEdit.clear()

    def openWindow(self):
        self.window = Window2()
        self.window.show()
        self.close()

    '''def moveData(self):
         side = self.tasksListWidget.currentRow() #questo è il problema, non riesco in alcun modo a selezionare solamente
         # la riga e il suo interno allo stesso tempo devo trovare un modo per popolare quella riga in particolare con
         # oggetti invece che con solo un nome e un quadrato di controllo
         print(side)
         #assegna cosa a seconda finestra
         #self.ui.labelReceiver.setText(row)
         self.window = QtWidgets.QMainWindow()
         self.ui = Ui_SecondWindow()
         self.ui.setupUi(self.window)
         self.window.show()'''

    '''def tagImportListClicked(self):
        print("You clicked the widget")
        row = self.tasksListWidget.currentRow()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        #assegna cosa a seconda finestra
        self.ui.labelReceiver.setText(row)'''


    '''def moveData(self):
        loadUi("mainCalendarioSelezionato.ui", self)

        self.tasksListWidget.clear()
        db = sqlite3.connect("DatabaseCalendario.db")
        cursor = db.cursor()'''

class Window2(QWidget):
    def __init__(self):
        super(Window2,self).__init__()
        loadUi("mainCalendarioSelezionato.ui", self)
        self.dataUpdate()
        self.backButton.clicked.connect(self.backWindow)

    def dataUpdate(self):
        db = sqlite3.connect("DatabaseCalendario.db")
        cursorName = db.cursor()
        cursorLocation = db.cursor()
        cursorTime = db.cursor()
        cursorOrganizer = db.cursor()
        cursorDesc = db.cursor()
        cursorName.execute("SELECT name FROM tasks")
        cursorLocation.execute("SELECT location FROM tasks")
        cursorTime.execute("SELECT time FROM tasks")
        cursorOrganizer.execute("SELECT organizer FROM tasks")
        cursorDesc.execute("SELECT description FROM tasks")
        result = cursorName.fetchone()
        result1 = cursorLocation.fetchone()
        result2 = cursorTime.fetchone()
        result3 = cursorOrganizer.fetchone()
        result4 = cursorDesc.fetchone()

        for row in result:
            self.widgetName.addItem(row)

        for row in result1:
            self.widgetLocation.addItem(row)

        for row in result2:
            self.widgetTime.addItem(row)

        for row in result3:
            self.widgetOrganizer.addItem(row)

        for row in result4:
            self.widgetDesc.addItem(row)

    def backWindow(self):
        self.window = Window()
        self.window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())