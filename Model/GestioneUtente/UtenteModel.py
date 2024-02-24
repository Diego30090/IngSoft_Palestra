import sqlite3


class UtenteModel(object):
    def __init__(self, idUtente: int, nome: str, cognome: str, dataDiNascita: str, username: str, password: str,
                 utenteTipo: str, email: str, telefono: str):
        self.idUtente = idUtente
        self.nome = nome
        self.cognome = cognome
        self.dataDiNascita = dataDiNascita
        self.username = username
        self.password = password
        self.utenteTipo = utenteTipo
        self.email = email
        self.telefono = telefono


    def getInfo(self):
        return [self.idUtente, self.nome, self.cognome, self.dataDiNascita, self.username, self.password,
                self.utenteTipo, self.email, self.telefono]

    def setInfo(self, newIdUtente, newNome, newCognome, newDataDiNascita, newUsername, newPassword, newUtenteTipo, newEmail, newTelefono):
        self.setIdUtente(newIdUtente)
        self.setNome(newNome)
        self.setCognome(newCognome)
        self.setDataDiNascita(newDataDiNascita)
        self.setUsername(newUsername)
        self.setPassword(newPassword)
        self.setUtenteTipo(newUtenteTipo)
        self.setEmail(newEmail)
        self.setTelefono(newTelefono)


    def getIdUtente(self):
        return self.idUtente

    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getDataDiNascita(self):
        return self.dataDiNascita

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getUtenteTipo(self):
        return self.utenteTipo

    def getEmail(self):
        return self.email

    def getTelefono(self):
        return self.telefono

    def setIdUtente(self, newIdUtente):
        self.idUtente = newIdUtente

    def setNome(self, newNome):
        self.nome = newNome

    def setCognome(self, newCognome):
        self.cognome = newCognome

    def setDataDiNascita(self, newDataDiNascita):
        self.dataDiNascita = newDataDiNascita

    def setUsername(self, newUsername):
        self.username = newUsername

    def setPassword(self, newPassword):
        self.password = newPassword

    def setUtenteTipo(self, newUtenteTipo):
        self.utenteTipo = newUtenteTipo

    def setEmail(self, newEmail):
        self.email = newEmail

    def setTelefono(self, newTelefono):
        self.telefono = newTelefono

