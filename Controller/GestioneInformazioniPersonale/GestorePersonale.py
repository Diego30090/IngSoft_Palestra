import datetime
from Controller.GestioneDatabase.GestoreDatabase import UtenteDB
from Model.GestioneUtente.UtenteModel import UtenteModel


class GestoreInformazioniPersonale(object):
    def __init__(self):
        self.dbPersonale = UtenteDB()
        self.listaUtenti = []


    def getUtentePerTipo(self, userType):
        self.listaUtenti.clear()
        lista = self.dbPersonale.selectUtente(user_type=userType)
        for user in lista:
            listUser = list(user)
            listUser.pop(7)
            utente= UtenteModel(*listUser)
            self.listaUtenti.append(utente)
        return self.listaUtenti

    def eliminaUtente(self, user: UtenteModel):
        print(user.idUtente)
        self.dbPersonale.deleteUtente(utenteId=user.getIdUtente())

    def getSingoloutente(self, userId):
        utente = self.getUtenteById(userId=userId)
        utente=list(utente)
        utente.pop(7)
        return UtenteModel(*utente)

    def getUtenteById(self, userId):
        return self.dbPersonale.getUtenteById(idUtente=userId)

    def controlloDati(self, nome, cognome, dataNascita, username, password, tipoUtente, email, telefono):
        errorFlag = False
        textList = [nome, cognome, password, email, telefono, username]
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

    def insertUser(self, nome, cognome, dataNascita, username, password, utenteTipo, email, telefono):
        self.dbPersonale.insertUser(nome=nome, cognome=cognome, data_nascita=dataNascita,
                                    username=username, password=password, utente_tipo=utenteTipo,
                                    email=email, telefono=telefono)

    def userUpdater(self, idUtente, nome, cognome, dataDiNascita, username, password, utenteTipo, email, telefono):
        self.dbPersonale.updateUser(nome= nome,
                        cognome=cognome,
                        dataNascita=dataDiNascita,
                        username=username,
                        password= password,
                        tipoUtente=utenteTipo,
                        email=email,
                        telefono=telefono,
                        idUtente=idUtente)

