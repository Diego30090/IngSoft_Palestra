from OggettoInventarioModel import OggettoInventarioModel


class BorsoneModel(OggettoInventarioModel):

    def __init__(self, id, giacenza, disponibilita, elemento, sesso, taglia, arma, mano, produttore, descrizione):
        super().__init__(id, giacenza, disponibilita, produttore, descrizione)
        self.elemento = elemento
        self.sesso = sesso
        self.taglia = taglia
        self.arma = arma
        self.mano = mano

    def getElemento(self):
        return self.elemento

    def setElemento(self, elemento):
        self.elemento = elemento

    def getSesso(self):
        return self.sesso

    def setSesso(self, newSesso):
        self.sesso = newSesso

    def getTaglia(self):
        return self.taglia

    def setTaglia(self, newTaglia):
        self.taglia = newTaglia

    def getArma(self):
        return self.arma

    def setArma(self, newArma):
        self.arma = newArma

    def getMano(self):
        return self.mano

    def setMano(self, newMano):
        self.mano = newMano


if __name__ == '__main__':
    obj = BorsoneModel(5, 5, 5, 'ciao', 'asd', 'asd', 'asd', 'asd', produttore='allstar', descrizione='asidads')
    print(obj.getDisponibilita())
