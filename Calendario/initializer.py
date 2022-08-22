import sqlite3
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from db import dbController as db



class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("mainCalendario.ui", self)
        self.calendarWidget.selectionChanged.connect(
            self.calendarDateChanged)  # quando la data che selezione cambia mi connetto alla funzione calendarDateChanged
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)
        self.infoButton.clicked.connect(self.openWindow)
        self.tasksListWidget.clicked.connect(self.openWindow)

    def calendarDateChanged(self):
        self.dateSelected = self.calendarWidget.selectedDate().toPyDate()  # funzione di QCalendarWidget che indica la data selezionata, in forma di stringa PyDate e strftime che lo mette in giorno mese anno
        print("Data selezionata: ", self.dateSelected)
        self.updateTaskList(self.dateSelected)

    def updateTaskList(self, date):
        self.tasksListWidget.clear()
        events = db.event_name_by_date(date)
        for event in range(len(events)):
            print(events[event])
            item = QListWidgetItem(str(events[event][0]))
            self.tasksListWidget.addItem(item)


    def saveChanges(self):
        cursor= db.connect()
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
        cursor= db.connect()

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
        self.window = Window2(name=self.tasksListWidget.currentItem().text(), date=self.calendarWidget.selectedDate().toPyDate())
        self.window.show()
        self.close()

class Window2(QWidget):
    def __init__(self, name, date):
        self.name=name
        self.date=date
        super(Window2, self).__init__()
        loadUi("mainCalendarioSelezionato.ui", self)
        self.dataUpdate(name=self.name, date= self.date)
        self.backButton.clicked.connect(self.backWindow)

    def dataUpdate(self, name, date):
        event = db.event_by_name_and_date(name, date)
        name_event = event[1]
        location_event = event[3]
        time_event = event[2]
        organizer_event = event[5]
        description_event = event[6]
        self.widgetName.addItem(name_event)
        self.widgetLocation.addItem(location_event)
        self.widgetTime.addItem(time_event)
        self.widgetOrganizer.addItem(organizer_event)
        self.widgetDesc.addItem(description_event)



    def backWindow(self):
        self.window = Window()
        self.window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
