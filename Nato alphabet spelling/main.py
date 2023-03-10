import pandas

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_df = pandas.DataFrame(nato_data)
nato_dic = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Type a word to spell: ").upper()
user_word_list = [nato_dic[letter] for letter in user_word]
print(user_word_list)
