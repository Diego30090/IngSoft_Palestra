def dictTest1():
    dict1 = {'try1': ['asd', 'asd1']}
    dict2 = {'try2': ['as', 'ss']}

    dict3 = {}
    dict3.update(dict1)
    dict3.update(dict2)

    print(dict3)


def dictTest2():
    key = ('key1', 'key2')
    values = ['val1', 'val2'], ['val3', 'val4']
    dict1 = dict.fromkeys(key)
    print(dict1)


def dictTest3():
    key = ('key1', 'key2')
    values = [['val1', 'val2'], ['val3', 'val4']]
    dict1 = dict.fromkeys(key)
    for i in range(len(key)):
        dict1[key[i]] = values[i]

    print(dict1)



if __name__ == "__main__":
    dictTest3()
    pass
