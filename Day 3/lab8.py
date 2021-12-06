"""
Question:
Given a n-digit number. Find the sum of its digits.
or Write a program to find sum of digits of a given number.
or given a three-digit number, find the sum of its digits.
hint:(self) if you enter no=248 then it result will be 14 (2+4+8)
"""
#first method
i=int(input("Enter Number to find sum of digits: "))
sum=0
while (i>0):
    sum=sum+i%10
    i=i//10
print("Sum of digits is",sum)



number=int(input("Enter"))

#Given a three-digit number, find the sum of a given number.
#another method
num=int(input("Enter number to find sum of digits:"))
a=num//100
b=num//10 % 10
c=num % 10
print(a+b+c)
