from Model.GestioneUtente.UtenteModel import UtenteModel as Model
import sqlite3
from Controller.GestioneDatabase.GestoreDatabase import UtenteDB


class GestioneAccount(UtenteDB):

    def __init__(self, username, password):
        super().__init__()
        self.utente = Model(None, None, None, None, username, password, None, None, None)

    #
    def login(self):
        ## Controlla che l'utente desiderato sia presente con username e password indicate
        value = self.count_user(username=self.utente.getUsername(), password=self.utente.getPassword())

        ## Se esiste, istanzia completamente il model
        ## Altrimenti, ritorna un valore di false
        if value[0] == 1:
            username = self.utente.getUsername()
            password = self.utente.getPassword()
            self.utente.setInfo(self.getUserInfoInDb('id_utente', username=username, password=password),
                                self.getUserInfoInDb('nome', username=username, password=password),
                                self.getUserInfoInDb('cognome', username=username, password=password),
                                self.getUserInfoInDb('data_nascita', username=username, password=password),
                                self.getUserInfoInDb('username', username=username, password=password),
                                self.getUserInfoInDb('password', username=username, password=password),
                                self.getUserInfoInDb('utente_tipo', username=username, password=password),
                                self.getUserInfoInDb('email', username=username, password=password),
                                self.getUserInfoInDb('telefono', username=username, password=password))
            return True
        else:
            return False

    #
    def setUserInfoInDb(self):
        self.updateUser(nome=self.utente.getNome(),
                        cognome=self.utente.getCognome(),
                        dataNascita=self.utente.getDataDiNascita(),
                        username=self.utente.getUsername(),
                        password=self.utente.getPassword(),
                        tipoUtente=self.utente.getUtenteTipo(),
                        email=self.utente.getEmail(),
                        telefono=self.utente.getTelefono(),
                        idUtente=self.utente.getIdUtente())


if __name__ == '__main__':
    gest = GestioneAccount('root', '0000')
    gest.login()
