class OggettoInventarioModel():

    def __init__(self, id, giacenza, disponibilita, produttore, descrizione):
        self.__id = id
        self.__giacenza = giacenza
        self.__disponibilita = disponibilita
        self.__produttore = produttore
        self.__descrizione = descrizione

    def getId(self):
        return self.__id

    def getGiacenza(self):
        return self.__giacenza

    def getDisponibilita(self):
        return self.__disponibilita

    def getProduttore(self):
        return self.__disponibilita

    def getDescrizione(self):
        return self.__descrizione

    def setId(self, id):
        self.__id = id

    def setGiacenza(self, giacenza):
        self.__giacenza = giacenza

    def setDisponibilita(self, disponibilita):
        self.__disponibilita = disponibilita

    def setProduttore(self, produttore):
        self.__produttore = produttore

    def setDescrizione(self, descrizione):
        self.__descrizione = descrizione

