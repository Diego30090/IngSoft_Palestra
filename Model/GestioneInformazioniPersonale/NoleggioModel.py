from OggettoConScadenzaModel import OggettoConScadenzaModel

class NoleggioModel(OggettoConScadenzaModel):

    def __init__(self, idElemento, idUtenteAssociato, dataInserimento, dataScadenza, multato, categoriaElemento, autorizzatoDa):
        super.__init__(idElemento, idUtenteAssociato, dataInserimento, dataScadenza, multato)
        self.categoriaElemento = categoriaElemento
        self.autorizzatoDa = autorizzatoDa

    def getCategoriaElemento(self):
        return self.categoriaElemento

    def getAutorizzatoDa(self):
        return self.autorizzatoDa

    def setCategoriaElemento(self, newCategoriaElemento):
        self.categoriaElemento = newCategoriaElemento

    def setAutorizzatoDa(self, newAutorizzatoDa):
        self.autorizzatoDa = newAutorizzatoDa
