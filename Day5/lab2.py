#2.Write a Python program to convert temperatures to and from celsius, fahrenheit.C = (5/9) * (F -32)

celsius=float(input("Enter temperature in celsius: "))
fahrenheit= (celsius*9/5)+32
print("%.2f Celsius is: %.2f Fahrenheit" %(celsius, fahrenheit))

