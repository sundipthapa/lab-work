



year=int(input("Enter year to be checked: "))
if(year % 4 ==0 and year%100 !=0 or year%400==0):
    print("the year is a leap year!")
else:
    print("The year isnot a leap year!")