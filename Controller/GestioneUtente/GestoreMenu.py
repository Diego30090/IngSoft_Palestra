from Controller.GestioneDatabase.GestoreDatabase import MenuDB
from Model.GestioneUtente.menuOptionModel import menuOption as menu


class GestoreMenu:
    def __init__(self):
        self.menuList = []
        self.menuDict = {}
        self.getMenuList()
        self.setChildMenu()
        self.getDictFromMenuVoices()

    '''
    Questa parte è dedicata all'ottenimento dei valori per il menu, messi all'interno di self.menuList per indicizzarli 
    tramite modello
    '''
    def getMenuList(self):
        menuList = MenuDB().getAllParents()
        for elem in menuList:
            self.menuList.append(menu(*elem))

    def setChildMenu(self):
        childs = self.getAllChild()
        for child in childs:
            for parent in self.menuList:
                if child.parentVoice == parent.id:
                    parent.child.append(child)

    def getAllChild(self):
        child = MenuDB().getAllChild()
        childList = []
        for elem in child:
            childList.append(menu(*elem))
        return childList

    def printChilds(self):
        for parent in self.menuList:
            print(str(parent.id) + " - " + parent.nome)
            for elem in parent.child:
                print(str(elem.id) + " - " + elem.nome)


    '''
    Questa parte si occupa di prendere i precedenti modelli indicizzati e trasformarli in un dizionario.
    Regole per questa parte:
        1 - I 'parents' corrispondono alle key
        2 - I 'childs' corrispondono ai valori
    '''

    def getDictFromMenuVoices(self):
        for parent in self.menuList:
            key = str(parent.id) + " - " + parent.nome
            childs = []
            for child in parent.child:
                value = str(child.id) + " - " + child.nome
                childs.append(value)
            self.menuDict[key] = childs



if __name__ == "__main__":
    gm = GestoreMenu()
    gm.getDictFromMenuVoices()