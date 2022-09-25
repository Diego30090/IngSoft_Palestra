import sqlite3
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from db import dbController as db



class Window(QWidget):
    def __init__(self, username):
        self.username = username
        super(Window, self).__init__()
        loadUi("../Calendario/mainCalendario.ui", self)
        self.calendarWidget.selectionChanged.connect(
            self.calendarDateChanged)  # quando la data che selezione cambia mi connetto alla funzione calendarDateChanged
        self.calendarDateChanged()
        self.addButton.clicked.connect(self.addNewTask)
        self.tasksListWidget.clicked.connect(self.openWindow)

    def calendarDateChanged(self):
        self.dateSelected = self.calendarWidget.selectedDate().toPyDate()  # funzione di QCalendarWidget che indica la data selezionata, in forma di stringa PyDate e strftime che lo mette in giorno mese anno
        print("Data selezionata: ", self.dateSelected)
        self.updateTaskList(self.dateSelected)

    def updateTaskList(self, date):
        self.tasksListWidget.clear()
        events = db.event_name_by_date(date)
        self.event_list = []
        for event in range(len(events)):
            item = QListWidgetItem(str(events[event][1]))
            self.tasksListWidget.addItem(item)
            self.event_list.append([str(events[event][0]),str(id(self.tasksListWidget.item(event)))])

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
        name_event = str(self.taskLineEdit.text())
        date_event = self.calendarWidget.selectedDate().toPyDate()
        location_event = str(self.taskLineEdit1.text())
        time_event = str(self.taskLineEdit2.text())
        organizer_event = str(self.taskLineEdit3.text())
        description_event = str(self.taskLineEdit4.text())

        db.insert_event(name_event, date_event, location_event, time_event, organizer_event, description_event)
        self.updateTaskList(date_event)
        self.taskLineEdit.clear()

    def openWindow(self):
        item = id(self.tasksListWidget.currentItem())
        for i in range(len(self.event_list)):
            if str(item) == str(self.event_list[i][1]):
                selectedId= str(self.event_list[i][0])
                self.window = Window2(id=selectedId, username=self.username)
                self.window.show()
                self.close()

class Window2(QWidget):
    def __init__(self, id, username):
        self.username = username
        self.id_event=id
        super(Window2, self).__init__()
        loadUi("../Calendario/mainCalendarioSelezionato.ui", self)
        self.init_list(id=self.id_event)
        self.dataUpdate()
        self.backButton.clicked.connect(self.backWindow)
        self.deleteButton.clicked.connect(self.event_delete)
        self.modifyButton.clicked.connect(self.openWindow)

    def init_list(self, id):
        self.tasksListWidget.clear()
        events = db.event_by_id(id)
        events = db.event_name_by_date(events[2])
        self.event_list = []
        for event in range(len(events)):
            item = QListWidgetItem(str(events[event][1]))
            self.tasksListWidget.addItem(item)
            #funzione da finire
        self.tasksListWidget.setDisabled(True)

    def dataUpdate(self):
        event = db.event_by_id(self.id_event)
        name_event = event[1]
        location_event = event[3]
        time_event = event[4]
        organizer_event = event[5]
        description_event = event[6]
        self.widgetName.addItem(name_event)
        self.widgetLocation.addItem(location_event)
        self.widgetTime.addItem(time_event)
        self.widgetOrganizer.addItem(organizer_event)
        self.widgetDesc.addItem(description_event)

    def event_delete(self):
        db.remove_event(self.id_event)
        self.backWindow()

    def openWindow(self):
        self.window = Window3(id=self.id_event)
        self.window.show()
        self.close()

    def backWindow(self):
        self.window = Window(username=self.username)
        self.window.show()
        self.close()

class Window3(QWidget):
    def __init__(self, id):
        self.id_event=id
        super(Window3, self).__init__()
        loadUi("../Calendario/mainCalendarioModifiche.ui", self)
        self.init_ui()
        self.negateButton.clicked.connect(self.negate_window)
        self.confirmButton.clicked.connect(self.modify_data)

    def init_ui(self):
        event = db.event_by_id(self.id_event)
        widget_list = [self.widgetName, self. widgetLocation, self.widgetTime, self.widgetOrganizer, self.widgetDesc]
        wid_value = [event[1], event[3], event[4], event[5], event[6]]
        for elem in range(len(wid_value)):
            widget_list[elem].clear()
            widget_list[elem].addItem(wid_value[elem])

    def negate_window(self):
        self.window = Window2(id=self.id_event)
        self.window.show()
        self.close()

    def modify_data(self):
        new_name = self.taskLineEdit.text()
        new_location = self.taskLineEdit1.text()
        new_time = self.taskLineEdit2.text()
        new_organizer = self.taskLineEdit3.text()
        new_description = self.taskLineEdit4.text()
        db.update_event(self.id_event, new_name, new_location, new_time, new_organizer, new_description)
        self.init_ui()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window(username='root0')
    window.show()
    sys.exit(app.exec())