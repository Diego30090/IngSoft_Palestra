

class NotifcaModel(object):

    def __init__(self, idNotifica, descrizione, data, idUtenteAssociato, tipoNotifica):
        self.idNotifica = idNotifica
        self.descrizione = descrizione
        self.data = data
        self.idUtenteAssociato = idUtenteAssociato
        self.tipoNotifica = tipoNotifica


    def getIdNotifica(self):
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
