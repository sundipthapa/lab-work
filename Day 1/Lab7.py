#find sum of first 10 odd numbers?


n= int(input("Enter number upto which you want to add odd numbers"))
i=1
sum= 0

while (i<=n): 
           sum=sum+i
           
           i=i+2
print("Sum of Odd numbers=",sum)