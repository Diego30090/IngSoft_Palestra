import sqlite3


# It sets the connection to the db, from any folder
def connect():
    con = sqlite3.connect('..\..\db\dbProject.db')
    cursor = con.cursor()
    return cursor


# Funzione universale per insert/delete/update
def idu(query):
    con = sqlite3.connect('..\..\db\dbProject.db')
    cur = con.cursor()
    cur.execute(query)
    con.commit()

# Funzioni inventario/mercato
def select_inventario(tab_type):
    cur = connect()
    query = f"SELECT * FROM {tab_type};"
    val = cur.execute(query).fetchall()
    return val


def insert_inventario(tab_type, info):
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
    idu(query)


def select_inventario_by_id(id, tab_type):
    cur = connect()
    query = f"SELECT * FROM {tab_type} WHERE id = {id};"
    val = cur.execute(query).fetchone()
    return val


if __name__ == "__main__":
    print('asd')