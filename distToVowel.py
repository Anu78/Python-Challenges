vowels = [97,101,105,111,117]

def vowelDistance(string):
    finalArray = []
    for element in string:
        finalArray.append(closestValue(ord(element)))
    print(finalArray)

def closestValue(number):
    distances = []
    for vowel in vowels:
        distances.append(abs(number-vowel))
    return min(distances)

vowelDistance(input("enter a string: "))
