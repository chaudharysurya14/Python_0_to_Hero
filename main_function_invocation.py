from  function_definitions import *

first_num = int(input("Please enter First number:"))
second_num = int(input("Please enter Second number:"))
returned_value = my_addition(first_num,second_num)
print("The Addition of the numbers is ",returned_value)

returned_value = my_square(first_num)
print("The Square of the number is ",returned_value)

returned_value = my_exponenation(first_num,second_num)
print("The exponenation of the numbers is ",returned_value)

my_string = input("Please enter a String: ")
returned_value = my_uppercase_func(my_string)
print("Upper case of the string is ",returned_value)

existing_salary = int(input("Pleased enter the existing_salary"))
raise_salary_percentage = int(input("Pleased enter the percentage"))

returned_value= raise_sal_percent(existing_salary,raise_salary_percentage)
print("The incremented salary is ",returned_value)

height = int(input("Pleased enter height in cms "))
returned_value= get_height(height)
print("Height in feet is ",returned_value)

no_of_dollars = int(input("Pleased enter no of dollars "))
returned_value= convert_to_rupee(no_of_dollars)
print("Amount is INR is " ,returned_value)

source = input("Pleased enter the source ")
destination = input("Pleased enter the destination ")
fare = float(input("Pleased enter the fare "))
discount_rate = float(input("Pleased enter the discount_rate in percentage "))

returned_value=get_fare_details(source, destination, fare, discount_rate)
print(returned_value)