import sqlite3


class GestioneDatabase(object):
    def __init__(self):
        self.db = sqlite3.connect('../../db/dbProject.db')
        self.cursor = self.db.cursor()


    def generalizedSelect(self, table):
        query = f"SELECT * FROM {table};"
        return self.cursor.execute(query).fetchall()

