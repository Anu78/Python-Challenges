import random
argument = input("Enter Sentence: ")
newString = ""
for character in argument:
    if random.uniform(0,1) >= .5:
        newString += character.upper()
    else:
        newString += character
print(newString)
