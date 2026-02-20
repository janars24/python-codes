import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
#read the data frame and change to dict
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

name = input("Enter your name: ").upper()
output_list = [phonetic_dict[letter] for letter in name]
print(output_list)