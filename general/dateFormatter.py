from PyQt5.QtCore import QDate


def str_to_date(val):
    print('returned a date')
    date=val.split('-')
    return QDate(int(date[0]), int(date[1]), int(date[2]))


if __name__ == '__main__':
    val='1955-02-21'
    d= QDate(9,9,9)
    print(str(str_to_date(val)))
