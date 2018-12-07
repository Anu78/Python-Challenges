#Print numbers divisible by 7 but not a multiple of 5
finalNums = []
for i in range(2000,3201):
    if i%7 == 0:
            finalNums.append(i)
for i in finalNums:
    if i%5 == 0:
        finalNums.remove(i)
print(finalNums)
