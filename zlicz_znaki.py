from random import randint
def zassij_slowo():
    lista = []
    f = open('slownik.txt', 'r')
    ile_linii = 0
    lines = f.readlines()
    for line in lines:
        lista.append(line.strip())
        ile_linii += 1
    f.close()
    return(lista[randint(0,ile_linii - 1)])

def dashe(nasze_slowo):
    znaki_w_slowie = len(nasze_slowo)
    return"_ " * znaki_w_slowie


# print(dashe())









