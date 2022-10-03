import sqlite3
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from db import dbController as db
from views import mainMenu as menu



class Window(QWidget):
    def __init__(self, username):
        self.username = username
        super(Window, self).__init__()
        loadUi("../Calendario/mainCalendario.ui", self)
        self.calendar_widget.selectionChanged.connect(self.calendarDateChanged)  # quando la data che selezione cambia mi connetto alla funzione calendarDateChanged
        self.calendarDateChanged()
        self.add_button.clicked.connect(self.addNewTask)
        self.event_list_widget.clicked.connect(self.openWindow)
        self.back_button.clicked.connect(self.toMainMenu)

    def calendarDateChanged(self):
        self.dateSelected = self.calendar_widget.selectedDate().toPyDate()  # funzione di QCalendarWidget che indica la data selezionata, in forma di stringa PyDate e strftime che lo mette in giorno mese anno
        print("Data selezionata: ", self.dateSelected)
        self.updateTaskList(self.dateSelected)

    def updateTaskList(self, date):
        self.event_list_widget.clear()
        events = db.event_name_by_date(date)
        self.event_list = []
        for event in range(len(events)):
            item = QListWidgetItem(str(events[event][1]))
            self.event_list_widget.addItem(item)
            self.event_list.append([str(events[event][0]),str(id(self.event_list_widget.item(event)))])

    def addNewTask(self):
        name_event = str(self.line_edit_name.text())
        date_event = self.calendar_widget.selectedDate().toPyDate()
        location_event = str(self.line_edit_location.text())
        time_event = str(self.line_edit_time.text())
        organizer_event = str(self.line_edit_organizer.text())
        description_event = str(self.line_edit_description.text())

        db.insert_event(name_event, date_event, location_event, time_event, organizer_event, description_event)
        self.updateTaskList(date_event)
        self.line_edit_name.clear()

    def openWindow(self):
        item = id(self.event_list_widget.currentItem())
        for i in range(len(self.event_list)):
            if str(item) == str(self.event_list[i][1]):
                selectedId= str(self.event_list[i][0])
                self.window = Window2(id=selectedId, username=self.username)
                self.window.show()
                self.close()

    def toMainMenu(self):
        self.screen = menu.MainMenu(username=self.username)
        self.screen.show()
        self.close()

class Window2(QWidget):
    def __init__(self, id, username):
        self.username = username
        self.id_event=id
        super(Window2, self).__init__()
        loadUi("../Calendario/mainCalendarioSelezionato.ui", self)
        self.init_list(id=self.id_event)
        self.dataUpdate()
        self.back_button.clicked.connect(self.backWindow)
        self.delete_button.clicked.connect(self.event_delete)
        self.modify_button.clicked.connect(self.openWindow)

    def init_list(self, id):
        self.event_list_widget.clear()
        events = db.event_by_id(id)
        events = db.event_name_by_date(events[2])
        self.event_list = []
        for event in range(len(events)):
            item = QListWidgetItem(str(events[event][1]))
            self.event_list_widget.addItem(item)
            #funzione da finire
        self.event_list_widget.setDisabled(True)

    def dataUpdate(self):
        event = db.event_by_id(self.id_event)
        name_event = event[1]
        location_event = event[3]
        time_event = event[4]
        organizer_event = event[5]
        description_event = event[6]
        self.widget_name.addItem(name_event)
        self.widget_location.addItem(location_event)
        self.widget_time.addItem(time_event)
        self.widget_organizer.addItem(organizer_event)
        self.widget_description.addItem(description_event)

    def event_delete(self):
        db.remove_event(self.id_event)
        self.backWindow()

    def openWindow(self):
        self.window = Window3(id=self.id_event, username= self.username)
        self.window.show()
        self.close()

    def backWindow(self):
        self.window = Window(username=self.username)
        self.window.show()
        self.close()

class Window3(QWidget):
    def __init__(self, id, username):
        self.username = username
        self.id_event=id
        super(Window3, self).__init__()
        loadUi("../Calendario/mainCalendarioModifiche.ui", self)
        self.init_ui()
        self.negate_button.clicked.connect(self.negate_window)
        self.confirm_button.clicked.connect(self.modify_data)

    def init_ui(self):
        event = db.event_by_id(self.id_event)
        widget_list = [self.widget_name, self. widget_location, self.widget_time, self.widget_organizer, self.widget_description]
        wid_value = [event[1], event[3], event[4], event[5], event[6]]
        for elem in range(len(wid_value)):
            widget_list[elem].clear()
            widget_list[elem].addItem(wid_value[elem])

    def negate_window(self):
        self.window = Window2(id=self.id_event, username=self.username)
        self.window.show()
        self.close()

    def modify_data(self):
        new_name = self.line_edit_name.text()
        new_location = self.line_edit_location.text()
        new_time = self.line_edit_time.text()
        new_organizer = self.line_edit_organizer.text()
        new_description = self.line_edit_description.text()
        db.update_event(self.id_event, new_name, new_location, new_time, new_organizer, new_description)
        self.init_ui()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window(username='root0')
    window.show()
    sys.exit(app.exec())