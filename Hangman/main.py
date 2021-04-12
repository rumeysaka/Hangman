

import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word= random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = int(input('Enter desired number of lives:'))

    while len(word_letters)>0 and lives>0:
        print('You have ',lives,' lives left and  you have used these letters:', (used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('')
        print('Current word: \t \t \t \t \t \t \t \t \t', ' '.join(word_list))

        user_letter = input('Guess your letter:').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            lives=lives-1
            print(f'you have already used {user_letter}. Please guess again.')
        else:
            print('you entered invalid character.')
            used_letters.add(user_letter)


    if lives==0:
        print('you died sorry. The word was', word)
    else:
        print('\t \t \t \t \t \t \t \t \t \t' ,' '.join(word))
        print('YAY you made it.')


hangman()