import sqlite3


class GestioneDatabase(object):
    def __init__(self):
        self.db = sqlite3.connect('../../db/dbProject.db')
        self.cursor = self.db.cursor()