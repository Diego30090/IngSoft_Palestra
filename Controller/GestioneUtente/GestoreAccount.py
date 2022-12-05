from Model.GestioneUtente.UtenteModel import UtenteModel as Model
import sqlite3
from Controller.GestioneDatabase.GestoreDatabase import GestioneDatabase


class GestioneAccount(GestioneDatabase):

    def __init__(self, username, password):
        super().__init__()
        self.utente = Model(None, None, None, None, username, password, None, None, None)

        #self.db = sqlite3.connect('../../db/dbProject.db')
        #self.cursor = self.__db.cursor()



    def login(self):
        ## Controlla che l'utente desiderato sia presente con username e password indicate
        query = f"SELECT COUNT(id_utente) FROM utente WHERE username = '{self.utente.getUsername()}' AND password = '{self.utente.getPassword()}';"
        value = self.cursor.execute(query).fetchone()

        ## Se esiste, istanzia completamente il model
        ## Altrimenti, ritorna un valore di false
        if value[0] == 1:
            self.utente.setInfo(self.getUserInfoInDb('id_utente'), self.getUserInfoInDb('nome'),
                                self.getUserInfoInDb('cognome'), self.getUserInfoInDb('data_nascita'),
                                self.getUserInfoInDb('username'), self.getUserInfoInDb('password'),
                                self.getUserInfoInDb('utente_tipo'), self.getUserInfoInDb('email'),
                                self.getUserInfoInDb('telefono'))
            return True
        else:
            return False

    def getUserInfoInDb(self, column):
        query = f"SELECT {column} FROM utente WHERE username = '{self.utente.getUsername()}' AND " \
                f"password = '{self.utente.getPassword()}';"
        val = self.cursor.execute(query).fetchone()
        return val[0]

    def setUserInfoInDb(self):
        query = f"UPDATE utente SET nome = '{self.utente.getNome()}'," \
                f"cognome = '{self.utente.getCognome()}'," \
                f"data_nascita = '{self.utente.getDataDiNascita()}'," \
                f"username = '{self.utente.getUsername()}'," \
                f"password = '{self.utente.getPassword()}', " \
                f"utente_tipo = '{self.utente.getUtenteTipo()}'," \
                f"email = '{self.utente.getEmail()}'," \
                f"telefono = '{self.utente.getTelefono()}' " \
                f"WHERE id_utente = '{self.utente.getIdUtente()}';"
        self.cursor.execute(query)
        self.db.commit()

if __name__ == '__main__':
    gest = GestioneAccount('root', '0000')
    gest.login()