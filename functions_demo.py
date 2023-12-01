"""
#function without a return statement 
def my_functionname():
    print("I am printing some value")

#return_val = my_functionname()    
#print("Returned value from the function is " , return_val)


#function with a return statement 
def my_functionname():
    print("I am printing some value")
    return 1 
    
return_val = my_functionname()    
print("Returned value from the function is " , return_val)



#function with a return statement and input parameters
def my_addition_function(num1,num2):
    return num1+num2

my_first_number = 1
my_second_number = 2 

return_val = my_addition_function(my_first_number,my_second_number)
print("Returned value from my_addition_function is ", return_val)


#function with default value from a literal 
def my_addition_function(num1=11,num2=10,num3=90):
    return num1+num2+num3

return_val = my_addition_function(11, num2=10,num3=100)
print("Returned value from my_addition_function is ", return_val)


#function with default value from a variable 
my_second_default_number = 10 
def my_addition_function(num1=my_second_default_number,num2=10,num3=90):
    return num1+num2+num3

my_second_default_number = 100

return_val = my_addition_function(11, num2=10)
print("Returned value from my_addition_function is ", return_val)


# pass by value
num1 = 10 
def pass_by_value(num1):
    num1 = 100

print("num1 value before function invocation", num1)
pass_by_value(num1)
print("num1 value after function invocation", num1)

# pass by reference
num_list = [10,]
def pass_by_ref(num_list):
    num_list.append(100)

print("num1 value before function invocation", num_list)
pass_by_ref(num_list)
print("num1 value after function invocation", num_list)

# pass by value
num_list = [10,]
def pass_list_by_value(num_list):
    num_list= [10000]

print("num1 value before function invocation", num_list)
pass_list_by_value(num_list)
print("num1 value after function invocation", num_list)



from  function_definitions import *
print(my_addition_arbitary_positional(1,2,3))
print(my_addition_arbitary_positional(1,2,3,4,5,6,7))

# this doesnot works since 
# the tuple passes is considered as first element of the new tuple that it creates
# to pass the value to the invoking function 
# print(my_addition_arbitary_positional((1,2,3,4,5,6,7,)))

     
print(my_addition(first_num=10,second_num=20))
print(my_addition_arbitary_keyword(first_num=10,second_num=20,third_num = 30 ))


# lambda arguments: expression    
my_addition_lambda = lambda first_num , second_num : first_num + second_num
print(my_addition_lambda(1,2))

# higher order function demonstration
# below are the lambda functions for each of the operation
lambda first_num,second_num : first_num+ second_num # for addition
lambda first_num: first_num * first_num # for square 
lambda first_num,second_num : first_num ** second_num # for exponentation

"""

# below is the snapshot of a higher order function that takes in above lambdas
#first_num,second_num = 1,2

# generic higher order function for calculator so that we can use it everywhere
# in our calculator example and not create each of different functions
# viz my_addition/ my_square / my_exponenation like we did in function_definitions.py 
def calculator_higher_order_function(function_definition,first_num,second_num = None):
    if second_num is None :
        return function_definition(first_num)
    return function_definition(first_num,second_num)

# invocation
#return_val = calculator_higher_order_function(lambda first_num,second_num : first_num + second_num,  first_num,second_num)
#print("Returned value from higher order function is " , return_val)

# I am trying to apply the concept of HOF in my calculator example we saw in Day03 solution sheet
def my_calculator_using_HOF():
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")
    choice = int(input ("Please select your choice"))

    if choice == 1 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        returned_value = calculator_higher_order_function(lambda first_num,second_num : first_num+ second_num,  first_num,second_num)
        print("The Addition of the numbers is ",returned_value)

    elif choice == 2 :
        first_num = int(input("Please enter First number:"))
        returned_value = calculator_higher_order_function(lambda first_num : first_num * first_num,  first_num)
        print("The Square of the number is ",returned_value)
    elif choice == 3 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        returned_value = calculator_higher_order_function(lambda first_num,second_num : first_num ** second_num,  first_num,second_num)
        print("The exponenation of the numbers is ",returned_value)

def iterative_calculator_HOF():
    while(True):
        print("Lets start   !!!! ")
        my_calculator_using_HOF()	
        choice = input("\n Do you want to continue (Y/N)").lower()     
        if choice == 'n':
            break

iterative_calculator_HOF() 
