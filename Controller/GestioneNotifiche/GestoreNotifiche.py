import datetime
import sqlite3

from Controller.GestioneDatabase import GestoreDatabase
from Model.GestioneNotifiche import NotificaModel


class GestoreNotifiche(object):

    def __init__(self):
        def __init__(self, destinatario, timestamp, dettaglio):
            self.db = sqlite3.connect('../../db/dbProject.db')
            self.cursor = self.db.cursor()
            self.dbNotifiche = GestoreDatabase.NotificaDB()
            self.notificheComplete = []  # lista tutte notifiche
            self.listaNotificheCompleta()  # ottiene la lista notifiche completa

    def listaNotificheCompleta(self):
        self.notificheComplete.clear()
        lista = self.dbNotifiche.listaNotificheCompleta()  # Ottiene la lista dal db
        for elem in lista:
            notifica = NotificaModel.NotificaModel(*elem)
            self.notificheComplete.append(notifica)

    def listaNotificheUtente(self, id_utente):
        self.notificheComplete.clear()
        lista = self.dbNotifiche.insert_notifica_utente(destinatario=id_utente)
        for elem in lista:
            notifica = NotificaModel.NotificaModel(*elem)
            self.notificheComplete.append(notifica)

    def getListaNotificheCompleta(self):
        return self.notificheComplete

    def getSingolaNotifica(self, id):
        notifica = self.dbNotifiche.getNotificaById(id)
        self.currentNotifica = NotificaModel.NotificaModel(*notifica)

    def getCurrentIdNotifica(self):
        idNotifica = self.currentNotifica.getId()
        return str(idNotifica)

    def getCurrentDataInvio(self):
        dataInvio = self.currentNotifica.getTimestamp()
        return str(dataInvio)

    def getCurrentDescrizione(self):
        descrizione = self.currentNotifica.getDescrizione()
        if descrizione == '':
            descrizione = 'Nessuna descrizione'
        return str(descrizione)

    def insertNotifica(self, descrizione, destinatario):
        currentDay = str(datetime.date.today())
        self.dbNotifiche.insert_notifica(destinatario=destinatario, timestamp=datetime.now(), descrizione=descrizione)
