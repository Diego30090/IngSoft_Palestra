class LogModel(object):
    def __init__(self, id, data, descrizione):
        self.id = id
        self.data = data
        self.descrizione = descrizione

    def getId(self):
        return self.id

    def getData(self):
        return self.data

    def getDescrizione(self):
        return self.descrizione

    def setId(self, id):
        self.id = id

    def setData(self, data):
        self.data = data

    def setDescrizione(self, descrizione):
        self.descrizione = descrizione