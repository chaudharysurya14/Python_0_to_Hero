# # comprehensions
# h_letters = [ letter for letter in 'human' ]
# print( h_letters)

# h_letters = { letter for letter in 'human' }
# print( h_letters)

# h_letters = tuple( letter for letter in 'human' )
# print( h_letters)



# #regular expressions

# import re
# pattern = '(^[a-zA-Z0-9: ])([a-z]*)'
# test_string = '@abcedef293109301939'
# #result = re.match(pattern, test_string)

# result = re.search(pattern, test_string)  
# print(type(result))
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))

# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")	

# num = 10      
# cnt = 0 
# for val in range(1,num):
#     cnt+=1
#     print(val)

    
import numpy as np

my_numpy_array = np.array([10])
print(my_numpy_array)

# *** Refer  Numpy Exercises.ipynb
