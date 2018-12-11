#make an fucntion that creates an array of numbers between x and y

def arrayCreator(x,y):
    haha = []
    for i in range(x,y+1):
        haha.append(i)
    print(haha)

x = int(input("x: "))
y = int(input("y: "))
arrayCreator(x,y)
