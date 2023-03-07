with open("./Input/Names/invited_names.txt") as data:
    name_list = data.readlines()
    new_list = []
    for item in name_list:
        new_list.append(item.strip("\n"))

with open("./Input/Letters/starting_letter.txt") as content:
    letter = content.read()

for name in new_list:
    with open(f"./Output/ReadyToSend/Letter_for_{name}", mode="w") as txt:
        new_letter = letter.replace("[name]", name)
        txt.write(new_letter)
