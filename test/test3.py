import datetime

if __name__ == '__main__':
    date1 = datetime.date(1952,10,12)

    print(str(date1) + '     ' + str(type(date1)))
    date2 = str(date1)
    print(str(date2) + '     ' + str(type(date2)))
