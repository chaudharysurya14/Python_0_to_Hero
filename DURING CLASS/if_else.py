"""age=int(input('Enter your age: '))
if age<18:
    print('not eligible for marrige!')
elif age<60 &  age>18:
    print('you are eligible for merrage!')
else:
    print('go home and come fast for merray!') 
"""
# RANDOM FUNCTION ==========================================================

import random

lucky_num = random.random(1,100)
user_input = int(input('Enter a no: '))

while lucky_num != user_input:
    
    if user_input == lucky_num:
        print('congratulation!....you won.')
    elif user_input>lucky_num:
        print('too large number,try again!')
    elif user_input<lucky_num:
        print('too small no,try again!') 

user_input = int(input('Enter a no: '))


