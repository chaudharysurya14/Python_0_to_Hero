print("i was executed")
"""receives two numbers from the invoking application and returns """
def my_addition(a,b):

    #a = int(input("Enter first number: "))
    #b = int(input("Enter second number: "))
    #c = int(a) + int(b)


    #print("addition of two no= " , (c))
    return a+b 

"""first number squared 2 """
def square(a):
    square= a * a #for multiplexing
    print("Square of 1st input number=" , (square))
    return str(a**2)
"""first number raised to number second number"""

def raise_second_no(a,b):
    power = a ** b
    print("A raise to B=" , (power))
    return a**b

"""Accept String from user and output upper case of the input string """

def uppercase():
    
    string = str(input("Enter your name: "))
    str_upper = string.upper()
    print("upper case of input string is here: " , (str_upper))
    

"""Define a variable named "raise_salary_percentage" and get the salary raise 
percentage from the user, Now apply the raise to an employee
with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
print the incremented salary to the console"""


def raised_salery_percentage():
    
    raise_salery_percent = input("Enter the salery raise percentage: ")
    name = "SURYA"
    salery = 900
    increament_salery = int(salery)*int(raise_salery_percent)/100
    final_salery = int(salery) + int(increament_salery)
    print("Increament salery by percentage: " , (final_salery))


"""Get the height from the user in cms and display the user height back to console
in foot/feet and inches"""

def height():
    print("Input your height: ")
    height_in_feet = int(input("Feet: "))
    height_in_inch = int(input("Inches: "))

    height_in_inch += height_in_feet * 12
    height_in_cm = round(height_in_inch * 2.54, 1)

    print("Your height is : %d cm." % height_in_cm)

"""
print("Input your height: ")
height_in_feet = int(input("Feet: "))
height_in_inch = int(input("Inches: "))

height_in_inch = height_in_feet * 12
height_in_cm = round(height_in_inch * 2.54, 1)

print("Your height is : %d cm." % height_in_cm)
"""

"""Get the no of the dollars from the user apply the conversion of 
1 dollar = 82 rupees and print the amount to the console in rupees"""

def rupie_conversion():
    doller = int(input("Enter your amount in doller: "))
    rupies = doller*82
    print("your amount in rupies=" , (rupies))


"""Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"
"""

def fare_amount():
    source = str(input("Enter the source: "))
    destination = str(input("Enter your destination: "))
    fare = int(input("Enter fare amount: "))
    discount = int(input("Enter discount in precent(%): "))
    print(f"fare from {source} to {destination} is {fare} INR with has a discount of {discount}%")
    
