#!/usr/local/bin/python3
operations = ["%","*","/","+","-","%", "MOD", "mod"]

operation_input = input("type an operation:  ")

while (operation_input in operations) == False:
    print("Failure")
    operation_input = input("type an operation: ")

print("Success")
