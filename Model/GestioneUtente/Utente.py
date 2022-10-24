import sqlite3


class UtenteModel(object):
    def __init__(self, idUtente: int, nome: str, cognome: str, dataDiNascita: str, username: str, password: str,
                 utenteTipo: str, email: str, telefono: str):
        self.__idUtente = idUtente
        self.__nome = nome
        self.__cognome = cognome
        self.__dataDiNascita = dataDiNascita
        self.__username = username
        self.__password = password
        self.__utenteTipo = utenteTipo
        self.__email = email
        self.__telefono = telefono


    def getInfo(self):
        return [self.__idUtente, self.__nome, self.__cognome, self.__dataDiNascita, self.__username, self.__password,
                self.__utenteTipo, self.__email, self.__telefono]

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
        return self.__idUtente

    def getNome(self):
        return self.__nome

    def getCognome(self):
        return self.__cognome

    def getDataDiNascita(self):
        return self.__dataDiNascita

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getUtenteTipo(self):
        return self.__utenteTipo

    def getEmail(self):
        return self.__email

    def getTelefono(self):
        return self.__telefono

    def setIdUtente(self, newIdUtente):
        self.__idUtente = newIdUtente

    def setNome(self, newNome):
        self.__nome = newNome

    def setCognome(self, newCognome):
        self.__cognome = newCognome

    def setDataDiNascita(self, newDataDiNascita):
        self.__dataDiNascita = newDataDiNascita

    def setUsername(self, newUsername):
        self.__username = newUsername

    def setPassword(self, newPassword):
        self.__password = newPassword

    def setUtenteTipo(self, newUtenteTipo):
        self.__utenteTipo = newUtenteTipo

    def setEmail(self, newEmail):
        self.__email = newEmail

    def setTelefono(self, newTelefono):
        self.__telefono = newTelefono


if __name__ == '__main__':
    user = UtenteModel(5, 'diego', 'abbat', '19-02-2022', 'root0', 'pwd', 'Atleta', None, '3425717')
    print(user.getNome())
    user.setNome('Giovanni')
    print(user.getInfo())