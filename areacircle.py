import math

def calcrad(radius):
    print( round((radius*radius)*math.pi,2) )

radius = input("Enter the radius of the circle: ")

while (type(radius) == str):
    try:
        radius = float(radius)
    except:
        print("Please type a number")
        radius = input("Enter the radius of the circle: ")

calcrad(radius)
