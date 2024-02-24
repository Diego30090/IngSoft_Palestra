##from datetime import datetime, timedelta

##from Model.GestionePagamento.PagamentoModel import MultaModel


## GestoreNotifiche(object):
    ##   def __init__(self, multe):
    ##      self.multe = multe

        ##  def listaNotifiche(self):
        ##  lista = self.dbNotifiche.lista_notifiche

        ## def controlla_scadenze(self):
        ##     oggi = datetime.now()
        ##     for pagamento in self.pagamenti:
        ##         scadenza = pagamento.getTimestamp()
        ##         giorni_trascorsi = (oggi - scadenza).days
        ##
        ##         if giorni_trascorsi >= 30 and not pagamento.getStatusMultato():
        ##             multa = self.crea_multa(pagamento)
        ##              self.multe.append(multa)
        ##             pagamento.setStatusMultato(1)

    ## def crea_multa(self, pagamento):
    ##    multa = MultaModel()
    ##    multa.setDettaglio(f"Multa per {pagamento.getId()}")
    ##    multa.setImporto(25)
    ##    multa.setId(None)
    ##    multa.setStato()
    ##    multa.setTimestamp(datetime.now())
    ##    return multa

        ##    def ottieni_multe(self):
        ##        return self.multe

import datetime
import sqlite3

from PyQt5.QtWidgets import QTableWidget

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
            self.populateTabellaNotifiche()

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
        self.dbNotifiche.insert_notifica(destinatario=destinatario, timestamp=currentDay, descrizione=descrizione)

    def populateTabellaNotifiche(self):
        query = "SELECT timestamp, dettaglio FROM notifica"
        self.cursor.execute(query)
        dati_notifiche = self.cursor.fetchall()

        self.tabellaPagamenti.setRowCount(len(dati_notifiche))
        self.tabellaPagamenti.setColumnCount(2)

        for riga, record in enumerate(dati_notifiche):
            for colonna, valore in enumerate(record):
                item = QTableWidget(str(valore))
                self.tabellaNotifiche.setItem(riga, colonna, item)