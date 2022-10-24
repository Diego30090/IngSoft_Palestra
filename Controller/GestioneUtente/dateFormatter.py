from PyQt5.QtCore import QDate


def str_to_date(val):
    print('returned a date')
    date=val.split('-')
    return QDate(int(date[0]), int(date[1]), int(date[2]))