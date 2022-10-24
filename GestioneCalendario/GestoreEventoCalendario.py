import sqlite3

from models.EventoCalendarioModel import EventoCalendarioModel

class GestoreEventoCalendario():

    def __init__(self, name_event, date_event, location_event, time_event, organizer_event, description_event):
        self.evento = EventoCalendarioModel(name_event, date_event, location_event, time_event, organizer_event, description_event)
        self.db = sqlite3.connect('dbProject.db')
        self.cursor = self.db.cursor()

    def insertEvent(self):
        query = f"INSERT INTO tasks(name, date, location, time, organizer, description) VALUES ('{self.name}','{self.date}', '{self.location}','{self.time}', '{self.organizer}', '{self.description}');"
        self.cursor.execute(query)
        self.db.commit()

        #Deve tenere gli il modello e l'interazione con il db

    ## Inserire gli algoritmi per l'interazione con il database ed il model
    ## Gli algoritmi creati devono esser utili alla vista
