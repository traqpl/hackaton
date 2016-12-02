import string

letters = string.ascii_letters
used_letters = ''

def ask_letter(question, chosen_letters):
    while True:
        choice = input(question)
        try:
            choice = str(choice)
        except Exception as e:
            print("Not a letter: ", e)
        else:
            if choice in chosen_letters:
                print("You already chose ", choice)
            elif choice not in letters:
                print("That wasn't a letter!\n")
            else:
                print("Thanks for the letter: ", choice)
                chosen_letters += choice
                ''.join(sorted(chosen_letters))
                print("Your chosen letters are: ", chosen_letters)
                return choice, chosen_letters

ask_letter("Give me a letter:\n", used_letters)
