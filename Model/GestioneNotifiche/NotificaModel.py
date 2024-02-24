

class NotifcaModel(object):

    def __init__(self, idNotifica, descrizione, data, destinatario, tipoNotifica, dettaglio, timestamp):
        ##    self.idNotifica = idNotifica
        ##    self.descrizione = descrizione
        ##    self.data = data
        self.destinatario = destinatario
        ##    self.tipoNotifica = tipoNotifica
        self.dettaglio = dettaglio
        self.timestamp = timestamp

    def getDestinatario(self):
        return self.destinatario

    def getTimestamp(self):
        return self.timestamp

    def getDettaglio(self):
        return self.dettaglio

    def setDestinatario(self, newDestinatario):
        self.destinatario = newDestinatario

    def setTimestamp(self, newTimestamp):
        self.timestamp = newTimestamp

    def setDettaglio(self, newDettaglio):
        self.dettaglio = newDettaglio

'''    def getIdNotifica(self):
        return self.idNotifica

    def getDescrizione(self):
        return self.descrizione

    def getData(self):
        return self.data

    def getIdUtenteAssociato(self):
        return self.idUtenteAssociato

    def getTipoNotifica(self):
        return self.tipoNotifica

    def setIdNotifica(self, newIdNotifica):
        self.idNotifica = newIdNotifica

    def setDescrizione(self, newDescrizione):
        self.descrizione = newDescrizione

    def setData(self, newData):
        self.data = newData

    def setIdUtenteAssociato(self, newIdUtenteAssociato):
        self.idUtenteAssociato = newIdUtenteAssociato

    def setTipoNotifica(self, newTipoNotifica):
        self.tipoNotifica = newTipoNotifica
'''