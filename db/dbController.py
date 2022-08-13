import sqlite3
import Calendario

#It sets the connection to the db, from any folder
def connect():
    con = sqlite3.connect('..\db\dbProject.db')
    cursor = con.cursor()
    return cursor

#Official login function
def login(user, pwd):
    cur=connect()
    query = f"SELECT COUNT(id_utente) FROM utente WHERE username = '{user}' AND password = '{pwd}';"
    val = cur.execute(query)
    val= val.fetchall()
    val = str(val)
    val = ''.join(val)
    val = val.replace('[(','')
    val = val.replace(',)]','')
    if val == '1':
        return True
    else:
        return False




def menu(con, cur):
    value = input(
        'Welcome to the menu.\nWhat do you want to do? \n     1)Check the schema\n     2)Select a table\n     '
        '3)Delete a record\n')
    if value == '1':
        check_schema(con, cur)
    elif value == '2':
        exec_select(con, cur)
    elif value == '3':
        del_elem(con, cur)
    else:
        print('insert correct value\n')
        menu(con, cur)


def check_schema(con, cur):
    schema = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    info_schema = cur.fetchall()
    print(str(info_schema))
    menu(con, cur)


def exec_select(con, cur):
    sel = input('from which table do you want to select?\n')
    print(f'chosen table {sel}\n')
    rows = cur.execute(f'SELECT * FROM {sel}')
    for row in rows:
        print(row)
    print('\n')
    menu(con, cur)


def del_elem(con, cur):
    table = input('from which table do you want to delete?\n')
    record = input('Which record do you want to delete?\n')
    cur.execute(f'DELETE FROM {table} WHERE id={record}')
    menu(con, cur)


def task_insert(val: int, table: str):
    con = sqlite3.connect('dbProject.db')
    cur = con.cursor()
    if val == 1:
        query = f'SELECT * FROM {table}'


if __name__ == "__main__":
    '''
    con = sqlite3.connect('dbProject.db')
    cur = con.cursor()
    #menu(con, cur)
    '''
    res= login('root1','pwd')
    print(res)
