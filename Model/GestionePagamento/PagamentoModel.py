class PagamentoModel(object):
    def __init__(self, id, mittente, destinatario, timestamp, importo, dettaglio, statusMultato, tipologia, descrizione):
        self.id = id
        self.mittente = mittente
        self.destinatario = destinatario
        self.timestamp = timestamp
        self.importo = importo
        self.dettaglio = dettaglio
        self.statusMultato = statusMultato
        self.tipologia = tipologia
        self.descrizione = descrizione
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

    def getTipologia(self):
        return self.tipologia

    def getDescrizione(self):
        return self.descrizione

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

    def setTipologia(self, tipologia):
        self.tipologia = tipologia

    def setDescrizione(self, descrizione):
        self.descrizione = descrizione


