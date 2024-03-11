import datetime

from Model.GestioneLog.LogModel import LogModel
from Controller.GestioneDatabase import GestoreDatabase
from Model.GestionePagamento.PagamentoModel import PagamentoModel


class GestoreMulta(object):

    def __init__(self):
        self.logDB = GestoreDatabase.LogDB()
        self.multeDB = GestoreDatabase.MultaDB()
        self.controllo = 'Controllo emissione multe'
        pass


    def emettiMulta(self):
        #emette le multe in base all'id
        listaPagamenti = self.getListaPagamentiNonMultati()
        if len(listaPagamenti) != 0:
            for elem in listaPagamenti:
                dataEffettiva = datetime.datetime.strptime(elem.timestamp, '%Y-%m-%d').date()
                if self.dataControl(data=dataEffettiva, days=30) is True:

                    elem.setStatusMultato(status=1)

                    self.multeDB.insertMulta(destinatario = elem.destinatario,
                                             timestamp = str(datetime.date.today()),
                                             importo = 5.0,
                                             dettaglio = f'Multa, mancato pagamento di iDPagamento: {elem.id} ')

                    self.multeDB.updatePagamentoMultato(pagamentoId=elem.id)

    def dataControl(self, data, days):
        dataOdierna = datetime.date.today()
        if (dataOdierna - datetime.timedelta(days=days)) > data:
            return True
        else: return False

    def getListaPagamentiNonMultati(self):
        pagamenti = self.multeDB.getPagamentiNonMultati()
        listaPagamenti = []
        for elem in pagamenti:
            pagamento = PagamentoModel(*elem)
            listaPagamenti.append(pagamento)
        return listaPagamenti



    def automaticControl(self):
        dataUltimoControllo = self.dataUltimoControllo()
        dataUltimoControllo = datetime.datetime.strptime(dataUltimoControllo,'%Y-%m-%d').date()
        if self.dataControl(data= dataUltimoControllo, days=1) is True:
            self.emettiMulta()
            self.insertControllo()
        else:
            pass

    def dataUltimoControllo(self):
        ultimoControllo = self.logDB.getLastCheck(self.controllo)
        if len(ultimoControllo) !=0:
            lastLog = LogModel(*ultimoControllo)
            return lastLog.data
        else:
            return '1900-01-01'


    def insertControllo(self):
        data = datetime.date.today()
        self.logDB.insertLog(data=data,descrizione=self.controllo)

if __name__ == "__main__":
    gest = GestoreMulta()
    data = gest.dataUltimoControllo()
    gest.automaticControl()