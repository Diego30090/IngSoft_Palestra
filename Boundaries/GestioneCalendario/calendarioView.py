import sys
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem
from PyQt5.uic import loadUi
from db import dbController as db
from Boundaries.GestioneUtente import mainMenu as menu
from Controller.GestioneUtente.GestoreAccount import GestioneAccount as AccountController

#Classi non più utilizzate
'''
class CalendarView(QWidget):
    def __init__(self, userController: AccountController):
        self.userController = userController
        super(CalendarView, self).__init__()
        loadUi("../GestioneCalendario/Calendario/mainCalendario.ui", self)
        self.calendar_widget.selectionChanged.connect(self.calendarDateChanged)  # quando la data che selezione cambia mi connetto alla funzione calendarDateChanged
        self.calendarDateChanged()
        self.add_button.clicked.connect(self.addNewTask)
        self.event_list_widget.clicked.connect(self.viewSelectedTask)
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
        date_event = self.calendar_widget.selectedDate()
        print(type(date_event))
        location_event = str(self.line_edit_location.text())
        time_event = str(self.line_edit_time.text())
        organizer_event = str(self.line_edit_organizer.text())
        description_event = str(self.line_edit_description.text())

        db.insert_event(name_event, date_event, location_event, time_event, organizer_event, description_event)
        self.updateTaskList(date_event)
        self.line_edit_name.clear()

    def viewSelectedTask(self):
        item = id(self.event_list_widget.currentItem())
        for i in range(len(self.event_list)):
            if str(item) == str(self.event_list[i][1]):
                selectedId= str(self.event_list[i][0])
                self.window = SelectedTaskView(id=selectedId, userController=self.userController)
                self.window.show()
                self.close()

    def toMainMenu(self):
        self.screen = menu.MainMenu(self.userController)
        self.screen.show()
        self.close()

class SelectedTaskView(QWidget):
    def __init__(self, id, userController):
        self.userController = userController
        self.id_event=id
        super(SelectedTaskView, self).__init__()
        loadUi("../GestioneCalendario/Calendario/mainCalendarioSelezionato.ui", self)
        self.init_list(id=self.id_event)
        self.dataUpdate()
        self.back_button.clicked.connect(self.closeThis)
        self.delete_button.clicked.connect(self.eventDelete)
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

    def eventDelete(self):
        db.remove_event(self.id_event)
        self.closeThis()

    def openWindow(self):
        self.window = ModifyView(id=self.id_event, userController=self.userController)
        self.window.show()
        self.close()

    def closeThis(self):
        self.window = CalendarView(self.userController)
        self.window.show()
        self.close()

class ModifyView(QWidget):
    def __init__(self, id, userController: AccountController):
        self.userController = userController
        self.id_event=id
        super(ModifyView, self).__init__()
        loadUi("../GestioneCalendario/Calendario/mainCalendarioModifiche.ui", self)
        self.init_ui()
        self.negate_button.clicked.connect(self.closeThis)
        self.confirm_button.clicked.connect(self.saveChanges)

    def init_ui(self):
        event = db.event_by_id(self.id_event)
        widget_list = [self.widget_name, self. widget_location, self.widget_time, self.widget_organizer, self.widget_description]
        wid_value = [event[1], event[3], event[4], event[5], event[6]]
        for elem in range(len(wid_value)):
            widget_list[elem].clear()
            widget_list[elem].addItem(wid_value[elem])

    def closeThis(self):
        self.window = SelectedTaskView(id=self.id_event, userController=self.userController)
        self.window.show()
        self.close()

    def saveChanges(self):
        new_name = self.line_edit_name.text()
        new_location = self.line_edit_location.text()
        new_time = self.line_edit_time.text()
        new_organizer = self.line_edit_organizer.text()
        new_description = self.line_edit_description.text()
        db.update_event(self.id_event, new_name, new_location, new_time, new_organizer, new_description)
        self.init_ui()
'''
