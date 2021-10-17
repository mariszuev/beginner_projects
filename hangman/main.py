import json
import random
import string

data = json.load(open("hangman/words.json"))

value_list = data['data'] # convert dictionary to a list

def hangman():
    choose = random.choice(value_list)
    word = choose.upper()
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # letters guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'attempts left!', 'You have used these letters: ', ' '.join(used_letters))

        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('You have lost. The word was', word)
    else:
        print('You nailed it!', word, '!')

if __name__ == '__main__':
    hangman()