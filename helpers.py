
def get_letter(question, chosen_letters):
    """
    Get a new letter from player. Step by step:
        ask question
        check if input is one character
        check if input is a letter
        convert input to lowercase
        check if input is in used letters
        return new chosen letter
    :param question:
        This is the question to be asked, when asking player for a new letter.
    :param chosen_letters:
        This is a list of letters already chosen by the player.
    :return:
        Returns one new letter, chosen by the player.
    """

    # grab letters
    from string import ascii_letters
    letters = ascii_letters

    while True:
        # ask question
        choice = input(question)

        # check if input is one character
        if len(choice) != 1:
            print(choice, "isn't just one letter!\n")
            continue

        # check if input is a letter
        if choice not in letters:
            print(choice, "isn't a letter!\n")
            continue

        # convert input to lowercase
        choice = choice.lower()

        # check if input is in used letters
        if choice in chosen_letters:
            print(choice, "has already been chosen!\n")
            continue

        # return new chosen letter
        return choice

# tests
if __name__ == '__main__':
    used_letters = ''
    print(get_letter("Gimme a letter!\n", 'abcdefghi'))