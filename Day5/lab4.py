#4.Write a Python program to construct the following pattern, using a nested for loop.
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

rows=5
for i in range(0, rows):
    for j in range(0,i+1):
        print("*", end=' ')
    print("\r")
for i in range(rows, 0, -1):
    for j in range(0, i-1):
        print("*", end=' ')
    print("\r")

