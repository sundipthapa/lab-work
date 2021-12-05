#A school decide to replace the desks in three classrooms. Each desks sits the two students. Given the number of students in each class, print
#the smallest possible number of desks that can be purchased. The program should read three intergers: the number of student in each of the three classes, a, b and c respectively.
#Suppose in the first test there are three groups has 20 students and thus needs 10 desks. The second group has 21 students. so thtey can get by whith no fewer than 11 desks. 
#11 desks are also enough for the third group of 22 students. So, we need 32 desks in total





a=int(input("Enter the no of std in the first class"))
b=int(input("Enter the no of std in the second class"))

c=int(input("Enter the no of std in third class"))
sum=a//2+b//2+c//2+a*2+b%2+c%2
print(f"The total no of desks we needed is:{sum}")