import pdb
inputNum = int(input("Type a number to get the factorial of:"))
for lessernums in range(1,inputNum):
    inputNum*=lessernums
if inputNum==0:
    print(1)
else:
    print(inputNum)