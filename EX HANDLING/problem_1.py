# my custom exception created  =========================================================================
'''class negative_number_error(Exception):
    pass

# 1)create a posative numbered list
#Note : raise a exception if the user insertes a negative no or user creates a empty list
def create_positive_numbered_list():
    my_list=[]
    for cntr in range(0,int(input('please enter number to be added: '))):
        if (num  :=int(input("please enter number to be added: ")))<0:
            raise  negative_number_error
        else:
            my_list.append(num)
    print(my_list)   

# invocation
try:
    create_positive_numbered_list()        
except negative_number_error:     
    print("I handled negative_number_error exception")
            
   ''' 
# QUESTION 2 ================================================================================================
# class posative_number_error(Exception):
#     pass


# def create_negative_numbered_list():
#     my_list=[]
#     for cntr in range(0,int(input('Please enter number of elements to the numbered list: '))):
#         if (num  :=int(input("please enter number to be added: ")))>=0:
#             raise  posative_number_error
#         else:
#             my_list.append(num)
#     print(my_list)   

# # invocation
# try:
#     create_negative_numbered_list()        
# except posative_number_error:   
#     print("I handled posative_number_error exception")
    
    
# ======================================================================================================

# n=int(input('How many value want to add in list: '))
# my_list=[]
# for my_list in range(0,int(input('How many value want to add in list: '))):
#     m=int(input('Enter element for set in integer form: '))
#     my_list.append(m)
#     print(my_list)
    
#     for my_list in range(0,str(input('Enter element for set in string form: '))):
#         s=input('Enter element for set in string form: ')
#         my_list.append(s)
#     print(my_list)



# =================================================================================================
# ==========================================================================================# my custom exception created 
# class negative_number_error(Exception):
#     pass
# class list_empty_error(Exception):
#     pass

# def create_positive_numbered_list():
#     global my_int_list1 
#     my_list = my_int_list1
# def create_positive_numbered_list(my_list):
#     """
#     1) Create a postive numbered list 
#     Note : raise an exception if the users inserts a negative number OR user creates an empty list 
# @@ -25,10 +23,7 @@ def create_positive_numbered_list():
# class positive_number_error(Exception):
#     pass

# def create_negative_numbered_list():
#     global my_int_list2
#     my_list = my_int_list2

# def create_negative_numbered_list(my_list):
#     """
#     # 2) Create a negative  numbered list 
#     # Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list
# # @@ -46,10 +41,7 @@ def create_negative_numbered_list():
# class homogenous_list_error(Exception):
#     pass

# def create_heterogenous_list():
#     global my_het_list3 
#     my_list = my_het_list3 

# def create_heterogenous_list(my_list):
#     """    3) Create a heterogenous list 
#     Note : raise an exception if the users creates a homogenous list (all elements of same datatype)
#     """
# # @@ -92,19 +84,9 @@ def create_heterogenous_list():
#     # else:
#         # print("We received a Heterogenous list ")       

# def find_an_element(flag):
#     def find_an_element(my_list):

#         if flag ==1 :
#             global my_int_list1
#             my_list = my_int_list1
#         elif flag ==2 :
#             global my_int_list2
#             my_list = my_int_list2
#         elif flag ==3 :
#             global my_het_list3
#             my_list = my_het_list3

#     datatype_choice = int(input("""Please choose a datatype of the element to be added \n 1) int \n 2) float \n 3) str \n 4) tuple \n 5) list \n 6) set \n 7) dictionary \n """))
#     datatype_choice = int(input("""Please choose a datatype of the element to be searched \n 1) int \n 2) float \n 3) str \n 4) tuple \n 5) list \n 6) set \n 7) dictionary \n """))

#     print(datatype_choice)
#     if datatype_choice == 1:
# # @@ -121,18 +103,19 @@ def find_an_element(flag):
#         input_val = set(input("Please enter a set like 1,2 ").replace(",",""))
#     if datatype_choice == 7:
#         my_temp_tuple_list = []
#         for str_elem in input("Please enter a dictionary to be added like key1:value1,key2:value2 ").split(","):
#             for str_elem in input("Please enter a dictionary like key1:value1,key2:value2 ").split(","):
#                 my_temp_tuple_list.append(tuple(str_elem.split(":")))
#                 input = dict(my_temp_tuple_list)
#                 input_val = dict(my_temp_tuple_list)

#         print(f"{input_val} found in provided list {my_list} : {input_val in my_list}")

# # invocation 
# my_int_list1=[]
# my_int_list2=[]
# my_het_list3=[]

# def my_exception_store(): 
#     my_int_list1=[]
#     my_int_list2=[]
#     my_het_list3=[]

#     while(True):
#         try:
#             print("Welcome to my_exception_store !!!!")
# # @@ -146,12 +129,12 @@ def my_exception_store():

#             choice = int(input("Please enter your choice !!!! "))
#             if choice ==1:
#                 create_positive_numbered_list()
#             if choice ==2:
#                 create_negative_numbered_list()
#             if choice ==3:
#                 create_heterogenous_list()
#             if choice ==4:
#                 create_positive_numbered_list(my_int_list1)
#             elif choice ==2:
#                 create_negative_numbered_list(my_int_list2)
#             elif choice ==3:
#                 create_heterogenous_list(my_het_list3)
#             elif choice ==4:
#                 print("Lists created are as below \n ----------------------")
#                 print(f"1 : {my_int_list1}")
#                 print(f"2 : {my_int_list2}")
# @@ -160,22 +143,25 @@ def my_exception_store():
#                 check =int(input("Which of the below list you would want to search from "))
#                 while True:
#                     if  check == 1:
#                         find_an_element(1)
#                         find_an_element(my_int_list1)
#                         break
#                     elif check == 2:
#                         find_an_element(2)
#                         find_an_element(my_int_list2)
#                         break
#                     elif check ==3:
#                         find_an_element(3)    
#                         find_an_element(my_het_list3)    
#                         break
#                     else:
#                         print("Please choose something from the above")
#             elif choice ==5:
#                 break
#             else:
#                 print("Please choose something from the above")
#         except negative_number_error:     
#             print("We received a negative number in the list and I handled negative_number_error exception")
#         except positive_number_error:     
#             print("We received a positive number in the list and I handled positive_number_error exception")
#         except homogenous_list_error:    
#             print("We received a Homogenous list and I handled homogenous_list_error exception")


# my_exception_store()    