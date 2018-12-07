
operations = ["+","-","*","/","^","MOD","mod"]
# Define function names
def opening_graphics():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("___________________________________________________________________________________")
    print("|||||||||||||||||||||||||||||::::::::::::::::::||||||||||||||||||||||||||||||||||||")
    print("||||||||||||||||||||||||||||| BASIC CALCULATOR ||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||||||::::::::::::::::::||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||________________________________________________________||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| For multiplication, ENTER * ||||||||||||||")
    print("||||||||||||| For division, ENTER / ||||||||||||||")
    print("||||||||||||| For addition, ENTER + ||||||||||||||")
    print("||||||||||||| For subtraction, ENTER - ||||||||||||||")
    print("||||||||||||| Exponents follow after ^ ||||||||||||||")
    print("||||||||||||| For Modulo operations, ENTER MOD or mod ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("||||||||||||| ||||||||||||||")
    print("___________________________________________________________________________________")


opening_graphics()


def grab_input():
    global num1, num2, operation_input
    num1 = input("Input a number: ")
    operation_input = input("OPERATION: ")


    for i in range(0,len(operations)):
        if operations[i] != operation_input:
            break

    num2 = input("Input another: ")

def calculations():
    global result
    if operation_input == operations[0]:
        result = float(num1) + float(num2)
    elif operation_input == operations[1]:
        result = float(num1) - float(num2)
    elif operation_input == operations[2]:
        result = float(num1) * float(num2)
    elif operation_input == operations[3]:
        result = float(num1) / float(num2)
    elif operation_input == operations[4]:
        result = pow(float(num1),float(num2))
    elif operation_input == operations[5] or operation_input == operations[6]:
        result = float(num1) % float(num2)
def display_ans():
    print("____________________________________________________")
    print("\n " + str(num1) + " " + operation_input + " " + str(num2) + " = " + str(result))
    print("____________________________________________________")
def var_reset():
    result = 0
    num1 = 0
    operation_input = 0
    num2 = 0

#Run
def run_prog():
    opening_graphics()
while True:
    grab_input()
    calculations()
    display_ans()

run_prog()
