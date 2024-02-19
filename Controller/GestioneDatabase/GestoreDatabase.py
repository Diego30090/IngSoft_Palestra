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
        self.table=table


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
        query = f"SELECT * FROM {self.table} WHERE id='{id}';"
        return self.cursor.execute(query).fetchall()[0]

    def insert_event(self, name, date, location, time, organizer, description):
        query = f"INSERT INTO {self.table}(name, date, location, time, organizer, description) VALUES ('{name}','{date}', '{location}','{time}', '{organizer}', '{description}');"
        self.queryExecuteCommitter(query)

    def remove_event(self, event_id):
        query = f"DELETE FROM {self.table} WHERE id='{event_id}';"
        self.queryExecuteCommitter(query)

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


if __name__ == "__main__":
    db = EventoDB()
    #print(db.check_username(user='root0'))
    print(db.event_name_by_date('2023-09-20'))
