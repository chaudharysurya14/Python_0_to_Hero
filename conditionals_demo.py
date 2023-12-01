"""
if the number is divisible by 3 print Fizz    
if the number is divisible by 5 print Buzz
if the number is divisible by 3 and also divisible by 5 print Fizz Buzz

Testcase : 
    21 --> Fizz
    50 --> Buzz
    15 --> Fizz Buzz
    22 --> Invalid Input 
"""

num = int(input("Please enter the number"))

"""
if num %5==0 and num % 3 ==0 :
    print("Fizz Buzz")
elif num%3 == 0 :
    print("Fizz")
elif num%5 == 0 :
    print("Buzz")
else:
    print("Invalid Input")
    


if num %5==0  :
    if num % 3 ==0 : 
        print("Fizz Buzz")
    else:
        print("Buzz")    
elif num%3 == 0 :
    print("Fizz")
else:
    print("Invalid Input")
    
"""
# very specific to python
is_inside_if_clause = 'N'
if num%3 == 0 :
    print("Fizz",end = ' ' )
    is_inside_if_clause = 'Y'

if num%5 == 0 :
    print("Buzz")
    is_inside_if_clause = 'Y'

if  is_inside_if_clause != 'Y':
    print("Invalid Input")


