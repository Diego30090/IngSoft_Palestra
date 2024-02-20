class PagamentoModel(object):
    def __init__(self, id, mittente, destinatario, timestamp, importo, dettaglio, stato, statusMultato):
        self.id = id
        self.mittente = mittente
        self.destinatario = destinatario
        self.timestamp = timestamp
        self.importo = importo
        self.dettaglio = dettaglio
        self.stato = stato
        self.statusMultato = statusMultato
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

    def getStato(self):
        return self.stato

    def setId(self, id):
        self.id = id

    def setMittente(self, mittente):
        self.mittente = mittente

    def setDestinatario(self, destinatario):
        self.destinatario = destinatario

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def setImporto(self, importo):
        self.importo = importo

    def setDettaglio(self, dettaglio):
        self.dettaglio = dettaglio

    def setStato(self, stato):
        self.stato = stato

class MultaModel(PagamentoModel):
    def __init__(self):
        super().__init__(id=None, mittente='Sistema',
                         destinatario=None, timestamp=None,
                         importo=None, dettaglio=None, statusMultato=None)
