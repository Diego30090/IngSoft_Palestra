from NotificaModel import NotifcaModel

class NotificaTestualeModel(NotifcaModel):

    def __init__(self, idNotifica, descrizione, data, idUtenteAssociato):
        super.__init__(idNotifica, descrizione, data, idUtenteAssociato, "Text")
