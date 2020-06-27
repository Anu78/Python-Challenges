import re
censorText = open("censorString/censor.txt", "r")

wordstoCensor = ["and", "over"]
replacedWords = []

for word in wordstoCensor:
    replacedWords.append(re.sub(r'[a-zA-z]', r'-', word))

for x in censorText:
    changedLine = x
    for index in range(0, len(wordstoCensor)):
        changedLine = changedLine.replace(
            wordstoCensor[index], replacedWords[index])
    censorText.write(changedLine)

censorText.close()