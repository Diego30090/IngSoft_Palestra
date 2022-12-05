import datetime

from PyQt5.QtCore import QDate

'''
Testing sul forzare il tipo di dato

'''

class ensure_type():
    def __init__(self, value, types):
        self.value = value
        self.types = types

    def ensure_type(value, types):
        if isinstance(value, types):
            return True
        else:
            raise TypeError('Value {value} is {value_type}, but should be {types}!'.format(
                value=value, value_type=type(value), types=types))

'''
def ensure_type(value, types):
    if isinstance(value, types):
        return value
    else:
        raise TypeError('Value {value} is {value_type}, but should be {types}!'.format(
            value=value, value_type=type(value), types=types))
'''



class Product:
    def __init__(self, name, quantity, date5):
        self.name = name
        self.quantity = quantity
        self.date = date5

    @property
    def name(self):
        return self.__dict__['name']

    @name.setter
    def name(self, value):
        if ensure_type.ensure_type(value, str) is True:
            self.__dict__['name'] = value
        #self.__dict__['name'] = ensure_type.ensure_type(value, str)


    @property
    def quantity(self):
        return self.__dict__['quantity']

    @quantity.setter
    def quantity(self, value):
        self.__dict__['quantity'] = ensure_type(value, int)

    @property
    def date(self):
        return self.__dict__['date']

    @date.setter
    def date(self, value):
        self.__dict__['date'] = ensure_type(value, datetime.date)

if __name__ == '__main__':
    date1 = datetime.date(1952,10,12)
    prodotto = Product('asd', 25, date1)




