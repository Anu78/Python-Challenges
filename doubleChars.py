import sys

def doubleChar(string):
    newString = ""
    for character in string:
        newString += character*2
    print(newString)

doubleChar(sys.argv[1])