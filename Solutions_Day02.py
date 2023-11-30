#Solutions 
"""
1) Accept two numbers from the user and print 
a) addition 
b) first number squared 2 
c) first number raised to number second number

"""
first_num = int(input("Please enter First number:"))
second_num = int(input("Please enter Second number:"))

print("The Addition of the numbers is ", str(first_num+ second_num))
print("First number squared is  ", str(first_num**2))
print("First number raised to number second number is  ", str(first_num**second_num))

"""
# 2) Accept String from user and output upper case of the input string
"""
my_string = input("Please enter a String: ")
print("Upper case of the string is " , my_string.upper())

"""
# \n is a line boundary 
sentence = r'I\nlove\nPython\nProgramming.'

# returns a list after spliting string at line breaks 
resulting_list = sentence.splitlines(keepends=False)

print(resulting_list)



3) Define a variable named "raise_salary_percentage" and get the salary raise 
percentage from the user, Now apply the raise to an employee
with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
print the incremented salary to the console
"""

raise_salary_percentage = int(input("Pleased enter the percentage"))
Name= 'gaurav' 
existing_salary = 900

print("The incremented salary is " ,(existing_salary + (existing_salary*raise_salary_percentage/100) ) )

"""
4) Get the height from the user in cms and display the user height back to console
in foot/feet and inches

"""
height = int(input("Pleased enter height in cms "))
print("Height in feet is " , round((height/30.48),2))

"""
5) Get the no of the dollars from the user apply the conversion of 
1 dollar = 82 rupees and print the amount to the console in rupees
"""
no_of_dollars = int(input("Pleased enter no of dollars "))
print("Amount is INR is " , (no_of_dollars*82))

"""
6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"
"""

source = input("Pleased enter the source ")
destination = input("Pleased enter the destination ")
fare = float(input("Pleased enter the fare "))
discount_rate = float(input("Pleased enter the discount_rate in percentage "))

print("Fare from" , source ," to " , destination , " is " , fare- (fare*discount_rate/100)  , " INR with has a applied discount of " , discount_rate, "%")

