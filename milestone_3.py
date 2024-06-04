import random

# TODO: Iteratively check if the input is a valid guess

word_list = ['apples', 'mangoes', 'guava', 'oranges', 'grapes']
word = random.choice(word_list)


# TODO: Define check_guess function

def check_guess(guess):
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")


# TODO: Define ask_for_input function

def ask_for_input():
    guess = input('Enter a single letter: ')
    while True:
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            guess = input(
                "Invalid letter. Please, enter a single alphabetical character: ")
    check_guess(guess)


# TODO: Call function
ask_for_input()
