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


if __name__ == "__main__":
    con= GestorePagamenti()
    print(con.pagamentiCompleti[0].__dict__)