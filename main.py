import pandas as pd
import os
import time

df = pd.read_csv('nato_phonetic_alphabet.csv')

dict_of_data = {row.letter:row.code for (index, row) in df.iterrows()}

while True:
    user_setence = input('Setence:\n')
    os.system('clear')
    list_of_words = [dict_of_data[f'{x}'] for x in user_setence.upper() if x != ' ']
    print(list_of_words)
    time.sleep(5)
    os.system('clear')
