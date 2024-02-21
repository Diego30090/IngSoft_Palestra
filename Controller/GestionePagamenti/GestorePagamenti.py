import datetime

from Controller.GestioneDatabase import GestoreDatabase
from Model.GestionePagamento import PagamentoModel
class GestorePagamenti(object):

    def __init__(self):
        self.dbPagamenti = GestoreDatabase.PagamentoDB()  #funzioni db dedicate ai pagamenti
        self.pagamentiCompleti =[] #lista pagamenti
        self.listaPagamentiCompleta() # ottiene la lista pagamenti


    def listaPagamentiCompleta(self):
        lista = self.dbPagamenti.listaPagamentiCompleta()  # Ottiene la lista dal db, secondo il GestoreDatabase
        for elem in lista: #Il for si occupa di inserire tutti i record ottenuti dal db e popolare il model
            pagamento = PagamentoModel.PagamentoModel(*elem)
            self.pagamentiCompleti.append(pagamento)

    def getListaPagamentiCompleta(self):
        return self.pagamentiCompleti

    def getSingoloPagamento(self, id):
        pagamento = self.dbPagamenti.getPagamentoById(id)
        self.currentPagamento = PagamentoModel.PagamentoModel(*pagamento)

    def getCurrentIdPagamento(self):
        idPagamento =self.currentPagamento.getId()
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


    def getCurrentDescrizione(self):
        descrizione = self.currentPagamento.getDescrizione()
        if descrizione is None:
            descrizione = 'Nessuna descrizione'
        return str(descrizione)

    def getCurrentDettaglio(self):
        dettaglio = self.currentPagamento.getDettaglio()
        return str(dettaglio)

    def insertPagamento(self, dettaglio, importo, descrizione, mittente, destinatario):
        print(f'dettaglio operazione: {dettaglio}\n'
              f'importo operazione : {importo}\n'
              f'descrizione operazione: {descrizione}\n'
              f'mittente: {mittente}\n'
              f'destinatario: {destinatario}')
        currentDay = str(datetime.date.today())
        self.dbPagamenti.insert_pagamento(mittente=mittente, destinatario=destinatario, timestamp=currentDay, importo=importo, dettaglio=dettaglio)
        pass



if __name__ == "__main__":
    con= GestorePagamenti()
    print(con.pagamentiCompleti[0].__dict__)