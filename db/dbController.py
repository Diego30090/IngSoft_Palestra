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
    val=str(val[0][0])
    if val == '1':
        return True
    else:
        return False
# funzioni user
def user_info(user):
    cur = connect()
    query = f"SELECT * FROM utente WHERE username='{user}';"
    val = cur.execute(query)
    val= val.fetchall()
    return val[0]

def user_type(user):
    val = user_info(user)
    return val[12]
# funzioni calendario
def event_name_by_date(date):
    cur = connect()
    query = f"SELECT name FROM tasks WHERE date = '{date}';"
    val= cur.execute(query)
    val= val.fetchall()
    return val

def event_by_name_and_date(name, date):
    cur = connect()
    query = f"SELECT * FROM tasks WHERE name = '{name}' and date = '{date}';"
    val= cur.execute(query).fetchall()
    return val[0]

if __name__ == "__main__":
    eT= event_by_name_and_date('Gara Esordienti', '2022-08-14')
    print(eT)