# TODO: Create a letter using starting_letter.docx
import docx2txt
with open("./Input/Names/invited_names.txt") as names:
    name = names.readlines()

    for i in range(len(name)):
        text = docx2txt.process("./Input/Letters/letters.docx")
        name_strip = name[i].strip()
        invitation = text.replace("Dear ", f"Dear {name_strip},")
        with open(f"./Output/ReadyToSend/{name_strip}.docx", mode="w") as output:
            output.write(invitation)

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp