#find BMI of a person where take mass and height as input from the user

inp1=int(input("Enter your mass:"))
inp2=int(input("Enter your height:"))
#formula of BMI
#BMI=mass in kg/(height in m)**2  (body mass index)
BMI=inp1/inp2**2
print(f"BMI of a person is {BMI} kg/m\u00b2")