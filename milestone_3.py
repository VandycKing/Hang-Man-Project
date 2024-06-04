# TODO: Ask user for input and validate it

guess = input('Enter a single letter: ')
while True:

    if guess.isalpha() and len(guess) == 1:
        break
    else:
        guess = input(
            "Invalid letter. Please, enter a single alphabetical character: ")
