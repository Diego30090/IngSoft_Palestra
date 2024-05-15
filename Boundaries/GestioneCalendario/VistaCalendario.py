import sys
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem
from PyQt5.uic import loadUi

from Controller.GestioneUtente.GestoreAccount import GestioneAccount as AccountController
from Controller.GestioneCalendario import GestoreCalendario
from Controller.GestioneDatabase.GestoreDatabase import EventoDB as EventoDB
from Boundaries.GestioneUtente import mainMenu as menu


## Sostituire le parti interessate con l'interazione a GestoreEventoCalendario
## In questo caso, la vista richiede al Gestore di popolarne i dati
## La vista agisce in modo attivo

# noinspection PyUnresolvedReferences
class VistaCalendario(QWidget):
    def __init__(self, accountController: AccountController):
        self.eventoDB = EventoDB()
        self.userController = accountController
        self.username = accountController.utente.getUsername()
        super(VistaCalendario, self).__init__()
        loadUi("../GestioneCalendario/Calendario/mainCalendario.ui", self)
          # quando la data che selezione cambia mi connetto alla funzione calendarDateChanged
        self.eventDefiner = [self.line_edit_name, self.line_edit_location, self.line_edit_time, self.line_edit_organizer, self.line_edit_description]
        self.calendarDateChanged()
        self.instruction()
        self.blockedOptions()

    def instruction(self):
        self.add_button.clicked.connect(self.addNewTask)
        self.event_list_widget.clicked.connect(self.viewSelectedTask)
        self.back_button.clicked.connect(self.toMainMenu)
        self.calendar_widget.selectionChanged.connect(self.calendarDateChanged)

    def blockedOptions(self):
        if self.userController.utente.utenteTipo == 'Atleta':
            self.add_button.setDisabled(True)


    def calendarDateChanged(self):
        self.dateSelected = self.calendar_widget.selectedDate().toPyDate()  # funzione di QCalendarWidget che indica la data selezionata, in forma di stringa PyDate e strftime che lo mette in giorno mese anno
        print("Data selezionata: ", self.dateSelected)
        self.updateTaskList(self.dateSelected)

    def updateTaskList(self, date):
        self.event_list_widget.clear()
        events = self.eventoDB.eventNameByDate(date=date)
        self.event_list = []

        for event in range(len(events)):
            item = QListWidgetItem(str(events[event][1]))
            self.event_list_widget.addItem(item)
            self.event_list.append([str(events[event][0]), str(id(self.event_list_widget.item(event)))])

    def addNewTask(self):
        list = [self.line_edit_name.text(),self.line_edit_location.text(), self.line_edit_time.text(), self.line_edit_organizer.text(),self.line_edit_description.text()]
        flag = True
        for elem in list:
            if elem == '':
                flag = False
        if flag is True:
            evento = GestoreCalendario.GestoreEventoCalendario(id_event=None, name_event=str(self.line_edit_name.text()),
                                                               date_event=self.calendar_widget.selectedDate().toPyDate(),
                                                               location_event=str(self.line_edit_location.text()),
                                                               time_event=str(self.line_edit_time.text()),
                                                               organizer_event=str(self.line_edit_organizer.text()),
                                                               description_event=str(self.line_edit_description.text()))
            evento.addEventoInDb()
            self.updateTaskList(evento.getDataEvento())
            for itemToClear in self.eventDefiner:
                itemToClear.clear()

    def viewSelectedTask(self):
        item = id(self.event_list_widget.currentItem())
        for i in range(len(self.event_list)):
            if str(item) == str(self.event_list[i][1]):
                selectedId = str(self.event_list[i][0])
                self.window = VistaEventoSelezionato(id=selectedId, accountController=self.userController)
                self.window.show()
                self.close()

    def toMainMenu(self):
        self.screen = menu.MainMenu(userController=self.userController)
        self.screen.show()
        self.close()


class VistaEventoSelezionato(QWidget):
    def __init__(self, id, accountController: AccountController):
        self.eventoDB = EventoDB()
        self.userController = accountController
        self.username = accountController.utente.getUsername()
        self.id_event = id
        super(VistaEventoSelezionato, self).__init__()
        loadUi("../GestioneCalendario/Calendario/mainCalendarioSelezionato.ui", self)
        self.init_list(id=self.id_event)
        self.dataUpdate()
        self.instruction()
        self.blockedOptions()

    def instruction(self):
        self.back_button.clicked.connect(self.closeThis)
        self.delete_button.clicked.connect(self.eventDelete)
        self.modify_button.clicked.connect(self.openWindow)

    def blockedOptions(self):
        if self.userController.utente.utenteTipo == 'Atleta':
            self.modify_button.setDisabled(True)
            self.delete_button.setDisabled(True)

    def init_list(self, id):
        self.event_list_widget.clear()
        events = self.eventoDB.eventById(id)
        events = self.eventoDB.eventNameByDate(events[2])
        self.event_list = []
        for event in range(len(events)):
            item = QListWidgetItem(str(events[event][1]))
            self.event_list_widget.addItem(item)
            # funzione da finire
        self.event_list_widget.setDisabled(True)

    def dataUpdate(self):
        event = self.eventoDB.eventById(self.id_event)
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
        self.eventoDB.removeEvent(self.id_event)
        self.closeThis()

    def openWindow(self):
        self.window = VistaModifica(id=self.id_event, accountController=self.userController)
        self.window.show()
        self.close()

    def closeThis(self):
        self.window = VistaCalendario(accountController=self.userController)
        self.window.show()
        self.close()


class VistaModifica(QWidget):
    def __init__(self, id, accountController: AccountController):
        super(VistaModifica, self).__init__()
        loadUi("../GestioneCalendario/Calendario/mainCalendarioModifiche.ui", self)
        self.userController = accountController
        self.eventController = GestoreCalendario.GestoreEventoCalendario(None, None, None, None, None, None, None)
        self.eventController.setEvento(id)

        self.init_ui()
        self.instruction()

    def instruction(self):
        self.negate_button.clicked.connect(self.closeThis)
        self.confirm_button.clicked.connect(self.saveChanges)

    def init_ui(self):
        evento =self.eventController.getEvento()
        widget_list = [self.widget_name, self.widget_location, self.widget_time, self.widget_organizer,
                       self.widget_description]
        wid_value = [evento.getNomeEvento(), evento.getLuogoEvento(), evento.getOrarioEvento(), evento.getDescrizioneEvento(), evento.getDescrizioneEvento()]

        for elem in range(len(wid_value)):
            widget_list[elem].clear()
            widget_list[elem].addItem(wid_value[elem])


    def closeThis(self):
        self.window = VistaEventoSelezionato(id=self.evento.setIdEvento(), accountController=self.userController)
        self.window.show()
        self.close()

    def saveChanges(self):
        self.eventController.evento.nomeEvento = self.line_edit_name.text()
        self.eventController.evento.luogoEvento = self.line_edit_location.text()
        self.eventController.evento.orarioEvento = self.line_edit_time.text()
        self.eventController.evento.organizzatoreEvento = self.line_edit_organizer.text()
        self.eventController.evento.descrizioneEvento = self.line_edit_description.text()
        self.eventController.updateEvent()
        self.init_ui()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #window = VistaCalendario(accountController=AccountController('root1', 'pwd'))
    window = VistaModifica(id = 56, accountController=AccountController('root1', 'pwd'))
    window.show()
    sys.exit(app.exec())
