import sqlite3
import Calendario


# It sets the connection to the db, from any folder
def connect():
    con = sqlite3.connect('..\db\dbProject.db')
    cursor = con.cursor()
    return cursor


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
    con = sqlite3.connect('..\db\dbProject.db')
    cur = con.cursor()
    query = f"INSERT INTO tasks(name, date, location, time, organizer, description) VALUES ('{name}','{date}', '{location}','{time}', '{organizer}', '{description}');"
    cur.execute(query)
    con.commit()


def remove_event(event_id):
    con = sqlite3.connect('..\db\dbProject.db')
    cur = con.cursor()
    query = f"DELETE FROM tasks WHERE id='{event_id}';"
    cur.execute(query)
    con.commit()


def update_event(event_id, name, location, time, organizer, description):
    con = sqlite3.connect('..\db\dbProject.db')
    cur = con.cursor()
    query = f"UPDATE tasks SET name = '{name}', location = '{location}', time = '{time}', organizer = '{organizer}', " \
            f"description = '{description}' WHERE id='{event_id}' "
    cur.execute(query)
    con.commit()


# Funzione update dello user
def update_user(name,surname, born_data, email, phone, user_type, username):
    con = sqlite3.connect('..\db\dbProject.db')
    cur = con.cursor()
    query= f"UPDATE utente SET nome= {name}, cognome = {surname}, data_nascita = {born_data}, email = {email}, telefono= {phone}, utente_tipo= {user_type} WHERE username={username};"
    cur.execute(query)
    con.commit()


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
    print(user_info_by_id(3)[0])

