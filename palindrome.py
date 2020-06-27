import sys

def palindrome(thing):
    if thing == thing[::-1]:
        print("yes")
    else:
        print("no")

palindrome(sys.argv[1])