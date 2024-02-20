from datetime import datetime, timedelta

from Model.GestionePagamento.PagamentoModel import MultaModel


class GestoreNotifiche(object):
    def __init__(self, multe):
        self.multe = multe

    def listaNotifiche(self):
        lista = self.dbNotifiche.lista_notifiche

    def controlla_scadenze(self):
        oggi = datetime.now()
        for pagamento in self.pagamenti:
            scadenza = pagamento.getTimestamp()
            giorni_trascorsi = (oggi - scadenza).days

            if giorni_trascorsi >= 30 and not pagamento.getStatusMultato():
                multa = self.crea_multa(pagamento)
                self.multe.append(multa)
                pagamento.setStatusMultato(1)

    ## def crea_multa(self, pagamento):
    ##    multa = MultaModel()
    ##    multa.setDettaglio(f"Multa per {pagamento.getId()}")
    ##    multa.setImporto(25)
    ##    multa.setId(None)
    ##    multa.setStato()
    ##    multa.setTimestamp(datetime.now())
    ##    return multa

    def ottieni_multe(self):
        return self.multe