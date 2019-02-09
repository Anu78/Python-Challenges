import pdb as ev
import sys
import math
roman_numsDict = {
     1:"I",
     5:"V",
    10:"X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

nums_val = [1,5,10,50,100,500,1000]

def roman_numeral(number):
    #variable defs
    largestNum = 0
    largestIndex = 0;
    tempStr = ""
    stringCopy = str(number)
    distTo = 0;

    #check if it's a string, if so, try to convert to int
    if type(number) == str:
        try:
            number = int(number)
        except:
            return "Please enter a number"

    #actual program begins here

    #find closest number out of array values
    for val in nums_val:
        distTo = abs(val-number)
        


    #return the stuff
    return tempStr

print(roman_numeral(str(sys.argv[1])))
