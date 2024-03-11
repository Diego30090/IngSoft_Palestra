from OggettoConScadenzaModel import OggettoConScadenzaModel


class PagamentoModel(OggettoConScadenzaModel):

    def __init__(self, idElemento, idUtenteAssociato, dataInserimento, dataScadenza, multato, importo, causale, idUtenteUploader, pagamentoEffettuato):
        super.__init__(idElemento, idUtenteAssociato, dataInserimento, dataScadenza, multato)
        self.importo = importo
        self.causale = causale
        self.idUtenteUploader = idUtenteUploader
        self.pagamentoEffettuato = pagamentoEffettuato

    def getImporto(self):
        return self.importo

    def getCausale(self):
        return self.causale

    def getIdUtenteUploader(self):
        return self.idUtenteUploader

    def getPagamentoEffettuato(self):
        return self.pagamentoEffettuato

    def setImporto(self, newImporto):
        self.importo = newImporto

    def setCausale(self, newCausale):
        self.causale = newCausale

    def setIdUtenteUploader(self, newIdUtenteUploader):
        self.idUtenteUploader = newIdUtenteUploader

    def setPagamentoEffettuato(self, newPagamentoEffettuato):
        self.pagamentoEffettuato = newPagamentoEffettuato