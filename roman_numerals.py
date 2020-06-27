roman_numsDict = {
    1000: "M",
    500: "D",
    100: "C",
    50: "L",
    10:"X",
     5:"V",
     1:"I"
}

def roman_numeral(number):
    for key, value in roman_numsDict.items():
            if number - key < 0:
                continue


roman_numeral(int(input("enter a number: ")))
