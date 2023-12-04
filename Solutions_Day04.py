# """1) Take a number from the user and print sum from 1 to that number """

# sum_upto_number = int(input("Please enter a number to sum upto"))

# cnt = 1 
# my_sum= 0  
# while(cnt <=sum_upto_number ):
#     my_sum = my_sum+cnt
#     cnt+=1
# print("The sum upto" ,sum_upto_number, "is",my_sum);


"""2) Take a number from the user and print all prime numbers from 1 to that number """

# number_from_user = int(input("Please enter a number "))

# # Pythonic way 
# for current_number_being_checked in range (2, number_from_user+1):
#     is_the_curent_number_prime = True
#     for divisor in range(2, (current_number_being_checked//2)+1):
#          is_the_curent_number_prime = not (current_number_being_checked%divisor == 0 )
#          if not is_the_curent_number_prime: 
#             break
#     if is_the_curent_number_prime:
#         print(f"{current_number_being_checked} is prime")
    
# # C style
# current_number_being_checked = 2
# while(current_number_being_checked<= number_from_user):
#     divisor = 2
#     is_the_curent_number_prime = "Yes"
#     while(divisor<= current_number_being_checked//2):
#         if current_number_being_checked%divisor == 0 :
#             is_the_curent_number_prime = "No"
#             break
#         divisor+=1
#     if is_the_curent_number_prime == "Yes":
#         print(f"{current_number_being_checked} is prime")
#     current_number_being_checked+=1

# """3) Take a number from the user and print all Odd numbers from 1 to that number """

# number_from_user = int(input("Please enter a number "))

# current_number_being_checked = 1
# while(current_number_being_checked<= number_from_user):
#     if current_number_being_checked%2 !=0:
#         print(current_number_being_checked,end=" ")
#     current_number_being_checked+=1

# """3) Take a number from the user and print all Even numbers from 1 to that number """

# number_from_user = int(input("Please enter a number "))

# current_number_being_checked = 1
# while(current_number_being_checked<= number_from_user):
#     if current_number_being_checked%2 ==0:
#         print(current_number_being_checked,end=" ")
#     current_number_being_checked+=1

"""
    5) Take a number from the user and print fibonacci sequence till that number
	eg : fibonnaci sequence for 5 is 1,2,3,5 """

num1 = -1
num2 = 1
input_number = int(input("Please enter the number till which you want to  print fibonacci sequence ?"))
while(True):
    sum = num1+num2
    if sum > input_number:
        break
    print(sum,end= " ") 
    num1 = num2
    num2 = sum
    