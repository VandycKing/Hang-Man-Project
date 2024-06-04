# %%

import random

# TODO: Create a list with your favourite fruits
word_list = ['apples', 'mangoes', 'guava', 'oranges', 'grapes']

# TODO: print items in word_list
for element in word_list:
    print(f'The word is: {element}')

# %%

# TODO: Get a word from the word list
word = random.choice(word_list)
print('The randomly selected word is {}'.format(word))


# %%

# TODO: Accepts input and checks if input is valid
guess = input('Enter a letter: ')

if guess.isalpha() and len(guess) == 1:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
