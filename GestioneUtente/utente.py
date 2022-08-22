from db import dbController as db

class User:
    id_utente = None
    username = None
    def __init__(self, username):
        self.username = username

    pass

    def getInfo(self):
        values= db.user_info(self.username)
        print(values)
        self.id_utente=values[0]
        self.nome= values[1]
        self.cognome= values[2]



if __name__ == "__main__":
    u=User("root")
    print(u.id_utente)
    u.getInfo()
    print(u.id_utente)
    print(u.nome)
