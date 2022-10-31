import sqlite3
from Model.GestioneInventario.DivisaModel import DivisaModel as divisaModel
from Model.GestioneInventario.ArmaModel import ArmaModel as armaModel
from Model.GestioneInventario.BorsoneModel import BorsoneModel as borsoneModel


class GestioneInventario(object):
    def __init__(self):
        self.listaDivise: divisaModel = []
        self.listaArmi: armaModel = []
        self.listaBorsoni: borsoneModel = []

        self.__db = sqlite3.connect('../../db/dbProject.db')
        self.__cursor = self.__db.cursor()
        self.getDiviseFromDb()
        self.getArmiFromDb()
        self.getBorsoniFromDb()

    def svuotaDivise(self):
        self.listaDivise.clear()

    def aggiungiDivise(self, result: divisaModel):
        self.listaDivise.append(result)

    def aggiungiArmi(self, result: armaModel):
        self.listaArmi.append(result)

    def aggiungiBorsoni(self, result: borsoneModel):
        self.listaBorsoni.append(result)

    def getDiviseFromDb(self):
        query = "SELECT * from divise;"
        diviseList = self.__cursor.execute(query).fetchall()
        for i in range(len(diviseList)):
            self.aggiungiDivise(divisaModel(*diviseList[i]))

    def getArmiFromDb(self):
        query = "SELECT * FROM armi;"
        armiList = self.__cursor.execute(query).fetchall()
        for i in range(len(armiList)):
            self.aggiungiArmi(armaModel(*armiList[i]))

    def getBorsoniFromDb(self):
        query = "SELECT * FROM borsoni;"
        borsoniList = self.__cursor.execute(query).fetchall()
        print(borsoniList[0])
        for i in range(len(borsoniList)):
            self.aggiungiBorsoni(borsoneModel(*borsoniList[i]))


if __name__ == '__main__':
    inv = GestioneInventario()
    for i in range(len(inv.listaBorsoni)):
        print(inv.listaBorsoni[i].__dict__)
    for i in range(len(inv.listaArmi)):
        print(inv.listaArmi[i].__dict__)
    for i in range(len(inv.listaDivise)):
        print(inv.listaDivise[i].__dict__)