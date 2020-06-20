#generate the first n numbers of the fibonacci sequence 
def fibonacci(n):
    array = [0,1]   
    for f in range(0,n-2):
        array.append(array[f]+array[f+1])
    print(array)


try:
    fibonacci(int(input("How many? ")))
except:
    print("Please type an integer.")