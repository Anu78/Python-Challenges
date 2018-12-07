#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
endNum = input("Type the ending number: ")
endNum = int(endNum, 10)
tablesDictionary = {}

for i in range(1,endNum+1):
    tablesDictionary[i] = i*i

print(tablesDictionary)
