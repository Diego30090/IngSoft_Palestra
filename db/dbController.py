import sqlite3
import Calendario


# It sets the connection to the db, from any folder
def connect():
    con = sqlite3.connect('..\db\dbProject.db')
    cursor = con.cursor()
    return cursor


# Funzione universale per insert/delete/update
def idu(query):
    con = sqlite3.connect('..\db\dbProject.db')
    cur = con.cursor()
    cur.execute(query)
    con.commit()


# Official login function
def login(user, pwd):
    cur = connect()
    query = f"SELECT COUNT(id_utente) FROM utente WHERE username = '{user}' AND password = '{pwd}';"
    val = cur.execute(query)
    val = val.fetchall()
    val = str(val[0][0])
    if val == '1':
        return True
    else:
        return False

def check_username(user):
    cur = connect()
    query = f"SELECT COUNT(id_utente) FROM utente WHERE username = '{user}';"
    val = cur.execute(query).fetchone()
    val = str(val[0])
    if val == '1':
        return True
    else:
        return False

# funzioni user
def user_info(user):
    cur = connect()
    query = f"SELECT * FROM utente WHERE username='{user}';"
    val = cur.execute(query)
    val = val.fetchall()
    return val[0]


def user_info_by_id(id):
    cur = connect()
    query = f"SELECT * FROM utente WHERE id_utente='{id}';"
    val = cur.execute(query).fetchone()
    return val


def user_type(user):
    val = user_info(user)
    return val[6]


def user_pass(user):
    val = user_info(user)
    return val[5]


# funzioni calendario
def event_name_by_date(date):
    cur = connect()
    query = f"SELECT * FROM tasks WHERE date = '{date}';"
    val = cur.execute(query)
    val = val.fetchall()
    return val


def event_by_id(id):
    cur = connect()
    query = f"SELECT * FROM tasks WHERE id='{id}';"
    val = cur.execute(query).fetchall()
    return val[0]


def insert_event(name, date, location, time, organizer, description):
    query = f"INSERT INTO tasks(name, date, location, time, organizer, description) VALUES ('{name}','{date}', '{location}','{time}', '{organizer}', '{description}');"
    idu(query)


def remove_event(event_id):
    query = f"DELETE FROM tasks WHERE id='{event_id}';"
    idu(query)


def update_event(event_id, name, location, time, organizer, description):
    query = f"UPDATE tasks SET name = '{name}', location = '{location}', time = '{time}', organizer = '{organizer}', " \
            f"description = '{description}' WHERE id='{event_id}' "
    idu(query)


# Funzione update dello user
def update_user(name, surname, born_data, email, phone, user_type, username):
    query = f"UPDATE utente SET nome= '{name}', cognome = '{surname}', data_nascita = '{born_data}', email = '{email}', telefono= '{phone}', utente_tipo= '{user_type}' WHERE username='{username}';"
    idu(query)


def insert_user(nome, cognome, data_nascita, username, password, utente_tipo, email, telefono):
    query = f"INSERT INTO utente(nome, cognome, data_nascita, username, password, utente_tipo, email, telefono) VALUES " \
            f"('{nome}','{cognome}', '{data_nascita}', '{username}', '{password}', '{utente_tipo}', '{email}', '{telefono}') ; "
    idu(query)


def select_utente(user_type):
    cur = connect()
    query = f"SELECT * from utente WHERE utente_tipo = '{user_type}';"
    val = cur.execute(query).fetchall()
    return val


# Funzioni inventario/mercato
def select_inventario(tab_type):
    cur = connect()
    if tab_type == 'armi':
        query = f"SELECT * FROM armi;"
    elif tab_type == 'divise':
        query = f"SELECT * FROM divise;"
    elif tab_type == 'borsoni':
        query = f"SELECT * FROM borsoni;"
    val = cur.execute(query).fetchall()
    return val


if __name__ == "__main__":
    print(check_username('root0'))