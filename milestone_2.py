# %%

import random

# TODO: Create a list with your favourite fruits
word_list = ['apples', 'mangoes', 'guava', 'oranges', 'grapes']

# TODO: print items in word_list
for i in word_list:
    print(f'The word is: {i}')

# %%

# TODO: Get a word from the word list
word = random.choice(word_list)
print('The randomly selected word is {}'.format(word))


# %%

# TODO:
guess = input('Enter a letter: ')

if guess.isalpha() and len(guess) == 1:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
