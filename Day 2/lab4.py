#N students take K apple and distribute them among each other evenly. The remaining (the individual) part remains in the bracket.
#How many app;es will each single student get? How many apples will remain in the basket? the program reads the numbers N and K it should
#print the two answers for the questions above.


std=int(input("Enter a the no of students: "))
apple=int(input("Enter the no of apples: "))
x=apple//std   #x is the apple of each students will get:(no of apples // no of students)
y=aaple % std   #y Remaining Apples (no of apples % no of students )
print(f"The number of apple each student will get:{x}")
print(f"The remaining no of apple in the basket:{y}")
