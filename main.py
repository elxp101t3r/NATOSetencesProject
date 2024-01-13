import pandas as pd
import os
import time

df = pd.read_csv('nato_phonetic_alphabet.csv')

dict_of_data = {row.letter:row.code for (index, row) in df.iterrows()}

while True:
    user_setence = input('Setence:\n')
    os.system('clear')
    list_of_words = [dict_of_data[letter] for letter in user_setence.upper() if letter != ' ']
    print(list_of_words)
    time.sleep(5)
    os.system('clear')
    
    if user_setence == 'exit':
        break
