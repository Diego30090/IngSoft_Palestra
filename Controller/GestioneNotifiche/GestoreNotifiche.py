import datetime

from Controller.GestioneDatabase import GestoreDatabase
from Model.GestioneNotifiche import NotificaModel

class GestoreNotifiche(object):

    def __init__(self):
        self.dbNotifiche = GestoreDatabase.NotificaDB()
        self.notificheComplete = []  # lista tutte notifiche
        self.notificheUtente = []
        self.listaNotificheCompleta()  # ottiene la lista notifiche completa

    def listaNotificheCompleta(self):
        self.notificheComplete.clear()
        lista = self.dbNotifiche.getListaNotificheCompleta()  # Ottiene la lista dal db
        for elem in lista:
            notifica = NotificaModel.NotificaModel(*elem)
            self.notificheComplete.append(notifica)
        return self.notificheComplete

    def listaNotificheUtente(self, id_utente):
        self.notificheUtente.clear()
        lista = self.dbNotifiche.get_notifica_destinatario(destinatario=id_utente)
        for elem in lista:
            notifica = NotificaModel.NotificaModel(*elem)
            self.notificheUtente.append(notifica)
        return self.notificheUtente

    def insertNotifica(self, descrizione, destinatario):
        currentDay = str(datetime.date.today())
        self.dbNotifiche.insert_notifica(destinatario=destinatario, timestamp=currentDay, descrizione=descrizione)

if __name__ == "__main__":
    controller = GestoreNotifiche()
    listaNotifiche = controller.listaNotificheCompleta()
    ListaNotificheUtente = controller.listaNotificheUtente(id_utente=2)
    for elem in ListaNotificheUtente:
        print(elem.__dict__)