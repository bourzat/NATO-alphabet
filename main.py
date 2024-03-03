import pandas as pd

# Take user input
user_input = input("Enter a word: ").upper()
user_letters = [letter for letter in user_input]

# Reading the CSV file using pandas
df = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_alphabet = dict(zip(df["letter"], df["code"]))

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
phonetic_list = [nato_alphabet[letter] for letter in user_letters if letter in nato_alphabet]
print(phonetic_list)
