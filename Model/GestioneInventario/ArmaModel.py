from Model.GestioneInventario.OggettoInventarioModel import OggettoInventarioModel


class ArmaModel(OggettoInventarioModel):

    def __init__(self, id, giacenza, disponibilita, arma, lunghezza, impugnatura, materiale, mano, produttore,
                 descrizione):
        super().__init__(id, giacenza, disponibilita, produttore, descrizione)
        self.arma = arma
        self.lunghezza = lunghezza
        self.impugnatura = impugnatura
        self.materiale = materiale
        self.mano = mano

    def getArma(self):
        return self.arma

    def getLunghezza(self):
        return self.lunghezza

    def getImpugnatura(self):
        return self.impugnatura

    def getMateriale(self):
        return self.materiale

    def getMano(self):
        return self.mano

    def setArma(self, arma):
        self.arma = arma

    def setLunghezza(self, lunghezza):
        self.lunghezza = lunghezza

    def setImpugnatura(self, impugnatura):
        self.impugnatura = impugnatura

    def setMateriale(self, materiale):
        self.materiale = materiale

    def setMano(self, mano):
        self.mano = mano
