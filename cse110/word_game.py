'''
File: word_game.py
Author: James Thomas
Purpose: Provide a word game similar to Wordle for user to play/
'''
# imports
from english_words import english_words_lower_alpha_set
import random

play = 'yes'


# game intro and explanation
print()
print('Welcome to the word guessing game!\n')

print('Color Key:\n')
print('\033[1;32mGreen\033[0m = In the correct spot.')
print('\033[1;33mYellow\033[0m = In the word, but not in the correct spot.')
print('\033[1;31mRed\033[0m = Not in the word.\n')


# keep playing until player says no to playing again
while play.lower() == 'yes':
    # convert english word set to list and take random word
    word_list = list(filter(lambda x: len(x) == 5,
                     set(english_words_lower_alpha_set)))
    correct_word = random.choice(list(word_list))

    num_guesses = 1

    print()
    print()
    print('Your hint is: _ _ _ _ _ \n')
    guess = input('Please enter a 5 letter word: ')
    print()

    while guess != correct_word:
        for i in range(correct_word.__len__()):
            if guess[i].lower() == correct_word[i]:
                print("\033[1;32m" + guess[i].upper(), end='' + '\033[0m')
            elif guess[i].lower() in correct_word:
                print('\033[1;33m' + guess[i].lower(), end='' + '\033[0m')
            else:
                print('\033[1;31m' + '_', end='' + '\033[0m')

        print()
        print()
        guess = input('Please enter a 5 letter word: ')
        print()
        num_guesses += 1

        if guess.lower() == correct_word:
            print()
            print()
            print(
                f"\033[1;32mThat's Correct! Congratulations! You Win! Number of guesses: {num_guesses}\n" + '\033[0m')
            print()
            play = input('Would you like to play again?(Yes/No)\n')


if play.lower() == 'no':
    print()
    print('Thank you for playing. Have a great day!')
    print()
