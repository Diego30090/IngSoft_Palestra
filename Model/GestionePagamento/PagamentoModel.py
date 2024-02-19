class PagamentoModel(object):
    def __init__(self):
        self.id = None
        self.mittente = None
        self.destinatario = None
        self.timestamp = None
        self.importo = None
        self.dettaglio = None
        pass

    def getId(self):
        return self.id

    def getMittente(self):
        return self.mittente

    def getDestinatario(self):
        return self.destinatario

    def getTimestamp(self):
        return self.timestamp

    def getImporto(self):
        return self.importo

    def getDettaglio(self):
        return self.dettaglio

    def setId(self, id):
        self.id= id

    def setMittente(self, mittente):
        self.mittente = mittente

    def setDestinatario(self, destinatario):
        self.destinatario = destinatario

    def setTimestamp(self, timestamp):
        self.Timestamp = timestamp

    def setImporto(self,importo):
        self.importo = importo

    def setDettaglio(self, dettaglio):
        self.Dettaglio = dettaglio