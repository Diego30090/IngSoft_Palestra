import datetime
import sqlite3

from Controller.GestioneDatabase.GestoreDatabase import GestioneDatabase
from Model.GestioneCalendario.EventoCalendarioModel import EventoCalendarioModel
from db import dbController as db


class GestoreEventoCalendario(GestioneDatabase):
    def __init__(self, id_event, name_event, date_event, description_event, organizer_event, time_event,
                 location_event):
        self.evento = EventoCalendarioModel(id_event, name_event, date_event, description_event, organizer_event,
                                            time_event, location_event)
        self.db = sqlite3.connect('../../db/dbProject.db')
        self.cursor = self.db.cursor()

    def addEventoInDb(self):
        # definizione della query
        query = f"INSERT INTO tasks(name, date, description, organizer, time, location) VALUES ('{self.evento.getNomeEvento()}','{str(self.evento.getDataEvento())}', '{self.evento.getDescrizioneEvento()}','{self.evento.getOrganizzatoreEvento()}', '{self.evento.getOrarioEvento()}', '{self.evento.getLuogoEvento()}');"
        # esecuzione della query
        self.cursor.execute(query)
        # commit nel database
        self.db.commit()

    def getDataEvento(self):
        return self.evento.getDataEvento()


if __name__ == '__main__':
    eventManager = GestoreEventoCalendario(5, 'asd', datetime.date(1952,10,12), 'prova1', 'org', '15-18', 'ngul ammammt')
    eventManager.addEventoInDb()
