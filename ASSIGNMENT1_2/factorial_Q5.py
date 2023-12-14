# ==============  FACTORIAL ===========================
# fact=1
# def factorial(fact):
fact=1
num=int(input('Enter number for factorial: '))
while num>0:
    fact=fact*num
    num=num-1
print("Factorial = " ,fact)







'''
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 7

# to take input from the user
# num = int(input("Enter a number: "))
# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)'''