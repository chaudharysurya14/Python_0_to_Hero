#function with a return statement 
'''def my_functionname():
    print("I am printing some value")
    return 1 
    
return_val = my_functionname()    
print("Returned value from the function is " , return_val)'''

'''def my_functionname():
    print("I am printing some value")
return_val = my_functionname()    
print("Returned value from the function is " , return_val)'''

'''def my_addition_function(num1,num2):
    return num1+num2
my_first_number = 1
my_second_number = 2 
return_val = my_addition_function(my_first_number,my_second_number)
print("Returned value from my_addition_function is ", return_val)'''

'''def my_addition_function(num1=11,num2=10,num3=90):
    return num1+num2+num3
return_val = my_addition_function(11,10,100)
print("Returned value from my_addition_function is ", return_val)'''

#function with default value from a variable 
'''my_second_default_number = 10 
def my_addition_function(num1=my_second_default_number,num2=10,num3=90):
    return num1+num2+num3
my_second_default_number = 100
return_val = my_addition_function(11,num2=10)
print("Returned value from my_addition_function is ", return_val)

# pass by value
num1 = 10 
def pass_by_value(num1):
    num1 = 100

print("num1 value before function invocation", num1)
pass_by_value(num1)
print("num1 value after function invocation", num1)
'''

# very specific to python
'''num = int(input("Please enter the number"))
is_inside_if_clause = 'N'
if num%3 == 0 :
    print("Fizz",end = ' ' )
    is_inside_if_clause = 'Y'

if num%5 == 0 :
    print("Buzz")
    is_inside_if_clause = 'Y'

if  is_inside_if_clause != 'Y':
    print("Invalid Input")'''
    
'''
user_input = 'y'
while user_input == 'y':
    
    num = int(input("Please enter the number"))
    if num%3 == 0 :
        print("Fizz" , end = " ")
   
    if num%5 == 0 :
        print("Buzz")
    else:    
        print("Invalid Input")
    user_input=str(input('Enter your choice as (Y/N): '))

print("thanku" , end = " ")
'''


"""
Addition/Squaring/exponenation should be done as part of single function named 
"my_calculator"
which takes in type of operation, number1,number2 as input 
and outputs the answer based on the operation
"""


"""Create a game for FIZZ BUZ and keeping playing with the user untill the user chooses to skip the game"""
def fizz_buzz():
    num = int(input("Please enter a number"))
    is_inside_if_clause = 'N'
    if num%3 == 0 :
        print("Fizz",end = ' ' )
        is_inside_if_clause = 'Y'

    if num%5 == 0 :
        print("Buzz")
        is_inside_if_clause = 'Y'

    if  is_inside_if_clause != 'Y':
        print("Invalid Input")


"""
Addition/Squaring/exponenation should be done as part of single function named 
"my_calculator"
which takes in type of operation, number1,number2 as input 
and outputs the answer based on the operation
"""

from function_definitions import *
def my_calculator():
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")
    choice = int(input ("Please select your choice"))

    if choice == 1 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        returned_value = my_addition(first_num,second_num)
        print("The Addition of the numbers is ",returned_value)

    elif choice == 2 :
        first_num = int(input("Please enter First number:"))
        returned_value = my_square(first_num)
        print("The Square of the number is ",returned_value)
    elif choice == 3 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        returned_value = my_exponenation(first_num,second_num)
        print("The exponenation of the numbers is ",returned_value)

def play_game():
    while(True):
        print("Lets Play Fizz Buzz   !!!! ")
        fizz_buzz()	
        choice = input("\n Do you want to continue (Y/N)").lower()     
        if choice == 'n':
            break

# function calls
play_game()  


def iterative_calculator():
    while(True):
        print("Lets start   !!!! ")
        my_calculator()	
        choice = input("\n Do you want to continue (Y/N)").lower()     
        if choice == 'n':
            break

iterative_calculator()     