def somar():
    print('Essa função somar valores')

def multi():
    print('Essa função vai multiplicar as valores')


def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
        return -1