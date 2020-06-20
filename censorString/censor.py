import re
censorText = open("censor.txt", "r")
resultText = open("result.txt", "w")

censoredWords = ["and", "over"]
replacedWords = []

for word in censoredWords:
    replacedWords.append(re.sub(r'[a-zA-z]', r'-', word))

for x in censorText:
    changedLine = x
    for index in range(0, len(censoredWords)):
        changedLine = changedLine.replace(censoredWords[index], replacedWords[index])
    resultText.write(changedLine)

censorText.close()
resultText.close()