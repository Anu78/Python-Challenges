def additivePersistence(number):
    count = 1
    if len(number) == 1:
        count = 0
    while len(str(addDigits(number))) != 1:
        number = addDigits(number)
        count += 1
    print(count)


def multiplicativePersistence(number):
    count = 1
    if len(number) == 1:
        count = 0
    while(len(str(addDigits(number)))) != 1:
        number = multiplyDigits(number)
        count +=1
    print(count)

def addDigits(number):
    number = str(number)
    final = 0
    for character in number:
        final += int(character)
    return final

def multiplyDigits(number):
    number = str(number)
    final = 0
    for character in number:
        final *= int(character)
    return final

choice = input("M or A: ")
if choice == "A":
    additivePersistence(input("enter a number: "))
elif choice == "M":
    multiplicativePersistence(input("enter a number: "))

