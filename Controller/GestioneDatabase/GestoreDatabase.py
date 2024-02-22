import datetime
import sqlite3



class GestioneDatabase(object):
    def __init__(self):
        self.db = sqlite3.connect('../../db/dbProject.db')
        self.cursor = self.db.cursor()

    def queryExecuteCommitter(self, query):
        self.cursor.execute(query)
        self.db.commit()

    def generalizedSelect(self, table):
        query = f"SELECT * FROM {table};"
        return self.cursor.execute(query).fetchall()

    def init_table(self, table):
        self.table = table

    def get_element_by_id(self, id):
        query = f"SELECT * FROM {self.table} WHERE id='{id}';"
        return self.cursor.execute(query).fetchall()[0]

    def delete_element_by_id(self, id):
        query = f"DELETE FROM {self.table} WHERE id='{id}';"
        self.queryExecuteCommitter(query)


class UtenteDB(GestioneDatabase):

    def __init__(self):
        super().__init__()
        self.init_table('utente')

    def count_user(self, username, password):
        query = f"SELECT COUNT(id_utente) FROM {self.table} WHERE username = '{username}' AND password = '{password}';"
        return self.cursor.execute(query).fetchone()

    def check_username(self, user):
        query = f"SELECT COUNT(id_utente) FROM {self.table} WHERE username = '{user}';"
        val = str(self.cursor.execute(query).fetchone()[0])
        if val == '1':
            return True
        else:
            return False

    def insert_user(self, nome, cognome, data_nascita, username, password, utente_tipo, email, telefono):
        query = f"INSERT INTO {self.table}(nome, cognome, data_nascita, username, password, utente_tipo, email, telefono) VALUES " \
                f"('{nome}','{cognome}', '{data_nascita}', '{username}', '{password}', '{utente_tipo}', '{email}', '{telefono}') ; "
        self.queryExecuteCommitter(query)

    def select_utente(self, user_type):
        query = f"SELECT * from {self.table} WHERE utente_tipo = '{user_type}';"
        return self.cursor.execute(query).fetchall()

    def getUserInfoInDb(self, column, username, password):
        query = f"SELECT {column} FROM {self.table} WHERE username = '{username}' AND " \
                f"password = '{password}';"
        return self.cursor.execute(query).fetchone()[0]

    def updateUser(self, nome, cognome, dataNascita, username, password, tipoUtente, email, telefono, idUtente):
        query = f"UPDATE {self.table} SET nome = '{nome}'," \
                f"cognome = '{cognome}'," \
                f"data_nascita = '{dataNascita}'," \
                f"username = '{username}'," \
                f"password = '{password}', " \
                f"utente_tipo = '{tipoUtente}'," \
                f"email = '{email}'," \
                f"telefono = '{telefono}' " \
                f"WHERE id_utente = '{idUtente}';"
        self.queryExecuteCommitter(query=query)

    def getAllUtenti(self):
        query = "SELECT id_utente, nome, cognome, data_nascita, username, password, utente_tipo, email, password FROM utente;"
        return self.cursor.execute(query).fetchall()

class EventoDB(GestioneDatabase):
    def __init__(self):
        super().__init__()
        self.init_table('tasks')

    def event_name_by_date(self, date):
        query = f"SELECT * FROM {self.table} WHERE date = '{date}';"
        val = self.cursor.execute(query)
        val = val.fetchall()
        return val

    def event_by_id(self, id):
        return self.get_element_by_id(id=id)

    def insert_event(self, name, date, location, time, organizer, description):
        query = f"INSERT INTO {self.table}(name, date, location, time, organizer, description) VALUES ('{name}','{date}', '{location}','{time}', '{organizer}', '{description}');"
        self.queryExecuteCommitter(query)

    def remove_event(self, event_id):
        self.delete_element_by_id(id=event_id)

    def update_event(self, event_id, name, location, time, organizer, description):
        query = f"UPDATE {self.table} SET name = '{name}', location = '{location}', time = '{time}', organizer = '{organizer}', " \
                f"description = '{description}' WHERE id='{event_id}' "
        self.queryExecuteCommitter(query)


class InventarioDB(GestioneDatabase):

    def __init__(self):
        super().__init__()

    def insert_inventario(self, tab_type, info):
        if tab_type == 'armi':
            query = f"INSERT INTO {tab_type}(giacenza, disponibilita, arma, ds, materiale, lunghezza, produttore, " \
                    f"impugnatura, descrizione) VALUES ({int(info[0])}, {int(info[1])}, '{info[2]}', '{info[3]}', '{info[4]}', " \
                    f"{int(info[5])}, '{info[6]}', '{info[7]}', '{info[8]}')"
        elif tab_type == 'divise':
            query = f"INSERT INTO {tab_type}(giacenza, disponibilita, elemento, ds, arma, taglia, sesso, " \
                    f"produttore, descrizione) VALUES ({int(info[0])}, {int(info[1])}, '{info[2]}', '{info[3]}', '{info[4]}', " \
                    f"{int(info[5])}, '{info[6]}', '{info[7]}', '{info[8]}')"
        else:
            query = f"INSERT INTO {tab_type}(giacenza, disponibilita, elemento, produttore, descrizione) VALUES " \
                    f"({int(info[0])}, {int(info[1])}, '{info[2]}', '{info[3]}', '{info[4]}')"
        self.queryExecuteCommitter(query)

    def select_inventario_by_id(self, id, tab_type):
        query = f"SELECT * FROM {tab_type} WHERE id = {id};"
        return self.cursor.execute(query).fetchone()


class PagamentoDB(GestioneDatabase):
    def __init__(self):
        super().__init__()
        self.init_table('pagamento')
        pass

    def insert_pagamento(self, mittente, destinatario, timestamp, importo, dettaglio, descrizione):
        query = f"INSERT INTO {self.table}(mittente, destinatario, timestamp, importo, dettaglio, tipologia, multato, descrizione) VALUES ('{mittente}','{destinatario}', '{timestamp}', '{importo}', '{dettaglio}', 'pagamento', 0, '{descrizione}');"
        self.queryExecuteCommitter(query)

    def update_pagamento(self, pagamentoId, importo, dettaglio, descrizione, tipologia):
        query = f"UPDATE {self.table} SET importo= '{importo}',dettaglio = '{dettaglio}', descrizione = '{descrizione}', tipologia = '{tipologia}'" \
                f"WHERE id ={pagamentoId}"
        self.queryExecuteCommitter(query)

    def delete_pagamento(self, id):
        self.delete_element_by_id(id=id)

    def getPagamentoById(self, id):
        return self.get_element_by_id(id=id)

    def getPagamentoByMittente(self, mittente):
        query = f"SELECT * FROM {self.table} WHERE mittente = '{mittente}';"
        return self.cursor.execute(query).fetchall()

    def getAllPagamentiSenzaMulte(self):
        query = f"SELECT * FROM {self.table} WHERE tipologia = 'pagamento'"
        return self.cursor.execute(query).fetchall()

    def setPagamentoEffettuato(self, pagamentoId):
        query = f"UPDATE {self.table} SET tipologia ='pagamento effettuato'" \
                f"WHERE id ={pagamentoId}"
        self.queryExecuteCommitter(query)

    def listaPagamentiCompleta(self):
        return self.generalizedSelect(table=self.table)

class MultaDB(GestioneDatabase):
    def __init__(self):
        super().__init__()
        self.init_table('pagamento')
        pass

    def insert_multa(self, destinatario, timestamp, importo, dettaglio):
        query = f"INSERT INTO {self.table}(mittente, destinatario, timestamp, importo, dettaglio, tipologia, multato) VALUES ('Sistema','{destinatario}', '{timestamp}', '{importo}', '{dettaglio}', 'multa', 1);"
        self.queryExecuteCommitter(query)

    def update_multa(self, multaId, mittente, destinatario, timestamp, importo, dettaglio):
        query = f"UPDATE {self.table} SET mittente = '{mittente}', destinatario = '{destinatario}', timestamp= {timestamp}, importo= '{importo}',dettaglio = '{dettaglio}'" \
                f"WHERE id ={multaId}"
        self.queryExecuteCommitter(query)

    def delete_multa(self, id):
        self.delete_element_by_id(id=id)

    def get_multa_by_id(self, id):
        return self.get_element_by_id(id=id)



    def getAllMulte(self):
        query = f"SELECT * FROM {self.table} WHERE tipologia = 'multa'"
        return self.cursor.execute(query).fetchall()

    def setMultaPagata(self, idMulta):
        query = f"UPDATE {self.table} SET tipologia = 'multa pagata' WHERE id='{idMulta}'"
        self.queryExecuteCommitter(query=query)


if __name__ == "__main__":

    '''
    db = MultaDB()
    multa= db.getAllMulte()
    print(multa)

    for i in range(10):
        mittente = 'user1'
        destinatario = 'user2'
        timestamp = str(datetime.date.today())
        importo = 5
        dettaglio = 'multa di prova'
        db.insert_multa(destinatario, timestamp, importo, dettaglio)
'''

    db= PagamentoDB()
    destinatario ='user1'
    print(db.getPagamentoByMittente(mittente='root1'))