class OggettoInventarioModel(object):

    def __init__(self, id, giacenza, disponibilita, produttore, descrizione):
        self.id = id
        self.giacenza = giacenza
        self.disponibilita = disponibilita
        self.produttore = produttore
        self.descrizione = descrizione

    def getId(self):
        return self.id

    def getGiacenza(self):
        return self.giacenza

    def getDisponibilita(self):
        return self.disponibilita

    def getProduttore(self):
        return self.disponibilita

    def getDescrizione(self):
        return self.descrizione

    def setId(self, id):
        self.id = id

    def setGiacenza(self, giacenza):
        self.giacenza = giacenza

    def setDisponibilita(self, disponibilita):
        self.disponibilita = disponibilita

    def setProduttore(self, produttore):
        self.produttore = produttore

    def setDescrizione(self, descrizione):
        self.descrizione = descrizione

