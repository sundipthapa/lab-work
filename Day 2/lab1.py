#convert second to day, hour and minute
#a=int (input("Enter the value  "))
#b=a/86400
#c=a/3600
#d=a/60
#print("the converted value of second into day is ",b)
#print("the converted value of second into hour is ",c)
#print("the converted value of second into minute is ",d)


s=int(input("enter the value for second"))

Day= (((s/60)/60)/24)
print(f"total day for given second: {Day}")
Hour=((s/60)/60)
print(f"total hours for given seconds:{Hour}")
Minute =(s/60)
print(f"total minutes for given seconds:{Min}")
