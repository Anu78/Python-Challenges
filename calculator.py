operations = ["+","-","/","*"]
def calculate(string):
    for element in operations:
        if(string.find(element) != -1):
            position = string.find(element)
            operation = element
    num1 = float(string[0:position])
    num2 = float(string[position+1:len(string)])
    if(operation == "+"):
        print(num1+num2)
    if(operation == "-"):
        print(num1-num2)
    if(operation == "/"):
        print(num1/num2)
    if(operation == "*"):
        print(num1*num2)
calculate(input("Enter a calculation: "))