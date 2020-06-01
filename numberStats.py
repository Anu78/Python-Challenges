from collections import Counter
numberArray = [6, 4, 9, 1, 1, 0, 34]
meanValue = 0
mode = 0
median = 0
length = len(numberArray)
numberArray.sort()
occurences = Counter(numberArray)
# Mean finding
for element in numberArray:
    meanValue += element
    meanValue /= len(numberArray)

# Mode finding


# Print histogram
for element in occurences:
    print(str(element) + " | ", end='')
    for boo in range(occurences[element]):
        print("*",end='')
    print("")

# Median finding
middleVal = int(length/2 - 1)
if length % 2 == 0:
    median = (numberArray[middleVal] + numberArray[middleVal+1])/2
else:
    median = numberArray[round(length/2)]

# Printing things
print("\nMean: " + str(round(meanValue, 2)))
print("Median: " + str(median))