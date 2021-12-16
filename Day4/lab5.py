"""
5.A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.

"""

a=int(input("Enter no of classes held:"))
b=int(input("Enter no of classes attende:"))

percentage=(b/a)*100
if percentage<=75:
    print("A student will not be allowed to sit in exam.")
elif percentage>75:
    print("A student is allowed to sit in exam")
