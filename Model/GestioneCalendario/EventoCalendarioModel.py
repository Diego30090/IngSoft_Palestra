from datetime import datetime

class EventoCalendarioModel(object):
    def __init__(self, idEvento: int, nomeEvento: str, dataEvento: datetime.date, luogoEvento: str,orarioEvento: str,organizzatoreEvento: str, descrizioneEvento: str):
        self.idEvento = idEvento
        self.nomeEvento = nomeEvento
        self.dataEvento = dataEvento
        self.luogoEvento = luogoEvento
        self.orarioEvento = orarioEvento
        self.organizzatoreEvento = organizzatoreEvento
        self.descrizioneEvento = descrizioneEvento



        ## Definizione attributi del modello come nei diagrammi

    def getIdEvento(self): ##restituisce il valore desiderato
        return self.idEvento

    def setIdEvento(self, idEvento): ##imposta il valore desiderato all'interno della classe
        self.idEvento = idEvento

    def getNomeEvento(self):
        return self.nomeEvento

    def setNomeEvento(self, nomeEvento):
        self.nomeEvento = nomeEvento

    def getDataEvento(self):
        return self.dataEvento

    def setDataEvento(self, dataEvento):
        self.dataEvento = dataEvento

    def getDescrizioneEvento(self):
        return self.descrizioneEvento

    def setDescrizioneEvento(self, descrizioneEvento):
        self.descrizioneEvento = descrizioneEvento

    def getOrganizzatoreEvento(self):
        return self.organizzatoreEvento

    def setOrganizzatoreEvento(self, organizzatoreEvento):
        self.organizzatoreEvento = organizzatoreEvento

    def getOrarioEvento(self):
        return self.orarioEvento

    def setOrarioEvento(self, orarioEvento):
        self.orarioEvento = orarioEvento

    def getLuogoEvento(self):
        return self.luogoEvento

    def setLuogoEvento(self, luogoEvento):
        self.luogoEvento = luogoEvento
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
