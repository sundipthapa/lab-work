#Given the interger N-the number of minutes that is passed since midnight -how many hours and minutes are displayed on the 24th digital clock? 
# The prgram should print two numbers: the number of  hours (between 0 and 23) an  the number of  minutes (between 0 and 59).
#For example, if N=150 then 150 minutes have passed since midnight -ie. now is 2:30 am. So, the program should print 2:30

NoOfMinutes=int(input("Enter a minute passed since  midnightnumber"))
hours=a//60
min=a%60
print(hours, min)


