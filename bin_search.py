searchVal = int(input("Enter the value to search: "))
searchArray = []
#array generation
for i in range(0,27):
    searchArray.append(int(i))
def binSearch(array, term):
    max = len(array)
    guessCount = 0
    min = 0
    guess = int((min+max)/2)
    while min <= max:
        guessCount+=1
        if(array[guess] == term):
            print(str(guess) + ", and it took " + str(guessCount) + " guess(es)")
            break
        elif(array[guess] < term):
            min = guess+1
            guess = int((min+max)/2)
        elif(array[guess] > term):
            max = guess-1
            guess = int((min+max)/2)
binSearch(searchArray, searchVal)
