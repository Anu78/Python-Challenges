#Take a factorial of a number
inputNum = input("Type a number to get a factorial of: ")
inputNum = int(inputNum,10)
originalNum = inputNum
lesserVals = []
#array of lesser values
for lessernums in range(2,inputNum):
    lesserVals.append(lessernums)
for value in range(0,len(lesserVals)):
    inputNum *= lesserVals[value]
print(inputNum)
