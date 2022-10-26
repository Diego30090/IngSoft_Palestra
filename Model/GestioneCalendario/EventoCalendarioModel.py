from datetime import datetime, date
import PyQt5


class EventoCalendarioModel(object):
    def __init__(self, idEvento: int, nomeEvento: str, dataEvento: PyQt5.QtCore.QDate, descrizioneEvento: str, organizzatoreEvento: str, orarioEvento: str, luogoEvento: str):
        self.__idEvento = idEvento
        self.__nomeEvento = nomeEvento
        self.__dataEvento = dataEvento
        self.__descrizioneEvento = descrizioneEvento
        self.__organizzatoreEvento = organizzatoreEvento
        self.__orarioEvento = orarioEvento
        self.__luogoEvento = luogoEvento
        ## Definizione attributi del modello come nei diagrammi

    def getIdEvento(self): ##restituisce il valore desiderato
        return self.__idEvento

    def setIdEvento(self, idEvento): ##imposta il valore desiderato all'interno della classe
        self.__idEvento = idEvento

    def getNomeEvento(self):
        return self.__nomeEvento

    def setNomeEvento(self, nomeEvento):
        self.__nomeEvento = nomeEvento

    def getDataEvento(self):
        return self.__dataEvento

    def setDataEvento(self, dataEvento):
        self.__dataEvento = dataEvento

    def getDescrizioneEvento(self):
        return self.__descrizioneEvento

    def setDescrizioneEvento(self, descrizioneEvento):
        self.__descrizioneEvento = descrizioneEvento

    def getOrganizzatoreEvento(self):
        return self.__organizzatoreEvento

    def setOrganizzatoreEvento(self, organizzatoreEvento):
        self.__organizzatoreEvento = organizzatoreEvento

    def getOrarioEvento(self):
        return self.__orarioEvento

    def setOrarioEvento(self, orarioEvento):
        self.__orarioEvento = orarioEvento

    def getLuogoEvento(self):
        return self.__luogoEvento

    def setLuogoEvento(self, luogoEvento):
        self.__luogoEvento = luogoEvento
    ##Definizione getter e setter del modello

if __name__ == "__main__":
    evento=EventoCalendarioModel(1, "Gara", "2022-11-04", "TEXT", "Marco", "11.00", "Ancona")
    print(evento.getIdEvento())
    print(evento.getNomeEvento())
    print(evento.getDataEvento())
    print(evento.getDescrizioneEvento())
    print(evento.getOrganizzatoreEvento())
    print(evento.getOrarioEvento())
    print(evento.getLuogoEvento())
