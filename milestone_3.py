import random

# TODO: Ask user for input and validate it

guess = input('Enter a single letter: ')
while True:

    if guess.isalpha() and len(guess) == 1:
        break
    else:
        guess = input(
            "Invalid letter. Please, enter a single alphabetical character: ")


# TODO: Iteratively check if the input is a valid guess

word_list = ['apples', 'mangoes', 'guava', 'oranges', 'grapes']
word = random.choice(word_list)

if guess in word:
    print(f"Good guess! '{guess}' is in the word.")
else:
    print(f"Sorry, '{guess}' is not in the word. Try again.")
