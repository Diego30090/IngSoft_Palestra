from models.GestioneUtente.Utente import UtenteModel as Model
import sqlite3

class GestioneAccount(object):
    def __init__(self, username, password):
        self.__utente = Model(None, None, None, None, username, password, None, None, None)
        self.__db = sqlite3.connect('../../db/dbProject.db')
        self.__cursor = self.__db.cursor()

    def login(self):
        query = f"SELECT COUNT(id_utente) FROM utente WHERE username = '{self.__utente.getUsername()}' AND password = '{self.__utente.getPassword()}';"
        value= self.__cursor.execute(query).fetchone()
        if value[0] == 1:
            self.__utente.setInfo(self.getUserInfoInDb('id_utente'), self.getUserInfoInDb('nome'),
                                  self.getUserInfoInDb('cognome'), self.getUserInfoInDb('data_nascita'),
                                  self.getUserInfoInDb('username'), self.getUserInfoInDb('password'),
                                  self.getUserInfoInDb('utente_tipo'), self.getUserInfoInDb('email'),
                                  self.getUserInfoInDb('telefono'))
            return True
        else:
            return False

    def getUserInfoInDb(self, column):
        query= f"SELECT {column} FROM utente WHERE username = '{self.__utente.getUsername()}' AND password = '{self.__utente.getPassword()}';"
        val = self.__cursor.execute(query).fetchone()
        return val[0]


if __name__ == '__main__':
    a= GestioneAccount('root', '0000')
    print(a.login())