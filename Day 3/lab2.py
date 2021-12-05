#WAP which accepts marks of four subjects and display total marks, percentage
#and grade. Hint: more than 70% -> distinction, more than 60% -> first, more than 40% -> pass,
#less than 40% ->fail

a=int(input("Enter a marks of first subject: "))
b=int(input("Enter a marks of second subject: "))
c=int(input("Enter a marks of  third subject: "))
d=int(input("Enter a marks of four subject: "))

#total marks
sum=a+b+c+d
print(f"total marks of four subject is {sum}")

percentage=(sum/400)*100
print(f"percentage of the four subject is {percentage}")

if percentage>=70:
    print("Distinction")
elif percentage>=60:
    print("first division")
elif percentage>=40:
    print("pass")
else:
    print("fali")