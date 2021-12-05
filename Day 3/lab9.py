"""
Question:
Take username and password from user and check it again for the three times whether the user
 has entered the right username and password.If yes then print a message "Logged in successfully". 
 If not then print invalid credentials for consecutive 3 times and if the limit exceeds than print 
 "Attempt finished" 
"""
print("Enter correct username and password combo to continue")
count=0
while password!='Sun12dip'  and username!='sundeep' and count<3:
      username=input("Enter your username: ")
      password=input("Enter your password: ")
      
if password=='Sun12dip' and  username=='sundeep':
    print("login successfully")
else:
    print("Invalid Credientals")
    count +=1


    
    