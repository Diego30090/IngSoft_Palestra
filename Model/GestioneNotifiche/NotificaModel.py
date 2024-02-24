

class NotificaModel(object):

    def __init__(self, idNotifica, dettagli, data, destinatario):
        self.idNotifica = idNotifica
        self.dettagli = dettagli
        self.data = data
        self.destinatario = destinatario

    def getIdNotifica(self):
        return self.idNotifica

    def getDettaglio(self):
        return self.dettagli

    def getData(self):
        return self.data

    def getDestinatario(self):
        return self.destinatario

    def setDestinatario(self, newDestinatario):
        self.destinatario = newDestinatario

    def setData(self, data):
        self.data = data

    def setDettagli(self, dettagli):
        self.dettagli = dettagli
