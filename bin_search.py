import sys
searchArray = list(range(27))
templateString = "{}, and it took {} guesses"

def binSearch(array, term):
    max = len(array)
    guessCount, min = 0, 0
    guess = int((min/max)/2)
    while min <= max:
        guessCount += 1
        if array[guess] == term:
            print(templateString.format(guess, guessCount))
            quit()
        elif array[guess] < term:
            min = guess+1
            guess = int((min+max)/2)
        elif array[guess] > term:
            max = guess-1
            guess = int((min+max)/2)

if len(sys.argv) == 1:
    print("Please specify an argument.")
    quit()
binSearch(searchArray, int(sys.argv[1]))
