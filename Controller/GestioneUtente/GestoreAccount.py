from Model.GestioneUtente.Utente import UtenteModel as Model
import sqlite3

class GestioneAccount(object):
    def __init__(self, username, password):
        self.__utente = Model(None, None, None, None, username, password, None, None, None)
        self.__db = sqlite3.connect('../../db/dbProject.db')
        self.__cursor = self.__db.cursor()

    def login(self):
        ## Controlla che l'utente desiderato sia presente con username e password indicate
        query = f"SELECT COUNT(id_utente) FROM utente WHERE username = '{self.__utente.getUsername()}' AND password = '{self.__utente.getPassword()}';"
        value = self.__cursor.execute(query).fetchone()
        ## Se esiste, istanzia completamente il model
        ## Altrimenti, ritorna un valore di false
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
        query= f"SELECT {column} FROM utente WHERE username = '{self.__utente.getUsername()}' AND " \
               f"password = '{self.__utente.getPassword()}';"
        val = self.__cursor.execute(query).fetchone()
        return val[0]

    def setUserInfoInDb(self):
        query = f"INSERT INTO utente(nome, cognome, data_nascita, username, password, utente_tipo, email, telefono) VALUES " \
                f"('{self.__utente.getNome()}','{self.__utente.getCognome()}'," \
                f" '{self.__utente.getDataDiNascita()}', '{self.__utente.getUsername()}'," \
                f" '{self.__utente.getPassword()}', '{self.__utente.getUtenteTipo()}'," \
                f" '{self.__utente.getEmail()}', '{self.__utente.getTelefono()}') ; "
        self.__cursor.execute(query)
        self.__db.commit()

if __name__ == '__main__':
    a= GestioneAccount('root', '0000')
    print(a.login())
