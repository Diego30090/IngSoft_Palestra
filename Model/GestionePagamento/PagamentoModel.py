class PagamentoModel(object):
    def __init__(self, id, mittente, destinatario, timestamp, importo, dettaglio):
        self.id = id
        self.mittente = mittente
        self.destinatario = destinatario
        self.timestamp = timestamp
        self.importo = importo
        self.dettaglio = dettaglio
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


class MultaModel(PagamentoModel):
    def __init__(self):
        super().__init__(id=None, mittente='Sistema',
                         destinatario=None, timestamp=None,
                         importo=None, dettaglio=None)


if __name__ == '__main__':
    multa = MultaModel()
    multa.setDestinatario(destinatario='Tumadre')
    print(multa.__dict__)
