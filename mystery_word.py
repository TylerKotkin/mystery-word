import random
import re


def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    easy_words = []
    for word in word_list:
        if len(word) >=4 and len(word) <= 6:
            easy_words.append(word)

    return easy_words



def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    medium_words = []
    for word in word_list:
        if len(word) >= 6 and len(word) <=8:
            medium_words.append(word)

    return medium_words



def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    hard_words = []
    for word in word_list:
        if len(word) >=8:
            hard_words.append(word)

    return hard_words


def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    mys_word = random.choice(word_list)
    return mys_word


def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    display = []
    for guess in word:
        if guess in guesses:
            display.append(guess)
        else:
            display.append('_')
    display = ' '.join(display).upper()
    return display


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """


    for letter in word:
        if letter not in guesses:
            return False
    return True





def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
    """
    with open ('/usr/share/dict/words') as d:
        all_words = d.read()
    all_words = all_words.split()





    difficulty = input( "Please select a difficulty level or enter quit to quit. \n Enter easy, medium or hard: ")
    if difficulty == 'easy':
        correct_word = random_word(easy_words(all_words))
        print('You selected the easy level. \n Goodluck.')
    elif difficulty == 'medium':
        correct_word = random_word(medium_words(all_words))
        print('You selected the medium level. \n Goodluck.')
    elif difficulty == 'hard':
        correct_word = random_word(hard_words(all_words))
        print('You selected the hard level. \n Goodluck.')
    elif difficulty == 'quit':
        print('Goodbye.')
        exit()
    else:
        print('That is not an accepted difficulty level.')
        return main()

#  guessing

    wrong = 8
    guessed = []
    print('The word has {} letters'.format(len(correct_word)))
    while wrong > 0 and is_word_complete(correct_word, guessed) == False:
        print(display_word(correct_word, guessed))
        print('{} guesses remaining'.format(wrong))
        print(guessed)
        while True:
            last_letter = input('Guess a letter: ').lower()
            if last_letter in guessed:
                print('Please guess a new letter.')
                continue
            elif len(last_letter) > 1:
                print('Only enter a single letter.')
                continue
            elif last_letter.isalpha() != True:
                print('You can only enter a letter.')
                continue
            elif last_letter in correct_word:
                guessed.append(last_letter)
                print('Correct.')
                break
            elif last_letter not in correct_word:
                print('Wrong.')
                wrong -= 1
                guessed.append(last_letter)
                break
            else:
                continue

# result

    if wrong <= 0:
        x = input(('You ran out of guesses. The word was {}. \n  Enter yes to play again: '.format(correct_word)))
        if x == 'yes':
            return main()
        else:
            exit()
    else:
        x = input('You guessed the word. \n Enter yes to play again: ')
        if x == 'yes':
            return main()
        else:
            exit()





if __name__ == '__main__':
    main()
