#Write a program function to find min of three numbers.(no parameter and no return type)

def min():
    x=10
    y=3
    z=12
    if x<y and x<z:
        print("x is min among other")
    elif y<x and y<z:
        print("y is min among other")
    elif z<x and z<y:
        print("z is min among other")

min()