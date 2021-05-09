import random
from words import words
import string

def Hangman():
    word=random.choice(words)
    word_letters=set(word)
    used_letters=[]
    print(word)
    lives=int(input('Enter your desired lives:'))
    while lives>0 and len(word_letters):
        guess_letter=input('Guess a letter:')
        if guess_letter in word_letters:
            print(guess_letter,' is in the word ')
            used_letters.append(guess_letter)
            word_list=[guess_letter if guess_letter in used_letters else "_" for guess_letter in word]
            word_letters.remove(guess_letter)
            print(word_list)
        elif guess_letter not in word_letters:
            lives-=1
            if lives>0:
                print(guess_letter,' is not in the word. Try again, lives remaining= ', lives)
                used_letters.append(guess_letter)
                print('Here is the letters you used.' ,used_letters)

    if lives == 0:
        print(guess_letter, ' is not in the word.', used_letters)
        print('Ran out of lives! GAME OVER ')
    else:
        print('\t', word.upper())

        print('YAY. You made it.')

Hangman()