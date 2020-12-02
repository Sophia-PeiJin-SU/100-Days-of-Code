import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_frame = pandas.DataFrame(data)

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(new_dict)

word = input("Enter a word: ").upper()
new_list = [new_dict[letter] for letter in word]
print(new_list)
