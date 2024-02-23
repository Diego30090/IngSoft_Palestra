import datetime

from Model.GestioneUtente.UtenteModel import UtenteModel as Model
import sqlite3
from Controller.GestioneDatabase.GestoreDatabase import UtenteDB


class GestioneAccount(UtenteDB):

    def __init__(self, username, password):
        super().__init__()
        self.utente = Model(None, None, None, None, username, password, None, None, None)
        self.login()
        self.listaUtenti = []

    def getSingoloutente(self, userId):
        utente = self.getUtenteById(idUtente=userId)
        utente=list(utente)
        utente.pop(7)
        return Model(*utente)

    def getUtentePerTipo(self, userType):
        self.listaUtenti.clear()
        lista = self.select_utente(user_type=userType)
        for user in lista:
            listUser = list(user)
            listUser.pop(7)
            utente= Model(*listUser)
            self.listaUtenti.append(utente)
        return self.listaUtenti

    def getEveryUtente(self):
        self.listaUtenti.clear()
        listaUser= self.getAllUtenti()
        for user in listaUser:
            utente=Model(*user)
            self.listaUtenti.append(utente)

    def returnEveryUsername(self):
        self.getEveryUtente()
        listaUsername = []
        for user in self.listaUtenti:
            listaUsername.append(user.getUsername())
        return listaUsername

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

    def controlloDati(self, nome, cognome, password, email, telefono, username, dataNascita):
        errorFlag = False
        textList = [nome, cognome, password, email, telefono, username]
        controller = UtenteDB()
        for elem in textList:
            if elem == '':
                errorFlag = True
                error = 'Error: Inserire tutti i campi'
                return [errorFlag, error]
        dataNascita = datetime.datetime.strptime(dataNascita,'%Y-%m-%d').date()
        if dataNascita > datetime.date.today():
            errorFlag = True
            error = 'Errore: Inserisci una data valida'
            return [errorFlag, error]

        usernameFlag = controller.check_username(user=username)
        print(f"username Flag: {str(usernameFlag)}")
        if usernameFlag is True:
            error = 'Errore: Username già esistente'
            errorFlag = True
            return [errorFlag, error]
        else:
            return [errorFlag, '']

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

    def userUpdater(self, idUtente, nome, cognome, dataDiNascita, username, password, utenteTipo, email, telefono):
        self.updateUser(nome= nome,
                        cognome=cognome,
                        dataNascita=dataDiNascita,
                        username=username,
                        password= password,
                        tipoUtente=utenteTipo,
                        email=email,
                        telefono=telefono,
                        idUtente=idUtente)

if __name__ == '__main__':
    gest = GestioneAccount('root', '0000')
    flag =gest.controlloDati(nome='aa', cognome= 'aa', dataNascita='1900-12-12', password='aa', email='aa', telefono='a', username='a')
    print(flag)
