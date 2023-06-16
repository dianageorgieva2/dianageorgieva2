import csv
import pandas as pd

# Import the Morse codes for alphabet and numbers.
with open("morse2.csv", encoding="utf8") as file:
    data = pd.read_csv(file)
    # print(data.code[data.letter == "A"])

# Get hold of the text to be converted and transform it to string of chars.
text_to_convert = input("What is the text to be converted in Morse? ").upper()
list_text = list(text_to_convert)
print(list_text)
print(data.code[data.letter == "A"])


#  Translate text into morse code text.
morse_text = []
for item in list_text:
    if item in data.letter.values:
        morse_code = data.code[data.letter == item].values
        print(morse_code)
        morse_text.append(morse_code[0])
    else:
        pass
print(f"Your text in morse code is: {morse_text}")



