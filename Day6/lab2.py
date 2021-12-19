#Write a function called fizz_buzz that takes a number.
#if the number is divisible by 3, it should return "Fizz."
#if it is divisible by 5, it should return "buzz".
#If it is divisible by both 3 and 5, it should return "FizzBuzz."
#otherwise, it should return the same number.abs(n)


def fizz_buzz(a):
    if a%3==0:
        return "Fizz"
        
       
    elif a%5==0 :
        return "Buzz"
       
        
    elif a%3 ==0 and a%5==0 :
        return "Fizzbuzz"
        
      
print(fizz_buzz(10))