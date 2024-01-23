import pandas as pd
import os
import time

df = pd.read_csv('nato_phonetic_alphabet.csv')

dict_of_data = {row.letter:row.code for (index, row) in df.iterrows()}

while True:
    user_setence = input('Setence:\n')
    os.system('clear')
    try:
        list_of_words = [dict_of_data[letter] for letter in user_setence.upper() if letter != ' ']
        print(list_of_words)
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
    time.sleep(len(list_of_words) + 1)
    os.system('clear')
    
    if user_setence == 'exit':
        break
