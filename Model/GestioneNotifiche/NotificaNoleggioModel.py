from NotificaModel import NotifcaModel

class NotificaNoleggioModel(NotifcaModel):
    def __init__(self, idNotifica, descrizione, data, idUtenteAssociato, idOggettoInventarioAssociato, rispostaValore):
        super.__init__(idNotifica, descrizione, data, idUtenteAssociato, "Noleggio")
        self.idOggettoInventarioAssociato = idOggettoInventarioAssociato
        self.rispostaValore = rispostaValore

    def getIdOggettoInventarioAssociato(self):
        return self.idOggettoInventarioAssociato

    def getRispostaValore(self):
        return self.rispostaValore

    def setIdOggettoInventarioAssociato(self, newIdOggettoInventarioAssociato):
        self.idOggettoInventarioAssociato = newIdOggettoInventarioAssociato

    def setRispostaValore(self, newRispostaValore):
        self.rispostaValore = newRispostaValore
