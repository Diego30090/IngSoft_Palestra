import sqlite3

from Controller.GestioneDatabase.GestoreDatabase import GestioneDatabase
from Model.GestioneInventario.DivisaModel import DivisaModel as divisaModel
from Model.GestioneInventario.ArmaModel import ArmaModel as armaModel
from Model.GestioneInventario.BorsoneModel import BorsoneModel as borsoneModel


class GestioneInventario(GestioneDatabase):
    def __init__(self):
        super().__init__()
        self.listaDivise: divisaModel = []
        self.listaArmi: armaModel = []
        self.listaBorsoni: borsoneModel = []

        self.getDiviseFromDb()
        self.getArmiFromDb()
        self.getBorsoniFromDb()

    def aggiungiDivisa(self, result: divisaModel):
        self.listaDivise.append(result)

    def aggiungiArma(self, result: armaModel):
        self.listaArmi.append(result)

    def aggiungiBorsone(self, result: borsoneModel):
        self.listaBorsoni.append(result)

    def getDiviseFromDb(self):
        self.listaDivise.clear()
        diviseList = self.generalizedSelect('divise')
        for i in range(len(diviseList)):
            self.aggiungiDivisa(divisaModel(*diviseList[i]))

    def getArmiFromDb(self):
        self.listaArmi.clear()
        armiList = self.generalizedSelect('armi')
        for i in range(len(armiList)):
            self.aggiungiArma(armaModel(*armiList[i]))

    def getBorsoniFromDb(self):
        self.listaBorsoni.clear()
        borsoniList = self.generalizedSelect('borsoni')
        for i in range(len(borsoniList)):
            self.aggiungiBorsone(borsoneModel(*borsoniList[i]))


if __name__ == '__main__':
    inv = GestioneInventario()
    for i in range(len(inv.listaBorsoni)):
        print(inv.listaBorsoni[i].__dict__)
    for i in range(len(inv.listaArmi)):
        print(inv.listaArmi[i].__dict__)
    for i in range(len(inv.listaDivise)):
        print(inv.listaDivise[i].__dict__)