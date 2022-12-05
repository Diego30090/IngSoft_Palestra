from Model.GestioneInventario.ElementoInventarioModel import ElementoInventarioModel


class BorsoneModel(ElementoInventarioModel):

    def __init__(self, id, giacenza, disponibilita, elemento, produttore, descrizione):
        super().__init__(id, giacenza, disponibilita, produttore, descrizione)
        self.elemento = elemento

    def getElemento(self):
        return self.elemento

    def setElemento(self, elemento):
        self.elemento = elemento
