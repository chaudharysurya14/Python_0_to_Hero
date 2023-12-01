print("I was executed")
pi = 3.14159265359

def my_addition(first_num,second_num):
    """
    1) receives two numbers from the invoking application and returns 
        a) addition 
    """
    return first_num+ second_num


def my_square(first_num):
    """
    1) receives two numbers from the invoking application and returns 
        b) first number squared 2 
    """
    return str(first_num**2)

def my_exponenation(first_num,second_num):
    """
    1) receives two numbers from the invoking application and returns 
        c) first number raised to number second number
    """
    return first_num**second_num


def my_uppercase_func(received_string):
    """
    # 2) receives String and returns upper case of the input string
    """
    return received_string.upper()


def raise_sal_percent(existing_salary,raise_salary_percentage):
    """
    3) receives "raise_salary_percentage" , salary raise ,
    percentage from the user, 
    returns the incremented salary to the console
    """
    return existing_salary + (existing_salary*raise_salary_percentage/100) 
    
def get_height(height):
    """
    4) receives height from the user in cms and returns the user height back 
    in foot/feet and inches
    """
    return round((height/30.48),2)
    

def convert_to_rupee(no_of_dollars):
    """
    5) receive no of the dollars from the user apply the conversion of 
    1 dollar = 82 rupees and return the amount to the console in rupees
    """
    return no_of_dollars*82

def get_fare_details(source, destination, fare_in_INR, discount_rate_percentage):
    """
    6) receive source, destination, fare in INR, discount_rate percentage from the user and return the 
    string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"
    """
    return "Fare from" + source +" to " + destination + " is " + str(fare_in_INR- (fare_in_INR*discount_rate_percentage/100) ) + " INR with has a applied discount of " + str(discount_rate_percentage)+ "%"

def my_addition_arbitary_positional(*numbers):
    """
    1) receives two numbers from the invoking application and returns 
        a) addition 
    """
    sum = 0 
    for num in numbers:
        sum = sum+ num
    return sum    

def my_addition_arbitary_keyword(**numbers_dict):
    """
    1) receives two numbers from the invoking application and returns 
        a) addition 
    """
    sum = 0 
    for num in numbers_dict.values():
        sum = sum+ num
    return sum 