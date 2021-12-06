#Write a program to print absolute value of a number entered by user.
#eg. input:1 output:1 input:-1 output:1

#first method
#num=int(input("Enter a number: "))
#absolute=abs(num)
#print("Number:{}".format(absolute))

"""
#another method using list
#Some random numbers
values=[-40,34,-78, 43, 234 ,-34,34]
#Get the absolute value for each number
absValues=[abs(number) for number in values]
#output data
print("The original number:\n",values)
print("The absolute number:\n",absValues)

"""

#third method
#some random integer
variableA=-67
variableB=0
variableC=90
variableD=-987
#get the absolute of the integers
absA=abs(variableA)
absB=abs(variableB)
absC=abs(variableC)
absD=abs(variableD)
#output the results
print("Absolute values of integers with 'abs()' :")
print("The value of variableA",absA)
print("The value of variableB",absB)
print("The value of variableC",absC)
print("The value of variableD",absD)