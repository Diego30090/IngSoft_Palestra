

class OggettoConScadenzaModel(object):
    def __init__(self, idElemento, idUtenteAssociato, dataInserimento, dataScadenza, multato):
        self.idElemento = idElemento
        self.idUtenteAssociato = idUtenteAssociato
        self.dataInserimento = dataInserimento
        self.dataScadenza = dataScadenza
        self.multato = multato

    def getIdElemento(self):
        return self.idElemento

    def getIdUtenteAssociato(self):
        return self.idUtenteAssociato

    def getDataInserimento(self):
        return self.dataInserimento

    def getDataScadenza(self):
        return self.dataScadenza

    def getMultato(self):
        return self.multato

    def setIdElemento(self, newIdElemento):
        self.idElemento = newIdElemento

    def setIdUtenteAssociato(self, newIdUtenteAssociato):
        self.idUtenteAssociato = newIdUtenteAssociato

    def setDataInserimento(self, newDataInserimento):
        self.dataInserimento = newDataInserimento

    def setDataScadenza(self, newDataScadenza):
        self.dataScadenza = newDataScadenza

    def setMultato(self, newMultato):
        self.multato = newMultato