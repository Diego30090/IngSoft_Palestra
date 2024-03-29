from Model.GestioneInventario.ElementoInventarioModel import ElementoInventarioModel


class DivisaModel(ElementoInventarioModel):

    def __init__(self, id, giacenza, disponibilita, elemento, sesso, taglia, arma, mano, produttore, descrizione):
        super().__init__(id, giacenza, disponibilita, produttore, descrizione)
        self.elemento = elemento
        self.sesso = sesso
        self.taglia = taglia
        self.arma = arma
        self.mano = mano

    def getElemento(self):
        return self.elemento

    def getSesso(self):
        return self.sesso

    def getTaglia(self):
        return self.taglia

    def getArma(self):
        return self.arma

    def getMano(self):
        return self.mano

    def setElemento(self, elemento):
        self.elemento = elemento

    def setSesso(self, sesso):
        self.sesso = sesso

    def setTaglia(self, taglia):
        self.taglia = taglia

    def setArma(self, arma):
        self.arma = arma

    def setMano(self, mano):
        self.mano = mano


if __name__ == '__main__':
    obj = DivisaModel(5, 5, 5, 'ciao', 'asd', 'asd', 'asd', 'asd', produttore='allstar', descrizione='asidads')
    print(obj.getDisponibilita())
