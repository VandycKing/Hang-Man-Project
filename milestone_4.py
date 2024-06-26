import random

# TODO: Define the Hangman Class


class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")

            for idx, element in enumerate(self.word):
                if element == guess:
                    self.word_guessed[idx] = element

            self.num_letters = - 1

        else:
            self.num_lives = - 1
            print(f"Sorry, '{element}' is not in the word.")
            print(f"You have '{self.num_lives}' lives left.")

    def ask_for_input(self):
        guess = input('Enter a single letter: ')

        while True:
            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
                break
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                break
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


word_list = ['apples', 'mangoes', 'guava', 'oranges', 'grapes']
hang_man_obj = Hangman(word_list)
hang_man_obj.ask_for_input()
