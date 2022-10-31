import sqlite3

from Model.GestioneCalendario.EventoCalendarioModel import EventoCalendarioModel
from db import dbController as db

class GestoreEventoCalendario():
    def __init__(self, id_event, name_event, date_event, description_event, organizer_event, time_event, location_event):
        self.evento = EventoCalendarioModel(id_event, name_event, date_event, description_event, organizer_event, time_event, location_event)
        self.__db = sqlite3.connect('dbProject.db')
        self.__cursor = self.__db.cursor()

    def addEventoInDb(self):
        # definizione della query
        query = f"INSERT INTO tasks(name, date, description, organizer, time, location) VALUES ('{self.__evento.getNomeEvento()}','{self.__evento.getDataEvento()}', '{self.__evento.getDescrizioneEvento()}','{self.__evento.getOrganizzatoreEvento()}', '{self.__evento.getOrarioEvento()}', '{self.__evento.getLuogoEvento()}');"
        #esecuzione della query
        self.__cursor.execute(query)
        #commit nel database
        self.__db.commit()

    def getDataEvento(self):
        return self.__evento.getDataEvento()

