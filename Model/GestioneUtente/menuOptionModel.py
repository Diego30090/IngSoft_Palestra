from Controller.GestioneDatabase.GestoreDatabase import MenuDB

class menuOption:
    def __init__(self, id, parentVoice, nome, isAtletaAllowed, isIstruttoreAllowed, isAdminAllowed):
        self.id = id
        self.parentVoice = parentVoice
        self.nome = nome
        self.isAtletaAllowed = isAtletaAllowed
        self.isIstruttoreAllowed = isIstruttoreAllowed
        self.isAdminAllowed = isAdminAllowed
        self.child = []

    def checkParent(self):
        if "." not in str(self.id):
            return True
        else:
            return False

    def childAppend(self, child):
        if isinstance(child, menuOption):
            self.child.append(child)
        else:
            raise ValueError("Child must be of type 'menuOption'")
