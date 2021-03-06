
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

def display_guess(word, chosen_letters):
    """
    Given the actual word to be guessed by player, display it in dashes.
    :param word:
        This is the word that the player is supposed to guess.
    :param chosen_letters:
        This is a list of letters already chosen by the player.
    :return:
    """
    dashed_word = ''
    for letter in word:
        if letter in chosen_letters:
            dashed_word += letter
        else:
            dashed_word += '_'
    return ' '.join(dashed_word)

# tests
if __name__ == '__main__':
    used_letters = 'abcdefg'
    word_to_guess = "hackathon"
    print(get_letter("Gimme a letter!\n", used_letters))
    print(display_guess(word_to_guess, used_letters))