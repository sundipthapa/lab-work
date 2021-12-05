"""
Question:
Given a positive number, print its fractional part

"""
#first method
#x=float(input("Enter a positive real number: "))
#print(x-int(x))



#another method
import math
a=float(input("Enter a positive real number: "))
x,y=math.modf(a)
print(x)
print(y)


#num=int(input("Enter the number: "))
#real=num-int(num)
#frac=str(round(real,3))
#print(frac)