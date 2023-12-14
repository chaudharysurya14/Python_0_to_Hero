
num = int(input("Please enter the number"))

if num%3==0:
    print("fizz")
elif num%5==0:
    print("Buzz")
elif (num%3==0,num%5==0):
    print("fizz Buzz")
else:
 print("Invalid input")
