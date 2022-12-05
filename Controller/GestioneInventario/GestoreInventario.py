from Model import GestioneInventario
import sqlite3

class GestioneInventario():

    def __init__(self):
        self.listaArmi
        self.listaDivise
        self.listaBorsoni
        self.db = sqlite3.connect('../../db/dbProject.db')
        self.cursor = self.db.cursor()

