import random
class Losowanie:
    def losuj_slowo(self):
        list = []
        f = open('slownik.txt','r')
        a = f.readlines()
        for line in a:
            list.append(line)
            slowo = random.choice(list)
        f.close()
        return slowo
if __name__ == '__main__':
    losowanie1 = Losowanie()
    print(losowanie1.losuj_slowo())
