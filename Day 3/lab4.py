"""
Question:
Given three integers, pprint the smallest one. (Three integers should be user input)

"""

inp1=int(input("Enter the first integer: "))
inp2=int(input("Enter the second integer: "))
inp3=int(input("Enter the third integer: "))

if inp1<=inp2 and inp1<=inp3:
    print("The inp1 is smaller one among inp2 and inp3")
elif inp2<=inp1 and inp2<=inp3:
    print("The inp2 is smaller one among inp1 and inp3")
else:
    print(("The inp3 is smaller one among inp1 and inp2"))
