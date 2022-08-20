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

def user_info(user):
    cur = connect()
    query = f"SELECT * FROM utente WHERE username='{user}';"
    val = cur.execute(query)
    val= val.fetchall()
    return val[0]

def user_type(user):
    val = user_info(user)
    return val[12]

if __name__ == "__main__":
    uT = user_type('root')
