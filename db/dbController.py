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


def user_type(user):
    val = user_info(user)
    return val[12]


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

def update_event(event_id, new_name, new_location, new_time, new_organizer, new_description):
    con = sqlite3.connect('..\db\dbProject.db')
    cur = con.cursor()
    query = f"UPDATE tasks SET name = '{new_name}', location = '{new_location}', time = '{new_time}', organizer = '{new_organizer}', description = '{new_description}' WHERE id='{event_id}'"
    cur.execute(query)
    con.commit()

if __name__ == "__main__":
    remove_event(13)