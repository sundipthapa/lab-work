#10.  WAP which accepts marks of four subjects and display total marks, percentage and 
#grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, 
#less than 40% –> fail
























#1ans.
name='kiran'
print[::-1]


def reverse(string):
	reversed_string = " "
	for i in string:
		reversed_string = i+reversed_string
	print("reversed string is:", reversed_string)
string = input("enter a string:")
print("entered string",string)
reverse(string)

#2ans.
def fizzbuzz (num):
    if (num%3==0) and (num%5==0):
        return "Fizzbuzz"
    elif num%5==0:
        return "Buzz"
    elif num%3==0:
        return "Fizz"
    else:
        print(num)
#calling function
a=int(input("enter the number:"))
b=fizzbuzz(a)
print(b)
print("end of program")

#3ans.
def check():
    a=int(input("enter the first number:"))
    b = int(input("enter the second number:"))
    c = int(input("enter the third number:"))
    if (a>b) and (a>c):
        print(a,"is maximum number.")  
    elif (b>a) and (b>c):
        print(b,"is maximum number.")
    else:
        print(c,"is greater.")
#function calling
check()
print("end of program")

#4ans.
def demo(name, age):
    print(name, age)
demo("Ben", 25)

#7ans.
multiply = (8,2,3,-1,7)
total =1
for x in multiply:
	total *=x
print(total)

#8ans.
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))

#9ans.
import random
list=[1,4,8,7,9,6,3]
print("original list is : ", list)
a = random.choice(list)
print("Random selected number is : ", a)

#10ans.
p=int(input("enter marks for physics:"))
c=int(input("enter marks for chemistry:"))
b=int(input("enter marks for biology:"))
m=int(input("enter marks for maths:"))
totalmarks=p+c+b+m
print("Total score is ",totalmarks)
percentage=(totalmarks/400)*100
print("total percent is ",percentage,"%")
if percentage>70:
    print("he got distinction ")
elif percentage>60:
    print("he got first division")
elif percentage>40:
    print("he passed the exam")
elif percentage<40:
    print("he is failed")
