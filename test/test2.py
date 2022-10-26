# Ha un utente, quell'utente deve poter aprire un nuovo conto corrente, accreditaStipendio

    # Classe Utente - Entity
    # Classe ContoCorrente - Entity
    # Classe ControlContoCorrente - Control
    # Classe BoundaryBanca - Boundary

'''
Esempio parzialmente completo sull'ECB Model
'''

class Utente(object):

    def __init__(self, nome, cognome, idUtente):
        self.nome = nome
        self.cognome = cognome
        self.idUtente = idUtente

    #getter - in funzione di classi esterne
    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getIdUtente(self):
        return self.idUtente

    #setter - in funzione della classe stessa
    def setNome(self, nome):
        self.nome = nome

    def setCognome(self, cognome):
        self.cognome = cognome

    def setIdUtente(self, idUtente):
        self.idUtente = idUtente


class ContoCorrente(object):

    def __init__(self, bilancio: int, idConto: int, proprietaConto: int):
        self.bilancio = bilancio
        self.idConto = idConto
        self.proprietaConto = proprietaConto

    def getBilancio(self):
        return self.bilancio

    def getIdConto(self):
        return self.idConto

    def getProprietaConto(self):
        return self.proprietaConto

    def setBilancio(self, bilancio):
        self.bilancio = bilancio

    def setIdConto(self, idConto):
        self.idConto = idConto

    def setProprietaConto(self, proprietaConto):
        self.proprietaConto = proprietaConto


class ControlContoCorrente(object):
    # L'utente deve poter creare un conto corrente
    # L'utente deve poter accreditare lo stipendio
    def __init__(self):
        self.contoCorrente = ContoCorrente(0,1,'placeholder')
        pass

    def creaContoCorrente(self, newProprieta):
        self.contoCorrente.setProprietaConto(newProprieta)
        return print(f'Hai creato il conto corrente di {self.contoCorrente.getProprietaConto()}')
        pass

    def accreditaLoStipendio(self):
        pass

    def visualizzaConto(self):
        pass



class BoundaryBanca(object):

    def __init__(self):
        self.controller = ControlContoCorrente()
        self.menu()

    def menu(self):
        print('Operazioni disponibili:\n   1) Crea il conto Corrente\n   2) Accredita lo stipendio\n    3) Visualizza il conto\n    4) Esci dal programma perchè sei una pussy')
        opzione = input("Inserisci l'operazione desiderata\n")
        if opzione == "1":
            self.creaContoCorrente()
        elif opzione == "2":
            self.accreditaSipendio()
        elif opzione == "3":
            self.esci()
        else:
            print("Scegli l'opzione corretta\n")
            self.menu()

    def creaContoCorrente(self):
        proprietaConto = input("Inserisci il nome della persona del conto Corrente\n")
        self.controller.creaContoCorrente(proprietaConto)
        self.menu()

    def accreditaSipendio(self):
        # self.controller = ...
        print("\n Hai accreditato lo stipendio!\n")
        self.menu()

    def esci(self):
        print("Ci si vede quando vorrai vendere di nuovo l'anima alle banche")


if __name__ == '__main__':
    banca = BoundaryBanca()



























# Ecb
    # Entity/Model =    Oggetto che vogliamo manipolare
                        # Presenza di variabili proprie dell'oggetto
                        # Operazioni diponibili = Getter e setter
                        #In sostanza, è una serie di getter e setter, non recuperano i dati al di fuori della classe

    # Control   =       Si occupa degli algotmi e dell'ottenimento dati da fonti esterne

    # Boundary =        Si occupa dell'interazione dell'actor con il programma
                        # è quello che vede l'utente finale
                        #Comportamento = richiede al controller di fare le operazioni di interesse e lo restituiscono al boundary