import sqlite3

from Controller.GestioneDatabase.GestoreDatabase import GestioneDatabase
from Model.GestioneCalendario.EventoCalendarioModel import EventoCalendarioModel
from db import dbController as db


class GestoreEventoCalendario(GestioneDatabase):
    def __init__(self, id_event, name_event, date_event, description_event, organizer_event, time_event,
                 location_event):
        self.evento = EventoCalendarioModel(id_event, name_event, date_event, description_event, organizer_event,
                                            time_event, location_event)

    def addEventoInDb(self):
        # definizione della query
        query = f"INSERT INTO tasks(name, date, description, organizer, time, location) VALUES ('{self.__evento.getNomeEvento()}','{self.__evento.getDataEvento()}', '{self.__evento.getDescrizioneEvento()}','{self.__evento.getOrganizzatoreEvento()}', '{self.__evento.getOrarioEvento()}', '{self.__evento.getLuogoEvento()}');"
        # esecuzione della query
        self.cursor.execute(query)
        # commit nel database
        self.db.commit()

    def getDataEvento(self):
        return self.evento.getDataEvento()
