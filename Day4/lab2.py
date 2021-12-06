
#2.Write a Python program to sum three given integers. However, if two or more values are
#equal sum will be zero.
"""
a=int(input("Enter the first integer: "))
b=int(input("Enter the second integer: "))
c=int(input("Enter the third integer: "))
sum=a+b+c
if a==b or b==c or a==c:
    print("Sum of the two or more values are equal to zero")
else:
    print("sum of three given integer is {}".format(sum))

"""

a=int(input("Enter the first integer: "))
b=int(input("Enter the second integer: "))
c=int(input("Enter the third integer: "))

if a==b or b==c or a==c:
    print("0")
else:
    print(a+b+c)




#another method using function
def sum(x,y,z):
    if x==y or y==z or x==z:
        sum=0
    else:
        sum=x+y+z
    return sum
#calling a function
print(sum(1,2,3))
print(sum(2,2,5))
print(sum(2,3,3))

#another way
def three_sum(x,y,z):
    if x==y or y==z or x==z:
        return 0
    else:
        return sum(x,y,z)
#calling a function
print(three_sum(1,2,3))
print(three_sum(2,2,5))