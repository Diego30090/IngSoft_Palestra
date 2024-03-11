import datetime

from Controller.GestioneDatabase import GestoreDatabase
from Model.GestionePagamento import PagamentoModel
from Model.GestioneUtente import UtenteModel

class GestorePagamenti(object):

    def __init__(self):
        self.dbPagamenti = GestoreDatabase.PagamentoDB()
        self.pagamentiCompleti = []
        self.listaPagamentiCompleta()

    def differenziazionePagamenti(self, utente: UtenteModel):
        print(utente.__dict__)
        if utente.utenteTipo == 'Admin':
            return self.listaPagamentiCompleta()
        else:
            return self.listaPagamentiUtente(utente.username)

    def listaPagamentiCompleta(self):
        self.pagamentiCompleti.clear()
        lista = self.dbPagamenti.listaPagamentiCompleta()
        for elem in lista:
            pagamento = PagamentoModel.PagamentoModel(*elem)
            self.pagamentiCompleti.append(pagamento)

    def listaPagamentiUtente(self, username):
        self.pagamentiCompleti.clear()
        lista = self.dbPagamenti.getPagamentoByDestinatario(
            destinatario=username)
        for elem in lista:
            pagamento = PagamentoModel.PagamentoModel(*elem)
            self.pagamentiCompleti.append(pagamento)

    def getListaPagamentiCompleta(self):
        return self.pagamentiCompleti

    def getSingoloPagamento(self, id):
        pagamento = self.dbPagamenti.getPagamentoById(id)
        self.currentPagamento = PagamentoModel.PagamentoModel(*pagamento)

    def returnSingoloPagamento(self, id):
        pagamento = self.dbPagamenti.getPagamentoById(id)
        return PagamentoModel.PagamentoModel(*pagamento)

    def getCurrentIdPagamento(self):
        idPagamento = self.currentPagamento.getId()
        return str(idPagamento)

    def getCurrentDataEmissione(self):
        dataEmissione = self.currentPagamento.getTimestamp()
        return str(dataEmissione)

    def getCurrentImporto(self):
        importo = self.currentPagamento.getImporto()
        return str(importo)

    def getCurrentStatus(self):
        status = 'Nessuno'
        if self.currentPagamento.getTipologia() == 'pagamento' or self.currentPagamento.getTipologia() == 'multa':
            status = 'Non Pagato'
        elif self.currentPagamento.getTipologia() == 'pagamento effettuato' or self.currentPagamento.getTipologia() == 'multa pagata':
            status = 'Pagato'
        else:
            status = 'Nessuno'
        return status

    def getCurrentTipologia(self):
        arg = self.currentPagamento.getTipologia()
        tipologia = ''
        if arg == 'pagamento' or arg == 'pagamento effettuato':
            tipologia = 'Pagamento'
        elif arg == 'multa' or arg == 'multa pagata':
            tipologia = 'Multa'
        else:
            tipologia = 'NaN'
        return tipologia

    def modificaPagamento(self, id, dettagli, importo, stato, descrizione):
        stato = self.statusInfo(id=id, stato=stato)
        self.dbPagamenti.updatePagamento(pagamentoId=id, importo=importo, dettaglio=dettagli, descrizione=descrizione, tipologia=stato)

    def statusInfo(self, id, stato):
        pagamento = self.returnSingoloPagamento(id)
        if stato == 'Pagato':
            if pagamento.tipologia == 'pagamento' or pagamento.tipologia == 'pagamento effettuato':
                return 'pagamento effettuato'
            elif pagamento.tipologia == 'multa' or pagamento.tipologia == 'multa pagata':
                return 'multa pagata'
            else:
                pass
        elif stato == 'Non Pagato':
            if pagamento.tipologia == 'pagamento' or pagamento.tipologia == 'pagamento effettuato':
                return 'pagamento'
            elif pagamento.tipologia == 'multa' or pagamento.tipologia == 'multa pagata':
                return 'multa'
            else:
                pass
        else:
            pass

    def getCurrentDescrizione(self):
        descrizione = self.currentPagamento.getDescrizione()
        if descrizione == '':
            descrizione = 'Nessuna descrizione'
        return str(descrizione)

    def getCurrentDettaglio(self):
        dettaglio = self.currentPagamento.getDettaglio()
        return str(dettaglio)

    def insertPagamento(self, dettaglio, importo, descrizione, mittente, destinatario):
        currentDay = str(datetime.date.today())
        self.dbPagamenti.insertPagamento(mittente=mittente, destinatario=destinatario, timestamp=currentDay,
                                         importo=importo, dettaglio=dettaglio, descrizione=descrizione)
        pass

    def eliminaPagamento(self, id):
        print(f"pagamento eliminato: {id}")
        self.dbPagamenti.deletePagamento(id=id)
        pass


if __name__ == "__main__":
    con = GestorePagamenti()
    con.listaPagamentiUtente(username='user2')
    print(con.pagamentiCompleti)
