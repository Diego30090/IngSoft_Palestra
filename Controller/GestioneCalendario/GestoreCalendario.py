import datetime
import sqlite3

from Controller.GestioneDatabase.GestoreDatabase import GestioneDatabase
from Controller.GestioneDatabase import GestoreDatabase
from Model.GestioneCalendario.EventoCalendarioModel import EventoCalendarioModel
from db import dbController as db


class GestoreEventoCalendario(GestioneDatabase):
    def __init__(self, id_event, name_event,date_event, location_event, time_event, organizer_event,  description_event):
        self.evento = EventoCalendarioModel(id_event, name_event, date_event, description_event, organizer_event,
                                            time_event, location_event)
        self.dbEvento=GestoreDatabase.EventoDB()

    def addEventoInDb(self):
        self.dbEvento.insertEvent(name=self.evento.getNomeEvento(), date=self.evento.getDataEvento(),
                                  location=self.evento.getLuogoEvento(), time=self.evento.getOrarioEvento(),
                                  organizer=self.evento.getOrganizzatoreEvento(), description=self.evento.getDescrizioneEvento())

    def updateEvent(self):
        self.dbEvento.updateEvent(self.evento.idEvento, self.evento.nomeEvento, self.evento.luogoEvento, self.evento.orarioEvento, self.evento.organizzatoreEvento, self.evento.descrizioneEvento)


    def getEvento(self):
        return self.evento

    def setEvento(self, id):
        evento = self.dbEvento.eventById(id)
        self.evento = EventoCalendarioModel(*evento)


    def getDataEvento(self):
        return self.evento.getDataEvento()


if __name__ == '__main__':
    eventManager = GestoreEventoCalendario(5, 'asd', datetime.date(1952,10,12), 'prova1', 'org', '15-18', 'ngul ammammt')
    ev = eventManager.getEvento(1)
    print(type(ev))
    print(ev.__dict__)
