from PIL import Image
import botek
import instrukcja
import helpers
import zlicz_znaki
import losuj_slowo
import szubienica

class run:
    #pobierz imie i wyswietl inst
    def firts_step(self):
        instrukcja.show_intr()



if __name__ == '__main__':
    guessed_word = '_'
    fuckups_counter = 0
    run = run()
    run.firts_step()
    zassane_slowo = zlicz_znaki.zassij_slowo()
    used_letters = ""
    print('dla nas dla sprawdzenia: ', zassane_slowo)
    print(zlicz_znaki.dashe(zassane_slowo))
    while fuckups_counter < 10 and '_' in guessed_word:
        chosen_letter = helpers.get_letter("Podaj litere: \n", used_letters)
        #kolekcja uzytych liter
        used_letters += chosen_letter
        if chosen_letter in zassane_slowo:
            guessed_word = helpers.display_guess(zassane_slowo, used_letters)
            print(guessed_word)
            print("uzyte litery: ", used_letters)
        else:
            nr_image = str(fuckups_counter) + str('.jpg')
            img = Image.open(nr_image)
            img.show()
            print("uzyte litery: ", used_letters)
            fuckups_counter += 1

        if fuckups_counter == 10:
            print(botek.bot('loose'))
            print("Przegrales")
            break

        if '_' not in guessed_word:
            print("Wygrales")
            print(botek.bot('winner'))
            break