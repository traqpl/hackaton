def imie():
    name = input('Podaj imie: ')
    return name

def show_intr():
    im = imie()
    print("\nWitaj %s \n"
    "Bedziesz zmuszony podawac litery z czapy\n"
    "nie majac pojecia o kategorii slowa\n"
    "ale jak zgadniesz slowo wgrasz samochód marki Trabant\n" % im
    )
