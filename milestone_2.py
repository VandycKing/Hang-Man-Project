# %%
import random

# TODO: Create a list with your favourite fruits
word_list = ['apples', 'mangoes', 'guava', 'oranges', 'grapes']

# TODO: print items in word_list
for i in word_list:
    print(f'The word is: {i}')

# TODO: Get a word from the word list
word = random.choice(word_list)
print('The randomly selected word is {}'.format(word))
# %%
